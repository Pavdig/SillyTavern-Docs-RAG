
# Advanced Formatting

The settings provided in this section allow for more control over the [prompt-building](SillyTavern_index.md) strategy, primarily for Text Completion APIs.

Most of the settings in this panel do not apply to Chat Completions APIs as they are governed by the prompt manager system instead.

+++ Text Completion APIs
* System Prompt
* Context Template
* Tokenizer
* Custom Stopping Strings
+++ Chat Completion APIs
* System Prompt: not applicable, use [Prompt Manager](SillyTavern_prompt-manager.md)
* Context Template: not applicable, use [Prompt Manager](SillyTavern_prompt-manager.md)
* Tokenizer
* Custom Stopping Strings
+++

## Resetting Templates

You can restore the default templates to their original state. This can be done either through the UI or by manually deleting the relevant data files.

### UI Reset

1. Open the ** Advanced Formatting** menu.
2. Pick the template you want to reset.
3. Click the ** Restore current template** button.
4. Confirm the action when prompted.

### Manual Reset

Make sure the `skipContentCheck` setting is set to `false` in [config.yaml](SillyTavern_Administration_config-yaml.md), otherwise the content check will not be triggered.

1. Navigate to your user data directory (see [Data paths](SillyTavern_Installation_index.md) for details).
2. Delete the `content.log` file from the root of your user data directory. This file tracks the default files copied for your user.
3. Delete the template JSON files from the relevant subdirectories (`context`, `instruct`, `sysprompt`, etc.).
4. Restart the SillyTavern server. The application will repopulate the default content, restoring any deleted default templates.

## Backend-defined templates

Applies to: Text Completion APIs
Not applicable to Chat Completion APIs as they use a different prompt builder.

Some Text Completion sources provide an ability to automatically choose templates recommended by the model author. This works by comparing a hash of the chat template defined in the model's `tokenizer_config.json` file with one of the default SillyTavern templates.

1. ** Derive templates** option must be enabled in the ** Advanced Formatting** menu. This can be applied to Context, Instruct, or both.
2. A supported backend must be chosen as a Text Completion source. Currently only llama.cpp and KoboldCpp support deriving templates.
3. The model must correctly report its metadata when the connection to the API is established. If this didn't work, try updating the backend to the latest version.
4. The reported chat template hash must match the one of the known SillyTavern templates (https://github.com/SillyTavern/SillyTavern/blob/release/public/scripts/chat-templates.js). This only covers default templates, such as Llama 3, Gemma 2, Mistral V7, etc.
5. If the hash matches, the template will be automatically selected if it exists in the templates list (i.e., not renamed or deleted).

## System Prompt

Applies to: Text Completion APIs
For equivalent settings in Chat Completion APIs, use [Prompt Manager](SillyTavern_prompt-manager.md). The **Main Prompt** is the equivalent of the System Prompt in Chat Completion APIs.

The System Prompt defines the general instructions for the model to follow. It sets the tone and context for the conversation. For example, it tells the model to act as an AI assistant, a writing partner, or a fictional character.

The System Prompt is a part of the [Story String](SillyTavern_context-template.md) and usually the first part of the prompt that the model receives.

See the [prompting guide](SillyTavern_index.md) to learn more about the System Prompt.

## Context Template

Applies to: Text Completion APIs
For equivalent settings in Chat Completion APIs, use [Prompt Manager](SillyTavern_prompt-manager.md).

Usually, AI models require you to provide the character data to them in some specific way. SillyTavern includes a list of pre-made conversion rules for different models, but you may customize them however you like. 

The options for this section are explained in [Context Template](SillyTavern_context-template.md).

## Tokenizer

A tokenizer is a tool that breaks down a piece of text into smaller units called tokens. These tokens can be individual words or even parts of words, such as prefixes, suffixes, or punctuation. A rule of thumb is that one token generally corresponds to 3~4 characters of text.

The options for this section are explained in [Tokenizer](SillyTavern_tokenizer.md).

## Custom Stopping Strings

Accepts a JSON-serialized array of stopping strings. Example: `["\n", "\nUser:", "\nChar:"]`. If you're unsure about the formatting, use an online JSON validator (https://jsonlint.com/). If the model output **ends** with any of the stop strings, they will be removed from the output.

Supported APIs:

1. KoboldAI Classic (versions 1.2.2 and higher) or KoboldCpp
2. AI Horde
3. Text Completion APIs: Text Generation WebUI (ooba), Tabby, Aphrodite, Mancer, TogetherAI, Ollama, etc.
4. NovelAI
5. OpenAI (max 4 strings) and compatible APIs
6. OpenRouter (both Text and Chat Completion)
7. Claude
8. Google AI Studio
9. MistralAI

## Start Reply With

Note
By default, the Start Reply With prefix won't be shown in the resulting message. Enable "Show reply prefix in chat" to display it.

### Text Completion APIs

Prefills the last line of the prompt, forcing the model to continue from that point. This is useful for enforcing content, such as nudging toward the [Model Reasoning](SillyTavern_Usage_Prompts_reasoning.md) with the defined prefix:

```txt

Sure!
```

### Chat Completion APIs

Adds an assistant role message to the end of the prompt. For some backend models, this is equivalent to prefilling the model response, but some may not support that at all and will fail with a validation error. If you're unsure, leave this field empty.
