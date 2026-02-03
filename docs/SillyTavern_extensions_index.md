
# Extensions

SillyTavern comes with many extensions that can be enabled or disabled in the Extensions panel. Extensions can add new
features, change the behaviour of existing features, or provide additional content for your AI to use. More extensions
can be installed from the "Download Extensions & Assets" menu in the Extensions panel.

## Extensions panel

To open or close the Extensions panel, choose **<i class="fa-solid fa-cubes fa-fw"></i> Extensions** in the top bar.

- **<i class="fa-solid fa-cubes"></i> Manage extensions**: Activate, deactivate, and update extensions
- **Download Extensions & Assets**: Install more extensions, characters, sounds, and backgrounds from the SillyTavern repository
- **Notify on extension updates**: Check to be notified when there are updates available for installed extensions
- **<i class="fa-solid fa-cloud-arrow-down"></i> Install extension**: Import a third-party extension from a Git repository URL

## Built-in extensions

These extensions are built into SillyTavern and do not need to be installed. They can be enabled or disabled in the Extensions panel.

**[Chat Translation](SillyTavern_Translation.md)**

Translate chat messages to a different language

**[Image Captioning](SillyTavern_captioning.md)**

Generates text from images so your AI can "see" and respond to visual content in your conversations

**[Image Generation](SillyTavern_Stable-Diffusion.md)**

Use local or cloud-based Stable Diffusion, FLUX or DALL-E APIs to generate images

**[Expression Images](SillyTavern_Expression-Images.md)**

Images (aka 'sprites') of your AI character, shown next to or behind the chat window

**[Summarize](SillyTavern_Summarize.md)**

Auto-summary of the chat history

**[Chat Vectorization](SillyTavern_Chat-vectorization.md)**

Finds relevant messages from chat history and adds them into the context

**[Text To Speech](SillyTavern_TTS.md)**

Voice narration for your chat messages via ElevenLabs, Silero, your system TTS, **[AllTalk](SillyTavern_AllTalk.md)**, **[XTTS](SillyTavern_XTTS.md)**, and more

**[Quick Reply](SillyTavern_For_Contributors_st-script.md)**

Reply to chat messages with a single click, run commands and STscripts, and more

**Token Counter**

Converts text into tokens and counts the number of tokens

---

## Installable extensions

