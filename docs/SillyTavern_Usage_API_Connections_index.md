
# API Connections

SillyTavern can connect to a wide range of LLM APIs.
Below is a description of their respective strengths, weaknesses, and use cases.

## ELI5: Chat Completions vs Text Completions

When you first navigate to the "API Connections" page in ST, you will notice a drop-down option to select between options using nomenclature such as "Chat Completion" and "Text Completion". It's helpful to understand what this means.

What it's not: It's easy to think of "Text Completion" as local models and "Chat Completion" as cloud-based LLMs, but that's not the case. Neither is e.g. "Novel AI" or "Kobold" actually a separate type of model altogether, even though they are separate options in the API dropdown in ST. You can force models into different API structures with the appropriate backend, but that's not the point of this section.

When you send a message using ST, your chat, character description, and other prompts such as lorebooks or author's notes are constructed into a single "prompt" to be sent to the model. The API "type" for the model you are using decides how exactly this prompt will be constructed (something that ST takes care of for you automatically in the background - you can open your ST terminal and see exactly what the prompt being sent to the AI looks like).

### Chat Completions

A Chat Completion model, as its name suggests, will structure your prompt into a series of messages between the User (you) and the Assistant (the AI) or System (neutral). Models that are trained for Chat Completion help create the feeling of a "Chat", with the AI "responding" to the last message. When you're using the ChatGPT website, you're dealing with a Chat Completions API in the background.

### Text Completions (a.k.a just "Completions")

A Text Completion on the other hand, and again as its name suggests, will convert your prompt into one long string, and the model will simply try to continue this (like, literally imagine all your text, your hundreds of messages, all your formatting, newlines, etc. squashed into one very long sentence).

If your messages in ST happen to be formatted as a series of messages between YourPersona: and Character:, the Text Completion model will try to continue this pattern and ST will render it as a new chat message for you, but really the model is just trying to continue the text. If you offered an input of "The Sun rises in the", a text completion model is likely to finish that message for you with "East".

