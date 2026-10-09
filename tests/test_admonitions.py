import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from sanitize_docs import parse_bang_header, sanitize_admonitions


class TestParseBangHeader(unittest.TestCase):
    def test_attached_type_with_title(self):
        self.assertEqual(parse_bang_header('warning Disclaimer'), ('warning', 'Disclaimer'))

    def test_attached_unknown_type(self):
        self.assertEqual(parse_bang_header('light'), ('light', None))

    def test_spaced_known_type(self):
        self.assertEqual(parse_bang_header(' Note'), ('note', None))

    def test_spaced_free_title(self):
        self.assertEqual(parse_bang_header(' Git backends explained'), (None, 'Git backends explained'))
        self.assertEqual(parse_bang_header(' Discontinued'), (None, 'Discontinued'))

    def test_quoted_title(self):
        self.assertEqual(parse_bang_header(' warning "Important Warning"'), ('warning', 'Important Warning'))

    def test_quote_only_stripped_when_wrapping_everything(self):
        self.assertEqual(
            parse_bang_header(" 'Pinned' prompts = Default prompts"),
            (None, "'Pinned' prompts = Default prompts"),
        )

    def test_bare_and_whitespace_only(self):
        self.assertEqual(parse_bang_header(''), (None, None))
        self.assertEqual(parse_bang_header('  '), (None, None))
        self.assertEqual(parse_bang_header('info  '), ('info', None))


class TestBangBlocks(unittest.TestCase):
    def test_real_sample_config_yaml(self):
        text = (
            "!!!warning Disclaimer\n\n"
            "This documentation may be obsolete.\n\n"
            "**WARNING: DO NOT EDIT THE DEFAULT CONFIG DIRECTLY.**\n"
            "!!!\n\n"
            "`config.yaml` is the main configuration file.\n"
        )
        out = sanitize_admonitions(text)
        self.assertNotIn('!!!', out)
        self.assertIn('**Warning Disclaimer:**', out)
        self.assertIn('This documentation may be obsolete.', out)
        self.assertIn('DO NOT EDIT THE DEFAULT CONFIG DIRECTLY', out)
        self.assertIn('`config.yaml` is the main configuration file.', out)

    def test_real_sample_single_line_body(self):
        text = (
            "!!!warning Disclaimer\n"
            "The use of this extension does not guarantee a better chatting experience.\n"
            "!!!\n\n"
            "Chat vectorization searches for messages.\n"
        )
        out = sanitize_admonitions(text)
        self.assertNotIn('!!!', out)
        self.assertIn('**Warning Disclaimer:** The use of this extension', out)
        self.assertIn('Chat vectorization searches for messages.', out)

    def test_title_equal_to_type_not_duplicated(self):
        out = sanitize_admonitions("!!!warning Warning\nBe careful.\n!!!\n")
        self.assertIn('**Warning:** Be careful.', out)
        self.assertNotIn('Warning Warning', out)

    def test_type_only_block(self):
        out = sanitize_admonitions("!!!tip\nUse the Tab key.\n!!!\n")
        self.assertIn('**Tip:** Use the Tab key.', out)

    def test_untyped_titled_block_with_body(self):
        out = sanitize_admonitions("!!! Git backends explained\nBody text.\n!!!\n")
        self.assertIn('**Git backends explained:** Body text.', out)

    def test_title_only_block_keeps_title(self):
        out = sanitize_admonitions("!!! Applies to: Text Completion APIs\n!!!\n\nNext paragraph.\n")
        self.assertNotIn('!!!', out)
        self.assertIn('Applies to: Text Completion APIs', out)
        self.assertIn('Next paragraph.', out)

    def test_markdown_bold_in_title_does_not_break_label(self):
        out = sanitize_admonitions("!!!warning **IMPORTANT!**\nRead this.\n!!!\n")
        self.assertIn('**Warning IMPORTANT!:** Read this.', out)

    def test_trailing_colon_in_title(self):
        out = sanitize_admonitions("!!!info Some terms:\nA is B.\n!!!\n")
        self.assertIn('**Info Some terms:** A is B.', out)
        self.assertNotIn('::', out)

    def test_multi_paragraph_body_label_on_own_line(self):
        out = sanitize_admonitions("!!!info Note\nFirst.\n\nSecond.\n!!!\n")
        self.assertIn('**Info Note:**\n\nFirst.\n\nSecond.', out)

    def test_list_body_label_on_own_line_and_indent_kept(self):
        out = sanitize_admonitions("!!!tip Tips\n- one\n  - nested\n- two\n!!!\n")
        self.assertIn('**Tip Tips:**\n\n- one\n  - nested\n- two', out)

    def test_bang_inside_code_fence_untouched(self):
        text = "```\n!!!warning not a block\n```\n"
        self.assertEqual(sanitize_admonitions(text), text)

    def test_unclosed_block_keeps_body(self):
        text = "!!!warning Heads up\nBody that never closes.\n\n!!!info Next\nOther.\n!!!\n"
        with self.assertLogs(level='WARNING'):
            out = sanitize_admonitions(text, 'x.md')
        self.assertNotIn('!!!', out)
        self.assertIn('Body that never closes.', out)
        self.assertIn('Heads up', out)
        self.assertIn('**Info Next:** Other.', out)

    def test_unclosed_block_at_eof(self):
        with self.assertLogs(level='WARNING'):
            out = sanitize_admonitions("!!!tip\nLast words.\n")
        self.assertNotIn('!!!', out)
        self.assertIn('Last words.', out)

    def test_html_wrapped_code_does_not_break_later_blocks(self):
        # Real case from uicustomization.md: the closing line is "```</code></pre>"
        text = (
            "<pre><code>```asciimath\n"
            "int_{-oo}^{oo} e^{-x^2} dx = sqrt{pi}\n"
            "```</code></pre>\n\n"
            "!!!info Deprecation notice\n"
            "The legacy syntax is no longer supported.\n"
            "!!!\n"
        )
        out = sanitize_admonitions(text)
        self.assertNotIn('!!!', out)
        self.assertIn('**Info Deprecation notice:** The legacy syntax is no longer supported.', out)

    def test_untyped_bare_block_keeps_body(self):
        out = sanitize_admonitions("!!!\nThis setting also affects inline media.\n!!!\n")
        self.assertNotIn('!!!', out)
        self.assertIn('This setting also affects inline media.', out)


class TestColonBlocks(unittest.TestCase):
    def test_callout_still_works(self):
        out = sanitize_admonitions(":::callout\nSome callout text.\n:::\n")
        self.assertNotIn(':::', out)
        self.assertIn('**Callout:** Some callout text.', out)


if __name__ == '__main__':
    unittest.main()