You **must** have git installed to download extensions. Follow the instructions on the Git installation page (https://git-scm.com/downloads) if you don't have it installed.

You can browse a list of all available extensions directly from the app by going to the **<i class="fa-solid fa-cubes"></i> Extensions** => **Download Extensions & Assets** menu and clicking the **<i class="fa-solid fa-plug-circle-exclamation"></i> Load Asset List** button. To install an extension, click the **<i class="fa-solid fa-download"></i> Download** button. To read more about an extension, click the **<i class="fa-solid fa-arrow-up-right-from-square"></i> Link** button next to its name to open its GitHub page.

Extensions are not Extras
The Extras project was discontinued in April 2024. You do not need to install Extras to use extensions.

**[Blip](SillyTavern_Blip.md)**

Animate the text of character messages with variable speed and play sound along the animation.

**[Dynamic Audio](SillyTavern_Dynamic-Audio.md)**

Adds immersive background music and ambient sounds to your chats.

**[EmulatorJS](SillyTavern_EmulatorJS.md)**

Play retro console games directly in SillyTavern chats.

**[Live2d](SillyTavern_Live2d.md)**

Adds support for live2d models. Customizable expressions, animations and interactions.

**[Objective](SillyTavern_Objective.md)**

Set an Objective for the AI to aim for during the chat.

**[RVC](SillyTavern_RVC.md)**

Adds Realtime Voice Cloning capabilities to the Text-to-Speech module.

**[Speech Recognition](SillyTavern_Speech-Recognition.md)**

Convert your speech to text using browser or extras.

**[VRM](SillyTavern_VRM.md)**

Adds support for VRM models. Customizable expressions, animations and interactions.

**[Web Search](SillyTavern_WebSearch.md)**

Adds web search results to LLM prompts.

**AccuWeather (https://github.com/SillyTavern/Extension-AccuWeather)**

Provides weather information using the AccuWeather API as a slash command or a function tool.

**Chat Top Bar (https://github.com/SillyTavern/Extension-TopInfoBar)**

Adds a top bar to the chat window with shortcuts to quick actions.

**Chess (https://github.com/SillyTavern/SillyTavern-Chess)**

Play the game of chess with the LLM.

**Code Runner (https://github.com/SillyTavern/Extension-CodeRunner)**

Allows running JavaScript and STscript code from code blocks in chat.

**D&D Dice (https://github.com/SillyTavern/Extension-Dice)**

A set of 7 classic D&D dice for all your dice rolling needs.

**Duplicate Finder (https://github.com/SillyTavern/Extension-DupeFinder)**

Adds an ability to cluster characters by similarity groups to easily find duplicates.

**Emoji Picker (https://github.com/SillyTavern/Extension-EmojiPicker)**

Adds a button to quickly insert emojis into a chat message.

**Group Greetings (https://github.com/SillyTavern/Extension-GroupGreetings)**

Allows setting alternate greetings that are specific to group chats.

**Group SendAs (https://github.com/SillyTavern/SillyTavern-GroupSendAs)**

Adds a button to quickly insert a /sendas command template for the selected group member.

**HypeBot (https://github.com/SillyTavern/Extension-HypeBot)**

Show personalized suggestions based on your recent chats using the NovelAI's HypeBot engine. Requires an active NovelAI subscription.

**Idle (https://github.com/SillyTavern/Extension-Idle)**

Adds "idle prompting" after the user has been idle for some time to organically continue the conversation.

**Image Metadata Viewer (https://github.com/SillyTavern/Extension-ImageMetadataViewer)**

View metadata of enlarged images attached to a chat.

**LaTeX (https://github.com/SillyTavern/Extension-LaTeX)**

Render LaTeX and AsciiMath formulas in chat messages.

**Mermaid (https://github.com/SillyTavern/Extension-Mermaid)**

Adds Mermaid diagrams & flowcharts rendering to SillyTavern chats.

**Notebook (https://github.com/SillyTavern/Extension-Notebook)**

Adds a place to store your notes. Supports rich text formatting.

**Parameter Randomizer (https://github.com/SillyTavern/Extension-Randomizer)**

Adds ability to randomize API settings sliders with every generation.

**Prome Visual Novel Extension (https://github.com/Bronya-Rand/Prome-VN-Extension)**

Enhances the current visual novel experience with more features (Focus Mode, Letterbox Mode, and more)!

**Prompt Inspector (https://github.com/SillyTavern/Extension-PromptInspector)**

Adds an option to inspect and edit output prompts before sending them to the server.

**Push Notifications (https://github.com/SillyTavern/SillyTavern-PushNotifications)**

Allows to receive push notifications for incoming chat messages.

**Quick Persona (https://github.com/SillyTavern/Extension-QuickPersona)**

Adds a dropdown menu for selecting user personas from the chat bar.

**RSS (https://github.com/SillyTavern/Extension-RSS)**

Gets the latest news from RSS feeds as a slash command or a function tool.

**Screen Share (https://github.com/SillyTavern/Extension-ScreenShare)**

Provides the screen image for multimodal models when you send a message.

**Silence Player (https://github.com/SillyTavern/Extension-Silence)**

Adds a silence audio player to the extensions menu. Can help if the browser tab is being killed in a background.

**Timelines (https://github.com/SillyTavern/SillyTavern-Timelines)**

Adds a timeline navigation to the chat history.

**Variable Viewer (https://github.com/LenAnderson/SillyTavern-Variable-Viewer)**

Easy way to view and modify variables.

**WebLLM (https://github.com/SillyTavern/Extension-WebLLM)**

Provides an interface for extensions to use language models directly in the browser.

## Third-party extensions

Using third-party extensions can have unintended side effects and may pose security risks. 
Always make sure you trust the source before importing an extension via **<i class="fa-solid fa-cloud-arrow-down"></i> Install extension**. 
We are not responsible for any damage caused by third-party extensions.

To install a third-party extension, go to the **<i class="fa-solid fa-cubes"></i> Extensions** => **<i class="fa-solid fa-cloud-arrow-down"></i> Install Extension** menu and paste the URL of the extension repository. Optionally, specify the branch and (in [multi-user](SillyTavern_Administration_multi-user.md) scenarios) the installation target: all users or just the current user. The extension will be downloaded and loaded automatically.