Most Text Completion models have a recommended "Instruct Template" (usually mentioned in the model's documentation or download page) that helps them "respond" to messages and instructions, just like a Chat Completion model. ST usually has most (if not all) Instruct Templates available for you to choose from in the "Advanced Formatting" page.

## Local APIs

- These LLM APIs can be run on your PC.
- They are free to use and have no content filter.
- Installation process can be complex (**The SillyTavern dev team does not provide support for this**).
- Requires separate download of LLM models from HuggingFace which can be 5-50GB each.
- Most models are not as powerful as cloud LLM APIs.

### KoboldCpp

- Easy-to-use API with CPU offloading (helpful for low VRAM users) and streaming
- Runs from a single binary file on Windows, Mac, and Linux
- Supports GGUF models
- Slower than GPU-only loaders such as AutoGPTQ and Exllama/v2
- GitHub, Setup Instructions

### llama.cpp

- The original source from which KoboldCpp and Ollama were forked
- Provides pre-compiled binaries and an option to compile from source
- Supports GGUF models
- Lightweight CLI interface for llama-server
- GitHub

### Ollama

- Easiest to set up and use of all llama.cpp-based APIs
- A nifty catalog of models available for one-click download
- Supports GGUF models wrapped in Ollama's own format
- GitHub, Website

### Oobabooga TextGeneration WebUI

- All-in-one Gradio UI with streaming
- Broadest support for quantized (AWQ, Exl2, GGML, GGUF, GPTQ) and FP16 models
- One-click installers available
- Regular updates, which can sometimes break compatibility with SillyTavern
- GitHub

**Correct Way to Connect SillyTavern to Ooba's new OpenAI API:**

1. Make sure you're on the latest update of Oobabooga's TextGen (as of Nov 14th, 2023).
2. Edit the CMD_FLAGS.txt file, and add the `--api` flag there. Then restart Ooba's server.
3. Connect ST to `http://localhost:5000/` (by default) without checking the 'Legacy API' box. You may remove the `/v1` postfix from the URL Ooba's console provides you.

*You can change the API hosting port with the `--api-port 5001` flag, where 5001 is your custom port.*

### TabbyAPI

- Lightweight Exllamav2-based API with streaming
- Supports Exl2, GPTQ, and FP16 models
- Official extension allows loading/unloading models directly from SillyTavern
- Not recommended for users with low VRAM (no CPU offloading)
- GitHub, Setup Instructions

### KoboldAI Classic (deprecated, abandoned)

- Runs on your PC, 100% private, wide range of models available
- Gives the most direct control of the AI's generation settings
- Requires large amounts of VRAM in your GPU (6-24GB, depending on the LLM model)
- Models limited to 2k context
- No streaming
- Popular KoboldAI versions:
  - Henky's United
  - 0cc4m's 4bit-supporting United

## Cloud LLM APIs

- These LLM APIs are run as cloud services and require no resources on your PC
- They are stronger/smarter than most local LLMs
- However, they all have content filtering of varying degrees, and most require payment

### AI Horde

- SillyTavern can access this API out of the box with no additional settings required
- Uses the GPU of individual volunteers (Horde Workers) to process responses for your chat inputs
- At the mercy of the Worker in terms of generation wait times, AI settings, and available models
- Website, Setup Instructions

### OpenAI (ChatGPT)

- Easy to set up and acquire an API key
- Requires prepayment for credits and charges per prompt
- Very logical. Creative style can be repetitive and predictable
- Most of the newer models (gpt-4-turbo, gpt-4o) support multimodality
- Website, Setup Instructions

### Claude (by Anthropic)

- Recommended for users who want their AI chats to have a creative, unique writing style
- Requires prepayment for credits and charges per prompt
- The newest models (Claude 3) support multimodality
- Requires a specific prompting style and utilization of prefills for reply steering
- Website, Setup Instructions

### Google AI Studio and Vertex AI

- Has a free tier with rate limits (Gemini Flash), may require billing information
- AI Studio usually has the latest models and features
- Vertex AI is trickier to set up, but more stable
- Setup Instructions

### Mistral (by Mistral AI)

- Efficient models of various sizes and use cases. You can create an account and API key on their platform.
- From 32k to 128k context sizes for general use, and 32k to 256k context sizes for coding.
- Free Tier with rate limits.
- Reasonable moderation, with Mistral's main principles being to be neutral and empower users, more information here.
- Website, Setup Instructions

### OpenRouter

- Provides a unified API to access all the major LLMs on the market
- Pay-per-token credit system, as well as free models with limited daily requests
- No enforced moderation, unless required by the LLM vendor
- Website, Setup Instructions

### DeepSeek

- Provides access to the latest versions of very popular DeepSeek V3 (`deepseek-chat`) and DeepSeek R1 (`deepseek-reasoner`) models
- Requires a payment for credits ($2 minimum), but the models are fairly cheap for their quality
- No moderation on the API, but the models may refuse certain prompts
- Website, Setup Instructions

### AI21

- Provides access to Jamba Family open models
- Has a free trial ($10 for three months), then requires to pay monthly per token
- Website, Setup Instructions

### Cohere

- Provides access to the latest models from Cohere (command-r, command-a, c4ai-aya, etc.)
- Has a free tier (Trial Keys) with enough rate limits for casual use
- Website, Setup Instructions

### Perplexity

- Provides access to unique Perplexity Sonar online-enabled models via their API
- Requires to have billing configured and credits purchased
- Website, Setup Instructions

### Mancer AI

- Service that hosts unconstrained models of various families
- Uses 'credits' to pay for tokens on various models
- Does not log prompts by default, but you can enable it to get credit discounts on tokens.
- Uses an API similar to `Oobabooga TextGeneration WebUI`, see Mancer docs for details.
- Website, Setup Instructions

### DreamGen

- Uncensored models tuned for steerable creative writing
- Free monthly credits, as well as a paid subscription
- Models ranging from 7B to 70B
- Setup Instructions

### Pollinations

- Requires no setup, can be used out of the box
- Provides access to a wide range of models free of charge
- Outputs may occasionally include ads with links to third-party services

### NovelAI

- No content filter, the latest model is based on Llama 3
- Paid subscription required, the tier determines the max context length
- Website, Setup Instructions

### Electron Hub

- One API key unlocks models from multiple vendors (OpenAI, Anthropic, DeepSeek, etc.) for text and image generation
- $0.25 of free credits every day, paid plans available
- Website, Setup Instructions

### AI/ML API

- Unified API for 300+ models including Claude, GPT-4o, Gemini, LLaMA 3, Mistral and others
- Has a free tier with rate limits, subscription plans, and pay-as-you-go options
- Website, Docs, Models
