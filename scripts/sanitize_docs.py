#!/usr/bin/env python3
import argparse
import logging
import re
import textwrap
from pathlib import Path
from urllib.parse import urlparse, urldefrag

ADMONITION_TYPES = {
    'note', 'abstract', 'info', 'tip', 'success', 'question',
    'warning', 'failure', 'danger', 'bug', 'example', 'quote', 'callout'
}

MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
MD_IMAGE_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
FRONT_MATTER_RE = re.compile(r'\A---\s*\n.*?\n---\s*(?:\n|$)', flags=re.DOTALL)
SCREENSHOTS_RE = re.compile(r'(?ms)^##\s*Screenshots\b.*?(?=^##\s*|\Z)')
EMPTY_TABLE_ROW_RE = re.compile(r'^\s*\|(?:\s*\|)+\s*$', flags=re.MULTILINE)
BR_RE = re.compile(r'<br\s*/?>', flags=re.IGNORECASE)
BLANK_LINES_RE = re.compile(r'\n{3,}')
# ::: blocks (e.g. ":::callout" ... ":::"), unchanged behaviour
COLON_OPEN_RE = re.compile(
    r'^\s*:::\s*([A-Za-z0-9_-]+)?(?:\s+["\'](.+?)["\'])?\s*$'
)
# !!! blocks. Upstream format:
#   !!!type Free text title      (type attached, title unquoted)
#   !!! Free text title          (no type, or a known type word)
#   body, usually NOT indented
#   !!!                          (bare !!! closes the block)
BANG_RE = re.compile(r'^\s*!!!(.*)$')
TYPE_TOKEN_RE = re.compile(r'^[A-Za-z0-9_-]+$')
# A fence line starts with ``` or ~~~. Lines like "```</code></pre>" are the tail of an
# HTML-wrapped block whose opener does not start the line, so they must not toggle state.
FENCE_RE = re.compile(r'^\s*(```|~~~)(?!.*</(?:code|pre)>)')
LIST_START_RE = re.compile(r'^(?:[-*+]\s|\d+[.)]\s)')

def is_external_link(url: str) -> bool:
    parsed = urlparse(url)
    return bool(parsed.scheme) or url.startswith('www.') or url.startswith('//')

def normalize_url(url: str) -> str:
    url = url.strip()
    url, _ = urldefrag(url)
    url = url.split('?', 1)[0]
    return url.strip()

def make_flat_output_name(rel_path: Path) -> str:
    rel_text = '_'.join(rel_path.parts)
    suffix = rel_path.suffix.lower()
    if suffix in {'.md', '.markdown'}:
        return rel_text if rel_text.endswith('.md') else f'{rel_text[:-len(suffix)]}.md'
    if suffix == '.yaml':
        return f'{rel_text[:-len(suffix)]}-yaml.md'
    if suffix == '.yml':
        return f'{rel_text[:-len(suffix)]}-yml.md'
    if suffix == '.json':
        return rel_text
    if not suffix:
        return f'{rel_text}.md'
    return rel_text

def resolve_relative_link(url: str, file_path: Path, root: Path) -> str | None:
    url = normalize_url(url)
    if not url or url.startswith('#') or is_external_link(url):
        return None
    if url.startswith('/'):
        target = root / url.lstrip('/\\')
    else:
        target = file_path.parent / url
    normalized = target.resolve(strict=False)
    root_abs = root.resolve(strict=False)
    try:
        rel_target = normalized.relative_to(root_abs)
    except ValueError:
        return None
    return make_flat_output_name(rel_target)

def replace_link(match: re.Match, file_path: Path, root: Path) -> str:
    anchor_text = match.group(1).strip()
    url = match.group(2).strip()
    if is_external_link(url):
        return f'{anchor_text} ({url})'
    resolved = resolve_relative_link(url, file_path, root)
    if resolved:
        return f'[{anchor_text}](SillyTavern_{resolved})'
    logging.debug('Unsupported link preserved as plain text: %s -> %s', anchor_text, url)
    return anchor_text

def replace_image(match: re.Match) -> str:
    return ''

def strip_wrapping_quotes(title: str) -> str:
    if len(title) >= 2 and title[0] == title[-1] and title[0] in '"\'':
        return title[1:-1].strip()
    return title

def parse_bang_header(rest: str) -> tuple[str | None, str | None]:
    """Parse the text after '!!!' into (type, title).

    - '!!!warning Disclaimer'  -> ('warning', 'Disclaimer')   type attached: always a type
    - '!!!light'               -> ('light', None)
    - '!!! Note'               -> ('note', None)               known type word
    - '!!! Git backends'       -> (None, 'Git backends')       free text title
    - '!!! warning "Title"'    -> ('warning', 'Title')
    - ''                       -> (None, None)
    """
    stripped = rest.strip()
    if not stripped:
        return None, None
    attached = not rest[0].isspace()
    parts = stripped.split(None, 1)
    first = parts[0]
    remainder = parts[1].strip() if len(parts) > 1 else ''
    is_type = False
    if TYPE_TOKEN_RE.match(first):
        is_type = attached or first.lower() in ADMONITION_TYPES
    if is_type:
        return first.lower(), (strip_wrapping_quotes(remainder) or None)
    return None, strip_wrapping_quotes(stripped)

