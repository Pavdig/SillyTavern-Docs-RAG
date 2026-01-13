
# Context Template

For equivalent settings in Chat Completion APIs, use Prompt Manager.

Usually, AI models require you to provide the character data to them in some specific way. SillyTavern includes a list of pre-made conversion rules for different models, but you may customize them however you like.

Edit these settings in the "Advanced Formatting" panel.

## Story String

This field is a template for the prompt preamble (known internally as a story string). This is the main way to add the information defined in Character Cards for text completion and instruct models.

The template supports Handlebars syntax, custom text injections or formatting, and any other macros. See the language reference here: <https://handlebarsjs.com/guide/>

We provide the following parameters to the Handlebars evaluator (wrapped in double curly braces):

1. `{{anchorBefore}}`: Prompts set to use the "Before Story String" position.
2. `{{anchorAfter}}`: Prompts set to use the "After Story String" position.
3. `{{description}}`: The character's Description.
4. `{{scenario}}`: The character's Scenario.
5. `{{personality}}`: The character's Personality.
6. `{{system}}`: The system prompt OR the character's main prompt override (if it exists and "Prefer Char. Prompt" is enabled in User Settings).
7. `{{persona}}`: The selected persona's description.
8. `{{char}}`: The character's name.
9. `{{user}}`: The selected persona's name.
10. `{{wiBefore}}` or `{{loreBefore}}`: Combined activated World Info entries with Position set to "Before Char Defs".
11. `{{wiAfter}}` or `{{loreAfter}}`: Combined activated World Info entries with Position set to "After Char Defs".
12. `{{mesExamples}}`: (Optional) The character's Example Dialogues, instruct-formatted with a separator.
13. `{{mesExamplesRaw}}`: The character's Example Dialogues in raw format, without any formatting.

When using `{{mesExamples}}` in the Story String, set **"Example Messages Behavior"** in the **<i class="fa-solid fa-user-cog"></i> User Settings** panel to **"Never include examples"** to avoid duplicating example messages in the prompt.

A special `{{trim}}` macro is supported to remove any newlines that surround it. Use it if you want a part of the text to not be separated from the previous line by a newline (_spaces **are not** trimmed_).

**WARNING**: If any of the above parameters are missing from the story string template, they will not be sent in the prompt at all.

### Prompt Anchors

The `{{anchorBefore}}` and `{{anchorAfter}}` are generic placeholders for prompts added by various extensions and miscellaneous features in a chosen static position, for example:

* Author's Note
* Summaries
* Chat Vectorization / Data Bank
* STscript injections
* Web Search

### Story String position

By default, the rendered story string (with all placeholders replaced) is placed at the very beginning of the prompt, followed by example messages and the visible chat history.

Alternatively, you can move it to a dynamic position by choosing the "In-chat @ Depth" option, which places the story string at a specific depth in the chat context.

If the template contains static prompt elements (model-specific prefixes or suffixes) for wrapping the story string, using the "In-Chat @ Depth" position will cause it to be incorrectly double-wrapped with duplicate sequences, which may lead to unexpected results.

In this case, you can fix the issue in one of the following ways:

1. **Built-in templates**: Reset the templates to their defaults using the steps described in Advanced Formatting.
2. **Custom templates**: Move the static elements from the story string template to Story String Sequences.

### Story String wrapping

The following section only applies when **Instruct Mode** is ON.

* **Default** position: The rendered Story String will be wrapped using the sequences defined in Story String Sequences.
* **In-chat @ Depth** position: The rendered Story String will be wrapped using the sequences defined in Chat Messages Sequences for a chosen role (default: System).

## Example Separator

Used as a block header and a separator between the example dialogue blocks. Any instance of `<START>` tags in the example dialogues will be replaced with the contents of this field.

## Chat Start

Inserted as a separator after the rendered story string and after the example dialogues blocks, but before the first message in context.

## Separators as Stop Strings

Adds "Example Separator" and "Chat Start" to the list of stop strings.

Helpful if the model tends to hallucinate or leak whole blocks of example dialogue preceded by the separator.

## Names as Stop Strings

Adds Character and User Persona names to the list of stop strings.

Recommended to keep it on to prevent model impersonation.

## Always add character's name to prompt

This setting has no effect when Instruct Mode is ON. The name behavior is instead defined by the selected Include Names option.

Appends the character's name to the prompt to force the model to complete the message as the character:

```txt
** OTHER CONTEXT HERE **
Character:
```
