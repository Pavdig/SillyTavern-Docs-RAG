
# Characters

Characters are the AI identities that you can create and manage to shape the AI's role in the conversation. Each
character has a name, personality, and conversation history. You can create as many characters as you like, and
switch between them at any time.

Characters can be used in solo chats, or add multiple characters to a group chat to
let them interact with each other.

## Character Management Panel

Open the  **Characters** panel from the navbar to access the character
list. Click on a character or group to chat with them or edit them, or
choose  **Create New Character** to add a new character.

### Panel Controls

*  **Pin Panel**: Keep panel open while interacting
*  **Character List**: Return to character list view
* **HotSwap Bar**: Quick access to favorite characters

### Character List

*  **Create New Character**: Add a new character
*  **Import Character**: Load character from file
*  **External Import**: Import from URL
*  **Create Group**: Start a new group chat

#### Search and sort

* **Search Bar**: Filter characters by name or attributes
* **Sort Dropdown**: Multiple sorting options:
    - Alphabetical (A-Z, Z-A)
    - Chronological (Newest, Oldest)
    - Usage-based (Recent, Most/Least chats)
    - Size-based (Most/Least tokens)
    - Special (Favorites, Random)

#### Filter characters by type or tag

*  **Favorites Filter**: Show favorite characters
*  **Groups Filter**: Show only group chats
*  **Tags as Folders**: Organize by tag hierarchy
*  **Manage Tags**: [Tag configuration](SillyTavern_Usage_Characters_Tags.md)
*  **Tag List**: View all available tags
*  **Clear Filters**: Reset all filters

### Character Creation/Edit Panel

* **Avatar Image**: Upload and preview character profile picture
* **Token Count**: [Token usage](SillyTavern_characterdesign.md) for the character
*  **Stats**: Chat history and usage statistics
* [Tag management](SillyTavern_Usage_Characters_Tags.md)

#### Quick Actions

-  Favorite toggle
-  Advanced definitions
-  Character lore
-  Chat lore: link the chat to a [World Info](SillyTavern_Usage_worldinfo.md)
-  Export character
-  Duplicate
-  Delete

#### Extended Options

* World Info linking
* Card lore import
* Scenario override
* Persona conversion
* Character rename
* Source linking
* Replace/Update
* Tag import
* Gallery view

#### Content Fields

* **[Character Description](SillyTavern_characterdesign.md)**: Brief character summary
* **[First Message](SillyTavern_characterdesign.md)**: Initial greeting or prompt when starting a new chat
* **Alternative greetings**: Define multiple first messages that you can swipe between when starting a chat

### Advanced Definitions Panel

Click on the  **Advanced Definitions** button to access the extended character settings.

#### Prompt Overrides (Chat Completion/Instruct Mode)

* **Main Prompt**: Replaces default [main/system prompt](SillyTavern_Usage_Prompts_index.md), can use
  \{\{original\}\} placeholder to include the original prompt
* **Post-History Instructions**: Overrides
  default [post-history instructions](SillyTavern_Usage_Prompts_index.md)

#### Creator's Metadata

Non-prompt information about the character:

- Creator name/contact
- Character version
- Creator's notes
- Embedded tags list

#### Character Personality

* **[Personality Summary](SillyTavern_characterdesign.md)**: Brief overview of character's traits
* **[Scenario](SillyTavern_characterdesign.md)**: Context and circumstances of the dialog
* **Character's Note**: Custom message with selectable depth and message role (also
  see [Author's Note](SillyTavern_Usage_Characters_Author's-Note.md))
* **Talkativeness** (Group Chats): Slider for Shy → Normal → Chatty
* **Example Messages**: Examples of character's writing style

### Group Chat Management

If this is a group chat, you can manage the group members and settings from this panel.

See [Group Chats](SillyTavern_Usage_Characters_groupchats.md) for more details.