def build_label(block_type: str | None, title: str | None) -> str:
    title = (title or '').replace('**', '').replace('__', '').strip()
    type_text = block_type.title() if block_type else ''
    if title and type_text and title.lower() == type_text.lower():
        return type_text
    return f'{type_text} {title}'.strip()

def normalize_admonition_block(block_type: str | None, title: str | None, lines: list[str]) -> str:
    inner = textwrap.dedent(''.join(lines)).strip('\n').rstrip()
    label = build_label(block_type, title)
    if not inner.strip():
        return f'\n**{label}**\n' if title and label else ''
    if not label:
        return f'\n{inner}\n'
    colon = '' if label.endswith(':') else ':'
    multiline = '\n\n' in inner or inner.startswith(('|', '```', '~~~')) or bool(LIST_START_RE.match(inner))
    if multiline:
        return f'\n**{label}{colon}**\n\n{inner}\n'
    return f'\n**{label}{colon}** {inner}\n'

def is_fence(line: str) -> bool:
    return bool(FENCE_RE.match(line))

def collect_bang_body(lines: list[str], idx: int) -> tuple[list[str], bool, int]:
    """Collect body lines until a bare '!!!'. Returns (body, closed, next_idx)."""
    body = []
    in_fence = False
    while idx < len(lines):
        line = lines[idx]
        if is_fence(line):
            in_fence = not in_fence
        elif not in_fence:
            stripped = line.strip()
            if stripped == '!!!':
                return body, True, idx + 1
            if stripped.startswith('!!!'):
                return body, False, idx  # next opener, this block was never closed
        body.append(line)
        idx += 1
    return body, False, idx

def sanitize_admonitions(text: str, source: str = '') -> str:
    lines = text.splitlines(keepends=True)
    output = []
    idx = 0
    in_fence = False
    while idx < len(lines):
        line = lines[idx]
        if is_fence(line):
            in_fence = not in_fence
            output.append(line)
            idx += 1
            continue
        if in_fence:
            output.append(line)
            idx += 1
            continue

        colon_match = COLON_OPEN_RE.match(line)
        if colon_match:
            block_type = colon_match.group(1).lower() if colon_match.group(1) else None
            title = colon_match.group(2)
            idx += 1
            block_lines = []
            while idx < len(lines) and not re.match(r'^\s*:::\s*$', lines[idx]):
                block_lines.append(lines[idx])
                idx += 1
            if idx < len(lines):
                idx += 1
            output.append(normalize_admonition_block(block_type, title, block_lines))
            continue

        bang_match = BANG_RE.match(line)
        if bang_match:
            block_type, title = parse_bang_header(bang_match.group(1))
            start_line = idx + 1
            body, closed, idx = collect_bang_body(lines, idx + 1)
            if closed:
                output.append(normalize_admonition_block(block_type, title, body))
            else:
                logging.warning('Unclosed !!! block at %s:%d, keeping body as plain text', source or '<text>', start_line)
                label = build_label(block_type, title)
                if title and label:
                    output.append(f'\n**{label}**\n')
                output.append(''.join(body))
            continue

        output.append(line)
        idx += 1
    return ''.join(output)

def sanitize_text(content: str, file_path: Path, root: Path) -> str:
    content = FRONT_MATTER_RE.sub('', content)
    content = SCREENSHOTS_RE.sub('', content)
    content = MD_IMAGE_RE.sub(replace_image, content)
    content = MD_LINK_RE.sub(lambda m: replace_link(m, file_path, root), content)
    content = sanitize_admonitions(content, file_path.name)
    content = EMPTY_TABLE_ROW_RE.sub('', content)
    content = BR_RE.sub('', content)
    content = BLANK_LINES_RE.sub('\n\n', content)
    return content.strip() + '\n'

def collect_markdown_files(source_dir: Path) -> list[Path]:
    return [path for path in source_dir.rglob('*.md') if path.is_file()]

def main() -> int:
    parser = argparse.ArgumentParser(description='Sanitize SillyTavern docs for RAG ingestion.')
    parser.add_argument('--source', default='work_dir', help='Source directory with markdown files')
    parser.add_argument('--output', default='processed_temp', help='Output directory for sanitized files')
    parser.add_argument('--root', default=None, help='Root for resolving relative links')
    parser.add_argument('--verbose', action='store_true', help='Enable debug logging')
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format='[%(levelname)s] %(message)s'
    )

    source_dir = Path(args.source).resolve()
    root_dir = Path(args.root).resolve() if args.root else source_dir
    output_dir = Path(args.output).resolve()

    if not source_dir.exists():
        logging.error('Source directory does not exist: %s', source_dir)
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)

    markdown_files = collect_markdown_files(source_dir)
    logging.info('Found %d markdown files under %s', len(markdown_files), source_dir)

    count = 0
    for file_path in markdown_files:
        try:
            text = file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            logging.warning('Unable to read file as UTF-8, skipping: %s', file_path)
            continue

        if 'This page has been moved to' in text:
            logging.debug('Skipping redirect stub: %s', file_path)
            continue

        sanitized = sanitize_text(text, file_path, root_dir)
        rel_path = file_path.relative_to(source_dir)
        output_name = make_flat_output_name(rel_path)
        output_file = output_dir / f'SillyTavern_{output_name}'
        output_file.write_text(sanitized, encoding='utf-8')
        count += 1

    logging.info('Processed %d markdown files.', count)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())