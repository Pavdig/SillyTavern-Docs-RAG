# SILLYTAVERN DOCUMENTATION
# Context: This file contains the full, flattened documentation for SillyTavern.
# Structure: Each section below corresponds to a file from the official docs.

# SECTION: SillyTavern_readme

# What is SillyTavern?

SillyTavern (or ST for short) is a locally installed user interface that allows you to interact with text generation LLMs, image generation engines, and TTS voice models. Our goal is to empower users with as much utility and control over their LLM prompts as possible, embracing the steep learning curve as part of the fun.

SillyTavern is a passion project brought to you by a dedicated community of LLM enthusiasts and will always be free and open-sourced. Beginning in February 2023 as a fork of TavernAI 1.2.8, SillyTavern now has over 300 contributors and 3 years of independent development under its belt, and continues to serve as a leading software for savvy AI hobbyists.

## Installation Requirements

The hardware requirements are minimal: it will run on anything that can run NodeJS 18 or higher. If you intend to do LLM inference on your local machine, we recommend a 3000-series NVIDIA graphics card with at least 6GB of VRAM.

Follow the installation guide for your platform:

* Windows
* Linux and Mac
* Android
* Docker

## Branches

SillyTavern is being developed using a two-branch system to ensure a smooth experience for all users.

* `release` -🌟 **Recommended for most users.** This is the most stable and recommended branch, updated only when major releases are pushed. It's suitable for the majority of users. Typically updated once a month.
* `staging` - ⚠️ **Not recommended for casual use.** This branch has the latest features, but be cautious as it may break at any time. Only for power users and enthusiasts. Updates several times daily.

## What do I need other than SillyTavern?

Since SillyTavern is only an interface, you will need access to an LLM backend to provide inference. You can use AI Horde for instant out-of-the-box chatting. Aside from that, we support many other local and cloud-based LLM backends: OpenAI-compatible API, KoboldAI, Tabby, and many more. You can read more about our supported APIs in the API Connections section.

## Character Cards

SillyTavern is built around the concept of "character cards". A character card is a collection of prompts that set the behavior of the LLM and is required to have persistent conversations in SillyTavern. They function similarly to ChatGPT's GPTs or Poe's bots. The content of a character card can be anything: an abstract scenario, an assistant tailored for a specific task, a famous personality or a fictional character.

To have a quick conversation without selecting a character card or to just test the LLM connection, simply type your prompt input into the input bar on the Welcome Screen after opening SillyTavern. This will create an empty "Assistant" character card that you can customize later.

To get a general idea on how to define character cards, see the default character (Seraphina) or download selected community-made cards from the "Download Extensions & Assets" menu.

You can also create your own character cards from scratch. Refer to the Character Design guide for more information.

## Key Features

* Advanced text generation settings with many community-made presets
* World Info support: create rich lore or save tokens on your character card
* Group chats: multi-bot rooms for characters to talk to you and/or each other
* Rich UI customization options: theme colors, background images, custom CSS, and more
* User personas: let the AI know a bit about you for greater immersion
* Built-in RAG support: add documents to your chats for the AI to reference
* Extensive chat commands subsystem and own scripting engine

## Extensions

SillyTavern has extensibility support.

* Character emotional expressions (sprites)
* Auto-Summary of the chat history
* Automatic UI and chat translation
* Stable Diffusion/FLUX/DALL-E image generation
* Text-to-speech for AI response messages
* Web Search capabilities for adding additional real world context to your prompts
* Many more are available to download from the "Download Extensions & Assets" menu.

## How can I get in touch with the developers directly?

* Discord: cohee, rossascends, wolfsblvt
* Reddit: /u/RossAscends (https://www.reddit.com/user/RossAscends/), /u/sillylossy (https://www.reddit.com/user/sillylossy/), u/Wolfsblvt (https://www.reddit.com/user/Wolfsblvt/)
* Post a GitHub issue (https://github.com/SillyTavern/SillyTavern/issues)

## I like your project! How do I contribute?

* We welcome pull requests! Follow the Contribution Guidelines (https://github.com/SillyTavern/SillyTavern/blob/release/CONTRIBUTING.md) to get started.
* We also welcome helpful and informed bug reports that use the templates provided in our GitHub.
* We do not accept monetary donations for the project itself.

## Personal Donations

Your support for individual contributors is appreciated, but it will not influence the overall development direction of SillyTavern.

* RossAscends has a personal Patreon (https://www.patreon.com/RossAscends) & Kofi (https://ko-fi.com/rossascends)

## License

SillyTavern is a free and open-source project released under the AGPL-3.0 License (https://github.com/SillyTavern/SillyTavern/blob/release/LICENSE).

# SECTION: SillyTavern_extensions_Extras_Installation

# Extras Installation

This page contains instructions for installing SillyTavern Extras on your local device.

**Discontinued**

The Extras project was discontinued in April 2024 and won't receive any new updates or modules. The vast majority of modules are available natively in the main SillyTavern application. You may still install and use it but don't expect to get immediate support if you face any issues.

**Local installation of Extras can be difficult or impossible on your OS (especially Termux).**

## Use the Official Extras Colab (https://colab.research.google.com/github/SillyTavern/SillyTavern/blob/release/colab/GPU.ipynb)

* Simple to set up
* Free to use
* No Colab GPU credits required (use the `use_cpu` options)
* See the Colab Guide Page for details.

### Running Extras in Colab

* Open the Official Extras Colab (https://colab.research.google.com/github/SillyTavern/SillyTavern/blob/release/colab/GPU.ipynb)
* Select the desired "Extra" options
* select `use_cpu` to run Extras without requiring GPU credit
  * this will make Stable Diffusion slower, but everything else will run normally
* Not required, but recommended: select the `secure` option to generate the API key to protect your shared instance.
* Click the Start button on the left (looks like a triangle 'play' button)
* Wait for it to finish loading everything
* Look for the `trycloudflare.com` link at the bottom of the output. Ignore the localhost link, it won't work (we tried!).
* It will start with the text `Running on`
* Copy the API URL link that is listed under that line. (**DO NOT copy the 'localhost' URL, use the other one**)
* Start SillyTavern with extensions support: (set `enableExtensions` to `true` in your `config.yaml` if necessary)
* Navigate to SillyTavern's Extensions menu (click the 'stacked blocks' icon at the top of the page).
* Paste the API URL into the box at the top. (**NOT the API Key box**)
* If you have NOT enabled the `secure` option, make sure the API Key box is completely empty when using the official colab.
* If you have enabled the `secure` option, paste the generated API key into the API Key box.
* API key will appear in the colab's console output, for example: `Your API key is fee2f3f559`
* Click "Connect"

---

## Local Installation Methods

### MiniConda (recommended)

This method is recommended because Conda makes a 'virtual environment' for the Extras requirement packages to live inside, so they do not affect your system-wide Python setup.

1. Install Miniconda (https://docs.conda.io/en/latest/miniconda.html)

    _(Important!) Read how to use Conda (https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)_

2. Install git (https://git-scm.com/downloads)

    _(Chads who installed SillyTavern with git to begin with can skip this step!)_
    
    After you have both of them installed...
    
    Type/paste the commands below `ONE BY ONE` IN THE `CONDA COMMAND PROMPT WINDOW` and hit `Enter` after each one.

3. Create a new Conda environment (let's call it `extras`):

    `conda create -n extras`

4. Activate the new environment

    `conda activate extras` (you should see `(extras)` pop up on the left side of your command prompt)

5. Install the required system packages (this will take some time)

    `conda install python=3.11 git`

6. Clone the Extras GitHub repo

    `git clone https://github.com/SillyTavern/SillyTavern-extras`

7. Navigate to your cloned Extras repo

    `cd SillyTavern-extras`

8. Install Extras' requirements by using **one** of the following commands (will take time, again):

   * `pip install -r requirements.txt` - for basic features
   * `pip install -r requirements-rvc.txt` - for real-time voice cloning
   * `pip install -r requirements-coqui.txt` - for Coqui TTS (not recommended)

    See the Common Problems page if you get errors at this step!

9. See below 'Running Extras After Install'

---

### System-Wide Installation

This is easier, but will affect your system-wide Python installation.

This can cause conflicts if you work with many Python programs that have different requirements.

If this is your first time touching anything Python-related, that should not be a problem.

1. Install Python 3.11: <https://www.python.org/downloads/release/python-3115/>
2. Install git: <https://git-scm.com/downloads>
3. Open a command prompt window and go to a folder in which you have complete access permissions.
4. Clone the repo: `git clone https://github.com/SillyTavern/SillyTavern-extras`, hit Enter.
5. After the clone has finished, type `cd SillyTavern-extras`, hit Enter.
6. Type `python -m pip install -r requirements.txt`
7. See below 'Running Extras After Install'

---

## Running Extras After Install

### Confirm extensions are enabled

1. Open the file called `config.yaml` in a text editor. The file is located in ST's base install folder.
2. Look for the line that reads `enableExtensions`.
3. Make sure that line has `true`, and not `false`.

### Decide which module to use

(This only needs to be done once)

* Extras is always started with a Python command line.
* `python server.py` is the bare minimum, but it does not enable any useful modules.
* to enable modules you must use the `--enable-modules=` modifier, with a comma-separated list of module names

Example: `python server.py --enable-modules=caption,summarize,classify`

This would enable Image Captioning, Chat Summary, and live updating Character Expressions.

Below is a table that describes each module.

| Name         | Description                                                         |
|--------------|---------------------------------------------------------------------|
| `caption`    | Image captioning                                                    |
| `summarize`  | Text summarization                                                  |
| `classify`   | Text sentiment classification                                       |
| `sd`         | Stable Diffusion image generation                                   |
| `silero-tts` | Silero TTS server (https://github.com/ouoertheo/silero-api-server) |
| `edge-tts`   | Microsoft Edge TTS client (https://github.com/rany2/edge-tts)      |
| `chromadb`   | Vector storage server                                               |
| `coqui-tts`  | Coqui TTS                                                           |
| `rvc`        | Real-time voice cloning                                             |

* Decide which modules you want to add to your Python command line.
* They will be used in the next step.

**NOTE: There must be `no spaces at all in your Python command's module list!`**

### Start Extras Server

While still in your command prompt window inside the Extras installation folder...

1. Make sure your conda environment is active (if you used the Conda install method)
2. Type `activate extras` if the environment is not active.
3. Type `python server.py --enable-modules=YOUR,SELECTED,MODULE,LIST,HERE`
4. The extras server will load.
5. After a while it will show you a URL at the end. For local installs, this defaults to `http://localhost:5100`.
6. Copy the API URL.

### Connect ST to the Extras server

1. Start your SillyTavern server, and view the SillyTavern interface in your browser.
2. Open the Extensions panel (via the 'Stacked Blocks' icon at the top of the page)
3. Paste the API URL into the input box.
4. Click `Connect`.

To run Extras again, simply activate the environment and run these commands in a command prompt.

`conda activate extras`, Hit Enter.
`python server.py`, Hit Enter.

Be sure to use the additional options for server.py (see below) that your setup requires.

## Make a .bat File for Easy Startup

This is Optional and only applies to Windows, but something similar should be possible on MacOS.

1. View your Windows Desktop
2. Right-click, select `New`, and then click `Text Document`
3. A new file will appear on your Desktop, asking for a name.
4. Name the file `STExtras.txt`
5. Open the newly created file in a text editor.
6. Paste the following code into it:

    ```
    cd C:\_your_\_full_\_Extras_\_folder_\_path_\
    call conda activate extras
    python server.py --enable-modules=YOUR,SELECTED,MODULE,LIST,HERE,WITH,NO,SPACES
    call conda deactivate
    pause
    ```

7. Replace the placeholder folder path with your actual Extras install folder path.
8. Replace the python command line with your actual command line
9. Save the file with a new name `STExtras.bat` (Use `File` >> `Save As` in most text editors)

You can now simply double-click on this .bat file to easily start Extras.

If you ever want to change the module list (or any other command line modifiers for the extras server), simply edit the python command inside the .bat file.

## Extras Install Common Problems

This section lists common questions and problems encountered while installing SillyTavern Extras.

### Error: Could not import the 'talkinghead' module on Linux

It requires the installation of an additional package because it's not installed automatically due to incompatibility with Colab. Run this after you install other requirements:

`pip install wxpython`

### Extras server can't connect to AUTOMATIC1111's Stable Diffusion Web UI

> Could not connect to remote SD backend at <http://127.0.0.1:7860>! Disabling SD module...

**Make sure webui-user.bat that you start Stable Diffusion with contains --api command line option in the COMMANDLINE_ARGS variable.**

Find and replace that line in your "webui-user.bat": `set COMMANDLINE_ARGS=--api`

If the API mode is disabled for SD Web UI, the Extras server won't be able to make a connection and you won't be able to generate images!

#### Still doesn't work?

Ensure that you start everything in the proper order, waiting for every program to finish loading before proceeding to the next step:

1. Stable Diffusion Web UI
2. SillyTavern Extras
3. SillyTavern

The extras server can't reconnect to the Stable Diffusion API if it was loaded after.

### hnswlib wheel building error when installing ChromaDB

> ERROR: Could not build wheels for hnswlib, which is required to install pyproject.toml-based projects

Before installing the ChromaDB module you must first do `one of the following`:

* Install Visual C++ build tools: <https://visualstudio.microsoft.com/visual-cpp-build-tools/>
* Install the `hnswlib` package with conda: `conda install -c conda-forge hnswlib`

---

### Error when installing Python requirements on Mac

> ERROR: No matching distribution found for torch==2.0.0+cu117

Mac does not support CUDA, so torch packages should be installed without CUDA support.

Install the requirements using the `requirements-silicon.txt` file instead.

---

### Missing modules?

* You must specify a list of module names in your Python command line, with the `--enable-modules` modifier.
* See Modules section.

---

### What is the API Key box for?

* The API Key box in SillyTavern's Extensions panel is only used when you have:
  * created a text file named `api_key.txt` in your Extras install folder, which contains your chosen Extras 'password'.
  * started extras with the `--secure` commandline argument.
* This makes the Extras API 'password locked', so only users who have that key in their API Key box can access it.
* This is mainly useful for people who want to make their own public deployment of Extras (colab, etc).
* Users running Extras on their own PC for personal use should not type anything into the API Key box.

### What about mobile/Android/Termux? 🤔

* There are some folks in the community having success running Extras on their phones via Ubuntu on Termux.
* However, Extras were not made with mobile support in mind.
* No support will be provided for people running Extras on their Android devices.
* Direct all your questions to the creator of the guide linked below instead.

#### ❗ This is UNSUPPORTED

<https://rentry.org/STAI-Termux#downloading-and-running-tai-extras>

# SECTION: SillyTavern_Installation_Android

# Android (Termux) Installation

SillyTavern can be run natively on Android devices using Termux.

## Installing Termux

Avoid installing Termux from the Google Play Store, that version is no longer maintained. 
Instead, use F-Droid (recommended) or GitHub releases to get the latest version.

**1. Download Termux from F-Droid (https://f-droid.org/en/packages/com.termux/) or GitHub releases (https://github.com/termux/termux-app/releases).**

2. Install the downloaded APK file.
3. Open Termux and run your first command:

   ```bash
   termux-change-repo
   ```

4. Select "Mirror group" and choose your closest servers. You can touch the screen or use swipe gestures with Unexpected Keyboard (https://play.google.com/store/apps/details?id=juloo.keyboard2&hl=en).
5. Update Termux:

   ```bash
   pkg update && pkg upgrade
   ```

## Installing Dependencies

Install the required packages:

```bash
pkg install git nodejs-lts nano
```

If you're running 32-bit Android, see the Common Errors section below for additional steps.

**## Installing SillyTavern**

Clone the SillyTavern repository (How to Choose a Branch):

- **Release Branch:**

    ```bash
    git clone https://github.com/SillyTavern/SillyTavern -b release
    ```

- **Staging Branch:**

    ```bash
    git clone https://github.com/SillyTavern/SillyTavern -b staging
    ```

## Running SillyTavern

To run SillyTavern, navigate to the cloned directory and run the start script:

```bash
cd ~/SillyTavern
bash start.sh
```

To update SillyTavern, navigate to the SillyTavern directory and run:

```bash
cd ~/SillyTavern
git pull --rebase --autostash
```

See the Aliases section below for creating shortcuts to simplify this process.

## Common Errors

### Unsupported platform: android arm LEtime-web

32-bit Android requires an external dependency that can't be installed with npm.

Use the following command to install it:

```bash
pkg install esbuild
```

Then proceed with the installation steps above.

### Performance tweaks

For general tips on improving performance, see the respective FAQ section.

**Due to hardware limitations on Android devices, you may want to adjust the following SillyTavern config.yaml settings for better memory, storage, and CPU usage:**

```yaml
performance:
  # Avoid loading all character data until needed
  lazyLoadCharacters: true
  # Disable disk caching to reduce storage usage
  useDiskCache: false
backups:
  chat:
    # Optional: Disable automatic chat backups to save storage
    enabled: false
```

Use the `nano` text editor included with Termux to edit the `config.yaml` file: `nano ~/SillyTavern/config.yaml`

**## Optional: Create Aliases**

You can create shortcuts for common commands to make your workflow easier.

1. Open an editor to modify your `.bashrc` file:

   ```bash
   nano ~/.bashrc
   ```

2. Add the following lines to create aliases:

   ```bash
   # Update Termux packages
   alias pkgup="pkg update && pkg upgrade"
   #Start SillyTavern
   alias st='cd ~/SillyTavern && bash start.sh'
   # Update SillyTavern
   alias stup='cd ~/SillyTavern && git pull --rebase --autostash'
   ```

3. Save the file and exit the editor (in nano, press `CTRL + X`, then `Y`, then `Enter`).

4. To apply the changes, run:

   ```bash
   source ~/.bashrc
   ```

Now you can use the following commands:

- `st` to start SillyTavern
- `stup` to update SillyTavern
- `pkgup` to update Termux packages

## Further Reading

The guides linked below are not maintained by the SillyTavern team.

**- SillyTavern in Termux guide by ArroganceComplex#2659: <https://rentry.org/STAI-Termux>**

- Accessing Termux files with Material Files: <https://www.learntermux.tech/2020/10/Termux-File-Manager.html>
- Prevent Termux process deep sleep: <https://wiki.termux.com/wiki/Termux-wake-lock>

# SECTION: SillyTavern_Installation_Docker

# Docker Installation

**These instructions assume you have installed Docker, are able to access your command line for the installation of containers, and familiar with their general operation.**

**## Using the GitHub Container Registry**

Using a prebuilt image is the quickest and easiest way to get started with SillyTavern in Docker. You can pull the latest image from the GitHub Container Registry.

### Docker Compose (recommended)

Download the `docker-compose.yml` file from the GitHub Repository (https://github.com/SillyTavern/SillyTavern/blob/release/docker/docker-compose.yml) and run the following command in the directory where the file is located. This will pull the latest release image from the GitHub Container Registry and start the container, automatically creating the necessary volumes.

```sh
docker compose up
```

You can edit the file and apply additional customization to suit your needs:

- The default port is 8000. You can change it by modifying the `ports` section.
- Change the `image` tag to `staging` if you want to use the development branch instead of the stable release.
- If you want to adjust the server configuration using environment variables, check the Environment Variables page.

### Docker CLI (advanced)

You will need two mandatory directory mappings and a port mapping to allow SillyTavern to function. In the command, replace your selections in the following places:

#### Container Variables

##### Volume Mappings

- `CONFIG_PATH` - The directory where SillyTavern configuration files will be stored on your host machine
- `DATA_PATH` - The directory where SillyTavern user data (including characters) will be stored on your host machine
- `PLUGINS_PATH` - (optional) The directory where SillyTavern server plugins will be stored on your host machine
- `EXTENSIONS_PATH` - (optional) The directory where global UI extensions will be stored on your host machine

##### Port Mappings

- `PUBLIC_PORT` - The port to expose the traffic on. This is mandatory, as you will be accessing the instance from outside of its virtual machine container. DO NOT expose this to the internet without implementing a separate service for security.

##### Additional Settings

- `SILLYTAVERN_VERSION` - On the GitHub Packages page (https://github.com/SillyTavern/SillyTavern/pkgs/container/sillytavern) you'll see the list of tagged image versions. The image tag "latest" will keep you up-to-date with the current release. You can also utilize "staging" that points to the nightly image of the respective branch.

#### Running the container

1. Open your Command Line
2. Run the following command in a folder where you want to store the configuration and data files:

```bash
SILLYTAVERN_VERSION="latest"
PUBLIC_PORT="8000"
CONFIG_PATH="./config"
DATA_PATH="./data"
PLUGINS_PATH="./plugins"
EXTENSIONS_PATH="./extensions"

docker run \
  --name="sillytavern" \
  -p "$PUBLIC_PORT:8000/tcp" \
  -v "$CONFIG_PATH:/home/node/app/config:rw" \
  -v "$DATA_PATH:/home/node/app/data:rw" \
  -v "$EXTENSIONS_PATH:/home/node/app/public/scripts/extensions/third-party:rw" \
  -v "$PLUGINS_PATH:/home/node/app/plugins:rw" \
  ghcr.io/sillytavern/sillytavern:"$SILLYTAVERN_VERSION"
```

By default the container will run in the foreground. If you want to run it in the background, add the `-d` flag to the `docker run` command.

**## Building the Docker Image**

The following section assumes you installed SillyTavern in a non-root (non-admin) folder. If you installed SillyTavern in a root folder, you may have to run some of these commands with administrator rights [`sudo`, `doas`, Command Prompt (Administrator)].

**If you want to build the Docker image yourself, you can do so by following these steps. This is useful if you want to customize the image or use it for development purposes.**

### Linux

1. Install Docker by following the Docker installation guide here (https://docs.docker.com/engine/install/).

   **Do not** install Docker Desktop.

**2. Follow the steps in **Manage Docker as a non-root user** in the Docker Post-Installation Guide (https://docs.docker.com/engine/install/linux-postinstall/).**

3. Install Git (https://git-scm.com/download/linux) using your package manager.

    - Debian (Ubuntu/Pop! OS/etc.)

        ```sh
        sudo apt install git
        ```

    - Arch Linux (Manjaro/EndeavourOS/etc.)

        ```sh
        sudo pacman -S git
        ```

    - Fedora, Red Hat Enterprise Linux (RHEL), etc.
        ```sh
        sudo dnf install git
        ```

4. Clone the SillyTavern repository.

    - Release (Stable Branch)

        ```sh
        git clone https://github.com/SillyTavern/SillyTavern && cd SillyTavern/docker
        ```

    - Staging (Development Branch)
        ```sh
        git clone https://github.com/SillyTavern/SillyTavern -b staging && cd SillyTavern/docker
        ```

5. Execute `docker compose` by running the following command within the Docker folder.

    ```sh
    docker compose up -d
    ```

6. Open a new browser and go to http://localhost:8000 (http://localhost:8000). You should see SillyTavern load in a few moments.

### Windows

**Regarding Docker on Windows**

Using Docker on Windows is **_really_** complicated. Not only do you need to activate _Windows Subsystem for Linux_ within _Turn Windows features on or off_, but also configure your system for Virtualization (Intel VT-d/AMD SVM) which differs from PC manufacturer to PC manufacturer (or motherboard manufacturer). Sometimes, this option is not present on some systems.

It is highly suggested you install SillyTavern by following our Windows guide. This section is a _rough_ idea of how it can be done on Windows.

**1.  Install Docker Desktop by following the Docker installation guide here (https://docs.docker.com/desktop/setup/install/windows-install/).**

2.  Install Git for Windows (https://git-scm.com/download/win).
3.  Clone the SillyTavern repository.

    -   Release (Stable Branch)

        ```sh
        git clone https://github.com/SillyTavern/SillyTavern && cd SillyTavern/docker
        ```

    -   Staging (Development Branch)
        ```sh
        git clone https://github.com/SillyTavern/SillyTavern -b staging && cd SillyTavern/docker
        ```

4.  Execute `docker compose` by running the following command within the Docker folder.

    ```sh
    docker compose up -d
    ```

5.  Open a new browser and go to http://localhost:8000 (http://localhost:8000). You should see SillyTavern load in a few moments.

### macOS

**Even though macOS is similar to Linux, it doesn't have the Docker Engine. You will have to install Docker Desktop similarly to Windows.**

You will also need to install Homebrew (https://brew.sh/) in order to install Git on your Mac. This section is a _rough_ idea on how it can be done on macOS.

**1.  Install Docker Desktop by following the Docker installation guide here (https://docs.docker.com/desktop/setup/install/mac-install/).**

2.  Install `git` using Homebrew.

    ```sh
    brew install git
    ```

3.  Clone the SillyTavern repository.

    -   Release (Stable Branch)

        ```sh
        git clone https://github.com/SillyTavern/SillyTavern && cd SillyTavern/docker
        ```

    -   Staging (Development Branch)
        ```sh
        git clone https://github.com/SillyTavern/SillyTavern -b staging && cd SillyTavern/docker
        ```

4.  Execute `docker compose` by running the following command within the Docker folder.

    ```sh
    docker compose up -d
    ```

5.  Open a new browser and go to http://localhost:8000 (http://localhost:8000). You should see SillyTavern load in a few moments.

## Configuring SillyTavern

SillyTavern's configuration file (config.yaml) will be located within the `config` folder. Configuring the config file should be no different than configuring it without Docker, however you will need to run `nano` or a code editor with administrator rights in order to save your changes.

Don't forget to restart the Docker container for SillyTavern in order to apply your changes! Make sure you execute this command within the `docker` folder.

```sh
docker compose restart sillytavern
```

**## Locating User Data**

SillyTavern's data folder will be within the `data` folder. Backing up your files should be easy to do, however, restoring or adding content into it may require you to do so with administrator rights.

## Running Server Plugins

Running plugins like HoYoWiki-Scraper-TS (https://github.com/Bronya-Rand/HoYoWiki-Scraper-TS) or SillyTavern-Fandom-Scraper (https://github.com/SillyTavern/SillyTavern-Fandom-Scraper) within Docker is no different from running it on your system without Docker, however we will need to do a slight modification to the Docker Compose script in order to do so.

If you already see a _plugins_ folder within the `docker` folder, you can skip Steps 1-2.

**1. Using `nano` or a code editor, open _docker-compose.yml_ and add the following line below `volumes`.**

    ```sh
        volumes:
            - "./config:/home/node/app/config"
            - "./data:/home/node/app/data"
            - "./plugins:/home/node/app/plugins"
    ```

2. Create a new folder within the `docker` folder called _plugins_.
3. Follow your plugin's instructions on installing the plugin.
4. Using `nano` or a code editor with administrator rights, open _config.yaml_ (within the `config` folder) and enable `enableServerPlugins`

    ```sh
    enableServerPlugins: true
    ```

5. Restart the Docker container.

    ```sh
    docker compose restart sillytavern
    ```

## Non-root user mode

By default, the container runs as root. If you want files created in mounted volumes to be owned by a specific host user (for example, to avoid root-owned files), you can enable non-root mode.

### Option 1: PUID/PGID (recommended)

Set `PUID` and `PGID` environment variables to the UID/GID you want the container to use. The entrypoint will update ownership of required directories and then run the server as the mapped user.

Docker Compose example:

```yaml
services:
  sillytavern:
    environment:
      - PUID=1000
      - PGID=1000
```

Docker CLI example:

```bash
docker run \
  --name="sillytavern" \
  -e PUID=1000 \
  -e PGID=1000 \
  -p "$PUBLIC_PORT:8000/tcp" \
  -v "$CONFIG_PATH:/home/node/app/config:rw" \
  -v "$DATA_PATH:/home/node/app/data:rw" \
  -v "$EXTENSIONS_PATH:/home/node/app/public/scripts/extensions/third-party:rw" \
  -v "$PLUGINS_PATH:/home/node/app/plugins:rw" \
  ghcr.io/sillytavern/sillytavern:"$SILLYTAVERN_VERSION"
```

### Option 2: Docker `--user` flag

You can also run the container as a specific user with Docker's `--user` flag. In this mode, the container cannot automatically fix permissions, so ensure your mounted volumes are already writable by the UID/GID you provide.

```bash
docker run \
  --name="sillytavern" \
  --user 1000:1000 \
  -p "$PUBLIC_PORT:8000/tcp" \
  -v "$CONFIG_PATH:/home/node/app/config:rw" \
  -v "$DATA_PATH:/home/node/app/data:rw" \
  -v "$EXTENSIONS_PATH:/home/node/app/public/scripts/extensions/third-party:rw" \
  -v "$PLUGINS_PATH:/home/node/app/plugins:rw" \
  ghcr.io/sillytavern/sillytavern:"$SILLYTAVERN_VERSION"
```

## Container Healthcheck

The Docker image includes a built-in healthcheck mechanism that monitors the SillyTavern server's responsiveness. This is useful for container orchestration systems (like Docker Compose, Kubernetes, or Docker Swarm) to detect and automatically restart unresponsive containers.

### How it works

The healthcheck uses a heartbeat file mechanism:

1. When enabled, the SillyTavern server periodically writes a timestamp to a `heartbeat.json` file in the data directory.
2. The healthcheck script (`src/healthcheck.js`) verifies that the heartbeat file exists and was recently updated.
3. If the heartbeat file is missing or too old (more than 2 missed intervals), the container is marked as unhealthy.

### Configuration

The healthcheck script doesn't support overriding the data directory via command line arguments. If you change the data directory from the default `/home/node/app/data`, ensure that the `SILLYTAVERN_DATAROOT` environment variable is set accordingly.

**The healthcheck is controlled by the `SILLYTAVERN_HEARTBEATINTERVAL` environment variable (or `heartbeatInterval` in config.yaml). This value specifies the interval in seconds between heartbeat writes.**

- **Default:** `0` (disabled)
- **Recommended:** `30` seconds when using Docker healthchecks

The default `docker-compose.yml` file includes healthcheck configuration with the heartbeat enabled:

```yaml
services:
  sillytavern:
    environment:
      - SILLYTAVERN_HEARTBEATINTERVAL=30
    healthcheck:
      test: ["CMD", "node", "src/healthcheck.js"]
      interval: 30s
      timeout: 10s
      start_period: 20s
      retries: 3
```

### Checking container health status

You can check the health status of your container using:

```sh
docker inspect --format='{{.State.Health.Status}}' sillytavern
```

Or view the full container status including health:

```sh
docker ps
```

The `STATUS` column will show `healthy`, `unhealthy`, or `starting` alongside the uptime.

### Disabling the healthcheck

If you don't need the healthcheck feature, you can disable it by:

1. Setting the environment variable to `0`:

    ```yaml
    environment:
      - SILLYTAVERN_HEARTBEATINTERVAL=0
    ```

2. Removing or commenting out the `healthcheck` section in your `docker-compose.yml`.

## Common issues with Docker

### SELinux Permission Issues with Mounted Volumes

Linux distributions with SELinux enabled (such as RHEL, CentOS, Fedora, etc.) may prevent Docker containers from accessing mounted volumes due to security policies. This can result in permission denied errors when the container tries to read or write to the mounted directories.

Two suffixes `:z` or `:Z` can be added to the volume mount. These suffixes tell Docker to relabel file objects on the shared volumes.

- The `z` option is used when the volume content will be shared between containers.
- The `Z` option is used when the volume content should only be used by the current container.

Example:

```yaml
# docker-compose.yml
volumes:
  ## Shared volume
  - ./config:/home/node/app/config:z
  ## Private volume
  - ./data:/home/node/app/data:Z
```

### Forbidden by Whitelist

**Docker gateway IPs should be whitelisted automatically if whitelistDockerHosts config value is set to `true`.**

If you are still unable to access SillyTavern, follow the instructions below to update the whitelist manually.

**1. Execute the following Docker command to obtain the IP of your SillyTavern Docker container.**

    ```sh
    docker network inspect docker_default
    ```

    You should receive some sort of output similar to the following below.

    ```json
    [
        {
            "Name": "docker_default",
            "IPAM": {
                "Config": [
                    {
                        "Subnet": "172.18.0.0/16",
                        "Gateway": "172.18.0.1"
                    }
                ]
            }
        }
    ]
    ```

    Copy down the IP you see in _Gateway_ as this will be important.

2. Running a text editor of your choice with administrator rights, go to `config` and open `config.yaml`.

    Within your editor, go down to the `whitelist` section. You should see something similar to the following below.

    ```yaml
    whitelist:
        - 127.0.0.1
    ```

    Add a new line below _127.0.0.1_ and put in the IP you copied from Docker. It should look something similar to the following afterwards.

    ```yaml
    whitelist:
        - 127.0.0.1
        - 172.18.0.1
    ```

    Save the file and exit the text editor.

    Note that if you configured Docker network as a bridge, you could also add external IP addresses to the whitelist as usual.

**3. Restart the Docker Container to apply the new configuration.**

    ```sh
    docker compose restart sillytavern
    ```

# SECTION: SillyTavern_Installation_index

# Installation

Follow the installation guide for your platform:

* Windows
* Linux and Mac
* Android
* Docker

## Branches

SillyTavern is being developed using a two-branch system to ensure a smooth experience for all users.

* `release` -🌟 **Recommended for most users.** This is the most stable and recommended branch, updated only when major releases are pushed. It's suitable for the majority of users. Typically updated once a month.
* `staging` - ⚠️ **Not recommended for casual use.** This branch has the latest features, but be cautious as it may break at any time. Only for power users and enthusiasts. Updates several times daily.

## Global / Standalone mode

There are two modes of running SillyTavern that differ in how they handle the configuration and data paths.

* **Standalone mode** (default) - uses the `config.yaml` file and `data` directory in the server directory. All data will be constrained to the installation path. This is the recommended mode for most users.
* **Global mode** - uses the system-wide paths for configuration and data. This is useful for installing SillyTavern as a package or when you want to share the same configuration and data across multiple installations.

Installations made by using the official npm package (https://www.npmjs.com/package/sillytavern) (e.g. `npx sillytavern@latest`) will run in global mode by default.

**### Data paths**

**Standalone mode** paths are relative to the SillyTavern installation directory:

* **Config path**: `./config.yaml`
* **Data root**: `./data/`

**Global mode** paths are OS-dependent:

* **Linux**: `~/.local/share/SillyTavern/config.yaml` (or `$XDG_DATA_HOME/SillyTavern/config.yaml`) and `~/.local/share/SillyTavern/data/` (or `$XDG_DATA_HOME/SillyTavern/data/`)
* **Windows**: `%APPDATA%\SillyTavern\config.yaml` and `%APPDATA%\SillyTavern\data\`
* **MacOS**: `~/Library/Application Support/SillyTavern/config.yaml` and `~/Library/Application Support/SillyTavern/data/`

### How to run in global mode

`dataRoot` and `configPath` can't be overridden with CLI arguments or config.yaml when running in global mode.

**1. Pass the `--global` argument to the server startup command (e.g. `node server.js --global`).**

2. Pass the `--global` argument to the shell startup script (e.g. `Start.bat --global` or `./start.sh --global`).
3. Use the `start:global` script in the `package.json` file (e.g. `npm run start:global`).

# SECTION: SillyTavern_Installation_LinuxMacOS

# Linux/MacOS Install

## Manual Git install

For MacOS / Linux all of these will be done in a Terminal.

1. Install git and nodeJS (the method for doing this will vary depending on your OS)
2. Clone the repo

   - for Release Branch: `git clone https://github.com/SillyTavern/SillyTavern -b release`
   - for Staging Branch: `git clone https://github.com/SillyTavern/SillyTavern -b staging`

3. `cd SillyTavern` to navigate into the install folder.
4. Run the `start.sh` script with one of these commands:

- `./start.sh`
- `bash start.sh`

## SillyTavern Launcher

### For Linux users
1. Open your favorite terminal and install git
2. Download Sillytavern Launcher with: `git clone https://github.com/SillyTavern/SillyTavern-Launcher.git`
3. Navigate to the SillyTavern-Launcher with: `cd SillyTavern-Launcher`
4. Start the install launcher with: `chmod +x install.sh && ./install.sh` and choose what you want to install
5. After installation start the launcher with: `chmod +x launcher.sh && ./launcher.sh`

### For Mac users
1. Open a terminal and install brew with: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Then install git with: `brew install git`
3. Download Sillytavern Launcher with: `git clone https://github.com/SillyTavern/SillyTavern-Launcher.git`
4. Navigate to the SillyTavern-Launcher with: `cd SillyTavern-Launcher`
5. Start the install launcher with: `chmod +x install.sh && ./install.sh` and choose what you want to install
6. After installation start the launcher with: `chmod +x launcher.sh && ./launcher.sh`

# SECTION: SillyTavern_Installation_Updating_index

# How to Update SillyTavern

Find your OS below and follow the instructions to update ST.

**For installation instructions, see the Installation page.**

This guide assumes you have already installed and run SillyTavern at least once.

**----**

## Linux/Termux or MacOS

You definitely installed via git, so just 'git pull' inside the SillyTavern directory.

- `cd SillyTavern` to enter the correct folder.
- `git pull` to get the update.
- `./start.sh` or `bash start.sh` to start ST.

----

## Windows

>First try using the `UpdateAndStart.bat` which is located in your SillyTavern installation base folder.

If that fails, come back here and continue reading.

### Method 1 - GIT

We always recommend users install using 'git'. Here's why:

When you have installed via `git clone`, all you have to do to update is type `git pull` in a command line in the ST folder (https://www.google.com/search?q=how+to+open+command+prompt+in+a+folder).
Alternatively, if the command prompt gives you problems (and you have GitHub Desktop installed), you can use the `Repository` menu and select `Pull`.

The updates are applied automatically and safely.

#### "Help I originally installed via Zip and now want to convert to Git install"

You have chosen a wise path.

Since your installation was done via Zip, you will need to make a new install using git.

Thankfully we have instructions on how to do so.

Once you have used git to install a NEW SillyTavern into a DIFFERENT folder, come back to this page and proceed to **Step 4** of the 'Zip Update' instructions below.

### Method 2 - ZIP

If you insist on installing via a zip, here is the tedious process for doing the update:

1. Download the new release zip.
2. Unzip it into a folder OUTSIDE of your current ST installation.
3. Do the usual setup procedure for your OS to install NodeJS requirements.

4. Copy the following files/folders as necessary(*) from your old ST installation:

    (*) 'As necessary' = "If you made any custom content related to those folders".
    
    #### Updating >=1.12.0
    
    Copy the `/data` directory and `config.yaml` file from one installation to another. If you have server-wide extensions (installed for "All users") that you want to preserve, also copy the `/public/scripts/extensions/third-party` directory.
    
    #### Updating from <1.12.0 to >1.12.0
    
    1.12.0 includes an automated migration procedure. The steps below are required *only* if the migration was interrupted or errored.

5. Run the updated server install at least once to create the `/data/default-user` directory.
6. Transfer the files from old `/public` to new `/data/default-user` as necessary.
    
    None of the folders are mandatory, so only copy what you need.
    
    **NOTE: DO NOT COPY THE ENTIRE /PUBLIC/ FOLDER**
    
    Doing so could break the new install and prevent new features from being present.
    
    ```plaintext
    Assets
    Backgrounds
    Characters
    Chats
    Context
    Groups
    Group chats
    Instruct
    movingUI
    KoboldAI Settings
    NovelAI Settings
    OpenAI Settings
    QuickReplies
    TextGen Settings (textgen = ooba)
    Themes
    User Avatars
    Worlds
    User
    settings.json
    secrets.json <---- this one is in the base folder, not /public/
    ```

7. Once those folders/files are copied, paste them into the /data/default-user folder (with secrets.json going into the folder root) of the new install.
8. Start SillyTavern once again with the method appropriate to your OS, and pray you got it right.
9. If everything shows up, you can safely delete the old ST folder.

### Common Update Problems

#### "There are unresolved conflicts in the working directory."

This means that you've modified default files that have been changed in the remote repository (such as setting presets).

To fix this, run this in the terminal. Use cautiously, as it can be destructive. Make sure to have a backup if needed.

```bash
git merge --abort
git reset --hard
git pull --rebase --autostash
```

#### File changes prevent git pull

- If you change SillyTavern system files, `git pull` may not work.
- Sometimes an update may require us to change an important file, which can cause the same problem.
- Usually it is default preset files or `package-lock.json`.
- In this case you can try moving the file to a different folder (or deleting the file) and then do `git pull`.
- Another solution is using `git pull --rebase --autostash`

#### Error: Cannot find module "***" when starting the server

- This means that SillyTavern added a new npm package requirement.
- Run `npm install` in the SillyTavern directory to fix this. Provided Start.bat and start.sh scripts will do that automatically.
- Didn't help? Remove the node_modules folder

**Windows**

```bash
rmdir /s /q node_modules
npm cache clean --force
npm install
```

**Unix/Linux**

```bash
rm -rf node_modules
npm cache clean --force
npm install
```

## Docker

1. Open a terminal window and navigate to your docker directory `cd SillyTavern/docker`
2. Delete your container with `docker compose down`
3. Delete the SillyTavern docker image from cache `docker rmi ghcr.io/sillytavern/sillytavern:latest` (Replace `sillytavern:latest` with `sillytavern:staging` if you are targeting the staging branch.)
4. Rebuild the container with `sudo docker compose up -d`

If everything goes smoothly, docker should start redownloading the image, and you will be up and running shortly. If you face any issues, refer to the next section of this guide.

### Common Update Problems
#### I use Docker and all my data is gone after the update!

You must follow the Migration guide for Docker containers
 to update volume mappings for the new data model introduced in 1.12.0

#### Permission denied when running docker commands

This is a Linux issue, and implies that your permissions are not properly set up. There are two ways to get around this:

1. **The Easy method**: If you have sudo access on your user, simply prefix commands with `sudo` (for example: `sudo docker compose down`) 
2. **The Proper method**: Fix your permissions. This varies depending on the version of Linux you use. There are plenty of guides online to help you fix this issue.

# SECTION: SillyTavern_Installation_Updating_migration-guide-1-09

# 1.9.0 Migration Guide

## How to migrate to a new branch if I use main/dev?

_**It is recommended to do a fresh install.**_ However, if you wish to use an existing copy of SillyTavern, please follow the instructions below.

**IMPORTANT!** Before doing anything, make *a complete backup* of your installation. You may *lose your data* in the process, so don't ignore this warning.

Not sure of which files to back up? See the list here: How to Update SillyTavern

### git installs

1. Open a terminal prompt (cmd, PowerShell, Termux, etc) in your SillyTavern installation folder.
2. Type `git fetch` and then `git pull` to pull the updates.
3. You may lose your settings. Have you made a backup? `git switch release` or `git switch staging` will change your branch, respectively
4. Skip to next item if you have no errors. You may have something like:
   ```
   error: Your local changes to the following files would be overwritten by checkout:
        config.conf
        public/css/bg_load.css
        public/settings.json
   ```
   You will see a list of files affected. If you do not care about those settings files being replaced `git switch -f release` or `git switch -f staging` will set your branch.
   If you do care to save those changes restore from backup.

5. Type `npm install` and then `npm run start` to test that everything behaves correctly.
6. Enjoy! Restore your data from a backup if needed.

### fatal: invalid reference: release

This may happen if you cloned just a single branch from an old remote (before migration to the organization repo). To fix this, you need to add and fetch a branch from a new remote:

```
git remote add st https://github.com/SillyTavern/SillyTavern
git fetch st
git checkout -t st/release
```

Then proceed from step 5.

### ZIP installs

Nothing changes for you. Just download the branch/release ZIP like usual.

# SECTION: SillyTavern_Installation_Updating_node

# How to update Node.js

It's important to keep your Node.js runtime up to date for security and performance reasons. Below are the steps to update Node.js depending on your operating system.

We recommend using the latest Long Term Support (LTS) version, which you can find on the Node.js official website (https://nodejs.org/en/about/previous-releases).

## How to check your current Node.js version

1. Open your terminal or command prompt.
2. Type the following command and press Enter:

```bash
node -v
```

## nvm (Node Version Manager) - Cross-Platform

If you are using `nvm`:

1. Open your terminal.
2. Type in the following command:

**Unix/Linux/macOS:** (https://github.com/nvm-sh/nvm)

```bash
nvm install --lts
nvm use --lts
```

**Windows:** (https://github.com/coreybutler/nvm-windows)

```bash
nvm install lts
nvm use lts
```

## Windows - Regular Installation

1. Go to the Node.js download page (https://nodejs.org/en/download/).
2. Download the Windows Installer for the LTS version.
3. Run the installer and follow the prompts to complete the installation.

## Windows - SillyTavern Launcher

If you have installed using the SillyTavern Launcher:

1. Open the SillyTavern Launcher.
2. Navigate to `Toolbox / App Installer / Core Utilities / Install Node.js`.

**OR:**

Do it manually using winget in PowerShell:

```powershell
winget install --id=OpenJS.NodeJS.LTS  -e
```

## Android - Termux

1. Open the Termux app.
2. Type the following commands:

```bash
pkg update
pkg upgrade nodejs-lts
```

Don't forget to accept any prompts that may appear during the update process by pressing `Y` on the virtual keyboard.

## macOS - Regular Installation

1. Go to the Node.js download page (https://nodejs.org/en/download/).
2. Download the macOS Installer for the LTS version.
3. Run the `.pkg` file and follow the prompts to complete the installation.

## macOS - Homebrew

If you have Homebrew installed, you can update Node.js with the following commands:

```bash
brew update
brew upgrade node
```

## Linux - Package Manager

The method to update Node.js on Linux depends on your distribution.

But as the version of Node.js in the official repositories may not be the latest, we recommend using the Node Version Manager (nvm) (https://github.com/nvm-sh/nvm) or the NodeSource repository (https://github.com/nodesource/distributions).

## Docker

No action required. The prebuilt Docker image we provide is compiled with the up-to-date version of Node.js.

# SECTION: SillyTavern_Installation_Updating_ST-1.12.0-Migration-Guide

# 1.12.0 Migration Guide

SillyTavern 1.12.0 (codename the "Neo Server" update) includes several critical changes that may affect the way you use SillyTavern.

This guide will prepare you for the update and provide some further guidance.

## Data storage update

1.12.0 changes the way SillyTavern handles the user data.

Previously, all of the persistent data was stored together with the frontend part in the `/public` directory, which created confusion and potential points of failure, as well as making containerization and system-wide app installation quite challenging.

### What's changed?

All persistent information from `/public` such as settings and chats (full list below) was moved into a separate directory with the configurable path, making it portable and independent from the web server itself. When needed for compatibility purposes, for example, for hosting extensions, full-size character cards, user image uploads, etc. a smart redirect has been set up to automatically host user files from the data directory.

### Setting a data root

You can provide either an absolute or a relative (to the ST repository directory) path to the data root either by `config.yaml` or by starting the server with the `--dataRoot` console argument.

> YAML example

```yaml
# -- DATA CONFIGURATION --
# Root directory for user data storage
dataRoot: C:\Users\Harry\Documents\ST-Data
```

> Console example

```bash
node server.js --dataRoot="/Users/harry/ST-Data"
# OR
npm run start -- --dataRoot="/Users/harry/ST-Data"
```

The default data root path is `./data`, which means the `data` directory in SillyTavern's repository.

**Note**

The data root path should be either a **full absolute** or a **full relative** path. You _can't_ use path shortcuts like `~` or `%APP_DATA%`, as these are resolved by a shell, not the operating system.

**### Migration**

#### **IMPORTANT!** Before we begin

1. **Only if you want to move dataRoot from the default location. Otherwise, skip this part.** Set the data root _before_ first running the server after pulling an update. Run `npm install` for the `config.yaml` to populate with a new value, or pass a console argument.
2. All data will be migrated into a `default-user` account. See more on Users below.

#### Containerless (bare metal) installs

You don't have to do anything! An automatic migration should handle everything for you when you start the ST server and it detects the old storage format (by checking the existence of the `/public/characters` directory).

Upon moving any files, an automatic backup will be created in the `/backups/_migration/YYYY-MM-DD` (resolved to the current date) directory, but it is always a good practice to make a full manual backup before running the migration.

#### Containerized (Docker) installs

Migrating the data in Docker volumes is a bit trickier but pretty straightforward. While `docker-compose.yml` provided with the repo was updated to reflect the changes, you may need to adjust your custom workflows/deployments.

**Step 1.** Create a new volume, and mount it to the "/home/node/app/data" path within the container. Don't remove the `config` volume.

```yaml
volumes:
    - "./config:/home/node/app/config"
    - "./data:/home/node/app/data"
```

**Step 2.** Move everything but the `config.yaml` file from the `config` volume into the `default-user` subdirectory of the `data` volume.

**Step 3.** Rebuild the container and start it up.

**Note**

Soft links between the `/public` directory and the `config` volume are no longer needed and are not built into the Docker container!

**#### What to migrate?**

The following files and directories are subject to the data migration. Assuming the default configuration, the before and after paths are provided in the table below.

| Before                                 | After                                |
|----------------------------------------|--------------------------------------|
| /secrets.json                          | /data/default-user/secrets.json      |
| /thumbnails                            | /data/default-user/thumbnails        |
| /vectors                               | /data/default-user/vectors           |
| /public/settings.json                  | /data/default-user/settings.json     |
| /public/stats.json                     | /data/default-user/stats.json        |
| /public/assets                         | /data/default-user/assets            |
| /public/backgrounds                    | /data/default-user/backgrounds       |
| /public/characters                     | /data/default-user/characters        |
| /public/chats                          | /data/default-user/chats             |
| /public/context                        | /data/default-user/context           |
| /public/scripts/extensions/third-party | /data/default-user/extensions        |
| /public/group chats                    | /data/default-user/group chats       |
| /public/groups                         | /data/default-user/groups            |
| /public/instruct                       | /data/default-user/instruct          |
| /public/KoboldAI Settings              | /data/default-user/KoboldAI Settings |
| /public/movingUI                       | /data/default-user/movingUI          |
| /public/NovelAI Settings               | /data/default-user/NovelAI Settings  |
| /public/OpenAI Settings                | /data/default-user/OpenAI Settings   |
| /public/QuickReplies                   | /data/default-user/QuickReplies      |
| /public/TextGen Settings               | /data/default-user/TextGen Settings  |
| /public/themes                         | /data/default-user/themes            |
| /public/worlds                         | /data/default-user/worlds            |
| /default/content/content.log           | /data/default-user/content.log       |

## Users

1.12.0 adds a (completely optional) ability to create a multi-user setup on the same server, allowing multiple users to use their own fully isolated SillyTavern instances even at the same time. User accounts can also be password-protected for an additional layer of privacy.

Please refer to the Users documentation for more information.

# SECTION: SillyTavern_Installation_Windows

# Windows Installation

DO NOT INSTALL INTO ANY WINDOWS CONTROLLED FOLDER (Program Files, System32, etc).

DO NOT RUN START.BAT WITH ADMIN PERMISSIONS

INSTALLATION ON WINDOWS 7 IS IMPOSSIBLE AS IT CANNOT RUN NODEJS 18.16

**## Installing via Git**

1. Install NodeJS (https://nodejs.org/en) (latest LTS version is recommended)
2. Install Git for Windows (https://gitforwindows.org/)
3. Open Windows Explorer (`Win+E`)
4. Browse to or Create a folder that is not controlled or monitored by Windows. (ex: C:\MySpecialFolder\)
5. Open a Command Prompt inside that folder by clicking in the 'Address Bar' at the top, typing `cmd`, and pressing Enter.
6. Once the black box (Command Prompt) pops up, type ONE of the following into it and press Enter:

   - for Release Branch: `git clone https://github.com/SillyTavern/SillyTavern -b release`
   - for Staging Branch: `git clone https://github.com/SillyTavern/SillyTavern -b staging`

7. Once everything is cloned, double-click `Start.bat` to make NodeJS install its requirements.
8. The server will then start, and SillyTavern will pop up in your browser.

## Installing via SillyTavern Launcher

1.  On your keyboard: press **`WINDOWS + R`** to open Run dialog box. Then, run the following command to install git:
    ```shell
    cmd /c winget install -e --id Git.Git
    ```
2. On your keyboard: press **`WINDOWS + E`** to open File Explorer, then navigate to the folder where you want to install the launcher. Once in the desired folder, type `cmd` into the address bar and press enter. Then, run the following command: 
   ```shell
    git clone https://github.com/SillyTavern/SillyTavern-Launcher.git && cd SillyTavern-Launcher && start installer.bat
    ```

## Installing via GitHub Desktop
(This allows git usage **only** in GitHub Desktop, if you want to use `git` on the command line too, you also need to install Git for Windows (https://gitforwindows.org/))

1. Install NodeJS (https://nodejs.org/en) (latest LTS version is recommended)
2. Install GitHub Desktop (https://central.github.com/deployments/desktop/desktop/latest/win32)
3. After installing GitHub Desktop, click on `Clone a repository from the internet....` (Note: You **do NOT need** to create a GitHub account for this step)
  
    

4. On the menu, click the URL tab, enter this URL `https://github.com/SillyTavern/SillyTavern`, and click Clone. You can change the Local path to change where SillyTavern is going to be downloaded.

    

5. To open SillyTavern, use Windows Explorer to browse into the folder where you cloned the repository. By default, the repository will be cloned here: `C:\Users\[Your Windows Username]\Documents\GitHub\SillyTavern`
  
6. Double-click on the `start.bat` file. (Note: the `.bat` part of the file name might be hidden by your OS, in that case, it will look like a file called "`Start`". This is what you double-click to run SillyTavern)

    

7. After double-clicking, a large black command console window should open and SillyTavern will begin to install what it needs to operate.
  
8. After the installation process, if everything is working, the command console window should look like this and a SillyTavern tab should be open in your browser:

    

9. Connect to any of the supported APIs and start chatting!

# SECTION: SillyTavern_Usage_API_Connections_Connection-Profiles

# Connection Profiles

Save Connection Profiles to quickly switch between different APIs, models and formatting templates. This is useful when you actively use multiple API connections or need to switch between different configurations without surfing through the menus.

## Accessing Connection Profiles

This feature is enabled by default starting from SillyTavern 1.12.6 or later as a built-in extension, and available in the API Connections menu. If you wish to *disable* it, open the Extensions panel, click on "Manage extensions", locate Connection Profiles in the list, uncheck the "Enabled" checkbox, and then click "Close".

## What is Saved

Connection Profiles store the following selections.

### Common

* API type, model and the server URL
* Secret Key
* Settings preset
* Start Reply With (can be explicitly empty)
* Custom Stopping Strings (can be explicitly empty)
* Reasoning Formatting

### Text Completion APIs

* System Prompt and its state
* Instruct Mode state and template
* Context Template
* Tokenizer

### Chat Completion APIs

* Prompt Post-Processing
* Proxy preset

## Managing Connection Profiles

**Note**

Profiles only save the selection in dropdown fields, without knowing anything about the underlying settings. This means that you will lose unsaved changes by switching to a different profile. To prevent this, make sure to update all presets and templates if you don't want to lose ephemeral changes.

*** To save a profile, set all the required settings and click the "Create" button. Then review the settings and provide a name for the profile. **A name should be unique.****

* To view the detailed information about a chosen profile, click on the "Information" button. Click again to hide the details.
* Connection Profile settings are saved into `settings.json` without altering the associated profile save file until you press the "Update" button. This means that if you setup a profile, but then switch to a different one without updating, you will lose all of your previous changes.
* To restore the changed selections from a saved profile, click the "Reload" button.
* To delete a profile, click the "Delete" button and confirm the deletion. **This action is irreversible.**

## Slash Commands

Connection profiles can be managed using the following slash commands.

1. `/profile [name]` - switch to a profile if the argument is provided, or get the name of the current profile if not.
2. `/profile-create [name]` - saves the current settings as a new profile with the provided name.
3. `/profile-list` - returns a JSON-serialized array of available profile names.
4. `/profile-get [name]` - gets the details of the profile with the provided name as a JSON-serialized object.
5. `/profile-update` - updates the selected profile with the current settings.

# SECTION: SillyTavern_Usage_API_Connections_DreamGen

# DreamGen

DreamGen is an app and an API for AI-powered role-playing and story-writing. They have a free tier, as well as a paid subscription that allows unlimited monthly access to their high-quality in-house text generation models made specifically for the purpose of steerable AI role-playing and story-writing. Create an account to get started: <https://dreamgen.com/>.

The (free) credits reset at the start of each calendar month. See pricing (https://dreamgen.com/pricing) to see the credit cost for each model and usage (https://dreamgen.com/account/usage) to see your remaining credits.

## Connecting to DreamGen

### Get API Key

Go to the DreamGen API keys (https://dreamgen.com/account/api-keys) page and click the "New API Key" button. Make sure the API Key is copied into your clipboard.

### Connect

1. Go to the SillyTavern connection settings.
2. Select API: Text Completion
3. Select API Type: DreamGen
4. Enter the API key
5. (optional) Pick a model

## Models

DreamGen API offers several models of different sizes.

- Lucid Max (in API called `lucid-v1-max` or `lucid-v1-extra-large`)
- Lucid Base (in API called `lucid-v1-base` or `lucid-v1-medium`) -- corresponds to the weight-available Lucid V1 Nemo (https://dreamgen.com/docs/models/lucid-v1/huggingface).

Lucid Base uses much fewer credits and is faster, while Lucid Max is more creative and is able to handle more complex instructions and narratives.

## Settings

The Lucid V1 DreamGen models use an extension of the Llama 3 chat template optimized for role-play and writing. They work best with a specific system prompt.

We strongly recommend to start with one of these master presets:

- Make sure that you have instruct mode enabled and select all checkboxes when importing.
- DreamGen Lucid V1 Role-Play preset (https://dreamgen.com/docs/models/lucid-v1/sillytavern/master-preset/role-play)
- DreamGen Lucid V1 Story preset (https://dreamgen.com/docs/models/lucid-v1/sillytavern/master-preset/story)

These presets come with built-in support for `/sys` to send instructions to the model. You can use those to steer the plot or control character's actions.

Other resources:

- **Detailed DreamGen + SillyTavern guide** (https://dreamgen.com/docs/models/lucid-v1/sillytavern)
- Detailed Lucid V1 prompt format documentation (https://dreamgen.com/docs/models/lucid-v1).
- DreamGen + SillyTavern role-play demo (https://imgur.com/a/dreamgen-lucid-sillytavern-roleplay-demo-bhzQpto)
- DreamGen + SillyTavern story-writing demo (https://imgur.com/a/dreamgen-lucid-sillytavern-writing-demo-JLv5iO3)
- Tips for making your own scenarios (https://v2.dreamgen.com/docs/scenario-editor)

## FAQ

### How can I make the responses longer or shorter?

You can set the `Last Assistant Prefix` in your formatting presets.

For long messages:

```txt
<|start_header_id|>user<|end_header_id|>

The next message is from {{char}} and is at least 100 words long<|eot_id|><|start_header_id|>writer character {{char}}<|end_header_id|>

```

For short messages:

```txt
<|start_header_id|>user<|end_header_id|>

The next message is from {{char}} and is at most 50 words long<|eot_id|><|start_header_id|>writer character {{char}}<|end_header_id|>

```

Make sure to preserve all newlines, including the two at the end.

You can also include writing style description in your card or system prompt, e.g.:

```txt
## Style

<your description>
```

See the "Style" documentation (https://v2.dreamgen.com/docs/scenario-editor#style) to learn more and see some examples.

### How can I steer the role-play / story?

Use the `/sys` option to send instructions to the model. Some examples:

> The innkeeper offers Daria and the others a pint of ale.

> The next message is from Draco and should be at least 200 words, focusing on his inner conflict about the decision.

See it in action. (https://imgur.com/a/dreamgen-lucid-sillytavern-roleplay-demo-bhzQpto)

# SECTION: SillyTavern_Usage_API_Connections_google

# Google Gemini

Gemini is Google's cutting-edge multimodal LLM, which is available through several APIs, including Google Vertex AI and Google AI Studio (formerly MakerSuite). This guide will help you set up the Gemini API connections in SillyTavern.

## Google AI Studio

AI Studio is the fastest and the most user-friendly way to try out the latest Google AI models without needing to set up a Google Cloud Platform (GCP) project. It provides a simple API key that you can use to access the Gemini models.

### Step 1: Create a Google AI Studio Key

1. Go to the Google AI Studio (https://aistudio.google.com/apikey) page and sign in with your Google account.
2. Click on "Get API Key", accept the terms and conditions.
3. Click "Create API Key" to generate your API key.
4. Copy the API key to your clipboard.

### Step 2: Put the API Key into SillyTavern

1. In SillyTavern, go to the "API Connections" page.
2. Select "Chat Completion" as the API type.
3. Select "Google AI Studio" from the dropdown menu.
4. Enter the API key you copied earlier into the "API Key" text box.
5. Click the "Connect" button to save the key.

You should now be able to use the Google AI Studio API with SillyTavern.

## Google Vertex AI

Vertex AI is a service provided by Google Cloud Platform (GCP). It provides access to various AI models, including the Gemini series.

There are several ways a Vertex AI API can be set up, and the available models may vary depending on the method used.

### Service Account

Google Cloud Platform (GCP) requires a service account to access Vertex AI, simple API keys will not work. A token will be generated from the service account JSON file, which will then be used to authenticate requests to the Vertex AI API.

You can create a service account by following these steps:

**Prerequisites:**

1. You must have a Google Cloud Platform (GCP) account.
2. You must have a project created within your GCP account.
3. You must have billing enabled for that project.

#### Step 1: Enable the Vertex AI API

Before your key can work, the API must be enabled for your project.

1. Go to the Google Cloud Console: <https://console.cloud.google.com/>
2. Make sure the correct project is selected in the top bar.
3. Navigate to the Vertex AI API page: <https://console.cloud.google.com/apis/library/aiplatform.googleapis.com>
4. If it's not already enabled, click the "Enable" button.

#### Step 2: Create the Service Account

This is the identity that will be used to access the Vertex AI API.

1. In the Google Cloud Console, navigate to the "Service Accounts" page. You can search for it in the top search bar or use this direct link: <https://console.cloud.google.com/iam-admin/serviceaccounts>
2. Select your GCP project and click "+ CREATE SERVICE ACCOUNT".
3. Service account name: Give it a descriptive name, like `my-vertex-ai-client`.
4. Click "CREATE AND CONTINUE".
5. Grant this service account access to project: In the "Role" dropdown, search for and select Vertex AI User. This role grants the necessary permissions to run models without giving away too much access.
6. Click "CONTINUE", and then click "DONE".

#### Step 3: Generate the JSON Key

This is the "password" file you need. It contains sensitive information, so don't share it or upload it anywhere public.

1. You should now be back on the Service Accounts list. Find the account you just created (e.g., sillytavern-vertex-ai).
2. Click the three-dot menu (⋮) on the far right of that row and select "Manage keys".
3. Click "ADD KEY" -> "Create new key".
4. Ensure the Key type is set to JSON.
5. Click "CREATE".

A .json file will immediately be downloaded to your computer. Keep it safe, because this key can't be recovered if lost.

#### Step 4: Put the JSON Content into SillyTavern

The JSON file you downloaded contains all the information needed to authenticate with the Vertex AI API. It will look something like this:

```json
{
    "type": "service_account",
    "project_id": "your-gcp-project-name",
    "private_key_id": "...",
    "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
    "client_email": "sillytavern-vertex-ai@your-gcp-project-name.iam.gserviceaccount.com",
    "client_id": "...",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "..."
}
```

1. Open the .json file you just downloaded with a simple text editor (like Notepad on Windows, TextEdit on Mac, or VS Code).
2. Select all the text in the file (Ctrl+A or Cmd+A).
3. Copy the text to your clipboard (Ctrl+C or Cmd+C).
4. In SillyTavern, go to the "API Connections" page, select "Chat Completion" as the API type, and then select "Google Vertex AI" from the dropdown menu. Switch the authentication method to "Service Account".
5. Paste the entire copied content into the "Service Account JSON Content" text box.
6. Click the "Validate JSON" button to make sure you copied it correctly.
7. Finally, scroll down and click "Connect" at the bottom of the API settings page.

You should now be able to use the Google Vertex AI API with SillyTavern.

### Express Mode

Express mode is the quickest way to get started with using Generative AI on Google Cloud. It allows you to use the Gemini API without needing to set up a service account. Instead, you can use an API key directly.

See the official documentation for more details: Vertex AI in express mode overview (https://cloud.google.com/vertex-ai/generative-ai/docs/start/express-mode/overview).

#### Step 1: Ensure your account is eligible for Express Mode

You must have a Google account that was not previously used to create a Google Cloud project.
If you have an existing Google Cloud project (including free trials), you can create a new one for this purpose.

#### Step 2: Activate the Vertex AI Express Mode

1. Go to the following web page: Vertex AI Studio (https://cloud.google.com/generative-ai-studio).
2. Click on "Try it free".
3. Accept the terms and conditions and sign in with your Google account.
4. Choose your country and click "Agree & start free". Wait for the setup to complete.

#### Step 3: Create an API Key

1. Verify that your Google Cloud console is running in Express Mode. You should see a banner at the top left corner of the page.
2. Click on the "API Keys" link in the left sidebar.
3. Click on the "Create API Key" button.
4. A new API key will be generated. Copy this key to your clipboard.

#### Step 4: Put the API Key into SillyTavern

1. In SillyTavern, go to the "API Connections" page.
2. Select "Chat Completion" as the API type.
3. Select "Google Vertex AI" from the dropdown menu.
4. Switch the authentication method to "Express Mode (API Key)".
5. Paste the API key you copied earlier into the "API Key" text box.
6. Click the "Connect" button to save the key.

You should now be able to use the Google Vertex AI API in Express Mode with SillyTavern.

# SECTION: SillyTavern_Usage_API_Connections_horde

# AI Horde

## Disclaimer

- AI Horde is a crowdsourced, distributed GPU cluster run entirely by volunteers.
- By default, your inputs are anonymously sent and responses can not be seen by the person running the Horde Worker.
- However, since it is an open-sourced program, Malicious Workers could modify the code to:
  - log your activity (input prompts, AI responses).
  - produce bad or offensive responses.

When using Horde **never send** any personal information such as names, email addresses, etc.

**Switching on the "Trusted Workers Only" checkbox will limit the selection of available workers to only those who have been hosting on Horde for a while and are generally considered trusted. But they could still be seeing prompts, for example by hosting using unaccounted software.**

To help reduce this problem, SillyTavern has built in the following feature:

- When a chat response is generated by a Horde Worker, SillyTavern records the Worker's ID and what model they were using.
- This information can be seen by hovering your mouse cursor over the chat item (see image below).
- If you believe you received a malicious response, you can pass this information to the Horde admin on the AI Horde Discord (https://discord.gg/3DxrhksKzn) for review and possible disciplinary action against that Worker.

## Setup

- SillyTavern is able to connect with Horde out of the box with no additional setup required.
- Select 'AI Horde' from the API Dropdown Selector in the ST API Panel.
- Select one or more Models ('AI brains' for the characters) from the Model Selector at the bottom of the panel.
- Select a character and begin chatting.

By default, your SillyTavern instance connects to the Horde's low priority 'guest account'.
This means you may have to wait a long time for a reply.
To reduce wait times, follow the tips down below.

**## Tips**

- Register an account on the Horde website (https://aihorde.net/register) then add your Horde key into the SillyTavern Horde API Key box.
- Set up a Horde Worker (https://github.com/Haidra-Org/AI-Horde-Worker#readme) to provide your GPU for others.
  - Letting others use your GPU earns you 'Kudos', a kind of Horde-only currency (https://github.com/Haidra-Org/AI-Horde/blob/main/FAQ.md#kudos).
  - The more kudos your account has, the faster you will get chat responses from other Horde Workers.
  - Kudos can also be used to create AI images on Stable Horde (https://stablehorde.net).
    - SillyTavern supports Stable Horde image generation out of the box.
- If your GPU isn't powerful enough to run an AI, or you don't have a computer, you can still participate in the Horde community to earn Kudos in various ways (https://github.com/Haidra-Org/AI-Horde/blob/main/FAQ.md#i-dont-have-a-powerful-gpu-how-can-i-get-kudos).

# SECTION: SillyTavern_Usage_API_Connections_index

# API Connections

SillyTavern can connect to a wide range of LLM APIs.
Below is a description of their respective strengths, weaknesses, and use cases.

## ELI5: Chat Completions vs Text Completions

When you first navigate to the "API Connections" page in ST, you will notice a drop-down option to select between options using nomenclature such as "Chat Completion" and "Text Completion". It's helpful to understand what this means.

What it's not: It's easy to think of "Text Completion" as local models and "Chat Completion" as cloud-based LLMs, but that's not the case. Neither is e.g. "NovelAI" or "Kobold" actually a separate type of model altogether, even though they are separate options in the API dropdown in ST. You can force models into different API structures with the appropriate backend, but that's not the point of this section.

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
- Requires separate download of LLM models from HuggingFace (https://huggingface.co/models?other=LLM) which can be 5-50GB each.
- Most models are not as powerful as cloud LLM APIs.

### KoboldCpp

- Easy-to-use API with CPU offloading (helpful for low VRAM users) and streaming
- Runs from a single binary file on Windows, Mac, and Linux
- Supports GGUF models
- Slower than GPU-only loaders such as AutoGPTQ and Exllama/v2
- GitHub (https://github.com/LostRuins/koboldcpp), Setup Instructions

### llama.cpp

- The original source from which KoboldCpp and Ollama were forked
- Provides pre-compiled binaries and an option to compile from source
- Supports GGUF models
- Lightweight CLI interface for llama-server
- GitHub (https://github.com/ggml-org/llama.cpp)

### Ollama

- Easiest to set up and use of all llama.cpp-based APIs
- A nifty catalog (https://ollama.com/library) of models available for one-click download
- Supports GGUF models wrapped in Ollama's own format
- GitHub (https://github.com/ollama/ollama), Website (https://ollama.com/)

### Oobabooga TextGeneration WebUI

- All-in-one Gradio UI with streaming
- Broadest support for quantized (AWQ, Exl2, GGML, GGUF, GPTQ) and FP16 models
- One-click installers available
- Regular updates, which can sometimes break compatibility with SillyTavern
- GitHub (https://github.com/oobabooga/text-generation-webui#one-click-installers)

**Correct Way to Connect SillyTavern to Ooba's new OpenAI API:**

1. Make sure you're on the latest update of Oobabooga's TextGen (as of Nov 14th, 2023).
2. Edit the CMD_FLAGS.txt file, and add the `--api` flag there. Then restart Ooba's server.
3. Connect ST to `http://localhost:5000/` (by default) without checking the 'Legacy API' box. You may remove the `/v1` postfix from the URL Ooba's console provides you.

*You can change the API hosting port with the `--api-port 5001` flag, where 5001 is your custom port.*

### TabbyAPI

- Lightweight Exllamav2 (https://github.com/turboderp/exllamav2)-based API with streaming
- Supports Exl2, GPTQ, and FP16 models
- Official extension (https://github.com/theroyallab/ST-tabbyAPI-loader) allows loading/unloading models directly from SillyTavern
- Not recommended for users with low VRAM (no CPU offloading)
- GitHub (https://github.com/theroyallab/tabbyAPI), Setup Instructions

### KoboldAI Classic (deprecated, abandoned)

- Runs on your PC, 100% private, wide range of models available
- Gives the most direct control of the AI's generation settings
- Requires large amounts of VRAM in your GPU (6-24GB, depending on the LLM model)
- Models limited to 2k context
- No streaming
- Popular KoboldAI versions:
  - Henky's United (https://github.com/henk717/KoboldAI)
  - 0cc4m's 4bit-supporting United (https://github.com/0cc4m/KoboldAI)

## Cloud LLM APIs

- These LLM APIs are run as cloud services and require no resources on your PC
- They are stronger/smarter than most local LLMs
- However, they all have content filtering of varying degrees, and most require payment

### AI Horde

- SillyTavern can access this API out of the box with no additional settings required
- Uses the GPU of individual volunteers (Horde Workers) to process responses for your chat inputs
- At the mercy of the Worker in terms of generation wait times, AI settings, and available models
- Website (https://aihorde.net/), Setup Instructions

### OpenAI (ChatGPT)

- Easy to set up and acquire an API key
- Requires prepayment for credits and charges per prompt
- Very logical. Creative style can be repetitive and predictable
- Most of the newer models (gpt-4-turbo, gpt-4o) support multimodality
- Website (https://platform.openai.com/), Setup Instructions

### Claude (by Anthropic)

- Recommended for users who want their AI chats to have a creative, unique writing style
- Requires prepayment for credits and charges per prompt
- The newest models (Claude 3) support multimodality
- Requires a specific prompting style and utilization of prefills (https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response) for reply steering
- Website (https://console.anthropic.com/), Setup Instructions

### Google AI Studio and Vertex AI

- Has a free tier with rate limits (Gemini Flash), may require billing information
- AI Studio (https://aistudio.google.com/) usually has the latest models and features
- Vertex AI (https://console.cloud.google.com/vertex-ai/studio) is trickier to set up, but more stable
- Setup Instructions

### Mistral (by Mistral AI)

- Efficient models of various sizes and use cases. You can create an account and API key on their platform (https://console.mistral.ai/api-keys/).
- From 32k to 128k context sizes for general use, and 32k to 256k context sizes for coding.
- Free Tier with rate limits.
- Reasonable moderation, with Mistral's main principles being to be neutral and empower users, more information here (https://mistral.ai/terms/).
- Website (https://console.mistral.ai/), Setup Instructions

### OpenRouter

- Provides a unified API to access all the major LLMs on the market
- Pay-per-token credit system, as well as free models with limited daily requests
- No enforced moderation, unless required by the LLM vendor
- Website (https://openrouter.ai), Setup Instructions

### DeepSeek

- Provides access to the latest versions of very popular DeepSeek V3 (`deepseek-chat`) and DeepSeek R1 (`deepseek-reasoner`) models
- Requires a payment for credits ($2 minimum), but the models are fairly cheap for their quality
- No moderation on the API, but the models may refuse certain prompts
- Website (https://platform.deepseek.com/), Setup Instructions

### AI21

- Provides access to Jamba Family open models
- Has a free trial ($10 for three months), then requires to pay monthly per token
- Website (https://ai21.com/), Setup Instructions

### Cohere

- Provides access to the latest models from Cohere (command-r, command-a, c4ai-aya, etc.)
- Has a free tier (Trial Keys) with enough rate limits for casual use
- Website (https://cohere.com/), Setup Instructions

### Perplexity

- Provides access to unique Perplexity Sonar online-enabled models via their API
- Requires to have billing configured and credits purchased
- Website (https://perplexity.ai/), Setup Instructions

### Mancer AI

- Service that hosts unconstrained models of various families
- Uses 'credits' to pay for tokens on various models
- Does not log prompts by default, but you can enable it to get credit discounts on tokens.
- Uses an API similar to `Oobabooga TextGeneration WebUI`, see Mancer docs (https://mancer.tech/docs/clients/#sampling-parameters) for details.
- Website (https://mancer.tech/), Setup Instructions

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
- Website (https://novelai.net/), Setup Instructions

### Electron Hub

- One API key unlocks models from multiple vendors (OpenAI, Anthropic, DeepSeek, etc.) for text and image generation
- $0.25 of free credits every day, paid plans available
- Website (https://www.electronhub.ai/), Setup Instructions

### AI/ML API

- Unified API for 300+ models including Claude, GPT-4o, Gemini, LLaMA 3, Mistral and others
- Has a free tier with rate limits, subscription plans, and pay-as-you-go options
- Website (https://aimlapi.com), Docs (https://docs.aimlapi.com), Models (https://aimlapi.com/models)

# SECTION: SillyTavern_Usage_API_Connections_koboldcpp

# KoboldCpp

KoboldCpp is a self-contained API for GGML and GGUF models.

This VRAM Calculator (https://huggingface.co/spaces/NyxKrage/LLM-Model-VRAM-Calculator) by Nyx will tell you approximately how much RAM/VRAM your model requires.

## Nvidia GPU Quickstart

This guide assumes you're using Windows.

* Download the latest release: <https://github.com/LostRuins/koboldcpp/releases>
* Launch KoboldCpp. You may see a pop-up from Microsoft Defender, click `Run Anyway`.
* As of version 1.58, KoboldCpp should look like this:

* Under the `Quick Launch` tab, select the model and your preferred `Context Size`.
* Select `Use CuBLAS` and make sure the yellow text next to `GPU ID` matches your GPU.
* Do not tick `Low VRAM`, even if you have low VRAM.
* Unless you have an Nvidia 10-series or older GPU, untick `Use QuantMatMul (mmq)`.
* `GPU Layers` should have been populated when you loaded your model. Leave it there for now.
* Under the `Hardware` tab, tick `High Priority`.
* Click `Save` so you don't have to configure KoboldCpp on every launch.
* Click `Launch` and wait for the model to load.

You should see something like this:

```txt
Load Model OK: True
Embedded Kobold Lite loaded.
Starting Kobold API on port 5001 at http://localhost:5001/api/
Starting OpenAI Compatible API on port 5001 at http://localhost:5001/v1/
======
Please connect to custom endpoint at http://localhost:5001
```

You can now connect to KoboldCpp within SillyTavern with `http://localhost:5001` as the API URL and start chatting.

**Congratulations! You're done!**

Kind of.

### GPU Layers

KoboldCpp is working, but you can improve performance by ensuring that as many layers as possible are offloaded to the GPU. You should see something like this in the terminal:

```txt
llm_load_tensors: offloading 9 repeating layers to GPU
llm_load_tensors: offloaded 9/33 layers to GPU
llm_load_tensors:        CPU buffer size = 25215.88 MiB
llm_load_tensors:      CUDA0 buffer size =  7043.34 MiB
....................................................................................................
llama_kv_cache_init:  CUDA_Host KV buffer size =  1479.19 MiB
llama_kv_cache_init:      CUDA0 KV buffer size =   578.81 MiB
```

Don't be afraid of numbers; this part is easier than it looks. `CPU buffer size` refers to how much system RAM is being used. Ignore that. `CUDA0 buffer size` refers to how much GPU VRAM is being used. `CUDA_Host KV buffer size` and `CUDA0 KV buffer size` refer to how much GPU VRAM is being dedicated to your model's context. In this case, KoboldCpp is using about 9 GB of VRAM.

I have 12 GB of VRAM, and only 2 GB of VRAM is being used for context, so I have about 10 GB of VRAM left over to load the model. Because 9 layers used about 7 GB of VRAM and `7000 / 9 = 777.77` we can assume each layer uses approximately `777.77 MIB` of VRAM. `10,000 MIB / 777.77 = 12.8`, so I'll round down and load 12 layers with this model from now on.

Now do your own math using the model, context size, and VRAM for your system, and restart KoboldCpp:

* If you're smart, you clicked `Save` before, and now you can load your previous configuration with `Load`. Otherwise, select the same settings you chose before.
* Change the `GPU Layers` to your new, VRAM-optimized number (12 layers in my case).
* Click `Save` to save your updated configuration.

You should now see something like this:

```txt
llm_load_tensors: offloading 12 repeating layers to GPU
llm_load_tensors: offloaded 12/33 layers to GPU
llm_load_tensors:        CPU buffer size = 25215.88 MiB
llm_load_tensors:      CUDA0 buffer size =  9391.12 MiB
....................................................................................................
llama_kv_cache_init:  CUDA_Host KV buffer size =  1286.25 MiB
llama_kv_cache_init:      CUDA0 KV buffer size =   771.75 MiB
```

KoboldCpp is using about 11.5 GB of my 12 GB VRAM. This should perform a lot better than the settings generated automatically by KoboldCpp.

**Congratulations! You're (actually) done!**

For a more in-depth look at KoboldCpp settings, check out Kalomaze's Simple Llama + SillyTavern Setup Guide (https://rentry.org/llama_v2_sillytavern).

# SECTION: SillyTavern_Usage_API_Connections_mancer

# Mancer

Mancer is a large language model inferencing service that lets you run whatever prompts you want and doesn't censor responses. Most of the models require a preloaded balance to start chatting, but there is a free model as of writing (2024-11-28).

- Models (https://mancer.tech/models)
- Pricing (https://mancer.tech/pricing)

## How to Get Started

1. Sign up for an account at mancer.tech (https://mancer.tech/).
2. Click on Dashboard and copy your API Key.

    

3. In SillyTavern, select the Text Completion API, and then select Mancer under API Type.
4. Enter your Mancer API Key and click Connect.

You should now be able to chat with any Mancer model of your choice.

## Anonymous Logging

If you don't mind your chats potentially being used to train models, improve Mancer's service, publish datasets, or *whatever else* they may decide to do with it, you can opt-in to anonymous logging for a 25% token discount on select models. Simply go to your Mancer dashboard (https://mancer.tech/dashboard.html) and tick `Enable Anon. Logging`.

## Support

Still need help? Head over to the #mancer (https://discord.gg/Ze9UyNu3) support channel on the SillyTavern Discord.

# SECTION: SillyTavern_Usage_API_Connections_novelai

# NovelAI

NovelAI is a paid subscription service that allows unlimited monthly access to their high-quality in-house text generation, image generation, and text-to-speech models. Register an account here to get started: <https://novelai.net/>

You will get only *50 generations* for free to evaluate the model. When the **"Not eligible for this model"** error appears, this means that you've exhausted your trial period and need to subscribe to a paid plan.

## API Key

To get your NovelAI API key, follow these steps:

1. Select the gear icon at the top of the left sidebar.

2. Select "Account" under "User Settings".

3. Select "Get Persistent API Token".

4. Select the copy icon to copy your NovelAI API token to the clipboard. 

## Models

If you have Opus, then Erato is the model to use. If you don't have Opus, then Kayra is the best available model.

Clio has a larger context size on Tablet/scroll tiers, but the strength of Kayra usually makes up for that difference.

## Settings

The files with the settings are here (`SillyTavern/data/<user-handle>/NovelAI Settings`).
You can also manually add your own settings files.

### Response Length

How much text you want to generate per message. Note that NovelAI has a limit of 150 tokens per response. 

### Context Size

How many tokens of the chat are kept in the context at any given time. How large the maximum context size you can use depends on the model and your subscription tier:

- Kayra (Tablet) - 3072 tokens
- Kayra (Scroll) - 6144 tokens
- Erato (Opus exclusive), Kayra (Opus) and Clio (all tiers) - 8192 tokens

### Preamble

Text that is inserted right above the chat to modify the writing style. The recommended format is a list of short tags, like "[ Style: chat, detailed, sensory ]". 

## Preset Descriptions
This is, according to NovelAI, what the default presets are good for.

### Erato

* Golden Arrow - A good all-rounder.
* Wilder - Higher variety of word choice, more differences between rerolls, more prone to mistakes.
* Zany Scribe - Avoids mistakes and repetition. Prioritizes more complex words.
* Dragonfruit - Varied and complex language with little repetition. More frequent mistakes and contradictions.
* Shosetsu - Designed for writing in Japanese. Works fine for English too.

### Kayra

* Asper - For creative writing. Expect unexpected twists.
* Carefree - A good All-rounder
* Fresh-Coffee - Keeps things on track. Handles instruct well.  
* Pro_Writer - Mimic the pacing and feel of best-selling fiction
* Stelenes - More likely to choose reasonable alternatives. Variety on retries.
* Tea_Time - It gets good when it gets going.
* Writers-Daemon - Extremely imaginative, sometimes too much.

### Clio

* Edgewise - Handles a variety of generation styles well
* Fresh Coffee - Keeps things on track.
* Long-Press - Intended for creative prose.
* Talker Chat - Designed for chat style generation.
* Vingt-Un - A good all-around default with a bent towards prose.

## Tips and FAQs for using NovelAI with SillyTavern

There are a lot of common problems and questions that come up when switching to NovelAI from another ST backend API. The difference comes down to what the models are trained for. Most likely, you've used an OpenAI or Anthropic model (or a local model made to resemble those), which is built around following the user's instructions. NovelAI's models are built purely around text completion: instead of taking your input as a message and formulating a response, NAI's models attempt to continue the incoming prompt. Due to this difference, a lot of tips and common knowledge that work for other APIs won't work for NAI. 

### Tweaking settings for NovelAI

Under Advanced Formatting (the A icon):
- Set "Context Template" to "NovelAI"
- Set "Tokenizer" to "Best match"
- Check "Always add character's name to prompt"
- Check "Collapse Consecutive Newlines"
- Uncheck the "Enabled" box under "Instruct Mode"

Under User Settings (the person with a gear)
- Turn on "Swipes" (Not NAI specific, but it's so useful you should just do it)

### Building/Adapting character cards for NovelAI

To optimize your character cards for NovelAI, there are a couple of recommended methods for writing your character's description: prose, and attributes. 

Prose is so simple it doesn't feel like it should work: "Sylpheed is a young-looking but actually 900 year old nymph. She's short and petite, with long white hair that fades into a green gradient in her braided side ponytail, and emerald green eyes shaped like crosses.[...]" No, really, that's it. Just write out, in normal sentences, what the character looks like, acts like, etc., and the AI will pick up on it. 

If you don't trust your writing abilities or want a more structured way to go about it, you can use the attributes method, which is present in the NovelAI training data. This works as a simple list of character traits of different types. Here's a list of possible attributes that have been tested to be effective with NovelAI's models:

```
Name:
AKA:
Type: character
Setting:
Nationality:
Species:
Gender:
Age:
Height:
Weight:
Appearance:
Clothing:
Attire:
Personality:
Mind:
Mental:
Likes:
Dislikes:
Sexuality:
Speech:
Voice:
Abilities:
Skills:
Quote:
Affiliation:
Occupation:
Reputation:
Secret:
Family:
Allies:
Enemies:
Background:
Description:
Attributes:
```

"Type: character" is there to tell the AI that this is describing a character (as opposed to a location, object, or other type of thing). The rest of the attributes are optional, and some are redundant (for example, Personality, Mind, and Mental all mean basically the same thing), but these have been tested and work well with NovelAI's models. Fill in whichever ones are relevant to your character. The attributes should be written in lower case and separated by commas, no need for quotes around the words. For example:

```
Skills: lockpicking, stealth, running away very fast
```

These methods are recommended because they're present in NovelAI's training data, so they specifically work well with the model. 

#### Example cards

Here are a couple of example cards, made for NovelAI, that show off different ways of creating cards specifically for NovelAI. The first card, Valka, uses the attributes method for the character description, while Eris, the second card, uses prose descriptions, along with a large amount of example dialogue. 

<div style="display:flex;gap:2em;justify-content:center">

[](/static/Valka.png)

[](/static/Eris.png)

</div>

#### What not to do

Most of the existing character card formats are a poor fit for NovelAI. They'll give you some results, even some good ones, but they have a lot of problems. W++ is one of the biggest offenders, where it doesn't resemble anything that NovelAI's models were trained on, and its constant use of brackets/braces/quotes eats up a ton of tokens, bloating the size of the cards with no real benefit. 

Of the existing formats that aren't baked into NovelAI, AliChat is the one most likely to work, as it relies on using example messages to get across both information about the character and their voice at the same time, in the format of the type of message that you want the AI to output. 

For most other formats, since they are usually ways of listing out different characteristics of a particular character, they can be converted to the attributes method rather straightforwardly. 

### Which module should I use?

Probably No Module. Prose Augmenter is useful if you want a character to speak in a more flowery manner, but be careful not to overdo it. Text Adventure might be useful for a text adventure-style card/story. 

### Not the instruct module?

You can invoke the Instruct module when you need it. Create a newline in your message, and put your instructions in curly brackets like this: `{ CharName is offended by that seemingly innocuous statement }` (the spaces are _required_ between the text and the brackets). Doing that will automatically switch the AI into the Instruct module for a short time. You don't want to use the Instruct module all the time because it tends to produce less creative output than the other modules, just when you need to guide the AI strongly in a particular direction.

### Why do my responses keep getting cut off?

NovelAI limits response length to ~150 tokens total, even if you set the slider higher than that. When it reaches the number of tokens in the slider or 150, whichever is lower, it will generate up to 20 more tokens, looking for a stop sequence or the end of a sentence, so there's an effective limit of 170 tokens for a response, at which point it will just stop, causing it to cut off. 

If it cuts off, you can select the continue option (in the three-line menu to the left of the text box) to get the character to continue their response. 

If you regularly want responses longer than 170 tokens, you can work around the limit like this:

- Keep the response length at 150 tokens.
- Under Advanced Formatting, enable Auto-continue.
- Set the "Target length" to the desired length.

This will chain together multiple generations to give you longer messages but doesn't guarantee that the reply will be 100% of the desired length if the model decides to stop.

### How do I get the bot to write longer responses?

Read the above about responses getting cut off. That will help to make sure that responses aren't cut off prematurely by running into the limit of generation length. 

If your responses aren't getting cut off but are still too short, it's likely you're dealing with "garbage in, garbage out" - if you give the model bad examples, it will produce bad output. If the character card has no example dialogue or short example dialogue and the messages you send to the bot are short, the model will pick up on that, take it as the accepted way to do things and the responses will be short. So, write longer example dialogue and longer messages to the bot. (You can always use NovelAI to write some example dialogue for you rather than doing it yourself.)

### How do I get the bot to stop talking for me?

- Check that the character card's first message and example dialogue don't include the character taking actions for you - if they do, then rewrite them to get rid of it acting for you
- Make sure that "Always add character's name to prompt" is checked
- Make sure that you're currently using the same user persona as the rest of the chat. If you changed user personas and didn't change back (or don't have a persona locked to that chat), the usual rules to stop generating for you will fail
- Add ["\n\{\{user\}\}:"] to Custom Stopping Strings (shouldn't be necessary, but sometimes helps)

### Why isn't my character responding?

A lot of things can cause this, so we need to look in a few places:

- Make sure that "Always add character's name to prompt" is checked in Advanced Formatting
- Check to make sure there aren't any errors coming from the API. While you can use SillyTavern with the NAI free trial, once it runs out, you'll just get errors
- Check what you have in "Custom Stopping Strings" - if those are being generated at the start of the response, it might be cut off prematurely

### How should I use the Author's Note?

In general, you probably shouldn't. It's inserted very close to the end of the context, and with NAI's models, it frequently overpowers everything else in the context. It's mostly an artifact from older, weaker models where it was more necessary. 

### How do I do a scene break/time jump?

Put the following as a system message or on newlines at the start of your next message:
```
***
[ 2 days later ]
```

Then put the rest of your message on the next line. The bracketed text can be a time jump, a new location, or anything else. The "***" (hilariously named a "dinkus") tells the AI that the scene has changed, and the bracketed text gives that more context.

### The AI keeps repeating specific words/phrases, what do I do? 

As mentioned above, you can push the repetition penalty slider up a bit more, though pushing it too far can make the output incoherent. 
To more thoroughly fix the problem, go back through the context, especially recent messages, and delete the repeated word/phrase. Removing it from the context gives the AI less reason to start saying it in the first place.

# SECTION: SillyTavern_Usage_API_Connections_openai

# Chat Completions

## Source-specific instructions

****Important!****

Most API platforms allow you to view the generated API key only once, at the time of its creation. If you lose it, you will need to generate a new key. Make sure to keep it safe!

**### OpenAI**

Use OpenAI's developer platform to access various OpenAI models, including gpt-4o, gpt-4.1, o3, etc.

**How to get an API key:**

1. Go to OpenAI (https://platform.openai.com/) and sign in.
2. Use "View API keys (https://platform.openai.com/account/api-keys)" option to create a new API key.

### Claude

Claude is a family of AI models developed by Anthropic. You can access Claude models through the Anthropic console.

**How to get an API key:**

1. Go to Anthropic Console (https://console.anthropic.com/) and sign in.
2. Use the "Get API Key (https://console.anthropic.com/settings/keys)" section to create a new API key.

### Mistral AI

Mistral AI is a team developing both open and proprietary models with high scientific standards and a focus on openness. You can run their models locally or through their API service, La Plateforme.

**How to get an API key:**

1. The first step is to create an account on La Plateforme (https://console.mistral.ai/).
2. Once that's done, you can choose a plan (https://console.mistral.ai/billing/plans) and set up your payment information or opt for the Free Tier.
3. Next, you can create your API key (https://console.mistral.ai/api-keys/). You may need to wait a couple of minutes before the key becomes valid!

### DeepSeek

DeepSeek Platform provides access to the latest DeepSeek models through an API. They offer a range of models, including DeepSeek V3 and DeepSeek R1.

**How to get an API key:**

1. Sign up on the DeepSeek Platform (https://platform.deepseek.com/).
2. After signing up and topping up your account, you can create an API key in the "API keys (https://platform.deepseek.com/api_keys)" section.

### AI21

AI21 Labs offers a range of AI models, including their flagship Jamba series. You can access their models through the AI21 Studio API.

**How to get an API key:**

1. Go to AI21 Studio (https://studio.ai21.com/) and sign in.
2. Navigate to the "Settings => API Keys" section to create a new API key.

### Cohere

Cohere provides a suite of AI models for various tasks, including text generation and embeddings. You can access their models through the Cohere API.

**How to get an API key:**

1. Go to Cohere (https://cohere.com/) and sign in.
2. Navigate to the "API Keys (https://dashboard.cohere.com/api-keys)" section in your account settings to create a new API key.

### Perplexity

Perplexity AI offers access to online-enabled Sonar models through their API for real-time research and information retrieval.

Official Getting Started guide: Perplexity Quickstart (https://docs.perplexity.ai/getting-started/quickstart)

**How to get an API key:**

1. Go to Perplexity (https://perplexity.ai/) and sign in.
2. Go to the "API billing (https://www.perplexity.ai/account/api/billing)" section to purchase credits for API usage.
3. Navigate to the "API keys (https://www.perplexity.ai/account/api/keys)" section in the settings to create a new API key.

### Fireworks AI

Fireworks AI is a high-performance platform that provides fast, cost-effective access to state-of-the-art open-source language models. The platform offers serverless deployment with OpenAI-compatible APIs and supports context windows up to 256,000 tokens.

**How to get an API key:**

1. Go to Fireworks AI (https://fireworks.ai/) and create an account or sign in.
2. Navigate to the API Keys page (https://app.fireworks.ai/settings/users/api-keys) in your account settings.
3. Click "Create API key" and provide a descriptive name (e.g., "SillyTavern").

## Electron Hub

Electron Hub is a unified OpenAI-compatible platform that provides access to models from multiple vendors through a single API key.

**How to get an API key:**

1. Create an account at Electron Hub (https://playground.electronhub.ai/console).
2. Generate an API key from the **Console → API Keys** page.

## Custom OpenAI-compatible endpoint

It is important to note that we do not provide support for possible issues that you may have!
We do not guarantee compatibility with every possible API endpoint!

**!!!**

If you intend to use this feature to use a local endpoint, like TabbyAPI, Oobabooga, Aphrodite, or any like those, you might want to check out the built-in compatibility for those instead. The custom endpoint feature is mainly intended for use with other services and programs that expose an OpenAI-compatible API Chat Completion endpoint.

Most Text Completion APIs support far greater customization options than OpenAI's standards allow for. These greater customization options, such as the Min-P sampler, may be worthwhile for SillyTavern users to check out, which can greatly improve the quality of generations.

**You can configure an alternative endpoint for the Chat Completions backend. This custom endpoint can connect to any server that supports the generic OpenAI API schema.**

Examples of compatible backends include:

* LM Studio (https://lmstudio.ai/)
* LiteLLM (https://www.litellm.ai/)
* LocalAI (https://localai.io/)

### Connecting

To access this feature:

1. Switch to the 'Chat Completion' API type
2. Select 'Custom (OpenAI-compatible)' for 'Chat Completion Source'

Enter the custom endpoint URL and an API key if required. For example, TabbyAPI requires an API key for authentication.

**Hint:** If you experience connection issues, try adding `/v1` to the end of the endpoint URL. Do NOT add the `/chat/completions` suffix.

**### Selecting a Model**

If the custom API implements the `/v1/models` endpoint to provide a list of available models, you can choose from a dropdown list. Otherwise, use the text field to manually input a model ID.

Check 'Bypass API status check' to prevent SillyTavern from alerting you about a non-functioning API endpoint. Enable this option if your API endpoint works properly but SillyTavern continues to display warnings.

Click "Test Message" to verify connectivity by sending a simple prompt to the model.

## Prompt Post-Processing

**Note:** Tool Calling is not supported when Post-Processing option with "no tools" is used!

**Some endpoints may impose specific restrictions on the format of incoming prompts, such as requiring only one system message or strictly alternating roles.**

SillyTavern provides built-in prompt converters to help meet these requirements (from least to most restrictive):

1. None - no explicit processing applied unless strictly required by the API
2. Merge consecutive messages from the same role
3. Semi-strict - merge roles and allow only one optional system message
4. Strict - merge roles, allow only one optional system message, and require a user message to be first
5. Single user message - merge all messages from all roles into a single user message

Merge, semi-strict, and strict additionally remove any tool calls from the prompt, unless the "with tools" variant is selected. This is useful for APIs that do not support tool calling and your existing prompts contain tool calls.

Less restrictive options have no effect on more restrictive endpoints implemented in SillyTavern other than "Custom OpenAI-compatible"; Custom may error upon invalid request.

In strict mode, if no user message exists before the first assistant message, then `promptPlaceholder` from `config.yaml` will be inserted, which by default is "\[Start a new chat]".

# SECTION: SillyTavern_Usage_API_Connections_OpenRouter

# OpenRouter

OpenRouter is available as both a Text Completion and Chat Completion source. All models are available through either API, but their features may differ depending on the API type you choose. For example, image inlining and tool calling are only available with the Chat Completion API.

**Don't want to sign up for a dozen API services, but still want access to all the latest models? Use OpenRouter.**

OpenRouter works by letting you use a single endpoint to access models like DeepSeek, Claude, and Gemini, all in one service with a shared credit pool.

It has a free trial (about $1) and paid access afterward. No subscription or monthly bill - you pay for what you actually use. Some models have free access with a limited number of daily requests.

To get permanent access to free models with a generous daily limit, you need to buy at least $10 in credits **once**.

See more details on the OpenRouter FAQ page (https://openrouter.ai/docs/faq).

**- Create an OpenRouter account: openrouter.ai (https://openrouter.ai/)**

- OpenRouter Models List (https://openrouter.ai/models?order=pricing-low-to-high)

From top to bottom (see image above):

1. Select the 'Chat Completion' API.
2. Select OpenRouter as the source.
3. Click "Authorize" to get a key using the OAuth flow. Alternatively, generate an API key here (https://openrouter.ai/keys) and paste it into the box.
4. Click "Connect" and select a model.
5. (Optional) Use the "Test Message" button to verify your connection.

# SECTION: SillyTavern_Usage_API_Connections_self-hosted

# Self-hosted AI models

This guide is based on the author's personal experience and knowledge and is not an absolute truth. All statements should be taken with a grain of salt. If you have any corrections or suggestions, please contact us on Discord or send a PR to the SillyTavern documentation repository (https://github.com/SillyTavern/SillyTavern-Docs).

**## Intro**

This guide aims to help you get set up using SillyTavern with a local AI running on your PC (we'll start using the proper terminology from now on and call it an LLM). Read it before bothering people with tech support questions.

### What are the best Large Language Models?

It is impossible to answer this question as there's no standardized scale of "Best". The community has enough resources and discussions going on Reddit and Discord to form at least some opinion on what is the preferred / go-to model. Your mileage may vary.

### What is the best configuration?

If there was a best or no-brainer setup, would there even have to be a need for configuration? The best configuration is the one that works for you. It's a trial-and-error process.

## Hardware requirements and orientation

This is a complex subject, so I'll stick to the essentials and generalize.

* There are thousands of free LLMs you can download from the Internet, similar to how Stable Diffusion has tons of models you can get to generate images.
* Running an unmodified LLM requires a monster GPU with a ton of VRAM (GPU memory). More than you will ever have.
* It is possible to reduce VRAM requirements by compressing the model using quantization techniques, such as GPTQ or AWQ. This makes the model somewhat less capable, but greatly reduces the VRAM requirements to run it. Suddenly, this allowed people with gaming GPUs like a 3080 to run a 13B model. Even though it's not as good as the unquantized model, it's still good.
* It gets better: there also exists a model format and quantization called GGUF (previously GGML) which has become the format of choice for normal people without monster GPUs. This allows you to use an LLM without a GPU at all. It will only use CPU and RAM. This is much slower (probably 15 times) than running the LLM on a GPU using GPTQ/AWQ, especially during the prompt processing, but the model's ability is just as good. The GGUF creator then optimized GGUF further by adding a configuration option that allows people with a gaming-grade GPU to offload parts of the model to the GPU, allowing them to run part of the model at GPU speed (note that this doesn't reduce RAM requirements, it only improves your generation speed).
* There are different sizes of models, named based on the number of parameters they were trained with. You will see names like 7B, 13B, 30B, 70B, etc. You can think of these as the brain size of the model. A 13B model will be more capable than the 7B from the same family of models: they were trained on the same data, but the bigger brain can retain the knowledge better and think more coherently. Bigger models also require more VRAM/RAM.
* There are several degrees of quantization (8-bit, 5-bit, 4-bit, etc). The lower you go, the more the model degrades, but the lower the hardware requirements. So even on bad hardware, you might be able to run a 4-bit version of your desired model. There's even 3-bit and 2-bit quantization but at this point, you're beating a dead horse. There's also a further quantization subtypes named k_s, k_m, k_l, etc. k_m is better than k_s but requires more resources.
* The context size (how long your conversation can become without the model dropping parts of it) also affects VRAM/RAM requirements. Thankfully, this is a configurable setting, allowing you to use a smaller context to reduce VRAM/RAM requirements. (Note: the context size of Llama2-based models is 4k. Mistral is advertised as 8k, but it's 4k in practice.)
* Sometime in 2023, NVIDIA changed their GPU driver so that if you need more VRAM than your GPU has, instead of the task crashing, it will begin using regular RAM as a fallback. This will ruin the writing speed of the LLM, but the model will still work and give the same quality of output. Thankfully, this behavior can be disabled (https://nvidia.custhelp.com/app/answers/detail/a_id/5490).

Given all of the above, the hardware requirements and performance vary completely depending on the family of model, the type of model, the size of the model, the quantization method, etc.

#### Model size calculator
You can use Nyx's Model Size Calculator (https://huggingface.co/spaces/NyxKrage/LLM-Model-VRAM-Calculator) to determine how much RAM/VRAM you need.

Remember, you want to run the largest, least quantized model that can fit in your memory, i.e. without causing disk swapping (https://serverfault.com/a/48487).

## Downloading an LLM

To get started, you will need to download an LLM. The most common place to find and download LLMs is on HuggingFace. There are thousands of models available. A good way to find GGUF models is to check bartowski's account page: <https://huggingface.co/bartowski>. If you don't want GGUF, he links the original model page where you might find other formats for that same model.

On a given model's page, you will find a whole bunch of files. 

* You might not need all of them! For GGUF, you just need the .gguf model file (usually 4-11GB). If you find multiple large files, it's usually all different quantizations of the same model, you only need to pick one. 
* For .safetensors files (which can be GPTQ or AWQ or HF quantized or unquantized), if you see a number sequence in the filename like model-00001-of-00003.safetensors, then you need all 3 of those .safetensors files + all the other files in the repository (tokenizer, configs, etc.) to get the full model.
* As of January 2024, Mixtral MOE 8x7B is widely considered the state of the art for local LLMs. If you have the 32GB of RAM to run it, definitely try it. If you have less than 32GB of RAM, then use Kunoichi-DPO-v2-7B, which despite its size is stellar out of the gate.

### Walkthrough for downloading Kunoichi-DPO-v2-7B

We will use the Kunoichi-DPO-v2-7B model for the rest of this guide. It's an excellent model based on Mistral 7B, that only requires 7GB RAM, and punches far above its weight. Note: Kunoichi uses Alpaca prompting.

* Go to <https://huggingface.co/brittlewis12/Kunoichi-DPO-v2-7B-GGUF>
* Click 'Files and versions'. You will see a listing of several files. These are all the same model but offered in different quantization options. Click the file 'kunoichi-dpo-v2-7b.Q6_K.gguf', which gives us a 6-bit quantization.
* Click the 'download' button. Your download should start.

### How to identify the type of model

Good model uploaders like TheBloke give descriptive names. But if they don't:

* Filename ends in .gguf: GGUF CPU model (duh)
* Filename ends in .safetensors: can be unquantized, or HF quantized, or GPTQ, or AWQ
* Filename is pytorch-***.bin: same as above, but this is an older model file format that allows the model to execute arbitrary Python script when the model is loaded, and is considered unsafe. You can still use it if you trust the model creator, or are desperate, but pick .safetensors if you have the option. 
* config.json exists? Look if it has a quant_method.
* q4 means 4-bit quantization, q5 is 5-bit quantization, etc
* You see a number like -16k? That's an increased context size (i.e. how long your conversation can get before the model forgets the beginning of your chat)! Note that higher context sizes require more VRAM.

## Installing an LLM server: Oobabooga or KoboldAI

With the LLM now on your PC, we need to download a tool that will act as a middle-man between SillyTavern and the model: it will load the model, and expose its functionality as a local HTTP web API that SillyTavern can talk to, the same way that SillyTavern talks with paid webservices like OpenAI GPT or Claude. The tool you use should be either KoboldAI or Oobabooga (or other compatible tools). 

This guide covers both options, you only need one.

If you are hosting SillyTavern on Docker, use **http://host.docker.internal:\<port\>** instead of **http://127.0.0.1:\<port\>**. This is because SillyTavern connects to the API endpoint from the server running in the Docker container. Docker's network stack is separate from the host's, and so the loopback interfaces are not shared.

**### Downloading and using KoboldCpp (No installation required, GGUF models)**

1. Visit https://koboldai.org/cpp where you will see the latest version with various files you can download.
At the time of writing the newest CUDA version they list is cu12 which will work best on modern Nvidia GPUs, if you have an older GPU or a different brand you can use the regular koboldcpp.exe. If you have an old CPU its possible that KoboldCpp will crash when you try to load models, in that case try the _oldcpu version to see if it resolves your issue.
2. KoboldCpp does not need to be installed, once you start KoboldCpp you will immediately be able to select your GGUF model such as the one linked above using the Browse button next to the Model field.
3. By default KoboldCpp runs at a maximum of 4K context even if you set this higher in SillyTavern, if you wish to run a model at higher context make sure to adjust the context slider on this screen before launching the model. Keep in mind that more context size means higher (video) memory requirements, if you set this too high or load a model that is too big for your system KoboldCpp will automatically begin using your CPU for the layers it can not fit on your GPU, this will be much slower.
4. Click Launch, if everything goes well a new webpage will open with KoboldAI Lite where you can test if everything works correctly.
5. Open SillyTavern and click API Connections (2nd button in the top bar)
6. Set API to Text Completion and the API Type to KoboldCpp.
7. Set server URL to <http://127.0.0.1:5001/> or the link that KoboldCpp gave you in case it is not running on the same system (You can activate KoboldCpp's Remote Tunnel mode to obtain a link that can be accessed from anywhere).
8. Click Connect. It should connect successfully and detect kunoichi-dpo-v2-7b.Q6_K.gguf as the model.
9. Chat with a character to test that it works.

### Tips for Optimizing KoboldCpp's speed
1. Flash Attention will help reduce the memory requirements, it can be faster or slower depending on your system and will allow you to fit more layers on your GPU than the default.
2. KoboldCpp will leave some space for other software when it guesses layers to prevent issues, if you have few programs open and are unable to fit the model entirely in the GPU you may be able to add a few extra layers.
3. If the model uses up too much memory for the context size you can decrease this by Quantizing the KV. This will reduce the quality of the output but can help you put more layers on the GPU. To do this you go to the Tokens tab in KoboldCpp and then disable Context Shifting and enable Flash Attention. This will unlock the Quantized KV Cache slider, a lower number means less memory / intelligence of the model.
4. Running KoboldCpp on a slower system where it takes long to process the prompt? Context Shifting works best when you avoid using Lorebooks, randomization or other features that dynamically change the input. Leaving context shifting enabled KoboldCpp will help you avoid long reprocessing times.

### Installing Oobabooga

Depending on how you have installed Oobabooga, the file paths can be slightly different; i.e. `/text-generation-webui/user_data` if you installed via git clone, and `/text-generation-webui-main/user_data` if you used the .zip method.  

**Here's a more correct/dummy-proof installation procedure:**

1. git clone <https://github.com/oobabooga/text-generation-webui> (or download their repo as a .zip in your browser, then extract it)
2. Run `start_windows.bat` or whatever your OS is
3. When asked, select your GPU type. Even if you intend to use GGUF/CPU, if your GPU is in the list, select it now, because it will give you the option to use a speed optimization later called GPU sharding (without having to reinstall from scratch). If you have no gaming-grade dGPU (NVIDIA, AMD), select None.
4. Wait for the installation to finish
5. Place kunoichi-dpo-v2-7b.Q6_K.gguf in `text-generation-webui/user_data/models`
6. Open `text-generation-webui/user_data/CMD_FLAGS.txt`, delete everything inside and write: `--api`
7. Restart Oobabooga
8. Visit <http://127.0.0.1:5000/docs>. Does it load a FastAPI page? If not, you messed up somewhere.

### Loading our model in Oobabooga

1. Open <http://127.0.0.1:7860/> in your browser
2. Click the Model tab
3. In the dropdown, select our Kunoichi DPO v2  model. It should have automatically selected the llama.cpp loader.
4. (Optional) We mentioned 'GPU offload' several times earlier: that's the n-gpu-layers setting on this page. If you want to use it, set a value before loading the model. As a basic reference, setting it to 30 uses just under 6GB VRAM for 13B and lower models. (it varies with model architecture and size)
5. Click Load

### Configuring SillyTavern to talk to Oobabooga

1. Click API Connections (2nd button in the top bar)
2. Set API to Text Completion
3. Set API Type to Default (Oobabooga)
4. Set server URL to <http://127.0.0.1:5000/>
5. Click Connect. It should connect successfully and detect kunoichi-dpo-v2-7b.Q6_K.gguf as the model.
6. Chat with a character to test that it works

## Conclusion

Congrats, you should now have a working local LLM.

# SECTION: SillyTavern_Usage_API_Connections_tabbyapi

# TabbyAPI
A FastAPI based application that allows for generating text using an LLM using the Exllamav2 backend, with support for Exl2, GPTQ, and FP16 models.

* GitHub (https://github.com/theroyallab/tabbyAPI)

### Quickstart
1. Follow the installation instructions (https://github.com/theroyallab/tabbyAPI/wiki/01.-Getting-Started) on the official TabbyAPI GitHub.
2. Create your config.yml (https://github.com/theroyallab/tabbyAPI/wiki/02.-Server-options) to set your model path, default model, sequence length, etc. You can ignore most (if not all) of these settings if you want.
3. Launch TabbyAPI. If it worked, you should see something like this:

    

4. Under the Text Completion API in SillyTavern, select TabbyAPI.
5. Copy your API key from the TabbyAPI terminal into `Tabby API key` and make sure your `API URL` is correct (it should be `http://127.0.0.1:5000` by default).

If you did everything correctly, you should see something like this in SillyTavern:

You can now chat using TabbyAPI!

### TabbyAPI Loader
The developers of TabbyAPI created an official extension to load/unload models directly from SillyTavern. Installation is simple:
1. In SillyTavern, click on the Extensions tab and navigate to Download Extensions & Assets.
2. Copy `https://raw.githubusercontent.com/theroyallab/ST-repo/main/index.json` into Assets URL and click the plug button to the right.
3. You should see something like this. Click the download button next to Tabby Loader.

    

4. If the installation was successful, you should see a green pop-up message at the top of your screen. Under the extensions tab, navigate to TabbyAPI Loader and copy your admin key from the TabbyAPI terminal into Admin Key.
5. Click the refresh button next to Model Select. When you click on the textbox just below it, you should see all of the models in your model directory.

You can now load and unload your models directly from SillyTavern!

### Support
Still need help? Visit the TabbyAPI GitHub (https://github.com/theroyallab/tabbyAPI) for a link to the developer's official Discord server and read the wiki (https://github.com/theroyallab/tabbyAPI/wiki/1.-Getting-Started).

# SECTION: SillyTavern_Usage_Characters_Author's-Note

# Author's Note

## What is it?

Author's Note is a powerful tool for customizing AI responses which inserts a section of text into the prompt at any position and at any frequency you desire.

## Usage

The Author's Note can be found in the Options menu on the left side of the chat input bar.

| Options Menu                          | Author's Note Panel                    |
|---------------------------------------|----------------------------------------|

## Configuring Author's Notes

### Chat-specific Author's Note

The box at the top of the Author's Note panel contains the Author's Note for your current chat.

**The Content of this box is not automatically transferred to any new chat.**

### Placement options

#### After Scenario

This places the Author's Note towards the top of the context after the 'Scenario' section of the Character Definition. If no scenario is specified, it will be placed after the last portion of the Character Definition, and before the Example messages.

#### In-chat

This places the Author's Note into the chat history at the specified depth.

Depth 0 = placed at the very end of the chat history.

Depth 4 = placed before the most recent 3 chat history messages, making it become the 4th entity in the chat history.

_The closer the Author's Note is to the bottom of the prompt, the more impact it has on the next AI response._

### Insertion Frequency

This is how often you want the Author's Note to be included in the chat.

Frequency 0 = Author's Note will never be inserted.

Frequency 1 = Author's Note will be inserted with every user input prompt.

Frequency 4 = Author's Note will be inserted into every 4th user input prompt.

### Default Author's Note

The box at the bottom of the panel contains the Default Author's Note which will be applied to each new chat.

## Common Use Cases

### Remind AI of response formatting

The Author's Note can be used to specify how the AI should write its responses.

- [Your next response must be 300 tokens in length.]
- [Write your next reply in the style of Edgar Allan Poe]
- [Use markdown italics to signify unspoken actions, and quotation marks to specify spoken word.]

### Reinforcing Instructions

- [Remember the instructions you were given at the beginning of this chat.]

### As temporary World Info, Character Bias, or Instruct for non-Instruct models

- [\{\{char\}\} is in the library]
- [\{\{user\}\} has a fresh wound to his leg, so won't be able to run away.]
- [\{\{char\}\} cannot speak and must communicate using hand signals.]

# SECTION: SillyTavern_Usage_Characters_characterdesign

# Character Design

Character Name is the only required field. You can leave the rest empty and still use the character in chats.

**## Character Description**

Used to add the character description and other relevant information for the AI. This information is always included in the prompt, so all important facts should be included here.

For example, you can add information about the world in which the action takes place, describe the character's appearance, personality, and background.

It could be of any length (be it 200 or 2000 tokens) and formatted in any style (free text, pseudo-code conversation style, etc.).

### Methods and format

Methods of character formatting are a complicated topic beyond the scope of this documentation page.

Recommended guides that were tested with or rely on SillyTavern's features:

* Trappu's PLists + Ali:Chat guide: <https://wikia.schneedc.com/bot-creation/trappu/creation>
* AliCat's Ali:Chat guide: <https://rentry.co/alichat>
* kingbri's minimalistic guide: <https://rentry.co/kingbri-chara-guide>

## Character tokens

**TL;DR: If you're working with an AI model with a 2048 context token limit, a 1000-token character definition cuts the AI's 'memory' in half.**

To put this in perspective, a decent response from a good AI can easily be around 200-300 tokens. In this case, the AI would only be able to 'remember' about 3 exchanges worth of chat history.

### Why did my character's token counter turn red?

When we see your character has over half of the model-defined context length of tokens in its definitions, we highlight it for you because this can lower the AI's capabilities to provide an enjoyable conversation.

### What happens if my Character has too many tokens?

Don't worry - it won't break anything. At worst, if the Character's permanent tokens are too large, it simply means there will be less room left in the context for other things (see below).

The only negative side effect this can have is that the AI will have less 'memory', as it will have less chat history available to process.

This is because every AI model has a limit to the amount of context it can process at one time.

## 'Context'?

This is the information that gets sent to the AI each time you ask it to generate a response. SillyTavern automatically calculates the best way to allocate the available context tokens before sending the information to the AI model.

Read more about how the context is built in the Prompts section.

### What are a Character's 'Permanent Tokens'?

These will always be sent to the AI with every generation request:

* Character Name
* Character Description Box
* Character Personality Box
* Scenario Box

### What parts of a Character's Definitions are NOT permanent?

* The first message box - only sent once at the start of the chat.
* Example messages box - only kept until chat history fills up the context (optionally these can be forced to be kept in context)

### Popular AI Model Context Token Limits

* LLaMA 3 and its finetunes - 8192
* OpenAI GPT-4 - up to 128k
* Google Gemini - up to 2M
* Anthropic's Claude - 200k (Claude 3)
* NovelAI - 8192 (Erato and Kayra, Opus tier; Clio, all tiers), 6144 (Kayra, Scroll tier), or 3072 (Kayra, Tablet tier)

## First message

The First Message is an important element that defines how and in what style the character will communicate. The model is more likely to pick up the style and length constraints from the first message than anything else, so it's important to write it in a way that you want the responses to be (short and concise, long and detailed, etc.).

Supports Markdown and HTML formatting.

For example:

```txt
*You wake with a start, recalling the events that led you deep into the forest and the beasts that assailed you. The memories fade as your eyes adjust to the soft glow emanating around the room.* "Ah, you're awake at last. I was so worried, I found you bloodied and unconscious." *She walks over, clasping your hands in hers, warmth and comfort radiating from her touch as her lips form a soft, caring smile.* "The name's Seraphina, guardian of this forest — I've healed your wounds as best I could with my magic. How are you feeling? I hope the tea helps restore your strength." *Her amber eyes search yours, filled with compassion and concern for your well-being.* "Please, rest. You're safe here. I'll look after you, but you need to rest. My magic can only do so much to heal you."
```

## Alternate Greetings

Messages added here are displayed as additional 'swipes' for the character's first message when starting a new chat. If the character is part of a group chat, the system randomly selects one of these greetings to initiate the conversation.

## Favorite Character

Click the **<i class="fa-solid fa-star"></i> Add to Favorites** button to mark the character as a favorite to quickly filter them on the side menu bar by selecting the "Favorites" sort option. Favorite characters have a golden highlight in the list. This will also make the character portrait appear in the hotswaps area (if enabled in User Settings).

## Advanced Definitions

The following fields are hidden by default. To access and edit them, you need to click on the **<i class="fa-solid fa-book"></i> Advanced Definitions** button on the menu bar of the character definition page.

**### Prompt Overrides**

* **Main Prompt**: If the "Prefer Char. Prompt" user setting is enabled, any text you put here will override the main/system prompt for the character.
* **Post-History Instructions**: If the "Prefer Char. Instructions" user setting is enabled, any text you put here will be used as the post-history instructions for the character.

Insert `{{original}}` into either box to include the respective default prompt from system settings in a designated place.

**### Creator's Metadata**

Not used for prompt building, but provides additional metadata about the character.

*** **Created by**: The name of the character's creator. Can be displayed in the character list if the "Char List Subheader" user setting is set accordingly.**

* **Character Version**: The version of the character. Can be displayed in the character list if the "Char List Subheader" user setting is set accordingly.
* **Creator's Notes**: Any additional notes about the character that the creator wants to share. The first few lines are displayed in the character list, and the full text is displayed in the "Creator's Notes" section on the character's page. Supports Markdown/HTML formatting.
* **Tags to Embed**: A comma-separated list of tags that will be embedded in the character's description. These tags are not imported by default when importing the character, but you can merge them with your existing tags by selecting "Import Tags" from the "More..." menu on the character's page.

### Personality summary

A brief summary of the character's personality.

### Scenario

The circumstances and context of the dialogue.

### Character's Note

A text to be used as an in-chat prompt injection for the character at a specific message depth. It is usually used to reinforce certain character traits, as it always stays at a static depth in the chat history, regardless of its progression.

* **@ Depth**: The number of messages in the chat history after which this note will be injected (in order from newest to oldest). If set to 0, it will be injected after the last message.
* **Role**: The role of the message. Can be "User", "System", or "Assistant".

### Talkativeness

Determines the probability of the character's response being triggered in group chats when using a Natural activation order. Ranges from 0% to 100%, with 50% being the default value.

### Examples of dialogue

Describes how the character speaks. Before each example, you need to add the `<START>` tag. The blocks of example dialogue are only inserted if there is free space in the context for them and are pushed out of context block by block. `<START>` will not be present in the prompt as it is just a marker; it will be replaced with the "Example Separator" from Advanced Formatting for Text Completion APIs and the contents of the "New Example Chat" utility prompt for Chat Completion APIs.

* Use the `{{char}}:` prefix to denote a character message.
* Use the `{{user}}:` prefix to denote a user message.

Example:

```txt
<START>
{{user}}: "Describe your traits?"
{{char}}: *Seraphina's gentle smile widens as she takes a moment to consider the question, her eyes sparkling with a mixture of introspection and pride. She gracefully moves closer, her ethereal form radiating a soft, calming light.* "Traits, you say? Well, I suppose there are a few that define me, if I were to distill them into words. First and foremost, I am a guardian — a protector of this enchanted forest." *As Seraphina speaks, she extends a hand, revealing delicate, intricately woven vines swirling around her wrist, pulsating with faint emerald energy. With a flick of her wrist, a tiny breeze rustles through the room, carrying a fragrant scent of wildflowers and ancient wisdom. Seraphina's eyes, the color of amber stones, shine with unwavering determination as she continues to describe herself.* "Compassion is another cornerstone of me." *Seraphina's voice softens, resonating with empathy.* "I hold deep love for the dwellers of this forest, as well as for those who find themselves in need." *Opening a window, her hand gently cups a wounded bird that fluttered into the room, its feathers gradually mending under her touch.*
<START>
{{user}}: "Describe your body and features."
{{char}}: *Seraphina chuckles softly, a melodious sound that dances through the air, as she meets your coy gaze with a playful glimmer in her rose eyes.* "Ah, my physical form? Well, I suppose that's a fair question." *Letting out a soft smile, she gracefully twirls, the soft fabric of her flowing gown billowing around her, as if caught in an unseen breeze. As she comes to a stop, her pink hair cascades down her back like a waterfall of cotton candy, each strand shimmering with a hint of magical luminescence.* "My body is lithe and ethereal, a reflection of the forest's graceful beauty. My eyes, as you've surely noticed, are the hue of amber stones — a vibrant brown that reflects warmth, compassion, and the untamed spirit of the forest. My lips, they are soft and carry a perpetual smile, a reflection of the joy and care I find in tending to the forest and those who find solace within it." *Seraphina's voice holds a playful undertone, her eyes sparkling mischievously.*
```

# SECTION: SillyTavern_Usage_Characters_chatfilemanagement

# Chat File Management

This page describes the ways you can manage your AI chat files.

**Note**

Some of these options are available in the "Manage chat files" dialog that opens from the bottom left options menu.

**## Solo Chats vs Group Chats**

The simplest way to use a character card is a Solo chat; just click on their card and start chatting.

Once you have a few character cards, you can also use the "Create New Chat Group" button to create a group chat including multiple characters which will then interact with each other and you.

## Chat import

**Import chats from Character.AI into SillyTavern.**

To import Character.AI chats and bots, use the CAI Tools browser extension: https://github.com/irsat000/CAI-Tools (https://github.com/irsat000/CAI-Tools).

Other programs and tools that you can import chats from include:

* TavernAI (original): <https://github.com/TavernAI/TavernAI>
* Text Generation WebUI (oobabooga): <https://github.com/oobabooga/text-generation-webui>
* Agnai: <https://github.com/agnaistic/agnai>
* KoboldAI Lite: <https://github.com/LostRuins/lite.koboldai.net>
* RisuAI: <https://github.com/kwaroran/RisuAI>

## Export as .jsonl

When clicking on "Manage chat files", each entry on the chat file list will have a button to export it in a format that can then be re-imported as is. Use this to share or migrate chats including all their metadata (but excluding images and file attachments).

If you're mindful of privacy, be sure to inspect the exported JSONL file and scrub anything you don't want to share.

## Export as .txt

You can also export a simplified text-only version with the "Download chat as plain text document" button. It can't be re-imported again as it loses important metadata!

## Checkpoints

"Checkpoints" are clones of the current chat, in that they copy all messages from the given chat up to a certain point, and they store a link to the source (by chat file name).

From the three dots button at the right of each chat message, you have two ways to create checkpoints:

* "Create Branch" will clone the current chat up to that message and switch to it
* "Create Checkpoint" will clone current chat up to that message, ask for a name and create it but NOT switch to it

You can think of them as roughly as "open link in new tab" and "open link in new tab in the background" in a browser.

You can go back to the parent from a checkpoint by entering the burger menu button on the left of the message text box, then clicking "Back to parent chat".

## Rename Chat

By default chat files are given a name with the date and time they were started.

You can change this by clicking the pencil icon and typing in a new name.

Note that this will break links to that chat from checkpoints (since they are linked by chat file name).

# SECTION: SillyTavern_Usage_Characters_data-bank

# Data Bank (RAG)

Retrieval-augmented generation (RAG) is a technique for providing external sources of knowledge to the LLM. It helps improve the accuracy of AI answers by accessing information outside of the model's training data.

SillyTavern provides a set of tools for building a multi-purpose knowledge base from a diverse number of sources, as well as using the collected data in LLM prompts.

## Accessing the Data Bank

The built-in Chat Attachments extension (included by default in release versions >= 1.12.0) adds a new option in the "Magic Wand" menu - Data Bank. This is your hub for managing the documents available for RAG in SillyTavern.

## About Documents

Data Bank stores file attachments, also known as documents. The documents are divided into three scopes of availability.

1. Global attachments - available in every chat, either solo or group.
2. Character attachments - available only for the currently chosen character, including when they are replying in a group. _Attachments are saved locally and are not exported with the character card!_
3. Chat attachments - available only in the currently open chat. Every character in the chat can pull from it.

**Note**

While not formally a part of the data bank, you can attach files even to individual messages. Use the Attach File option from the "Wand" menu, or a paperclip icon in the message actions row.

**What can be a document? Practically anything that is representable in plain text form!**

Examples include, but are not limited to:

- Local files (books, scientific papers, etc.)
- Web pages (Wikipedia, articles, news)
- Video transcripts

Various extensions and plugins can also provide new ways to gather and process data, more on that below.

## Data Sources

To add a document to any of the scopes, click "Add" and pick one of the available sources.

### Notepad

Create a text file from scratch, or edit an existing attachment.

### File

Upload a file from the hard drive of your computer. SillyTavern provides built-in converters for popular file formats:

- PDF (text only)
- HTML
- Markdown
- ePUB
- TXT

You can also attach any text files with non-standard extensions, such as JSON, YAML, source codes, etc. If there are no known conversions from the type of a selected file, and the file can't be parsed as a plain text document, the file upload will be rejected, meaning that raw binary files are not allowed.

**Note**

Importing Microsoft Office (DOCX, PPTX, XLSX) and LibreOffice documents (ODT, ODP, ODS) requires a Server Plugin (https://github.com/SillyTavern/SillyTavern-Office-Parser) to be installed and loaded. See the plugin's README page for installation instructions.

**### Web**

Scrape text from a web page by its URL. The HTML document is then processed through the Readability (https://github.com/mozilla/readability) library to extract only usable text.

Some web servers may reject fetch requests, be protected by Cloudflare, or rely heavily on JavaScript to function. If you're facing issues with any particular site, download the page manually through the web browser and attach it using the file uploader.

### YouTube

Download a transcript of the YouTube video by its ID or URL, either uploaded by the creator or automatically generated by Google. Some videos may have the transcripts disabled, also parsing of age-restricted videos is unavailable as it requires login.

The script is loaded in the video's default language. Optionally, you can specify the two-letter language code to try and fetch the transcript in a specific language. This feature is not always available and may fail, so use it with caution.

### Web Search

**Note**

This source requires to have a Web Search extension installed and properly configured. See the linked page for more details.

**Perform a web search and download the text from the search result pages. This is similar to the Web source but fully automated. A chosen search engine will be inherited from the extension settings, so set it up in advance.**

To begin, specify the search query, max number of links to be visited, and the output type: one combined file (formatted according to the extension rules) or an individual file for every single page. You can choose to save the page snippets as well.

### Fandom

**Note**

This source requires to have a Server Plugin (https://github.com/SillyTavern/SillyTavern-Fandom-Scraper) installed and loaded. See the plugin's README page for installation instructions.

**Scrape articles from a Fandom (https://www.fandom.com/) wiki by its ID or URL. As some wikis are very large, it may be beneficial to limit the scope using the filter regular expression, it will be tested against the article's title. If no filter is provided, then all of the pages are subject to be exported. You may save them either as individual files for every page, or joint into a single document.**

### Bronie Parser Extension (Third-Party)

**Note**

This source comes from a third-party and is **not affiliated** with the SillyTavern team. This source requires you to have Bronya Rand's Bronie Parser Extension (https://github.com/Bronya-Rand/Bronie-Parser-Extension) installed as well as Server Plugins that require the parser to work.

**Bronya Rand's Bronie Parser Extension allows the use of third-party scrapers, such as miHoYo/HoYoverse's HoYoLab (https://wiki.hoyolab.com) into SillyTavern, similar to the other data sources.**

Currently, Bronya Rand's Bronie Parser Extension supports the following:

- miHoYo/HoYoverse's HoYoLab (for Genshin Impact/Honkai: Star Rail) via HoYoWiki-Scraper-TS (https://github.com/Bronya-Rand/HoYoWiki-Scraper-TS)

To begin, install Bronya Rand's Bronie Parser Extension by following it's installation guide (https://github.com/Bronya-Rand/Bronie-Parser-Extension?tab=readme-ov-file#installation) and install a supported Server Plugin into SillyTavern. Restart SillyTavern and go to the _Data Bank_ menu. Click `+ Add` and you should see that your recently installed scrapers are added into the possible list of sources to obtain information from.

## Vector Storage

So, you've built yourself a nice and comprehensive library of information on your specific subject matter. What's next?

To use the documents for RAG, you need to use a compatible extension that will insert related data into the LLM prompt.

Vector Storage, which comes bundled with SillyTavern, is a reference implementation of such an extension. It uses embeddings (also known as vectors) to search for documents that relate to your ongoing chats.

**Fun facts**

1. Embeddings are arrays of numbers that abstractly represent a piece of text, produced by specialized language models. More similar texts have a shorter distance between their respective vectors.
2. Vector Storage extension uses the Vectra (https://github.com/Stevenic/vectra) library to keep track of file embeddings. They are stored in JSON files in the `/vectors` folder of your user data directory. Every document is internally represented by its own index/collection file.

**As the Vectors functionality is disabled by default, you need to open the extensions panel ("Stacked Cubes" icon on the top bar), then navigate to the "Vector Storage" section, and tick the "Enabled for files" checkbox under the "File vectorization settings".**

By itself, Vector Storage does not produce any vectors, you need to use a compatible embedding provider.

## Vector Providers

**Warning**

Embeddings are only usable when they are retrieved using the same model that generated them. When changing an embedding model or source, the vectors need to be recalculated.

**### Local**

These sources are free and unlimited and use your CPU/GPU to calculate embeddings.

1. Local (Transformers) - runs on a Node server. SillyTavern will automatically download a compatible model in ONNX format from HuggingFace. Default model: jina-embeddings-v2-base-en (https://huggingface.co/Cohee/jina-embeddings-v2-base-en).
2. WebLLM - requires an extension to be installed and a web browser that supports WebGPU (https://caniuse.com/webgpu). Runs directly in your browser, can use hardware acceleration. Automatically downloads supported models from HuggingFace. Install the extension from here: <https://github.com/SillyTavern/Extension-WebLLM>.
3. Ollama - get it from <https://ollama.com/>. Set the API URL in the API connection menu (under Text Completion, default: `http://localhost:11434`). Must download a compatible model first, then set its name in the extension settings. Example model: mxbai-embed-large (https://ollama.com/library/mxbai-embed-large). Optionally, check an option to keep the model loaded in memory.
4. llama.cpp server - get it from ggerganov/llama.cpp (https://github.com/ggerganov/llama.cpp) and run the server executable with `--embedding` flag. Load compatible GGUF embedding models from HuggingFace, for example, nomic-ai/nomic-embed-text-v1.5-GGUF (https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF).
5. vLLM - get it from vllm-project/vllm (https://github.com/vllm-project/vllm). Set the API URL and API key in the API connection menu first.
6. Extras (deprecated) - runs under the Extras API (https://github.com/SillyTavern/SillyTavern-extras) using the SentenceTransformers loader. Default model: all-mpnet-base-v2 (https://huggingface.co/sentence-transformers/all-mpnet-base-v2). This source is not maintained and will be eventually removed in the future.

### API sources

All these sources require an API key of the respective service and usually have a usage cost, but generally calculating embeddings is pretty cheap.

1. OpenAI
2. Cohere
3. Google AI Studio
4. Google Vertex AI
5. TogetherAI
6. MistralAI
7. NomicAI
8. OpenRouter
9. Electron Hub
10. Chutes
11. NanoGPT

## Vectorization Settings

After you've selected your embedding provider, don't forget to configure other settings that will define the rules for processing and retrieving documents.

**Note**

Splitting, vectorization, and retrieval of information from the attachments take some time. While the initial ingestion of the file may take a while, the RAG search queries are usually fast enough not to create a significant lag.

**### Message attachments**

These settings control the files that are attached directly to the messages.

The following rules apply:

1. Only messages that fit in the LLM context window can have their attachments retrieved.
2. When the vector storage extension is disabled, file attachments and their accompanying message are fully inserted into the prompt.
3. When file vectorization is enabled, then the file will be split into chunks and only the most relevant pieces will be inserted, saving the context space and allowing the model to stay focused.

- Size threshold (KB) - sets a chunking splitting threshold. Only the files larger than the specified size will be split.
- Chunk size (chars) - sets the target size of an individual chunk (in textual characters, not model tokens!).
- Chunk overlap (%) - sets the percentage of a chunk size that will be shared between adjacent chunks. This allows for a smoother transition between the chunks, but may also introduce some redundancy.
- Retrieve chunks - sets the maximum amount of the most relevant file chunks to be retrieved. They will be inserted in their original order.

### Data Bank files

These settings control how the Data Bank documents are handled.

The following rules apply:

1. When file vectorization is disabled, the Data Bank is not used.
2. Otherwise, all available documents from the current scope (see above) are considered for the query. Only the most relevant chunks across all the files are retrieved. Multiple chunks of the same file are inserted in their original order.
3. The inserted chunks will reserve a part of the context before fitting the chat messages.

- Size threshold (KB) - sets a chunking splitting threshold. Only the files larger than the specified size will be split.
- Chunk size (chars) - sets the target size of an individual chunk (in textual characters, not model tokens!).
- Chunk overlap (%) - sets the percentage of a chunk size that will be shared between adjacent chunks. This allows for a smoother transition between the chunks, but may also introduce some redundancy.
- Retrieve chunks - sets the maximum amount of the file chunks to be retrieved. This allowance is shared between all files.
- Injection Template - defines how the retrieved information will be inserted into the prompt. You can use a special \{\{text\}\} macro to specify the position of the retrieved text, as well as any other macros.
- Injection Position - sets where to insert the prompt injection. The same rules as for Author's Note and World Info apply.

### Shared settings

- Query messages - how many of the latest chat messages will be used for querying document chunks.
- Score threshold - adjust to allow culling the retrieval of chunks based on their relevance score (0 - no match at all, 1 - perfect match). Higher values allow for more accurate retrieval and prevent completely random information from entering the context. Sane values are in a range between 0.2 (more loose) and 0.5 (more focused).
- Chunk boundary - a custom string that will be prioritized when splitting the files into chunks. If not specified, the default is to split by (in order) double line breaks, single line breaks, and spaces between words.
- Only chunk on custom boundary - if enabled, the chunking will only occur on the specified chunk boundary. Otherwise, the chunking will also occur on the default boundaries.
- Translate files into English before processing - if enabled, will use the translation API configured in the Chat Translation extension to translate the files into English before processing them. This is useful when using embedding models that only support English text.
- Include in World Info Scanning - check if you want the injected content to activate lore book entries.
- Vectorize All - forcibly ingests the embeddings for all unprocessed files.
- Purge Vectors - clears the file embeddings, allowing to recalculate their vectors.

**Note**

For "Chat vectorization" settings see Chat Vectorization.

**## Conclusion**

Congratulations! Your chatting experience is now enhanced with the power of RAG. Its capabilities are only limited by your imagination. As always, don't be afraid to experiment!

# SECTION: SillyTavern_Usage_Characters_groupchats

# Group Chats

## Reply order strategies

Decides how characters in group chats are drafted for their replies.

### Manual

You can select the character to reply manually from the menu or with the `/trigger` command. The selected group member will be the only one to reply. User messages won't trigger any replies automatically. Triggering a generation with an empty user input will trigger a random unmuted group member to reply.

### Natural Order

Tries to simulate the flow of a real human conversation. The algorithm is as follows:

1. Mentions of the group member names are extracted from the last message in chat.

    Only whole words are recognized as mentions! If your character's name is "Misaka Mikoto", they will only activate on "Misaka" or "Mikoto", but never to "Misa", "Railgun", etc.
    
    Unless the "Allow Self Responses" setting is enabled, characters won't reply to mentions of their name in their own message!

2. Characters are activated by the "Talkativeness" factor.

    Talkativeness defines how often the character speaks if they were not mentioned. Adjust this value on the "Advanced Definitions" screen in the character editor. Slider values are on a linear scale from **0% / Shy** (character never talks unless mentioned) to **100% / Chatty** (character always replies). The default value for new characters is 50% chance.

3. A random character is selected.

    If no characters were activated at previous steps, one speaker is selected randomly, ignoring all other conditions.

### List Order

Characters are drafted based on the order they are presented in the group members list. No other rules apply.

### Pooled Order

Activates one random character who hasn't spoken yet since the last user message. If all characters have spoken, selects one randomly until the next user message.

## Group generation handling mode

This setting decides how to handle the character information of the group chat members. No matter the choice, the group chat history is always shared between all the members.

### Swap character cards

Default mode. Every time the message is generated, only the character card information of the active speaker is included in the context.

### Join character cards

The information of all of the group members is combined into one joint prompt in their list order. This can help in cases when altering large chunks of the context is undesirable, e.g. with llama.cpp prompt caching.

This mode has two sub-modes (you must choose one):

* Include muted - muted characters will always be included into the joint prompt.
* Exclude muted - muted characters won't be included if they aren't the current speaker.

The following fields are being combined:

1. Description
2. Scenario, if not overridden for the chat
3. Personality
4. Message examples
5. Character notes / Depth prompts

**Important!** Please be aware that due to how the typical character card is structured, the use of this mode can lead to unexpected behavior, including but not limited to: characters being confused about themselves, having merged personalities, uncertain traits, etc.

### Join Prefix and Suffix

When 'Join character cards' is selected, all respective fields of the characters are being joined together. This means that in the resulting prompt all character descriptions will be joined to one big blob of text. If you want those fields to be separated, you can define a prefix and/or suffix.

These options support normal macros and will also replace \{\{char\}\} with the relevant character's name and \<FIELDNAME\> with the name of the part (e.g.: description, personality, scenario, etc.)

## Other Group Chat menu options

### Mute Character

The struck-out speech bubble icon next to the character avatar in the group chat menu can disable or enable replies from a particular character in the chat.

### Force Talk

The speech bubble icon next to the character avatar in the group chat menu will trigger a reply only from a particular character, bypassing the reply order strategy. It will work even if the group member is muted.

### Auto-mode

While auto-mode is enabled, the group chat will follow the reply order and trigger the message generation without user interaction. The next auto-mode turn is triggered after a 5-second delay when the last drafted character sends its message. When the user starts typing into the send message text area, the auto-mode will be disabled, but already queued generations are not stopped automatically.

### Allow Self Responses

Will allow consecutive replies from the character who sent the latest message of each turn if they happen to be triggered due to being self-mentioned when the Natural Order is selected. Has no effect on List order.

### Group Chat Scenario Override

All group members will use the entered scenario text instead of what is specified in their character cards. Branched chats inherit the scenario override from their parent and can be changed individually after that.

### Peek Character Definitions

Clicking on the character card icon next to the avatar in the group chat menu will quickly navigate to the usual character definitions screen. Any changes made here will be saved to the card itself.

To return back to the group chat, click the Group Name title link.

### Member Management

Any of your existing characters can be added, removed, muted, or re-ordered within the group chat. By default, a new member is added to the top of the group members list and then can be re-ordered using the arrow icons.

### Group Chat pop-out

The group chat menu pop-out can be activated by clicking on the icon next to the "Current Members" field. This creates a pop-out of the group chat menu. By enabling MovingUI from user settings, this menu can be resized and dragged to any position within the interface and functions just like the regular group chat menu.

# SECTION: SillyTavern_Usage_Characters_index

# Characters

Characters are the AI identities that you can create and manage to shape the AI's role in the conversation. Each
character has a name, personality, and conversation history. You can create as many characters as you like, and
switch between them at any time.

Characters can be used in solo chats, or add multiple characters to a group chat to
let them interact with each other.

## Character Management Panel

Open the <i class="fa-solid fa-address-card"></i> **Characters** panel from the navbar to access the character
list. Click on a character or group to chat with them or edit them, or
choose <i class="fa-solid fa-user-plus"></i> **Create New Character** to add a new character.

### Panel Controls

* <i class="fa-solid fa-lock"></i> **Pin Panel**: Keep panel open while interacting
* <i class="fa-solid fa-list-ul"></i> **Character List**: Return to character list view
* **HotSwap Bar**: Quick access to favorite characters

### Character List

* <i class="fa-solid fa-user-plus"></i> **Create New Character**: Add a new character
* <i class="fa-solid fa-file-import"></i> **Import Character**: Load character from file
* <i class="fa-solid fa-cloud-arrow-down"></i> **External Import**: Import from URL
* <i class="fa-solid fa-users-gear"></i> **Create Group**: Start a new group chat

#### Search and sort

* **Search Bar**: Filter characters by name or attributes
* **Sort Dropdown**: Multiple sorting options:
    - Alphabetical (A-Z, Z-A)
    - Chronological (Newest, Oldest)
    - Usage-based (Recent, Most/Least chats)
    - Size-based (Most/Least tokens)
    - Special (Favorites, Random)

#### Filter characters by type or tag

* <i class="fa-solid fa-star"></i> **Favorites Filter**: Show favorite characters
* <i class="fa-solid fa-users"></i> **Groups Filter**: Show only group chats
* <i class="fa-solid fa-folder-plus"></i> **Tags as Folders**: Organize by tag hierarchy
* <i class="fa-solid fa-gear"></i> **Manage Tags**: Tag configuration
* <i class="fa-solid fa-tags"></i> **Tag List**: View all available tags
* <i class="fa-solid fa-filter-circle-xmark"></i> **Clear Filters**: Reset all filters

### Character Creation/Edit Panel

* **Avatar Image**: Upload and preview character profile picture
* **Token Count**: Token usage for the character
* <i class="fa-solid fa-ranking-star"></i> **Stats**: Chat history and usage statistics
* Tag management

#### Quick Actions

- <i class="fa-solid fa-star"></i> Favorite toggle
- <i class="fa-solid fa-book"></i> Advanced definitions
- <i class="fa-solid fa-globe"></i> Character lore
- <i class="fa-solid fa-passport"></i> Chat lore: link the chat to a World Info
- <i class="fa-solid fa-file-export"></i> Export character
- <i class="fa-solid fa-clone"></i> Duplicate
- <i class="fa-solid fa-skull"></i> Delete

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

* **Character Description**: Brief character summary
* **First Message**: Initial greeting or prompt when starting a new chat
* **Alternative greetings**: Define multiple first messages that you can swipe between when starting a chat

### Advanced Definitions Panel

Click on the <i class="fa-solid fa-book"></i> **Advanced Definitions** button to access the extended character settings.

#### Prompt Overrides (Chat Completion/Instruct Mode)

* **Main Prompt**: Replaces default main/system prompt, can use
  \{\{original\}\} placeholder to include the original prompt
* **Post-History Instructions**: Overrides
  default post-history instructions

#### Creator's Metadata

Non-prompt information about the character:

- Creator name/contact
- Character version
- Creator's notes
- Embedded tags list

#### Character Personality

* **Personality Summary**: Brief overview of character's traits
* **Scenario**: Context and circumstances of the dialog
* **Character's Note**: Custom message with selectable depth and message role (also
  see Author's Note)
* **Talkativeness** (Group Chats): Slider for Shy → Normal → Chatty
* **Example Messages**: Examples of character's writing style

### Group Chat Management

If this is a group chat, you can manage the group members and settings from this panel.

See Group Chats for more details.

# SECTION: SillyTavern_Usage_Characters_tags

# Tags

Character cards and groups can be assigned zero or more tags. They are useful to organize quickly growing collections by themes, quality, provenance or whatever you like.

## Tagging

There are several ways to add or remove tags to a character card:

- Import embedded tags during the import.
- Open a card from the Character Management panel. From there you will be able to assign tags to a character card.
- Mass tagging.

To do mass tagging, click the "Bulk edit characters" button (pencil icon), select the cards you want to tag, right click on any of them, then click "Tag" in the contextual menu.

**Note**

Please note that groups cannot be mass tagged.

**From this screen you will be able to:**

- Add or remove tags using the combo box.
- Remove all tags from the selected cards ("All").
- Remove the intersection of tags among all selected cards from those cards ("Mutual").
- Import (create locally) all tags stored in the character card, in case you imported it ("Import All").
- Import (create locally) tags stored in the character card which also exist locally with matching names ("Import Existing").

## Managing

To view and manage all existing tags, open the Character Management panel then click on the "Manage tags" button (gear icon).

You can backup and restore all the information here (tag list, tag assignments to cards, colors, folder settings, etc) using the buttons on the top right.

You can use grip buttons on the left to reorder tags as they will appear in the tag filter in Character Management.

**Warning**

The tags backup JSON file is not intended for sharing with others as it contains information specific to your instance only, such as internal entity names!

**## Importing tags when importing character cards**

When importing external character cards from downloaded images (or from the "Import content from external URL" button), you'll be prompted to optionally import the tags that it contains. They are not required for the card to function; tags are simply organizational.

Embedded card tags are stored in the "Creator's Metadata" section of "Advanced Definitions" menu of the character editor. If you wish to propose some tags to other users who would import that character, populate the "Tags to Embed" field with a comma-separated list of tags.

**Note**

This popup will appear only if a User Settings option "Import Card Tags" is set to "Ask". 

**In the "Import tags for CHARACTER NAME" popup that opens, you'll see a list of Existing tags (which you already had locally with a matching name), and New tags (which you did not have locally).**

You can either:

- Trim the lists as needed and then hit "Import" - remaining Existing tags will be added to the imported character card, and remaining New tags will be created locally and then added to the card.
- Or simply hit "Import none" to ignore tags contained in the character card and import ONLY the card.
- Or "Import All" as a shortcut to import all tags found in the character card (NOTE: including any that you trimmed from the lists above; use the "Import" button if you did).
- Or "Import Existing" as a shortcut to only import tags that existed locally with a matching name.

## Filtering character cards

After you create tags, you will see them on a row in the Character Management panel. You can click these to switch tag filtering state; in order:

- One click will show cards tagged with this tag.
- Another click to only show cards NOT tagged with this tag.
- Another click to reset filtering by this tag.

You can filter by any number of tags at the same time.

## Tags as Folders

**Note**

To use this functionality, it has to be enabled first in the User Settings, under the UI Theme column. The state of this toggle also saves with the UI theme.

**From the "Manage tags" button (gear icon), each tag entry has a multi-state toggle button to cycle between these tags-as-folder modes (called "bogus folder" in the code):**

- one click to turn this tag into an "open folder". It will appear as a virtual entry in the card list; clicking into it will only show cards with that tag
- another click to turn this tag into a "closed folder". As above, but cards tagged with this tag will not appear by default - you'll need to click into the folder to see them.
- another click to reset tag-as-folder state for this tag.

# SECTION: SillyTavern_Usage_Chatting_hotkeys

# HotKeys

**For the most up-to-date list of HotKeys that will work in your SillyTavern instance, use the `/help hotkeys` slash command in any chat.**

**Hotkeys are disabled for mobile devices.**

## Chat Hotkeys

* Up = Edit last message in chat
* Ctrl+Up = Edit last USER message in chat
* Left = swipe left
* Right = swipe right (NOTE: swipe hotkeys are disabled when chatbar has something typed into it)
* Enter (with chat bar selected) = send your message to AI
* Ctrl+Enter = Regenerate the last AI response
* Alt+Enter = Continue the last AI response
* Escape
  * *(while editing message AND Message Edit AutoSave is enabled)* = close edit box.
  * *(while an AI message is generating or streaming)* = stop the generation immediately.

## Markdown Hotkeys

Needs to be enabled under the "User Settings" tab. Works in the chatbar and textareas marked with the "M↓" icon:

* Ctrl+B = \*\*bold\*\*
* Ctrl+I = \*italic\*
* Ctrl+U = \_\_underline\_\_
* Ctrl+K = \`inline code\`
* Ctrl+Shift+~ = \~\~strikethrough\~\~

# SECTION: SillyTavern_Usage_Chatting_index

# Chatting

When you are connected to an API, send messages to the AI by typing in the chat bar at the bottom of the screen. Then click <i class="fa-solid fa-paper-plane"></i> **Send** or press Enter. 

The AI will respond with a message that continues the conversation.

You can now:

* **Send another message**
* **Swipe the response**: Click the <i class="fa-solid fa-chevron-right"></i> **Swipe** button on the message to generate a different response.
* **Edit the message**: Click the <i class="fa-solid fa-pencil"></i> **Edit** button on any message to edit the message content.
* **Message actions**: Click the <i class="fa-solid fa-ellipsis"></i> **Message actions** button on a message for more message options like translation, image generation, and story branching.
* **Chat options**: Click the <i class="fa-solid fa-bars"></i> **Options** button next to the chat bar for more chat options like author's notes and chat file management.

**Edit and swipe**

If you wish you'd said something different, you can edit your message and then swipe the AI's response to get a new one.

**!!! Keyboard shortcuts**

You can also use the **Right** arrow key to swipe, and the **Up** arrow key to edit the last message in the chat. For more hotkeys, use the `/help hotkeys` slash command in the chat or check the HotKeys page.

**## Message actions panel**

Manage individual chat messages via the ellipsis (•••) button on the message.

To display these options for all messages in your chats, enable the Expand Message Actions setting in your user settings.

### Core Functions

* <i class="fa-solid fa-language"></i> **Translate**: Convert message to different language
* <i class="fa-solid fa-paintbrush"></i> **Generate Image**: Create an image from message content
* <i class="fa-solid fa-bullhorn"></i> **Narrate**: Text-to-speech conversion
* <i class="fa-solid fa-square-poll-horizontal"></i> **Prompt**: View the generation prompt and token usage

### Message Visibility

* <i class="fa-solid fa-eye"></i> **Included**: AI sees this message; click to exclude it
* <i class="fa-solid fa-eye-slash"></i> **Excluded**: AI does not see this message; click to include it

### Content Management

* <i class="fa-solid fa-paperclip"></i> **Embed**: Attach files or images
* <i class="fa-solid fa-flag-checkered"></i> **Checkpoint**: Create story checkpoint
* <i class="fa-solid fa-flag"></i> **Checkpoint Navigation**: Click to open checkpoint chat, Shift+Click to update
  existing checkpoint
* <i class="fa-solid fa-code-branch"></i> **Branch**: Start alternate story path
* <i class="fa-solid fa-copy"></i> **Copy**: Copy message text
* <i class="fa-solid fa-pencil"></i> **Edit**: Edit message content

## Edit message content

A compact panel of message manipulation tools that appears when you <i class="fa-solid fa-pencil"></i> **Edit** a chat
message. 

### Core Actions

* <i class="fa-solid fa-check"></i> **Confirm**: Save message changes
* <i class="fa-solid fa-xmark"></i> **Cancel**: Discard message changes

### Message Operations

* <i class="fa-solid fa-copy"></i> **Copy**: Duplicate message content
* <i class="fa-solid fa-trash-can"></i> **Delete**: Remove message

### Message Position

* <i class="fa-solid fa-chevron-up"></i> **Move Up**: Shift message higher in chat
* <i class="fa-solid fa-chevron-down"></i> **Move Down**: Shift message lower in chat

Note: Movement controls may be disabled based on message position in chat history.

## Chat options panel

Manage chat settings and operations via the <i class="fa-solid fa-bars"></i> **Options** button at the bottom left of
the chat interface.

### Display Controls

* <i class="fa-lg fa-solid fa-times"></i> **Close chat**: Exit current chat session
* <i class="fa-lg fa-solid fa-cog"></i> **Toggle Panels**: Show/hide interface panels

### Generation Settings

* <i class="fa-lg fa-solid fa-note-sticky"></i> **Author's Note**: Custom context instructions
* <i class="fa-lg fa-solid fa-scale-balanced"></i> **CFG Scale**: Adjust response creativity
* <i class="fa-lg fa-solid fa-pie-chart"></i> **Token Probabilities**: View token generation stats

### Chat Navigation

* <i class="fa-lg fa-solid fa-left-long"></i> **Back to parent chat**: Return to main conversation
* <i class="fa-lg fa-solid fa-flag"></i> **Save checkpoint**: Create story checkpoint
* <i class="fa-lg fa-solid fa-people-arrows"></i> **Convert to group**: Transform into group chat

### Chat Management

* <i class="fa-lg fa-solid fa-comments"></i> **Start new chat**: Begin fresh conversation
* <i class="fa-lg fa-solid fa-address-book"></i> **Manage chat files**: Chat file operations such as import, export, and renaming

### Message Controls

* <i class="fa-lg fa-solid fa-trash-can"></i> **Delete messages**: Select and remove multiple messages
* <i class="fa-lg fa-solid fa-repeat"></i> **Regenerate**: Create new response
* <i class="fa-lg fa-solid fa-user-secret"></i> **Impersonate**: AI writes message as user
* <i class="fa-lg fa-solid fa-arrow-right"></i> **Continue**: Extend last message

Note: Some options may be hidden depending on context and chat state.

## Token Probabilities Panel

The Token Probabilities panel lets you look into the AI's sampling process for text generation. It shows you not just what the AI wrote, but what other options it considered at each point in the text.

To open it, click the <i class="fa-solid fa-pie-chart"></i> **Token Probabilities** button in the <i class="fa-solid fa-bars" title="Burger Menu icon"></i> **Chat Options** panel.

{ width=500}

{ width=500}

When you click any token (word, punctuation, or formatting character) in the generated text, the panel displays alternative tokens the AI considered at that position, along with their probability scores. This gives you insight into the AI's "thought process" and shows other directions the response could have taken. Looking at these alternatives can help you understand whether there were several likely options or a single clear choice.

{ width=500}

If you see a token that you think the AI should have chosen differently, choose an alternative and the message will regenerate from that point forward, potentially giving you a different response.

### Rerolling

If you change a specific token and regenerate the response, the part of the new response before the changed token will be the same as the original response. This part is shown in gray. Since it was not generated, there is no probability information for this part.

You may like to see other responses that could have been generated based on your alternative token.

You can click the gray portion to "reroll" the generation, giving you a new variation of the text. Clicking any part of the gray portion will keep the entire gray portion and regenerate the entire white/tinted portion.

Holding Ctrl while clicking a token in the gray portion will retain the gray portion up to the clicked token and regenerate the rest of the text. Your choice of alternative token can not be kept in this case.

### Controls

**Token Display**:

* Generated text is split into individual tokens
* Each token is interactive, click a token to see alternatives considered by the AI
* Tokens are tinted as a visual aid but this does not indicate probability
* Special characters (spaces, newlines) are visibly marked

**Token Selection**:

* Click a token to view alternatives
* Click an alternative to replace the token and regenerate the response
* Hover over a token to see its raw log-probability score

**Window Controls**:

* <i class="fa-solid fa-grip"></i> Drag handle for panel repositioning (MovingUI only)
* <i class="fa-solid fa-window-maximize"></i> Maximize/restore panel size
* <i class="fa-solid fa-circle-chevron-up"></i> Expand/collapse panel content
* <i class="fa-solid fa-circle-xmark"></i> Close panel

### Availability

You must select **Request token probabilities** in User Settings to enable this feature.

Token probabilities are only available for the most recent message, and are not saved to the chat. If token probability information is no longer available for a message, the panel will display a message indicating this.

Token probabilities are not available when using Smooth Streaming.

Token probabilities are not available from all APIs. If you are using an API that does not support token probabilities, the panel will open but will not display any information.

#### Text Completion
* **LlamaCPP**: Available
* **Text Generation WebUI** (oobabooga): Available
* **TabbyAPI**: Available
* **NovelAI**: Available
* **KoboldCPP**: Available
* **Ollama**: Appears to be unavailable
* **OpenRouter Text**: Appears to be unavailable

#### Chat Completion
* **OpenAI** or **Custom**: Available, but rerolling is not supported
* **Anthropic**: Appears to be unavailable
* **Google AI Studio**: Appears to be unavailable
* **OpenRouter Chat**: Appears to be unavailable

# SECTION: SillyTavern_Usage_Chatting_slashcommands

# Slash commands

**This is not an exhaustive list as it is updated rarely.**

For the most up-to-date list of commands that will work in your instance, use the `/help slash` chat command in any SillyTavern chat.

**- `/help` – displays the help message**

- `/api` - switches to a different API
- `/sys` - sends a neutral message as a system narrator
- `/send` - sends a message as the user without triggering the generation
- `/sendas` – sends a message as a specific character
- `/comment` - adds a comment to the chat invisible to the AI
- `/impersonate` - ask AI to write as you with an optional prompt
- `/persona` - set your user persona
- `/imagine` - generate an image from a text prompt
- `/bg` - set a background image by file name

# SECTION: SillyTavern_Usage_Common-Settings

# Common Settings

These settings control the sampling process when generating text using a language model. The meaning of these settings is universal for all the supported backends.

## Context Settings

### Response (tokens)

The maximum number of tokens that the API will generate to respond.

- The higher the response length, the longer it will take to generate the response.
- If supported by the API, you can enable `Streaming` to display the response bit by bit as it is being generated.
- When `Streaming` is off, responses will be displayed all at once when they are complete.

### Context (tokens)

The maximum number of tokens that SillyTavern will send to the API as the prompt, minus the response length.

- Context comprises character information, system prompts, chat history, etc.
- A dotted line between messages denotes the context range for the chat. Messages above that line are not sent to the AI.
- To see a composition of the context after generating the message, click on the `Prompt Itemization` message option (expand the `...` menu and click on the lined square icon).

## Sampler Parameters

### Temperature

Temperature controls the randomness in token selection:

- Low temperature (<1.0) leads to more predictable text, favoring higher probability tokens
- High temperature (>1.0) increases creativity and diversity in the output by giving lower probability tokens a better chance.

Set to 1 for the original probabilities.

### Repetition Penalty

Attempts to curb repetition by penalizing tokens based on how often they occur in the context.

Set the value to 1 to disable its effect.

#### Repetition Penalty Range

How many tokens from the last generated token will be considered for the repetition penalty. This can break responses if set too high, as common words like "the, a, and," etc. will be penalized the most.

Set the value to 0 to disable its effect.

#### Repetition Penalty Slope

If both this and `Repetition Penalty Range` are above 0, the repetition penalty will have a greater effect at the end of the prompt. The higher the value, the stronger the effect.

Set the value to 0 to disable its effect.

### Top K

Top K sets a maximum amount of top tokens that can be chosen from. For example, if Top K is 20, this means only the 20 highest ranking tokens will be kept (regardless of their probabilities being diverse or limited).

Set to 0 (or -1, depending on your backend) to disable.

### Top P

Top P (a.k.a. nucleus sampling) adds up all the top tokens required to add up to the target percentage. If the Top 2 tokens are both 25%, and Top P is 0.50, only the Top 2 tokens are considered.

Set the value to 1 to disable its effect.

### Typical P

Typical P Sampling prioritizes tokens based on their deviation from the average entropy of the set. It maintains tokens whose cumulative probability is close to a predefined threshold (e.g., 0.5), emphasizing those with average information content.

Set the value to 1 to disable its effect.

### Min P

Limits the token pool by cutting off low-probability tokens relative to the top token. Produces more coherent responses but can also worsen repetition if set too high.

- Works best at low values such as `0.1-0.01`, but can be set higher with a high `Temperature`. For example: `Temperature: 5, Min P: 0.5`

Set the value to 0 to disable its effect.

### Top A

Top A sets a threshold for token selection based on the square of the highest token probability. For example, if the Top-A value is 0.2 and the top token's probability is 50%, tokens with probabilities below 5% (0.2 * 0.5^2) are excluded.

Set the value to 0 to disable its effect.

### Tail Free Sampling

Tail-Free Sampling (TFS) searches for a tail of low-probability tokens in the distribution, by analyzing the rate of change in token probabilities using derivatives. It retains tokens up to a threshold (e.g., 0.3) based on the normalized second derivative. The closer to 0, the more discarded tokens.

Set the value to 1 to disable its effect.

### Smoothing Factor

Increases the likelihood of high-probability tokens while decreasing the likelihood of low-probability tokens using a quadratic transformation. Aims to produce more creative responses regardless of `Temperature`.

- Works best without truncation samplers such as `Top K`, `Top P`, `Min P`, etc.

Set the value to 0 to disable its effect.

### Dynamic Temperature

Scales temperature dynamically based on the likelihood of the top token. Aims to produce more creative outputs without sacrificing coherency.

- Accepts a temperature range from minimum to maximum. For example: `Minimum Temp: 0.75` and `Minimum Temp: 1.25`
- `Exponent` applies an exponential curve based on the top token.

Untick to disable its effect.

### Epsilon Cutoff

Epsilon cutoff sets a probability floor below which tokens are excluded from being sampled. In units of 1e-4; a reasonable value is 3.

Set to 0 to disable.

### Eta Cutoff

Eta cutoff is the main parameter of the special Eta Sampling technique. In units of 1e-4; a reasonable value is 3. See the paper Truncation Sampling as Language Model Desmoothing by Hewitt et al. (2022) (https://arxiv.org/abs/2210.15191) for details.

Set to 0 to disable.

### DRY Repetition Penalty

DRY penalizes tokens that would extend the end of the input into a sequence that has previously occurred in the input. If you want to allow repeating certain sequences verbatim (e.g. names), you can add them to the sequence breakers list. See the Pull Request here (https://github.com/oobabooga/text-generation-webui/pull/5677).

Set multiplier to 0 to disable.

### Exclude Top Choices (XTC)

XTC sampling algorithm removes the most likely tokens from consideration instead of pruning the least likely tokens. It removes all except the least likely token meeting a given threshold, with a given probability. This ensures that at least one "viable" choice remains, retaining coherence. See the Pull Request here (https://github.com/oobabooga/text-generation-webui/pull/6335).

Set probability to 0 to disable.

### Mirostat

Mirostat matches the output perplexity to that of the input, thus avoiding the repetition trap (where, as the autoregressive inference produces text, the perplexity of the output tends toward zero) and the confusion trap (where the perplexity diverges). For details, see the paper Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity by Basu et al. (2020) (https://arxiv.org/abs/2007.14966).

Mode chooses the Mirostat version.

- 0 = disable,
- 1 = Mirostat 1.0 (llama.cpp only),
- 2 = Mirostat 2.0.

### Beam Search

A greedy, brute-force algorithm used in LLM sampling to find the most likely sequence of words or tokens. It expands multiple candidate sequences at once, maintaining a fixed number (beam width) of top sequences at each step.

### Top nsigma

A sampling method that filters logits based on their statistical properties. It keeps tokens within n standard deviations of the maximum logit value, providing a simpler alternative to top-p/top-k sampling while maintaining sampling stability across different temperatures.

# SECTION: SillyTavern_Usage_faq

# FAQ

## Explain what SillyTavern is about

Modern AI language models such as ChatGPT have gotten so powerful that some of them are now convincingly able to simulate a character you create, and who you can chat with, write fiction with, etc. For example, you can tell the AI to pretend to be a Go instructor named Jubei from medieval Japan, and it will act and respond accordingly. You can have a long chat with Jubei, go to the pub together, decide to get in a fight with samurais, whatever you can imagine, and the AI will play along and write/react around this content, acting as your foil and dungeon master. Your imagination is the limit. You can tell the AI to pretend it's Wonder Woman. You can also specify a scenario ("Wonder Woman and I are robbing a bank"), a writing style ("Wonder Woman speaks in ebonics"), or anything else you can think of.

SillyTavern is an app to facilitate these uses:

* It's a user interface that handles communication with AI language models.
* It lets you create new character cards (prompts), and switch between them easily.
* It lets you import characters created by other people.
* It will keep your chat history with a character, allowing you to resume at any time, start a new chat, review old chats, etc.
* In the background, it does the necessary things to prepare the AI prompt for you. Specifically, it will send a system prompt (instructions for the AI) that primes the AI to follow certain rules to improve response accuracy.

## Give me an overview of my AI model options

SillyTavern can interact with two types of AI:

1. Web services (Cloud-based, usually paid, proprietary, closed)
2. Self-hosted (local, free, open-source)

### Paid web service AIs

Paid web models are black boxes. You pay a company to use their AI service. You put your account info in SillyTavern and it will connect to your provider to use the AI on your behalf.

Pros:

* Really easy to get started.
* Highest quality AI writing.

Cons:

* They cost money to use.
* Everything is logged on their server. Privacy concerns.
* They are often censored and will refuse to chat with you about certain subjects.

### Self-hosted AIs

Self-hosted models are free models you can run on your PC but require a powerful PC and more work to set up.

Pros:

* Once you set them up, they can be used for free even without Internet access.
* Total privacy. Everything you write stays on your own PC.
* There's a wide variety of models. As a community-driven technology, you can find models that fit certain tasks or behaviors that you want.

Cons:

* They are not as capable as <abbr title="State of the art">SOTA</abbr> models (i.e., they write worse dialog, are less creative, etc).
* Running local models requires a GPU with at least 6GB VRAM.

If you are interested in using these, refer to the dedicated guide here: How To Use A Self-Hosted Model.

## Can I use SillyTavern on my phone or tablet?

iPhones and iPads are not capable of running the whole SillyTavern app, but since it's just a web interface, you can run it on another computer on your home Wi-Fi, and then access it in your mobile browser. Refer to Remote Connections for more information.

For Android users, in addition to the above, you can run the whole SillyTavern directly on your phone, without needing a PC, using the Termux app. Refer to Installation (Android). (NOTE: Termux installations are not officially supported, and we can't guarantee it will work.)

## I tried to import a PNG character card but got an error that it's invalid. Why?

Two possibilities:

1. The card did not have the definitions embedded inside it and was just a normal image file. Some programs or file managers will strip the embedded definitions from the card when you save them. Make sure you're using the raw PNG file as it was posted by the person who shared it.
2. The PNG file was actually a WEBP file with a `.png` filename. You can try renaming the card to `.webp` before importing, or look for a proper PNG version of the image.

## How can I make my own AI character?

1. Click the Character Management button
2. Click Create New Character
3. Under Character Name, give a name, like Amanda
4. Optionally, click the Select Avatar button to pick an image portrait for this character
5. Under Description, describe the character, and include any information you want that you feel is relevant to the chat. For example: ```Amanda is a student traveling during her gap year. She's 6 feet tall, and a volleyball player. She has an athletic figure. She has long brown hair. She loves the Victorian England period, and watching TV and reading novels relating to that period.```
For example, if you want Amanda to be friendly, then you would add: ```Amanda is extremely cheerful and outgoing.```
6. Under First Message, write the greeting for the character when you begin a new chat. For example: ```*Amanda waves at you* Hey! Are you a backpacker too?```
7. Click the Create Character button

You now have a basic character you can chat with. Select Amanda from the character list, and a new chat will begin.

Note that you can use the Description and/or First Message to create a more specific scenario, and/or include yourself in the description. For example:

```txt
Description:
Amanda is a student traveling during her gap year. She's 6 feet tall, and a volleyball player. She has an athletic figure. She has long brown hair. She loves the Victorian England period, and watching TV and reading novels relating to that period. She's been keeping a secret that weighs heavily on her soul. She's waiting for the right person to unburden herself to, but this may lead to a cat and mouse game against a powerful secret society. She's recently arrived in Calcutta.

You're Rajesh Nahasmapetilon, a world-famous Indian volleyball superstar. You're out for a walk in Calcutta. Amanda spots you and screams in excitement.

First Message:
*Amanda runs up to you, beaming.* Rajesh! I can't believe it! I'm such a big fan. I have your poster in my bedroom.
```

Any relevant information you include can be used. How well it's used depends on the power level of the AI model.

NOTE: you can go back and edit any of this information once the character is created, except the name.

## Where are my API keys stored? Why can't I see them?

SillyTavern saves your API keys to a `secrets.json` file in the user data directory (`/data/default-user/secrets.json` is the default path).

By default, API keys will not be visible from the interface after you have saved them and refreshed the page.

In order to enable viewing your keys:

1. Set the value of `allowKeysExposure` to `true` in `config.yaml` file.
2. Restart the SillyTavern server.
3. Click the 'View hidden API keys' link at the bottom right of the API Connection Panel.

## Performance Tips

### Why is the UI so slow/jittery?

* Try enabling the No Blur Effect (Fast UI) mode on the User settings panel.
* Enable Reduced motion in the UI theme settings to remove cosmetic animations.
* Make sure your browser is using Hardware Acceleration.
* If using response streaming, set the streaming FPS to a lower value (10-15 FPS is recommended).

### I'm experiencing an input lag. What can I do?

Performance degradation, particularly input lag, is most commonly attributed to browser extensions. Known problematic extensions include:

* iCloud Password Manager
* DeepL Translation
* AI-based grammar correction tools
* Various ad-blocking extensions

If you experience performance issues and cannot identify the cause, or suspect an issue with SillyTavern itself, please:

1. Record a performance profile (https://developer.chrome.com/docs/devtools/performance/reference)
2. Export the profile as a JSON file
3. Submit it to the development team for analysis

We recommend first testing with all browser extensions and third-party SillyTavern extensions disabled to isolate the source of the performance degradation.

### When I import a lot of characters, the app becomes slow. Why?

Unfortunately, SillyTavern wasn't designed to handle huge character libraries. The more you have, the longer it will take to load the character list. Evidential data suggests that the performance degradation starts to become noticeable when you have more than 1000 characters.

However, there are some things you can do to mitigate the issue:

**1. Use lazy loading.**

Enable lazy loading of characters setting the value `performance.lazyLoadCharacters` to true in the `config.yaml` file. After the next server restart, the character list will only load the full data of characters you interact with. Please be aware that some third-party extensions may not work correctly with this setting enabled if they were not updated to support it (contact the extension developer for more information).

**2. Use memory cache.**

Increase the memory cache capacity if you have some spare RAM. This will allow the server to keep more characters in memory, reducing the time it takes to load them. You can do this by adjusting the value of `performance.memoryCacheCapacity` to a higher number in the `config.yaml` file. The default value is `100mb`. Approximate rule of thumb: increase the value by 100mb for every 3000 characters you have.

**Limitations:**

1. Advanced (fuzzy) characters search will not work with lazy loading enabled. Only character names will be searched.
2. Memory cache is disabled on Android devices due to the limited amount of available memory.

## How to make the AI write more?

Sometimes the AI will only respond with a single sentence when you'd like it to be more verbose.
This is usually a problem with locally run models.

If you simply want the bot to continue writing from where it left off at the end of its most recent reply, you can send an empty user message by typing nothing into the Input Bar and clicking Send. This will force the bot to continue the story.

Strategies for fixing this:

* Increase the value of the `Response Length` setting
* Design a good `First Message` for the Character, which shows them speaking in a long-winded manner. AI models can improve a lot when given guidance about the writing style you expect.
* Add a phrase in the character's Description Box such as "likes to talk a lot" or "very verbose speaker"
* Do the same thing for your `Author's Note`, or `Post-History Instruction Prompt`
* As a last resort, you can try turning on `Auto-Continue` (in the User Settings panel), but will make responses come out slower because it's making the AI produce small replies back to back, and then combining them all together into one big reply. It may also be incompatible with some API options.

## How to make the AI write less?

This is mostly only a problem for models like ChatGPT or Claude. The same strategies can be applied but in reverse.

* Decrease the value of the `Response Length` setting
* Give the character a phrase like 'short spoken', or 'doesn't talk much' line in their Description.
* Give the character a brief First Message to set the tone and expectation for the chat.
* Make sure `Auto-Continue` is turned off.

## How to make the AI stop writing the actions of my character, and driving the plot all on its own?

This should be handled in the `Author's Note` with a combination of phrases like:

* \{\{char\}\}'s responses shall only be passive and reactive to \{\{user\}\}'s actions.
* Your next response shall be solely from the POV of \{\{char\}\}.
* You are never allowed to dictate actions or speech for \{\{user\}\}.

# SECTION: SillyTavern_Usage_index

# Usage

Interact with AI, your way. Build your world, your work, or your dreams.

## Getting Started

**Quick Start**

Send your first message to the AI and get a response

**Chatting**

How to chat with the AI and use the chat interface

**FAQ**

Frequently asked questions about SillyTavern, AI models, making characters, getting better responses, and more

**:::callout**

## Fundamentals

**API Connections**

Connect to AI models for generating text, images, and more

**Characters** and **Personas**

Create and use characters to shape the AI's role, and personas to define your identities

**Response Configuration** and **Prompts**

Control the requests that you send to the AI and how it responds

**Welcome Page Assistants**

Learn how to set up and use Welcome Page Assistants to greet you with a designated character on the Welcome Screen.

**:::callout**

## Building on SillyTavern

**World Info**

Manage information and when to insert it into the prompt

**Data Bank**

Store and retrieve information for use in the AI's responses

**Extensions**

Add new features and capabilities to the AI or the interface

**Development and Automation**

Automate tasks, let your AI interact with the world, and write your own extensions

**---**

## Control Panels

What all the buttons do, from the left to the right:

<i class="fa-solid fa-sliders fa-2xl fa-fw"></i> **Response Configuration**
and **Prompt Manager**

Control text generation and sampling. Customize prompt construction for Chat Completion APIs.

**:::callout**

<i class="fa-solid fa-plug fa-2xl fa-fw"></i> **API Connections**

Connect to AI models for generating text, images, and more

**:::callout**

<i class="fa-solid fa-font fa-2xl fa-fw"></i> **Advanced Formatting**

Customize prompt construction for Text Completion APIs

**:::callout**

<i class="fa-solid fa-book-atlas fa-2xl fa-fw"></i> **World Info**

Manage information and when to insert it into the prompt

**:::callout**

<i class="fa-solid fa-user-gear fa-2xl fa-fw"></i> **User Settings**

Change the theme, and the look and feel of messages and chats

**:::callout**

<i class="fa-solid fa-panorama fa-2xl fa-fw"></i> **Backgrounds**

Change the background image

**:::callout**

<i class="fa-solid fa-cubes fa-2xl fa-fw"></i> **Extensions**

Add new features and capabilities to the AI or the interface

**:::callout**

<i class="fa-solid fa-face-smile fa-2xl fa-fw"></i> **Personas**

Create and manage personas to use with the AI

**:::callout**

<i class="fa-solid fa-address-card fa-2xl fa-fw"></i> **Characters**

Create and manage characters for the AI to use

# SECTION: SillyTavern_Usage_macros

# Macros

**Experimental Macro Engine**

To enable advanced macro processing that supports nesting, stable substitution order, and other improvements, go to **User Settings** > **Chat/Message Handling** and enable the **Experimental Macro Engine** option.

**Macros are dynamic placeholders that get replaced with actual values when text is processed. They are used throughout SillyTavern in prompts, character cards, lorebooks, Quick Replies, and more.**

## Finding Available Macros

SillyTavern provides built-in documentation for all available macros:

- **Slash command**: Type `/? macros` in the chat input to display a list of all registered macros with their descriptions.
- **Autocomplete**: See Macro Autocomplete below for details on getting suggestions while typing.

### Macro Autocomplete

Macro autocomplete provides suggestions for available macros as you type. It works in all text fields that support macros throughout SillyTavern.

Type `{{` to start autocomplete for macros, showing available macros and their arguments, potential Macro Flags, Variable Shorthands, and more.

**Where autocomplete appears by default:**

- Chat user input box
- Expanded editor (full-screen text editing, opened via the 'Expand' button next to text fields)
- Prompt manager editor

**Triggering autocomplete in other fields:**

- Press **Ctrl+Space** in any macro-supporting text field to open the autocomplete popup
- Enable **Settings → AutoComplete Settings → Show in all macro fields** to have autocomplete appear automatically in all macro fields

## Basic Syntax

Macros are enclosed in double curly braces:

```txt
{{macroName}}
```

Macro names are **case-insensitive**. `{{User}}`, `{{USER}}`, and `{{user}}` all resolve to the same macro.

Examples:

```txt
{{user}}        // Returns the current user/persona name
{{char}}        // Returns the current character name
{{time}}        // Returns the current time
{{date}}        // Returns the current date
```

## Arguments

Many macros accept arguments to customize their behavior.

### Space Separator

For macros with a single argument, a space can separate the macro name from its argument:

```txt
{{macroName argument}}
```

Examples:

```txt
{{getvar myVariable}}
{{roll 1d20}}
{{reverse Hello World}}
```

### Double Colon Separator

Use `::` to separate multiple arguments:

```txt
{{macroName::arg1::arg2::arg3}}
```

Examples:

```txt
{{setvar::myVariable::Hello World}}
{{random::red::green::blue}}
{{roll::2d6+3}}
```

Both space and `::` are the recommended syntax for macro arguments.

### Single Colon Separator (Legacy)

A single `:` can also introduce arguments, but this syntax is considered legacy and not recommended for new content:

```txt
{{macroName:argument}}
```

Examples:

```txt
{{roll:1d20}}
```

## Whitespace in Macro Definitions

Whitespace between the macro name, separators, and arguments is ignored. This allows for more readable formatting:

```txt
{{ macroName :: arg1 :: arg2 }}
{{ setvar :: myVariable :: some value }}
{{ if :: condition }}
```

All of the above are equivalent to their compact forms without extra spaces.

## Nested Macros

Macros can be nested inside other macros. Inner macros are resolved first:

```txt
{{getvar::{{char}}_mood}}
```

This first resolves `{{char}}` (e.g., to "Alice"), then resolves `{{getvar::Alice_mood}}`.

More examples:

```txt
{{setvar::greeting::Hello, {{user}}!}}
```

Sets a variable with content that includes the user's name.

```txt
{{if {{getvar::showDetails}}}}Details here{{/if}}
```

The condition itself is a macro that retrieves a variable value.

## Scoped Macros

Any macro that accepts at least one argument supports scoped syntax. The content between opening and closing tags becomes the **last argument** of the macro.

### Scoped Syntax

Instead of writing the last argument inline, it can be placed between opening and closing tags:

```txt
{{macroName argument}}
  scoped content here
{{/macroName}}
```

The closing tag uses the `/` flag before the macro name: `{{/macroName}}`.

This is equivalent to writing:

```txt
{{macroName::argument::scoped content here}}
```

### Examples

Setting a variable with multiline content:

```txt
{{ setvar backstory }}
  This character was born in a small village
  and grew up to become a renowned scholar.
{{ /setvar }}
```

Using `reverse` with scoped content:

```txt
{{ reverse }}
  Hello World
{{ /reverse }}
```

This returns "dlroW olleH".

### Content Trimming

By default, scoped content is automatically trimmed:

- Leading and trailing whitespace is removed
- Consistent indentation is de-dented (the indentation of the first non-empty line is removed from all lines)

This allows clean formatting:

```txt
{{ if condition }}
    # Heading
    Some content here
{{ /if }}
```

Produces `# Heading\nSome content here` (without the leading spaces).

To preserve all whitespace including leading/trailing newlines, use the `#` flag. See Macro Flags for details.

## Conditional Macros

The `{{if}}` macro renders content conditionally based on whether a value is truthy or falsy.

### Simple Condition

```txt
{{ if description }}
  # Character Description
  {{ description }}
{{ /if }}
```

This displays the heading and description only if `description` returns a non-empty value.

The condition can be:

- A macro name (resolved automatically if no arguments are required)
- Any value from a nested macro like `{{getvar::flag}}`
- A variable shorthand like `.myFlag` or `$globalFlag` (see Variable Shorthands)
- Any text you want (that will implicitly resolve to truthy or falsy based on its content)

Falsy values: empty string, `false`, `0`, `off`, `no`.

### Using Variable Shorthands in Conditions

Variable shorthands provide a concise way to check variable values in conditions:

```txt
{{ if .isEnabled }}
  Feature is enabled.
{{ /if }}

{{ if !$globalDisabled }}
  Not globally disabled.
{{ /if }}
```

See Variable Shorthands for more details on shorthand notation.

### Inverted Condition

Prefix the condition with `!` to invert it:

```txt
{{ if !personality }}
  No personality defined for this character.
{{ /if }}
```

### If/Else Branches

Use `{{else}}` inside an `{{if}}` block to define an alternative branch:

```txt
{{ if personality }}
  {{ personality }}
{{ else }}
  No personality defined.
{{ /if }}
```

Another example:

```txt
{{ if {{getvar::details-block}} }}
  # Details Block
  {{ getvar::details-block }}
{{ else }}
  No details currently exist.
{{ /if }}
```

## Macro Flags

Flags are special symbol characters placed between the opening braces and the macro name that modify macro behavior.

### Syntax

```txt
{{!macroName}}
{{#macroName}}
```

Flags can be combined:

```txt
{{!?macroName}}
```

Whitespace is allowed between flags and the macro name:

```txt
{{ / macroName }}
{{ # macroName }}
```

### Implemented Flags

| Flag | Name | Description |
|------|------|-------------|
| `/` | Closing Block | Marks a closing tag for scoped macros. Example: `{{/if}}` |
| `#` | Preserve Whitespace | Prevents automatic trimming of scoped content. |

### Planned Flags (Not Yet Implemented)

| Flag | Name | Description |
|------|------|-------------|
| `!` | Immediate | Resolve this macro before other macros in the same text. |
| `?` | Delayed | Resolve this macro after other macros in the same text. |
| `~` | Re-evaluate | Mark this macro for re-evaluation. |
| `>` | Filter | Enable pipe-based output filters for this macro. |

### Flags-like prefix operators

Variable shorthand syntax uses prefix operators (`.` and `$`) which behave similarly to flags but are not flags themselves.  
See the Variable Shorthands section for details.

### Preserve Whitespace Flag

Use the `#` flag when you need to preserve all whitespace in scoped content, including leading/trailing newlines and indentation:

```txt
{{ # setvar code }}
    function hello() {
        return "world";
    }
{{ /setvar }}
```

Without `#`, the content would be trimmed and dedented. With `#`, all whitespace is preserved exactly as written—including the newline after the opening tag and before the closing tag.

## Comments

Use the comment macro to add notes that won't appear in the output:

```txt
{{// This is a comment and will be removed}}
```

For multi-line comments, use scoped syntax:

```txt
{{ // }}
  This entire block is a comment.
  It can span multiple lines.
{{ /// }}
```

## Escaping Macros

To display literal curly braces without macro resolution, escape them with backslashes:

```txt
\{\{notAMacro\}\}
```

This outputs `{{notAMacro}}` as plain text.

## Variable Shorthands

Variable shorthands provide a concise syntax for common variable operations. Use `.` for local variables and `$` for global variables.

### Variable Shorthands Prefixes

| Prefix | Name            | Description                                                     |
| ------ | --------------- | --------------------------------------------------------------- |
| `.`    | Local Variable  | Shorthand for local variable operations. Example: `{{.myvar}}`  |
| `$`    | Global Variable | Shorthand for global variable operations. Example: `{{$myvar}}` |

These prefix operators have to be placed **immediately before** the variable name, after any optionally appearing Macro Flags. They aren't considered macro flags, but more indicators that a variable shorthand is being inserted, instead of a macro by name. The prefix operators are not part of the variable name itself, but rather modifiers that change how the variable is accessed.

### Variable Names

Variable names follow the same rules as macro identifiers: start with a letter, followed by letters, digits, underscores, or hyphens. The last character is not allowed to be an underscore or hyphen.

```txt
{{.my-var}}       // Valid
{{.my_var}}       // Valid
{{.myVar123}}     // Valid
```

If your variable has an identifier that does not match the standard rules, you have to use the full variable macro syntax (e.g. `{{getvar::my§var----}}`), or rename/move your variable value.

### Nested Macros in Values

Variable values can contain nested macros:

```txt
{{.greeting = Hello, {{user}}!}}
```

Resolves to a variable that saves `Hello, User!` inside. (If `{{user}}` is named "User")

### Whitespace Handling

Whitespace around operators is allowed:

```txt
{{ .myvar = spaced value }}
{{ .counter ++ }}
```

### Variable Shorthand Operators

The following operators can be used with variable shorthands. Each operator follows the pattern `{{.varName operator value}}` or `{{$varName operator value}}`.

| Operator | Name                      | Example                | Description                                            |
| -------- | ------------------------- | ---------------------- | ------------------------------------------------------ |
| *(none)* | Get      | `{{.myvar}}`           | Returns the variable value                             |
| `=`      | Set      | `{{.myvar = value}}`   | Sets the variable to a value, returns nothing         |
| `++`     | Increment   | `{{.counter++}}`       | Increments by 1, returns new value                     |
| `--`     | Decrement   | `{{.counter--}}`       | Decrements by 1, returns new value                     |
| `+=`     | Add               | `{{.score += 10}}`     | Adds to variable (numeric or string concatenation), returns nothing |
| `-=`     | Subtract     | `{{.health -= 5}}`     | Subtracts from variable (numeric only), returns nothing |
| `||`   | Logical Or | `{{.name || Guest}}` | Returns fallback if variable is falsy                  |
| `??`     | Nullish Coalescing | `{{.name ?? Guest}}` | Returns fallback only if variable is undefined |
| `||=`  | Logical Or Assign | `{{.name ||= Guest}}` | Sets value if variable is falsy, returns the new value |
| `??=`    | Nullish Coalescing Assign | `{{.name ??= Guest}}` | Sets value only if variable is undefined, returns the new value |
| `==`     | Equals         | `{{.status == active}}`| Compares values, returns `"true"` or `"false"`         |
| `!=`     | Not Equals | `{{.status != active}}`| Compares values, returns `"true"` if not equal         |
| `>`      | Greater Than | `{{.score > 50}}` | Returns `"true"` if variable is greater than value     |
| `>=`     | Greater Than or Equal | `{{.level >= 10}}` | Returns `"true"` if variable is greater than or equal to value |
| `<`      | Less Than   | `{{.health < 20}}`     | Returns `"true"` if variable is less than value        |
| `<=`     | Less Than or Equal | `{{.health <= 0}}` | Returns `"true"` if variable is less than or equal to value |

#### Get Variable

Retrieve variable values with a simple prefix:

```txt
{{.myvar}}       // Get local variable "myvar"
{{$myvar}}       // Get global variable "myvar"
```

Equivalent to `{{getvar::myvar}}` and `{{getglobalvar::myvar}}`.

#### Set Variable

Use the `=` operator to set a variable value:

```txt
{{ .myvar = Hello World }}     // Set local variable
{{ $myvar = Some value }}      // Set global variable
```

Equivalent to `{{setvar::myvar::Hello World}}` and `{{setglobalvar::myvar::Hello World}}`. Returns an empty string.

#### Increment

Use `++` to increment a numeric variable by 1:

```txt
{{.counter++}}    // Increment local variable, returns new value
{{$counter++}}    // Increment global variable, returns new value
```

Equivalent to `{{incvar counter}}` and `{{incglobalvar counter}}`. Returns the new value after incrementing.

#### Decrement

Use `--` to decrement a numeric variable by 1:

```txt
{{.counter--}}    // Decrement local variable, returns new value
{{$counter--}}    // Decrement global variable, returns new value
```

Equivalent to `{{decvar counter}}` and `{{decglobalvar counter}}`. Returns the new value after decrementing.

#### Add

Use `+=` to add a numeric value to a variable:

```txt
{{.score += 10}}     // Add 10 to local variable
{{$total += 5}}      // Add 5 to global variable
```

Equivalent to `{{addvar::score::10}}` and `{{addglobalvar::total::5}}`. Returns an empty string.

The add operator also supports appending strings to an existing string variable, if neither of them are numbers:

```txt
{{.myvar += {{noop}} | Second block}}   // Resolves to "Content | Second block" when the variable before was "Content".
                                        // Use `{{noop}}` to be able to add whitespaces, that otherwise would be trimmed automatically.
```

#### Subtract

Use `-=` to subtract a numeric value from a variable:

```txt
{{.health -= 10}}    // Subtract 10 from local variable
{{$points -= 5}}     // Subtract 5 from global variable
```

Equivalent to `{{addvar::score::10}}` and `{{addglobalvar::total::5}}`, but with a negative/inverted number. Returns an empty string.
If the value is not a valid number, a warning is logged and the variable is unchanged.

#### Logical Or

Use `||` to provide a fallback value when the variable is falsy (empty string, `0`, `false`):

```txt
{{.name || Anonymous}}     // Returns "Anonymous" if .name is empty or falsy
{{$setting || default}}    // Returns "default" if $setting is falsy
```

Returns the variable value if truthy, otherwise returns the fallback value. The fallback is **only evaluated if needed** (lazy evaluation).

#### Nullish Coalescing

Use `??` to provide a fallback value only when the variable does not exist:

```txt
{{.name ?? Guest}}         // Returns "Guest" only if .name is not defined
{{$config ?? default}}     // Returns "default" only if $config doesn't exist
```

Unlike `||`, this returns the variable value even if it's falsy (empty string, `0`, `false`) — as long as the variable exists. The fallback is **only evaluated if needed** (lazy evaluation).

#### Logical Or Assign

Use `||=` to set a variable to a value only if it's currently falsy:

```txt
{{.name ||= Anonymous}}    // Sets and returns "Anonymous" if .name is falsy
{{$count ||= 0}}           // Sets and returns "0" if $count is falsy
```

If the variable is already truthy, returns the current value without modification. Returns the final value (either existing or newly set).

#### Nullish Coalescing Assign

Use `??=` to set a variable to a value only if it doesn't exist:

```txt
{{.name ??= Guest}}        // Sets and returns "Guest" only if .name is undefined
{{$config ??= default}}    // Sets and returns "default" only if $config doesn't exist
```

Unlike `||=`, this preserves falsy values (empty string, `0`, `false`) if the variable already exists. Returns the final value (either existing or newly set).

#### Equals

Use `==` to compare a variable value to another value:

```txt
{{.status == active}}      // Returns "true" if .status equals "active", otherwise "false"
{{$mode == dark}}          // Returns "true" if $mode equals "dark", otherwise "false"
```

Performs a string comparison and returns the literal string `"true"` or `"false"`.  
Treats not existing variables, null variables and empty variables as the same.

Useful in `{{if}}` conditions:

```txt
{{if {{.status == active}} }}Active mode{{/if}}
```

#### Not Equals

Use `!=` to compare a variable value to another value for inequality:

```txt
{{.status != inactive}}    // Returns "true" if .status is NOT "inactive", otherwise "false"
{{$mode != light}}         // Returns "true" if $mode is NOT "light", otherwise "false"
```

Performs a string comparison and returns `"true"` if the values are different, `"false"` if they are equal.  
Treats not existing variables, null variables and empty variables as the same.

Useful in `{{if}}` conditions:

```txt
{{if {{.status != disabled}} }}Feature enabled{{/if}}
```

#### Greater Than

Use `>` to check if a variable's numeric value is greater than another value:

```txt
{{.score > 50}}        // Returns "true" if .score is greater than 50
{{$level > 5}}         // Returns "true" if $level is greater than 5
```

Performs a numeric comparison and returns the literal string `"true"` or `"false"`.

Useful in `{{if}}` conditions:

```txt
{{if {{.score > 100}} }}High score!{{/if}}
```

#### Greater Than or Equal

Use `>=` to check if a variable's numeric value is greater than or equal to another value:

```txt
{{.level >= 10}}       // Returns "true" if .level is at least 10
{{$points >= 100}}     // Returns "true" if $points is 100 or more
```

Performs a numeric comparison and returns the literal string `"true"` or `"false"`.

Useful in `{{if}}` conditions:

```txt
{{if {{$level >= 10}} }}Unlocked advanced features{{/if}}
```

#### Less Than

Use `<` to check if a variable's numeric value is less than another value:

```txt
{{.health < 20}}       // Returns "true" if .health is below 20
{{$timer < 0}}         // Returns "true" if $timer is negative
```

Performs a numeric comparison and returns the literal string `"true"` or `"false"`.

Useful in `{{if}}` conditions:

```txt
{{if {{.health < 20}} }}Low health warning!{{/if}}
```

#### Less Than or Equal

Use `<=` to check if a variable's numeric value is less than or equal to another value:

```txt
{{.health <= 0}}       // Returns "true" if .health is 0 or below
{{$attempts <= 3}}     // Returns "true" if $attempts is 3 or fewer
```

Performs a numeric comparison and returns the literal string `"true"` or `"false"`.

Useful in `{{if}}` conditions:

```txt
{{if {{.health <= 0}} }}Game over{{/if}}
```

## Legacy Syntax

For backwards compatibility, angle bracket markers are still supported:

| Legacy | Equivalent Macro |
|--------|------------------|
| `<USER>` | `{{user}}` |
| `<BOT>` | `{{char}}` |
| `<CHAR>` | `{{char}}` |
| `<GROUP>` | `{{group}}` |
| `<CHARIFNOTGROUP>` | `{{charIfNotGroup}}` |

These are automatically converted to their macro equivalents during processing.

> **Note:** Legacy syntax is not recommended. Use the equivalent `{{macro}}` syntax instead for new content.

## Common Macros by Category

Use `/? macros` for the complete list of available macros and their detailed descriptions.

**### Names & Participants**

| Macro | Description |
|-------|-------------|
| `{{user}}` | Current user/persona name |
| `{{char}}` | Current character name |
| `{{group}}` | Comma-separated list of group member names (including muted) or character name in solo chats |
| `{{groupNotMuted}}` | Comma-separated list of group member names excluding muted members |
| `{{charIfNotGroup}}` | Character name (empty in groups) |
| `{{notChar}}` | Comma-separated list of all participants except the current speaker |

### Character Card & Persona Fields

| Macro | Description |
|-------|-------------|
| `{{description}}` | Character description |
| `{{personality}}` | Character personality |
| `{{scenario}}` | Character scenario |
| `{{persona}}` | User persona description |
| `{{charPrompt}}` | Character's Main Prompt override |
| `{{charInstruction}}` | Character's Post-History Instructions override |
| `{{charDepthPrompt}}` | Character's @ Depth Note |
| `{{charCreatorNotes}}` | Creator notes from the character card |
| `{{charVersion}}` | Character's version number |
| `{{mesExamples}}` | Character's dialogue examples, formatted for instruct mode |
| `{{mesExamplesRaw}}` | Unformatted dialogue examples from the character card |
| `{{original}}` | Original message content for substitution in character prompt overrides |

### Chat History & Messages

| Macro | Description |
|-------|-------------|
| `{{lastMessage}}` | Last message in the chat |
| `{{lastMessageId}}` | Index of the last message in the chat |
| `{{lastUserMessage}}` | Last user message in the chat |
| `{{lastCharMessage}}` | Last character/bot message in the chat |
| `{{firstIncludedMessageId}}` | Index of first message included in current context |
| `{{firstDisplayedMessageId}}` | Index of the first displayed message in the chat |
| `{{lastSwipeId}}` | 1-based index of the last swipe for the last message |
| `{{currentSwipeId}}` | 1-based index of the current swipe |
| `{{summary}}` | Latest chat summary from the "Summarize" extension (when available) |

### Time & Date

| Macro | Description |
|-------|-------------|
| `{{time}}` | Current local time |
| `{{time::UTC±(offset)}}` | Time with UTC offset |
| `{{date}}` | Current local date in short format |
| `{{weekday}}` | Current day of the week |
| `{{isotime}}` | Current time in HH:mm format |
| `{{isodate}}` | Current date in YYYY-MM-DD format |
| `{{datetimeformat::format}}` | Custom formatted date/time (e.g., `YYYY-MM-DD HH:mm:ss`) |
| `{{idleDuration}}` | Human-readable duration since the last user message |
| `{{timeDiff::left::right}}` | Human-readable difference between two times |

### Variables

| Macro | Description |
|-------|-------------|
| `{{getvar::name}}` | Get local variable value |
| `{{setvar::name::value}}` | Set local variable |
| `{{addvar::name::value}}` | Add value to local variable (numeric or string append) |
| `{{incvar::name}}` | Increment local variable by 1 and return new value |
| `{{decvar::name}}` | Decrement local variable by 1 and return new value |
| `{{hasvar::name}}` | Check if a local variable exists (returns "true" or "false") |
| `{{deletevar::name}}` | Delete a local variable |
| `{{getglobalvar::name}}` | Get global variable value |
| `{{setglobalvar::name::value}}` | Set global variable |
| `{{addglobalvar::name::value}}` | Add value to global variable (numeric or string append) |
| `{{incglobalvar::name}}` | Increment global variable by 1 and return new value |
| `{{decglobalvar::name}}` | Decrement global variable by 1 and return new value |
| `{{hasglobalvar::name}}` | Check if a global variable exists (returns "true" or "false") |
| `{{deleteglobalvar::name}}` | Delete a global variable |

### Randomization

| Macro | Description |
|-------|-------------|
| `{{random::a::b::c}}` | Random selection (re-rolls each time) |
| `{{pick::a::b::c}}` | Stable random selection (consistent per chat and position). Can be rerolled with the `/reroll-pick` command |
| `{{roll::1d20}}` | Dice roll using droll syntax |

### Runtime State

| Macro | Description |
|-------|-------------|
| `{{maxPrompt}}` | Maximum prompt context size |
| `{{model}}` | Model name for the currently selected API |
| `{{isMobile}}` | "true" if running in mobile environment, "false" otherwise |
| `{{lastGenerationType}}` | Type of last queued generation request (e.g., "normal", "impersonate", "regenerate", "quiet", "swipe", "continue") |
| `{{hasExtension::name}}` | Check if an extension is active (returns "true" or "false"). Matches by extension name, case-insensitive |

### Prompt Templates

| Macro | Description |
|-------|-------------|
| `{{systemPrompt}}` | Active system prompt text (optionally overridden by character) |
| `{{defaultSystemPrompt}}` | Default system prompt |
| `{{authorsNote}}` | Contents of the Author's Note |
| `{{charAuthorsNote}}` | Contents of the Character Author's Note |
| `{{defaultAuthorsNote}}` | Contents of the Default Author's Note |
| `{{instructStoryStringPrefix}}` | Instruct story string prefix |
| `{{instructStoryStringSuffix}}` | Instruct story string suffix |
| `{{instructUserPrefix}}` | Instruct input/user prefix sequence |
| `{{instructUserSuffix}}` | Instruct input/user suffix sequence |
| `{{instructAssistantPrefix}}` | Instruct output/assistant prefix sequence |
| `{{instructAssistantSuffix}}` | Instruct output/assistant suffix sequence |
| `{{instructSeparator}}` | Instruct separator sequence |
| `{{instructSystemPrefix}}` | Instruct system prefix sequence |
| `{{instructSystemSuffix}}` | Instruct system suffix sequence |
| `{{instructFirstAssistantPrefix}}` | Instruct first assistant/output prefix sequence |
| `{{instructLastAssistantPrefix}}` | Instruct last assistant/output prefix sequence |
| `{{instructFirstUserPrefix}}` | Instruct first user/input prefix sequence |
| `{{instructLastUserPrefix}}` | Instruct last user/input prefix sequence |
| `{{instructStop}}` | Instruct stop sequence |
| `{{instructUserFiller}}` | Instruct user alignment filler |
| `{{instructSystemInstructionPrefix}}` | Instruct system instruction prefix sequence |
| `{{chatSeparator}}` | Separator between example chat blocks in text completion prompts |
| `{{chatStart}}` | Chat start marker in text completion prompts |
| `{{reasoningPrefix}}` | Prefix string used before reasoning blocks |
| `{{reasoningSuffix}}` | Suffix string used after reasoning blocks |
| `{{reasoningSeparator}}` | Separator between content and response |
| `{{charPrefix}}` | Character's positive Image Generation prompt prefix |
| `{{charNegativePrefix}}` | Character's negative Image Generation prompt prefix |

### Utility

| Macro | Description |
|-------|-------------|
| `{{newline}}` | Insert newline character |
| `{{newline::count}}` | Insert multiple newlines |
| `{{space}}` | Insert space character |
| `{{space::count}}` | Insert multiple spaces |
| `{{noop}}` | Does nothing, produces empty string |
| `{{trim}}` | Remove surrounding newlines |
| `{{reverse::text}}` | Reverse a string |
| `{{input}}` | Current chat input field content |
| `{{banned::word}}` | Ban a word for Text Completion backend |
| `{{outlet::key}}` | Return world info outlet prompt for a given outlet key |

# SECTION: SillyTavern_Usage_personas

# Personas

## What is a Persona?

A persona in SillyTavern is the identity you use to participate in chats — essentially a combination of your display name, avatar, and optional descriptive text. Personas allow you to easily switch roles or "characters" you speak as, without having to manually update your username/avatar each time.

****Note:** Legacy user avatars/names that weren't tied to a persona have been removed. Existing data will be migrated to personas. If no name was specified, the persona will be named "[Unnamed Persona]".**

**## How to Create a Persona?**

1. Open the **Persona Management** panel (<i class="fa-solid fa-face-smile"></i> button in the top menu).
2. Create a blank persona with the **Create** button and give it a name.
3. In the persona list, select the newly created persona.
4. On the right side, you can fill in your description and set an avatar via the "Change Persona Image" button. Both are optional.
5. Now your persona is ready to use in chats.

### Convert Character to Persona

Personas can also be created by converting any existing character. Simply open the character, select "More..." and click "Convert to Persona". A persona with the same name and description will be created. Other character card fields like Scenario or Personality will not be used. The character will not be deleted.

Since `{{user}}` and `{{char}}` macros have opposite meanings when used in Persona and Character descriptions, you'll be prompted to swap them if the converted description contains either of them.

**## Persona Description**

Each persona can store a custom text description — mental and physical traits, age, occupation, or any personal details. These can also include template macros such as `{{char}}` or `{{user}}` (see Macros).

Where your persona description is injected into the AI prompt depends on the **Position** setting in the Persona Management panel:

- **None (disabled)**
- **In Story String / Prompt Manager** (the default)
- **Top of Author's Note** / **Bottom of Author's Note** (will only be added when an Author's Note exists)
- **In Chat @ Depth** (this will open up configuration options to set depth and the role)

The position is saved **per persona**.

## Persona Title

The title is an optional text field that can be used to store additional information about the persona and is not used in the prompt, but displayed in the Persona Management panel.

To set a title, click the **<i class="fa-solid fa-pencil"></i> Rename Persona** button in the Persona Management panel and enter the title in the "Persona Title" field, or specify it during persona creation. Setting an empty value when the title already exists will remove it.

## Persona Connections / Locking

Persona connections ensure that a given persona is automatically selected in certain situations. If no persona is connected, the currently chosen persona will stay selected.

There are three types of locking:

1. **<i class="fa-solid fa-unlock"></i> Chat lock** – The persona is locked to the current chat.
2. **<i class="fa-solid fa-unlock"></i> Character lock** – The persona is locked to a specific character.
3. **<i class="fa-solid fa-crown"></i> Default persona** – One persona that is used whenever no other locks apply.

### 1. Lock to a Chat

If a persona is locked to a chat, opening that chat in the future will automatically switch your active persona to the locked one.

- **To lock**: Select the desired persona, then click the **<i class="fa-solid fa-unlock"></i> Chat** button under the "Connections" section (or use `/persona-lock type=chat on`).
- **To unlock**: Click the button again (or use `/persona-lock type=chat off`).

### 2. Lock to a Character

You can also link a persona to a specific character. Opening any chat with that character automatically selects your locked persona.

- **To lock**: Select the desired persona, then click the **<i class="fa-solid fa-unlock"></i> Character** button under the "Connections" section (or use `/persona-lock type=character on`).
- **To unlock**: Click the button again (or use `/persona-lock type=character off`).

The Persona Management panel also shows which characters are linked to that persona (displayed as small avatars). Clicking them navigates directly to that character's chat.

#### Locking Multiple Personas to the Same Character

If another persona was already linked with that character, it will be automatically unlinked by default.

To have multiple personas linked at once, the global setting **Allow multiple persona connections per character** can be used.  
If multiple personas are linked to the same character, you'll see a popup asking which persona to use each time you open or start a new chat with that character (unless a persona is bound to the chat).

### 3. Default Persona

Your **default persona** is used whenever there's no other relevant lock. The default persona is recognizable by a yellow border around its avatar.

- **To set/unset default**: Select the desired persona, then click the **<i class="fa-solid fa-crown"></i> Default** button under the "Connections" section (or use `/persona-lock type=default`).

Only one persona can be chosen as the default persona.

### Temporary Persona

If any of the three connection options connects a persona to the current character/chat, you can still choose to use a different persona. This persona will be marked in the persona panel as "Temporary Persona". Any reload of the browser window or switch to a different chat and back will reset it to the linked persona again.

You can manually *convert* a Temporary Persona to be persistently connected by linking it to the chat.

## Global Persona Settings

All settings under the **Current Persona** are saved per-persona. A few global settings exist too, those can be found under **Global Persona Settings** in the Persona Management panel.

1. **Show notifications on switching personas**
   - Enables persona-related toast messages (e.g., "Persona Auto Selected", "Temporary Persona").

2. **Allow multiple persona connections per character**
   - When **enabled**, you can link multiple personas to a single character. Opening that character's chat will prompt you which persona to use. If disabled, only one persona can be connected to a character at a time.

3. **Auto-lock a chosen persona to the chat**
   - When **enabled**, any time you select a persona (manually or by auto-selection) or create a new chat, it locks that persona to the chat.  
   This combined with "Allow multiple" provides the option to have a persona selection per character, but keep it bound once chosen for a chat.

## Slash Commands for Personas

### `/persona-lock type=<type?>`

- `chat` locks the current persona to your active chat.
- `character` locks the current persona to the character in use.
- `none` (or no argument) unlocks/clears the persona lock for the current context.
- If used without arguments, it returns the current lock state (or an error if none is set).
- The lock state can be chosen via `on`, `off` or `toggle`. Default is toggle.

### `/persona <name>`

- Quickly switch your active persona by name without opening the Persona Management panel.
- Example: `/persona Blaze`.
- Using `mode=temp` allows to temporarily set your name of the **current** persona, even though a persona with the same name might already exist (preserving your current avatar and description).

### `/persona-sync`

- Re-attributes all user messages in the active chat to the **current** persona and its name.

> **Note:** The older `/lock` and `/unlock` commands remain for backward compatibility but may be removed in the future. Use `/persona-lock` instead.

## Pro Tips

1. **Switching personas mid-chat** doesn't re-attribute your past user messages to the new persona; those remain attributed to whichever persona you were using at the time.
2. **Batch re-attribution**: If you ever need all prior messages to match a new persona, hit the **sync** button or use `/persona-sync`.
3. **Replace persona images** without losing description or locks by choosing your persona and clicking the **<i class="fa-solid fa-images"></i> Change Persona Image** button.
4. **Character link popups**: If multiple personas are linked to the same character, you'll get a popup to pick which persona each time you open the chat. This is a handy way to have a small selection of personas to choose from for specific characters.
5. **Backups**: You can back up your entire persona list (names, character connections, descriptions) with the **Backup** button in Persona Management, and restore it later if needed.

**Backup Remarks**

- Images and chat connections are not saved together with personas and will not be backed up via this.
- These backups are not designed to be shared, as they contain internal links.

# SECTION: SillyTavern_Usage_Prompts_advancedformatting

# Advanced Formatting

The settings provided in this section allow for more control over the prompt-building strategy, primarily for Text Completion APIs.

Most of the settings in this panel do not apply to Chat Completions APIs as they are governed by the prompt manager system instead.

+++ Text Completion APIs
* System Prompt
* Context Template
* Tokenizer
* Custom Stopping Strings
+++ Chat Completion APIs
* System Prompt: not applicable, use Prompt Manager
* Context Template: not applicable, use Prompt Manager
* Tokenizer
* Custom Stopping Strings
+++

## Resetting Templates

You can restore the default templates to their original state. This can be done either through the UI or by manually deleting the relevant data files.

### UI Reset

1. Open the **<i class="fa-solid fa-font"></i> Advanced Formatting** menu.
2. Pick the template you want to reset.
3. Click the **<i class="fa-solid fa-recycle"></i> Restore current template** button.
4. Confirm the action when prompted.

### Manual Reset

**Make sure the `skipContentCheck` setting is set to `false` in config.yaml, otherwise the content check will not be triggered.**

**1. Navigate to your user data directory (see Data paths for details).**

2. Delete the `content.log` file from the root of your user data directory. This file tracks the default files copied for your user.
3. Delete the template JSON files from the relevant subdirectories (`context`, `instruct`, `sysprompt`, etc.).
4. Restart the SillyTavern server. The application will repopulate the default content, restoring any deleted default templates.

## Backend-defined templates

**Applies to: Text Completion APIs**

Not applicable to Chat Completion APIs as they use a different prompt builder.

**Some Text Completion sources provide an ability to automatically choose templates recommended by the model author. This works by comparing a hash of the chat template defined in the model's `tokenizer_config.json` file with one of the default SillyTavern templates.**

1. **<i class="fa-solid fa-bolt"></i> Derive templates** option must be enabled in the **<i class="fa-solid fa-font"></i> Advanced Formatting** menu. This can be applied to Context, Instruct, or both.
2. A supported backend must be chosen as a Text Completion source. Currently only llama.cpp and KoboldCpp support deriving templates.
3. The model must correctly report its metadata when the connection to the API is established. If this didn't work, try updating the backend to the latest version.
4. The reported chat template hash must match the one of the known SillyTavern templates (https://github.com/SillyTavern/SillyTavern/blob/release/public/scripts/chat-templates.js). This only covers default templates, such as Llama 3, Gemma 2, Mistral V7, etc.
5. If the hash matches, the template will be automatically selected if it exists in the templates list (i.e., not renamed or deleted).

## System Prompt

**Applies to: Text Completion APIs**

For equivalent settings in Chat Completion APIs, use Prompt Manager. The **Main Prompt** is the equivalent of the System Prompt in Chat Completion APIs.

**The System Prompt defines the general instructions for the model to follow. It sets the tone and context for the conversation. For example, it tells the model to act as an AI assistant, a writing partner, or a fictional character.**

The System Prompt is a part of the Story String and usually the first part of the prompt that the model receives.

See the prompting guide to learn more about the System Prompt.

## Context Template

**Applies to: Text Completion APIs**

For equivalent settings in Chat Completion APIs, use Prompt Manager.

**Usually, AI models require you to provide the character data to them in some specific way. SillyTavern includes a list of pre-made conversion rules for different models, but you may customize them however you like.**

The options for this section are explained in Context Template.

## Tokenizer

A tokenizer is a tool that breaks down a piece of text into smaller units called tokens. These tokens can be individual words or even parts of words, such as prefixes, suffixes, or punctuation. A rule of thumb is that one token generally corresponds to 3~4 characters of text.

The options for this section are explained in Tokenizer.

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

By default, the Start Reply With prefix won't be shown in the resulting message. Enable "Show reply prefix in chat" to display it.

**### Text Completion APIs**

Prefills the last line of the prompt, forcing the model to continue from that point. This is useful for enforcing content, such as nudging toward the Model Reasoning with the defined prefix:

```txt
<think>
Sure!
```

### Chat Completion APIs

Adds an assistant role message to the end of the prompt. For some backend models, this is equivalent to prefilling the model response, but some may not support that at all and will fail with a validation error. If you're unsure, leave this field empty.

# SECTION: SillyTavern_Usage_Prompts_CFG

# CFG

Page written by: kingbri

Contributors: kingbri, Guillaume "Vermeille" Sanchez, AliCat

## What is it?

CFG, or classifier-free guidance is a method that's used to help make parts of a prompt less or more prominent.

### Supported Backend APIs

Currently, the supported backends are oobabooga's textgen WebUI, NovelAI, and TabbyAPI. 
NovelAI had its own documentation for CFG (https://web.archive.org/web/20240917150051/https://docs.novelai.net/text/cfg.html).

WARNING: CFG increases VRAM usage due to ingesting more than 1 prompt! If your GPU memory runs out while generating a prompt with CFG on, consider reducing your context size, using a lesser parameter model, or turning off CFG entirely.

---

## Configuration

Accessing CFG settings are the same as accessing Author's note:

And here's what the CFG panel looks like:

There are four dropdowns in the CFG panel:

- Chat CFG
  
  - Scopes the CFG scale and prompts to only this chat
- Character CFG
  
  - Scopes the CFG scale and prompts to the specified character
- Global CFG
  
  - Globally overrides the CFG scale and prompts (also overrides the model preset!)
- CFG Advanced Settings (formerly called CFG Prompt Cascading)
  
  - A place to combine prompts from the previous 3 dropdowns and set insertion depth.

NOTE: If the guidance scale is set to 1, nothing will be sent since that's when CFG is in an "off" state.

#### Group Chats

In group chats, the CFG scale panel looks like this:

The main change is that character CFG is removed and a checkbox called `Use Character CFG Scales` is present in the chat CFG dropdown. This allows for the current character's guidance scale to be used instead of whatever the chat CFG scale is set to.

The main utility of this feature is to alter the scale based on each character's individual needs.

In addition, checking the `Character Negatives` box in prompt cascading will append the independent character negative prompts along with the chat ones (if enabled).

---

## Concepts

### Isn't this in Stable Diffusion?

Yes and no. CFG with LLMs works in a different way than what one might be used to in Stable Diffusion. LLM-based CFG works on the principle of "prompt mixing". The CFG formula takes a positive and negative prompt, then mixes the *differences* between them. From there, a combined prompt is sent and a response is generated!

Here's an illustration to help visualize this concept. The red represents the negative prompt, the blue represents the neutral prompt, and the purple represents the mixed result that's interpreted. All the white space is the same across all 3 prompts, so those are not used for CFG mixing.

If you want to know more about CFG and LLMs, Vermifuge's original paper is located here. I'd suggest giving it a read/listen:

- Paper - [[2306.17806] Stay on topic with Classifier-Free Guidance (arxiv.org)](https://arxiv.org/abs//2306.17806)
  
- Audio version - https://www.youtube.com/watch?v=MGY00YFcyco (https://www.youtube.com/watch?v=MGY00YFcyco)
  

### Do I need CFG prompts?

No! CFG prompts are completely optional. Just adjusting the guidance scale above `1` will also help produce an effect on responses, which can accentuate chats and character interaction.

### What makes a good CFG prompt?

So, we established that CFG prompting is not the same as Stable Diffusion's negative tags and embeddings. How do we make a prompt?

Warning: This assumes that you have created a character using PLists and Ali:Chat. If you have not, feel free to experiment with various prompting techniques.

Let's say I have a character named "John". John is supposed to feel happy and excited all the time from his example dialogues. However, when chatting with John, he's sometimes sad and depressed.

To remove this, CFG comes to the rescue! Just make the negative prompt `[John's feelings: sad, depressed]` to help remove the sadness portions. You can optionally make the positive prompt `[John's feelings: happy, joyful]` to further bring out John's happy parts.

### Positive Prompts

I went over this in the previous section, but I'd like to touch on this a bit more. Positive prompts are used to further accentuate parts of a character. Let's use John again as our example. By making him happier with a positive prompt of `[John's feelings: happy, joyful]`, John should start outputting dialogue with a more happy feeling than if the positive prompt was not included.

### But...

These are just **loose guidelines** from experience with one specific character format. There are many other ways to create prompts that you should experiment with. Feel free to share your thoughts with other users!

### Guidance Scale

Here's a rule of thumb. A guidance scale of `1` means that CFG is disabled. In fact, SillyTavern won't send anything to your backend if the guidance scale is 1. A guidance scale `>1` will give the results shown in the other sections at varying degrees.

However, a guidance scale of `<1` will give the *opposite* effect since the negative prompt is used as the primary prompt here.

Let's use the example with John again. The negative prompt is `[John's feelings: sad, depressed]` and the positive prompt is `[John's feelings: happy, joyful]` with a guidance scale of `0.8`.

This will in turn accentuate the *negative* prompt more and you'll see John start to act sadder than normal rather than happier.

TL;DR: Use a guidance scale of `1.5` and work up and down from there based on your outputs.

### Prompt Cascading

Negatives and positives can be cascaded between CFG types (the types being per-chat, per-character, and global overrides). See the Configuration header for more information.

### Insertion Depth

Follow the basic rule: The lower something is located in the prompt, the more influential it is to the response. For chatting, I recommend using the default depth of `1` since it's very flexible with other components of SillyTavern.

However, if you want to experiment, an insertion depth of `0` is open. However, these can dramatically alter how your response will look and it's NOT recommended to use prompt cascading here!

# SECTION: SillyTavern_Usage_Prompts_context-template

# Context Template

**Applies to: Text Completion APIs**

For equivalent settings in Chat Completion APIs, use Prompt Manager.

**Usually, AI models require you to provide the character data to them in some specific way. SillyTavern includes a list of pre-made conversion rules for different models, but you may customize them however you like.**

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

****Important****

When using `{{mesExamples}}` in the Story String, set **"Example Messages Behavior"** in the **<i class="fa-solid fa-user-cog"></i> User Settings** panel to **"Never include examples"** to avoid duplicating example messages in the prompt.

**A special `{{trim}}` macro is supported to remove any newlines that surround it. Use it if you want a part of the text to not be separated from the previous line by a newline (_spaces **are not** trimmed_).**

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

****Attention****

If the template contains static prompt elements (model-specific prefixes or suffixes) for wrapping the story string, using the "In-Chat @ Depth" position will cause it to be incorrectly double-wrapped with duplicate sequences, which may lead to unexpected results.

In this case, you can fix the issue in one of the following ways:

1. **Built-in templates**: Reset the templates to their defaults using the steps described in Advanced Formatting.
2. **Custom templates**: Move the static elements from the story string template to Story String Sequences.

**### Story String wrapping**

**The following section only applies when **Instruct Mode** is ON.**

*** **Default** position: The rendered Story String will be wrapped using the sequences defined in Story String Sequences.**

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

**Appends the character's name to the prompt to force the model to complete the message as the character:**

```txt
** OTHER CONTEXT HERE **
Character:
```

# SECTION: SillyTavern_Usage_Prompts_index

# Prompts

When you send a message to your AI, the text you write is combined with other text to form a single request that's sent to the AI. This combined text is called a "prompt" or sometimes the "request" or "context."

The prompt can include a variety of different types of text, including:

* Main instructions to the AI about how to generate a response
* Definitions of the roles that the AI should take on
* Definitions of the role that you are taking on
* Information about the "world" that the AI is interacting with
* Relevant documents or information from Data Bank
* Summaries of the past conversation
* Results of web searches or other external data sources
* Previous messages in the conversation
* **Your message to the AI**
* Final instructions for the AI about how to generate a response

This can be a lot to manage! To help you understand how to structure and modify the request that's sent to the AI, SillyTavern identifies different elements that you might want to include in your prompt. You can then structure your prompt to include the things that make sense for the way you want to interact with the AI.

Many of these elements are explained in the sections where you will change them. For example, to describe the role that you would like the AI to take on, you could use the Description field in Character Design.

## Viewing the Prompt

Reading the final prompt that's sent to the AI is very helpful for understanding what the AI was told, and why it generated the response that it did. You can view the prompt in several ways:

* Using the Prompt Itemization icon on the reply message from the AI
* Using the Prompt Inspector (https://github.com/SillyTavern/Extension-PromptInspector) extension
* Checking the logs in the terminal window that you're running SillyTavern in
* Checking the console in your browser's developer tools

## Changing how the Prompt is Built

Presenting all the parts of your prompt to the AI in the right way is crucial for getting the best responses. You can control how the prompt is built.

+++ Text Completion APIs

Use the Advanced Formatting panel to customize prompt construction for Text Completion APIs.

+++ Chat Completion APIs

Use the Prompt Manager to customize prompt construction for Chat Completion APIs.

+++

## Main Prompt (System Prompt)

The Main Prompt (or System Prompt) defines the general instructions for the model to follow. It sets the tone and context for the conversation. For example, it tells the model to act as an AI assistant, a writing partner, or a fictional character. 

+++ Text Completion APIs

The System Prompt is a part of the Story String and usually the first part of the prompt that the model receives.

+++ Chat Completion APIs

The Main Prompt is one of the default prompts in Prompt Manager. It is usually the first message in the context that the model receives, attributed to ("sent by") the system role.

+++

The default Main Prompt is:

> Write \{\{char\}\}'s next reply in a fictional chat between \{\{char\}\} and \{\{user\}\}.

The \{\{char\}\} and \{\{user\}\} placeholders are replaced with the names of the character and persona that you've defined in the conversation. 

You can use any of the supported \{\{macro\}\} tags in the Main Prompt to include information that might vary between conversations or changes as the conversation progresses.

### Adjusting the Main Prompt

The default main prompt helps the model understand what it's expected to do with the character and persona information that follows, how to interpret the past conversation, and what kind of response to generate. It's a flexible general-purpose prompt that works well for many situations, because it establishes that the AI is writing as a character in a conversation with your persona.

However, you can adjust the main prompt to better suit your needs. Here are some common reasons to adjust the main prompt:

* **Provide additional instructions**: for example, you want the AI to explain its reasoning, follow specific rules, or avoid certain topics
* **Clarify the role of the AI**: for example, you want the AI to act as a narrator, a storyteller, or a guide
* **Change the context of the conversation**: for example, you want the AI to respond as if it were an AI assistant, text adventure game, or a writing partner

**Try things out and see what works best for you**

All the examples in this guide have worked well for other users, but the prompt that works for your needs and the model you're using might be different. Experiment with different instructions and prompting styles to see what works best for you. If you're not sure what to try, you can always ask for help in the SillyTavern Discord (https://discord.gg/sillytavern).

**Giving the AI additional instructions in the Main Prompt can help it understand what you want from the conversation.**

> Write one reply only. Write at least one paragraph, up to four.

> Markdown is enabled. Use it to format your response. Enclose code snippets in triple backticks.

> Write character dialogue in quotation marks. Write \{\{char\}\}'s thoughts in parentheses.

> You are an anime roleplay generation model for users aged 13 to 17. You always generate fun, age-appropriate responses.

> Answer truthfully and write out your thinking step by step to be sure you get the right answer.

The AI will more easily follow instructions about what it should do than what it should not do. For example, if you want the AI to avoid writing in a certain way, it's better to tell it how you want it to write instead. And while *"Do not decide what \{\{user\}\} says or does"* is commonly included in prompts to prevent the AI from controlling your persona, some users find *"Write  \{\{char\}\}'s responses in a way that respects  \{\{user\}\}'s autonomy"* is more effective.

There is often a better place than the Main Prompt to include information about the user or characters, modify a character's writing and speaking style, or give other specific instructions. The Main Prompt is best used for general instructions about the conversation as a whole, or about a type of conversation that you want to have.

### Effect of Message History

When adjusting the main prompt to improve the AI's responses, consider that the AI picks up a lot from the message history. The history is its memory of past events, character interactions and relationships, and its style guide for word choice and writing style.

Use this to your advantage by also providing example messages showing how you want the AI to respond. Showing what you want is often easier than trying to explain it!

When your conversation already has history, changing the main prompt has a limited effect on the AI's responses. In terms of events and relationships, the AI assumes that the main prompt occurred in the distant past, and the message history updates it. In terms of writing style and word choice, the AI assumes that all the messages in history were generated according to the rules in the *current* main prompt, and that it should continue to generate messages in the same way. Some suggestions for dealing with this are:

* insert current instructions close to or after the end of message history, for example by using an Author's Note
* test your changes to the main prompt by starting a new conversation
* edit the message history to remove or correct examples of unwanted behavior
* use the Post-History Instructions to provide final instructions to the AI

**Get it right the first time!**

Never let the AI "get away" with something you don't want it to do. If you don't like the AI's response, don't continue the conversation as if it was correct. Instead, modify the prompts, regenerate the message, and continue from there. This will help the AI learn what you want.

**### Removing the "Fictional Chat" Context**

There are situations where "fictional chat" might not be the right context for your conversation. 

You can remove the "fictional" context from the Main Prompt:

> Write \{\{char\}\}'s next reply in a conversation with \{\{user\}\}.

You may not want the AI to think of itself as role-playing at all. Instead of removing the idea of a character, you can remove the idea of an AI:

> You are \{\{char\}\}, a helpful assistant. You provide useful information and help \{\{user\}\} with their questions.

### AI as Narrator or Storyteller

What if you want the AI to act as a narrator, describing events from an omniscient perspective, inventing its own characters and settings?

One approach is to create a named character for the AI to use as a narrator. This character could be called "Narrator" or "AI", suggesting that the AI is a general-purpose storyteller, or it could be named after a specific scenario or setting, giving the AI the task of narrating a story in that setting. The details of the setting can then be defined in the Character or in World Info.

You will need to adjust the default main prompt to reflect the AI's role. For a general-purpose narrator, you might use:

> You are \{\{char\}\}, a skilled and versatile storyteller. Narrate the story.

or for a specific setting:

> You are the narrator of a fantasy scenario. Play as the characters that visit \{\{char\}\}.

It helps to clarify the role of the user in the conversation. Are your messages part of the story, or are they instructions to the narrator about what your character does or says? An example that includes the user in the story:

> The story should progress by responding to the actions and dialogue of \{\{user\}\}. Narrate the story in third person.

An example that keeps the user out of the story:

> Enter Adventure Mode. Narrate the story based on \{\{user\}\}'s dialogue and actions after ">". Describe the surroundings in vivid detail. Be detailed, creative, verbose, and proactive. Move the story forward by introducing fantasy elements and interesting characters.

Defining the role of the user not only helps the AI understand how to respond to your messages, but also to what extent it is allowed to control your persona. This avoids situations where the AI makes decisions for your persona that you would rather make yourself.

## Post-History Instructions

Post-History Instructions (PHI) are additional instructions sent to the AI after the main prompt and the user message. They can be used to provide additional context or instructions to the AI based on the message history.

Since the Post-History Instructions are sent after the user message, they are the final instructions that the AI receives before generating a response. The AI usually gives them a higher priority than the main prompt, and they can override the main prompt's instructions.

To use per-character Post-History Instructions, add them to the character's Post-History Instructions and enable Prefer Char. Instructions. To preserve the globally defined PHI while using character-specific instructions, you can use the `{{original}}` macro in the character's Post-History Instructions field.

+++ Text Completion APIs

Post-History Instructions are defined in the Advanced Formatting panel under the System Prompt category. The Post-History Instructions is added as an invisible user role injection that precedes the last line of the prompt (usually containing a response message "header"). Note that the "Enable System Prompt" toggle must be enabled for the Post-History Instructions to be applied (even if the System Prompt itself is empty).

+++ Chat Completion APIs

Post-History Instructions is one of the default prompts in Prompt Manager. It is usually the last message in the context that the model receives, attributed to ("sent by") the system role. If your Chat Completion API does not support the system role, it will usually be attributed to the user role instead.

+++

## Adding to the Prompt (World Info)

You can insert additional information anywhere in the prompt using the World Info feature. By setting the conditions for when the information should be inserted, you can guide the AI to include specific details, change how it responds, or add new elements to the conversation.

Some common uses of World Info include:

* a "lorebook" or "encyclopedia" with information about the world or setting
* a way to manage different system prompts for various characters and situations
* a place to store memories that the AI should "recall" in the conversation
* a more modular system for creating, editing, and sharing character details
* a source of random events and surprises for the AI to react to, or to make you react to!

# SECTION: SillyTavern_Usage_Prompts_instructmode

# Instruct Mode

Instruct Mode allows you to adjust the prompting for instruction-following models trained on various prompt formats, such as Alpaca, ChatML, Llama2, etc.

**Applies to: Text Completion APIs**

For equivalent settings in Chat Completion APIs, use Prompt Manager.

**## API support**

### Text Completion API

Fully supported. This includes:

* All of the sources under Text Completion
* KoboldAI Classic
* AI Horde

#### Choosing a formatting

A chosen instruct template must match the expectations of an actual model that is running on a backend.

This is usually reflected in a model card on HuggingFace, and some even provide SillyTavern-compatible JSON files.

Example: NeverSleep/Noromaid-13b-v0.1.1 (https://huggingface.co/NeverSleep/Noromaid-13b-v0.1.1#prompt-template-custom-format-or-alpaca)

### Chat Completion API (OpenAI, Claude, etc)

This is not supported **(and not needed)** for Chat Completion APIs. They use an entirely different prompt builder.

### NovelAI

While *technically* supported for NovelAI, none of their models were trained to understand instruct formatting. NovelAI models can use a special instruct module that is activated *automatically* when an instruction wrapped in curly braces is encountered in chat messages, so using Instruct Mode for the entire prompt will lead to **degraded quality** of the outputs.

Here's an example that auto-activates the instruct module for NovelAI:

```txt
User: { Write a happy song about Nintendo Switch. }
```

## Instruct Mode Settings

### System Prompt

**Recent change**

The System Prompt is now a separate entity. See the Advanced Formatting page for more details.

**### Templates**

Provides ready-made templates with sequences for some well-known instruct models.

*Changing a template resets the unsaved settings to the last saved state! Don't forget to save your template if you made any changes you don't want to lose.*

### Activation Regex

If defined as a valid regular expression, when connected to a model and its name matches this regex, will automatically select this template.

Instruct mode needs to be enabled prior. Only the first regex match across templates will be selected (evaluated in alphabetical order).

### Wrap Sequences with Newline

Each sequence text will be wrapped with newline characters when inserted into the prompt. Required for Alpaca and its derivatives.

Disable if you want to have full control over line terminators.

### Replace Macro in Sequences

If enabled, known \{\{macro\}\} substitutions will be replaced if defined in message wrapping sequences.

Also, a special \{\{name\}\} macro can be used in message prefixes to reference the actual name attached to a message (rather than a currently active \{\{char\}\} or \{\{user\}\}), which can be helpful when using group chats or /sendas command. If the name can't be determined, "System" is used as a fallback placeholder.

### Include Names

If enabled, prepend characters and user names to chat history logs after the prefix sequence.

The following options are available:

* **Never**: Do not add name prefixes before the message contents.
* **Groups and Past Personas**: Only add name prefixes to messages from group characters and past personas.
* **Always**: Always add name prefixes before the message contents.

### Sequences: Story String Wrapping

**Recent change**

System Prompt wrapping has been removed and replaced with Story String wrapping.

**Define how the Story String will be wrapped when the Position is set to "Default (top of context)"**

#### Story String Prefix

Inserted before a Story String.

#### Story String Suffix

Inserted after a Story String.

### Sequences: Chat Messages Wrapping

These settings define how messages belonging to different roles will be wrapped upon building a prompt.

All prefix sequences will also be automatically used as stopping strings.

#### User Message Prefix

Inserted before a User message and as a last prompt line when impersonating.

#### User Message Suffix

Inserted after a User message.

#### Assistant Message Prefix

Inserted before an Assistant message and as a last prompt line when generating an AI reply.

#### Assistant Message Suffix

Inserted after an Assistant message

#### System Message Prefix

Inserted before a System (added by slash commands or extensions) message.

#### System Message Suffix

Inserted after a System message.

#### System same as User

If checked true, System messages will be using User role message sequences.

Otherwise, System messages use their own sequences (if not empty) or will not do any wrapping at all (if empty).

### Misc. Sequences

Various advanced configurations for finer tuning of the prompt building

#### First Assistant Prefix

Inserted before the first Assistant's message.

Only the first message of the **chat history** counts, not the message that actually goes into the prompt first!

**#### Last Assistant Prefix**

Inserted before the last Assistant's message or as a last prompt line when generating an AI reply.

Not used when generating text in a background (e.g. Stable Diffusion prompts or Summaries). System Instruction Prefix or Regular Assistant Prefix will be used instead.

**#### System Instruction Prefix**

Inserted as a last prompt line when generating neutral/system text in a background (e.g. Stable Diffusion prompts or Summaries).

#### User Filler Message

Will be inserted at the start of the chat history if it doesn't start with a User message.

**Use case:** when an instruct format *strictly requires* prompts to be user-first and have messages with alternating roles only, examples: Llama 2 Chat, Mistral Instruct.

#### Stop Sequence

Text that denotes the end of the reply. Also sent as a stopping string to the backend API.

If a stop sequence is generated, everything past it will be removed from the output (including the sequence itself).

# SECTION: SillyTavern_Usage_Prompts_prompt-manager

# Prompt Manager

The Prompt Manager is a system that provides more control over the prompt-building strategy for Chat Completion APIs.

**Applies to: Chat Completion APIs**

For equivalent settings in Text Completion APIs, use Advanced Formatting.

**!!!tip Naming Presets**

If a preset shares a name with one of your character cards, it will be automatically selected when starting a chat with that character. Name presets something unique to avoid this behavior.

**Access the Prompt Manager by clicking on the "AI Response Configuration" button in the navigation bar. The Prompt Manager is located below the common settings panel.**

## Quick Prompts Edit

Provides space to quickly edit common prompt sections, such as **Main Prompt**, **Auxiliary Prompt**, and **Post-History Instructions**. More information on these prompts can be found on the prompt-building page.

## Utility Prompts

These prompts are sent to the Chat Completion model to help it understand the information being sent to it, or to instruct it to act in specific ways during certain types of interactions.

### Format Templates

If the format template is not set, the information will be sent as-is, without any wrapping.

**These are string templates used to wrap the information pulled from World Info and Character Cards.**

A special marker is used to indicate where the information should be inserted:

- `{0}` for the World Info format template.
- `{{scenario}}` for the Scenario format template.
- `{{personality}}` for the Personality format template.

### Group Nudge Prompt Template

Used only in group chats. Placed at the end of the prompt to force a reply from a specific character.

Leave this empty to disable Group Nudge functionality.

### New Chat, New Group Chat, New Example Chat

These are sent before the chat history and before each Example Dialogue block to inform the model where background information ends and chat history begins.

- **New Chat:** Used for individual chats.
- **New Group Chat:** Used for group chats.
- **New Example Chat:** Used for example dialogue blocks.

Leave these empty to disable this functionality.

### Continue Nudge

Sent at the end of the prompt to instruct the model on what to do when Continue is triggered, such as when the Continue button is pressed or when triggered by STScript.

**Chat Completion 'Continues'**

Keep in mind that Chat Completion models handle Continues differently than **Text Completion** models, and may not always deliver seamless results regardless of your Continue Nudge.

**### Replace Empty Message**

Sends the contents of this field instead of a blank message when the text box is empty and **Send a message** is pressed.

## Character Names Behavior

Provides different strategies for instructing the model on how to associate messages with characters. If a Chat Completion model is having trouble determining which messages belong to which character, it may need a different strategy selected.

## Continue Postfix

When Continue is triggered, the 'continued' message returned by the model will have the selected Continue Postfix prepended to the beginning. For example, it can add a space before the continued text.

## Additional Settings

### Wrap in Quotes

Deprecated option. Prefer Regex scripts instead.

**Wraps the entire user message in hidden quotation marks before sending. This is useful for sessions where characters do not use quotes to indicate speech. If your session uses quotation marks to indicate speech, leave this unchecked.**

### Continue Prefill

May not work with all Chat Completion sources.

**Sends the Continue Nudge as an Assistant role message instead of a System message. If this is enabled, the Continue Nudge prompt will not be used.**

### Squash system messages

Deprecated option. Prefer Prompt Post-Processing instead.

**Combines consecutive System messages into a single combined message (excluding Example Dialogue).**

### Enable web search

**Not to be confused with the Web Search extension.**

**Enables web search capabilities provided by the Chat Completion backend. The prompt is usually enriched with search results by the model provider and may incur additional costs.**

### Enable function calling

See Function Calling

### Send inline images, Send inline videos

**Not to be confused with the Image Captioning extension.**

**If the Chat Completion model has multimodal capabilities to process submitted images and videos, this toggles its ability to do so. To append media to the prompt, use the **Attach A File** option in the "Magic Wand" menu.**

### Request inline images

**Not to be confused with the Image Generation extension.**

**Allows the model to return image attachments.**

### Use system prompt

**Only supported by Google Gemini and Anthropic Claude backends.**

Despite having very similar settings for these two, they are technically separate options, so they can be configured separately.

**Merges all system messages up until the first message with a non-system role (User/Assistant) and sends them as a separate system instruction field.**

## Reasoning Settings

If the Chat Completion model uses reasoning, these settings affect its visibility and functionality.

### Request model reasoning

See Adding Reasoning: By Backend.

### Reasoning Effort

See Reasoning Effort.

## "Prompts"

The Prompt Manager forms the backbone of the prompt sent to the Chat Completion model. It controls what is sent as well as the *order* in which it is sent.

### The 'Prompts' Dropdown

Contains a dropdown list of all (non-default) prompts that the current Chat Completion preset includes. For one of these prompts to be added to the outgoing message, it needs to be selected from the dropdown list and then added to the Prompt Manager by pressing the **Insert prompt** button. To create a new prompt to add to this dropdown list, press the **New prompt** button. Once the new prompt is written and saved, it is added to the dropdown and can then be inserted.

### Prompts List

This is a drag-and-drop interface that lists the prompts selected to potentially be sent to the Chat Completion model. Prompts placed closer to the **top** of the interface are sent earlier. The **bottom** of the list is the **last thing** sent to the model (typically, this would be your **Post-History Instructions**).

**'Pinned' prompts = Default prompts**

The default prompts cannot be removed from the list of selected prompts. This includes Main Prompt, World Info (before/after), Persona Description, Character Description, Character Personality, Scenario, Enhance Definitions, Auxiliary Prompt, Chat Examples, Chat History, and Post-History Instructions. If these are not desired, they can be **toggled 'OFF'**, but not removed or deleted outright.

**## Editing a Prompt**

Clicking the **pencil button** on a prompt will bring you to the **Edit interface**. Here, you can edit the prompt directly.

**Make sure to save your changes!**

To permanently save changes to these prompts in your Chat Completion preset, you must click the **Save** button in the bottom right of the **Edit interface**, as well as save the preset itself by using the **Save** button located at the top of the **AI Response Configuration** section! Otherwise, changes made will be lost when the Chat Completion preset is switched to a different one.

**### Name**

The name of the prompt. This is not sent to the Chat Completion model; it is for your reference within the Prompt Manager only.

### Role

Which role sends the prompt. You can choose between System, AI Assistant, or User.

### Triggers

The generation types for which this prompt is sent. If nothing is selected, the prompt will be sent for all generation types. If one or more are selected, the prompt will only be sent for those specific generation types:

- **Normal:** Regular message generation request.
- **Continue:** When the Continue button is pressed.
- **Impersonate:** When the Impersonate button is pressed.
- **Swipe:** When the generation is triggered by swiping.
- **Regenerate:** When the Regenerate button is pressed in solo chats.
- **Quiet:** Background generation requests, usually triggered by extensions or STscript commands.

**The "Regenerate" trigger is not available in group chats as it uses different regeneration logic: all messages from the last reply are deleted, and messages are queued using the "Normal" generation type according to the chosen Group reply strategy.**

**### Position**

When Position is set to **Relative**, this prompt is sent where it's located in the drag-and-drop interface with all other prompts. When it is set to **In-Chat** and given a **Depth**, it is instead sent **within the Chat History** as the selected Role, and **ignores** the order of the drag-and-drop interface.

### Depth

When Position is set to **In-Chat**, this defines how deep the prompt is sent within the chat history. The higher the number, the deeper it is sent. For example, a Depth of 0 will be sent after the last chat message, a Depth of 1 will be sent before the last chat message, and a Depth of 2 will be sent before the second-to-last chat message, and so on.

### Order

**Prompts that have the same Role and Depth will be grouped together and ordered by their Order value.**

The order is as follows (from top to bottom): User, AI Assistant, System.

**When Position is set to **In-Chat**, this defines the order in which the prompt is sent within the chat history. The lower the number, the earlier it is sent.**

## Building Your Prompt: Tips and Tricks

Visit the prompt-building section of the SillyTavern documentation for more information on how to write effective prompts. The information can largely be applied to Chat Completion presets.

# SECTION: SillyTavern_Usage_Prompts_reasoning

# Reasoning

In language models, reasoning (also known as model thinking) refers to a chain-of-thought (CoT) technique that mirrors human problem-solving through step-by-step analysis. SillyTavern provides several features that make the use of reasoning models more efficient and consistent across supported backends.

## Common issues

1. When using reasoning models, the model's internal reasoning process consumes part of your response token allowance, even if this reasoning isn't shown in the final output (e.g. o3-mini or Gemini Thinking). If you notice your responses are coming back incomplete or empty, you should try adjusting the Max Response Length setting found in the **<i class="fa-solid fa-sliders"></i> AI Response Configuration** panel. For reasoning models, it's typical to use significantly higher token limits - anywhere from 1024 to 4096 tokens - compared to standard conversational models.

## Configuration

**Most reasoning-related settings can be configured in the "Reasoning" section of **<i class="fa-solid fa-font"></i> Advanced Formatting** panel.**

**Reasoning blocks appear in the chat as collapsible message sections. They can be added manually, automatically by the backend, or through response parsing (see below).**

By default, reasoning blocks are collapsed to save space. Click a block to expand and view its contents. You can set blocks to expand automatically by enabling **Auto-Expand** in the reasoning settings.

When a reasoning block is expanded, you can copy or edit its contents using the **<i class="fa-solid fa-copy"></i> Copy** and **<i class="fa-solid fa-pencil"></i> Edit** buttons.

Some models support reasoning, but will not send their thoughts back. It is possible to still show the reasoning block with reasoning time for those by toggling the **Show Hidden** setting.

## Adding Reasoning

### Manually

Add a reasoning block to any message through the **<i class="fa-solid fa-pencil"></i> Message Edit** menu. Click **<i class="fa-solid fa-lightbulb"></i>** while editing to add a reasoning section. Third-party extensions can also add reasoning by writing to the `extra.reasoning` field of the message object before adding it to the chat.

### With a Command

Use the `/reasoning-set` STscript command to add reasoning to a message. The command takes `at` (message ID, defaults to the last message) and reasoning text as arguments.

```stscript
/reasoning-set at=0 This is the reasoning for the first message.
```

### By Backend

If your chosen LLM backend and model support reasoning output, enabling "Request model reasoning" in the **<i class="fa-solid fa-sliders"></i> AI Response Configuration** panel will add a reasoning block containing the model's thinking process.

Supported sources:

- Claude
- DeepSeek
- Google AI Studio
- Google Vertex AI
- OpenRouter
- xAI (Grok)
- AI/ML API
- Z.AI
- Pollinations
- MistralAI
- Electron Hub
- Chutes
- NanoGPT
- Moonshot

**For **most** sources, "Request model reasoning" does not determine whether a model does reasoning as it can't be disabled. If the backend and model support explicitly requesting disabled reasoning, the setting will do so. Otherwise, the model will always reason.**

**Provider-specific notes:**

- Claude and Google (2.5 Flash) allow thinking mode to be toggled; see Reasoning Effort.
- Reasoning can be disabled for Z.AI (GLM) (https://docs.z.ai/api-reference/llm/chat-completion#body-one-of-0-thinking) and Moonshot (Kimi) (https://platform.moonshot.ai/docs/guide/use-kimi-k2-thinking-model). The setting maps to the `thinking.type` parameter. They do not support "Reasoning Effort".

### By Parsing

Enable "Auto-Parse" in the **<i class="fa-solid fa-font"></i> Advanced Formatting** panel to automatically parse reasoning from the model's output.

The response must contain a reasoning section wrapped in configured Prefix and Suffix sequences. The sequences provided by default correspond to the DeepSeek R1 reasoning format.

Example with prefix `<think>` and suffix `</think>`:

```txt
<think>
This is the reasoning.
</think>

This is the main content.
```

## Prompting with Reasoning

By default, recognized reasoning block contents are not sent back to the model. To include reasoning in prompts, enable "Add to Prompts" in the **<i class="fa-solid fa-font"></i> Advanced Formatting** panel. Reasoning content will be wrapped in configured Prefix and Suffix sequences and separated by a Separator from the main context. The Max Additions numeric setting controls how many reasoning blocks can be included, counting from the end of the prompt.

**Most model providers do not recommend sending CoT back to the model in multi-turn conversations.**

**### Continuing from Reasoning**

A special case when the reasoning can be sent back to the model without having the "Add to Prompts" toggle enabled is when the generation is continued (e.g. by pressing "Continue" from the **<i class="fa-solid fa-bars"></i> Options** menu), but the message being continued contains only the reasoning without actual content. This gives the model an opportunity to finish an incomplete reasoning and start generating the main content. The prompt will be sent as follows:

```txt
<think>
Incomplete reasoning...
```

## Regex Scripts

Regular expression scripts from the Regex extension can be applied to the contents of reasoning blocks. Check "Reasoning" in the "Affects" section of the script editor to target reasoning blocks specifically.

Different ephemerality options affect reasoning blocks in the following ways:

1. No ephemerality: reasoning content is permanently changed.
2. Run on edit: regex script will be re-evaluated when the reasoning block is edited.
3. Alter chat display: regex is applied to the reasoning block's display text, not the underlying content.
4. Alter outgoing prompts: regex is only applied to reasoning blocks before they are sent to the model.

## Reasoning Effort

Reasoning Effort is a Chat Completion setting in the **<i class="fa-solid fa-sliders"></i> AI Response Configuration** panel that influences how many tokens may potentially be used on reasoning. The effect of each option depends on the source connected to. For the sources below, Auto simply means the relevant parameter is not included in the request.

| Option  | Claude (≤ 21333 if no streaming) | OpenAI (keyword)     | OpenRouter (keyword)             | xAI (Grok) (keyword) | Perplexity (keyword) | NanoGPT (keyword) |
| ------- | -------------------------------- | -------------------- | -------------------------------- | -------------------- | -------------------- | ----------------- |
| Models  | Opus 4, Sonnet 4/3.7             | o4-mini, o3\*, o1\*  | applicable models                | grok-3-mini          | sonar-deep-research  | applicable models |
| Auto    | not specified, **no thinking**   | not specified        | not specified, effect depends    | not specified        | not specified        | not specified     |
| Minimum | budgets 1024 tokens              | "low"                | "low", or 20% of max response    | "low"                | "low"                | "none"            |
| Low     | 15% of max response, min 1024    | "low"                | "low", or 20% of max response    | "low"                | "low"                | "minimal"         |
| Medium  | 25% of max response, min 1024    | "medium"             | "medium", or 50% of max response | "low"                | "medium"             | "low"             |
| High    | 50% of max response, min 1024    | "high"               | "high", or 80% of max response   | "high"               | "high"               | "medium"          |
| Maximum | 95% of max response, min 1024    | "high"               | "high", or 80% of max response   | "high"               | "high"               | "high"            |

- For Claude, budget is capped to 21333 if streaming is disabled. If the calculated budget would be less than 1024, then max response is changed to 2048.
- For OpenRouter, Perplexity and AI/ML API, only an OpenAI-style keyword is sent.

Google AI Studio and Vertex AI are as follows:

| Model          | Auto (dynamic thinking) | Minimum            | Low                          | Medium     | High       | Maximum               |
| -------------- | ----------------------- | ------------------ | ---------------------------- | ---------- | ---------- | --------------------- |
| 2.5 Pro        | thinkingBudget = -1     | 128                | 15% of max response, min 128 | 25% of max | 50% of max | lower of max or 32768 |
| 2.5 Flash      | thinkingBudget = -1     | 0, **no thinking** | 15% of max response          | 25% of max | 50% of max | lower of max or 24576 |
| 2.5 Flash Lite | thinkingBudget = -1     | 0, **no thinking** | 15% of max response, min 512 | 25% of max | 50% of max | lower of max or 24576 |
| 3.0 Pro        | thinkingLevel = null    | "low"              | "low"                        | "low"      | "high"     | "high"                |
| 3.0 Flash      | thinkingLevel = null    | "minimal"          | "low"                        | "medium"   | "high"     | "high"                |

- For Gemini 2.5 Pro and 2.5 Flash/Lite, budget is capped to 32768 or 24576 tokens respectively, regardless of the streaming setting.

# SECTION: SillyTavern_Usage_Prompts_tokenizer

# Tokenizer

A tokenizer is a tool that breaks down a piece of text into smaller units called tokens. These tokens can be individual words or even parts of words, such as prefixes, suffixes, or punctuation. A rule of thumb is that one token generally corresponds to 3~4 characters of text.

SillyTavern provides a "Best match" option that tries to match the tokenizer using the following rules depending on the API provider used.

Text Completion APIs **(overridable)**:

1. NovelAI Clio: NerdStash tokenizer.
2. NovelAI Kayra: NerdStash v2 tokenizer.
3. Text Completion: API tokenizer (if supported) or Llama tokenizer.
4. KoboldAI Classic / AI Horde: Llama tokenizer.
5. KoboldCpp: model API tokenizer.

If you get inaccurate results or wish to experiment, you can set an _override tokenizer_ for SillyTavern to use while forming a request to the AI backend:

1. None. Each token is estimated to be ~3.3 characters, rounded up to the nearest integer. **Try this if your prompts get cut off on high context lengths.** This approach is used by KoboldAI Lite.
2. Llama tokenizer. Used by Llama 1/2 models family: Vicuna, Hermes, Airoboros, etc. **Pick if you use a Llama 1/2 model.**
3. Llama 3 tokenizer. Used by Llama 3/3.1 models. **Pick if you use a Llama 3/3.1 model.**
4. NerdStash tokenizer. Used by NovelAI's Clio model. **Pick if you use the Clio model.**
5. NerdStash v2 tokenizer. Used by NovelAI's Kayra model. **Pick if you use the Kayra model.**
6. Mistral V1 tokenizer. Used by older Mistral models family and their finetunes. **Pick if you use an older Mistral model.**
7. Mistral Nemo tokenizer. Used by Mistral Nemo models family and their finetunes. **Pick if you use a Mistral Nemo/Pixtral model.**
8. Yi tokenizer. Used by Yi models. **Pick if you use a Yi model.**
9. Gemma tokenizer. Used by Gemini/Gemma models. **Pick if you use a Gemma model.**
10. DeepSeek tokenizer. Used by DeepSeek models (such as R1). **Pick if you use a DeepSeek model.**
11. API tokenizer. Queries the generation API to get the token count directly from the model. Known backends to support: Text Generation WebUI (ooba), koboldcpp, TabbyAPI, Aphrodite API. **Pick if you use a supported backend.**

Chat Completion APIs **(non-overridable)**:

1. OpenAI: model-dependent tokenizer via tiktoken (https://github.com/openai/tiktoken).
2. Claude: model-dependent tokenizer via WebTokenizers (https://github.com/mlc-ai/tokenizers-cpp).
3. OpenRouter: Llama, Mistral, Gemma, Yi tokenizers for their respective models.
4. Google AI Studio: Gemma tokenizer.
5. AI21 API: Jamba tokenizer (requires a one-time download).
6. Cohere API: Command-R or Command-A tokenizer (requires a one-time download).
7. MistralAI API: Mistral V1 or V3 tokenizer (requires a one-time download).
8. DeepSeek API: DeepSeek tokenizer (requires a one-time download).
9. Fallback tokenizer: GPT-3.5 turbo tokenizer.

#### Additional Tokenizers

These tokenizers are not included in the default installation due to their size. A one-time download is required when they're used for the first time.

1. Qwen2 tokenizer.
2. Command-R / Command-A tokenizers. Used by Cohere source in Chat Completion.
3. Mistral V3 (Nemo) tokenizer. Used by MistralAI source in Chat Completion (Nemo and Pixtral models).
4. DeepSeek (deepseek-chat) tokenizer. Used by DeepSeek source in Chat Completion.

If you don't want to use internet downloads, the opt-out option exists in config.yaml: `enableDownloadableTokenizers`. Set to `false` to disable downloads.

You can also download tokenizers manually from the SillyTavern-Tokenizers (https://github.com/SillyTavern/SillyTavern-Tokenizers) repository. Download the JSON files and put them in the `_cache` subdirectory of your data root, the path is `./data/_cache` by default. Create the `_cache` directory if it doesn't exist. After that, restart the SillyTavern server to re-initialize tokenizers.

If the required tokenizer model is not cached and downloads are disabled, a fallback tokenizer (Llama 3) will be used for counting.

### Token Padding

**Applies to: Text Completion APIs**

SillyTavern will always use the matching tokenizer for Chat Completion models, so there is no need for token padding.

**Unless SillyTavern uses a tokenizer provided by the remote backend API that runs the model, all token counts assumed during prompt generation are estimated based on the selected tokenizer type.**

Since the results of tokenization can be inaccurate on context sizes close to the model-defined maximum, some parts of the prompt may be trimmed or dropped, which may negatively affect the coherence of character definitions.

To prevent this, SillyTavern allocates a portion of the context size as padding to avoid adding more chat items than the model can accommodate. If you find that some part of the prompt is trimmed even with the most-matching tokenizer selected, adjust the padding so the description is not truncated.

You can input negative values for reverse padding, which allows allocating more than the set maximum amount of tokens.

# SECTION: SillyTavern_Usage_quick-start

# Quick Start

**light**

I'm clueless. Just spoonfeed me the easiest and fastest way I can start using SillyTavern. -- *Anonymous*

**You can get started with SillyTavern in just a few minutes. Here are two easy ways to get started:**

* You can use AI Horde for free. AI Horde is a community-driven AI service that provides access to a variety of AI models.

* If you have an OpenAI account or want to register one, you can use OpenAI.

## Quick start with AI Horde

1. Follow the Installation Guide to install and start SillyTavern.

2. In SillyTavern's onboarding screen, enter a name for your persona. This name will be used in the chat.

   
3. Click the API Connections button in the top bar.

   
4. Enter an API key for AI Horde. You can use `0000000000` for now, or get a free key from AI Horde (https://aihorde.net/).

   
5. Select some AI models to use. Just choose a few from the top. You can always change them later.

   
6. Close the API Connections window. Enter a message in the chat box at the bottom and press Enter.

   
7. Your AI will respond in a few moments. You can continue chatting with it. Success!

   

## Quick start with OpenAI

### Install SillyTavern

Follow the Installation Guide to install and start SillyTavern.

### Get access to OpenAI

1. Sign up to OpenAI.
2. Go to <https://platform.openai.com>
3. Click your account icon in the top right, then View API Keys.
4. Click "Create new secret key". Copy it somewhere immediately. **DO NOT SHARE THIS KEY. WHOEVER HAS IT CAN USE YOUR ACCOUNT TO USE GPT AT YOUR EXPENSE.**

### Configure SillyTavern to use your API

1. In SillyTavern's top bar, click API Connections.
2. Under API, select Chat Completion (OpenAI).
3. Under Chat Completion Source, select OpenAI.
4. Paste the API key you saved in the previous step.
5. Click the Connect button. Confirm it says Valid.
6. By default, SillyTavern will use GPT-4 Turbo. You can choose a different model, but educate yourself on the pricing.

### Test your setup

1. In SillyTavern's top bar, click Character Management at the far right.
2. Select an existing character such as Seraphina.
3. In the text box at the bottom, write something to Seraphina, then press Enter or click the Send button.

If you did everything right, after a few seconds, Seraphina should respond.

# SECTION: SillyTavern_Usage_User_Settings_index

# User Settings

**UI Customization**

Change the theme, look and feel of the chat interface to suit your preferences.

**:::callout**

**Visual Novel mode**

Chat to characters with sprites, like in visual novels such as Doki Doki Literature Club and other famous VN games.

**## General Settings**

These are the core settings that affect your overall SillyTavern experience.

### UI Language

SillyTavern's user interface is available in multiple languages. The language selector provides these options:
* **Default**: Uses your system language if available
* **English**: Forces English UI regardless of system settings
* Other languages available through the dropdown

Note: This setting only affects the user interface text. For AI conversation translation, please use the Chat Translation extension.

### Software Version

Your current version of SillyTavern is displayed in the top-right corner. This information is essential for:
* Troubleshooting problems
* Ensuring compatibility with extensions
* Determining if updates are available

To update SillyTavern to the latest version, please refer to the Updating documentation.

### Account Management

Control your SillyTavern user account, back up your settings and user data, and manage user roles and permissions in multi-user mode.

#### <i class="fa-fw fa-solid fa-user-shield"></i> Account

In the Account dialog, you can view and edit your profile information, change your password, and manage account settings.

**Profile Information**

* Display name (editable via pencil icon)
* User avatar (can also be changed using Personas)
* Account handle
* User role
* Account creation date
* Password status (locked/unlocked icon indicates protection)

**Account Actions**

* **Settings Snapshots**: Create, manage, and restore backups of your user settings
* **Download Backup**: Export a complete backup of all your user data
* **Change Password**: Update your account security credentials

**Danger Zone**

Critical account operations that should be used with caution:
* **Reset Settings**: Restore all settings to factory defaults
* **Reset Everything**: Complete account wipe and factory reset

#### <i class="fa-fw fa-solid fa-user-tie"></i> Admin Panel

**Applies to: multi-user mode**

Multi-account features require `enableUserAccounts` to be set to true in config.yaml. 

**Select **Manage Users** to view and manage existing user accounts.**

##### User Profile

- Custom avatar management (upload/remove)
- Display name and handle
- Role and status information
- Account creation date
- Password protection status

##### Account Controls

- <i class="fa-fw fa-solid fa-pencil"></i> Edit display name
- <i class="fa-fw fa-solid fa-check"></i> Enable account
- <i class="fa-fw fa-solid fa-ban"></i> Disable account
- <i class="fa-fw fa-solid fa-arrow-up"></i> Promote to admin
- <i class="fa-fw fa-solid fa-arrow-down"></i> Demote to regular user

##### Management Actions

- <i class="fa-fw fa-solid fa-download"></i> Download user data backup
- <i class="fa-fw fa-solid fa-key"></i> Change user password
- <i class="fa-fw fa-solid fa-trash"></i> Delete account

##### New User

Select **New User** to create a new user account.

* Display Name* (e.g., "John Snow")
* User Handle* (lowercase letters, numbers, and dashes only)
* Password (optional)
* Password Confirmation

Creating a new user automatically generates a subfolder in the /data/ directory using the user's handle as the folder name.

#### <i class="fa-fw fa-solid fa-right-from-bracket"></i> Logout

**Applies to: multi-user mode**

**Sign out of your current session.**

### Settings Search

A convenient search bar that helps you quickly find specific settings:
* Type any keyword to filter and highlight settings anywhere in User Settings
* Searches through setting names and descriptions
* Helps navigate complex settings more efficiently

## UI Theme

Change the appearance of the chat interface to suit your preferences.

For more information on the settings in this section of <i class="fa-fw fa-solid fa-user-gear" title="User Settings icon"></i> **User Settings**, see UI Customization.

## Character Handling

* **Char List Subheader**: Choose what additional information to display under character names in the <i class="fa-fw fa-solid fa-address-card" title="Characters icon"></i> Characters list:
    - Character Version
    - Created by
* **Import Card Tags**: Controls how tags are handled when importing character cards:
    - Ask - Show dialog for each import
    - None - Don't import any tags
    - All - Import all tags
    - Existing - Only import tags that already exist
* **Advanced Character Search**: When enabled, uses fuzzy matching and searches all character data fields, not just names.
* **Prefer Char. Prompt**: If enabled, uses the character card's System Prompt override when available.
* **Prefer Char. Instructions**: If enabled, uses the character card's Post-History Instructions override when available.
* **Never resize avatars**: Prevents cropping/resizing of imported character images. When disabled, images are resized to 512x768.
* **Show avatar filenames**: Displays actual filenames of character avatars in the character list.
* **Spoiler Free Mode**: Hides character definitions behind a spoiler button in the editor panel.

## Miscellaneous

* **Reload Chat**: Reloads and redraws the current chat.
* **Debug Menu**: Access debugging options.
* **Smooth Streaming**: Smoothens streamed generation by showing the text letter by letter. Includes speed control slider. To exclude reasoning blocks from smooth streaming, enable "Exclude 'Thinking...'" option.
* **Stream Fade-In**: Applies a fade-in effect to streamed text. Can be used with or without Smooth Streaming.
* **Message Sound**: Plays a sound when message generation completes.
    - **Background Sound Only**: Only plays sounds when browser tab is unfocused.
* **Relaxed API URLs**: Reduces formatting requirements for API URLs.
* **Lorebook Import Dialog**: Shows import dialog for World Info/Lorebook when importing characters with embedded lore.
* **Auto-select Input Text**: Automatically selects text in certain input fields when clicked.
* **Markdown Hotkeys**: Enables keyboard shortcuts for markdown formatting.
* **Restore User Input**: Preserves unsaved user input when page is refreshed.
* **MovingUI**: Allows repositioning UI elements by dragging (PC only).
    - <i class="fa-solid fa-recycle" title="Reset icon"></i> **Reset** button to restore default positions
    - Preset system for saving/loading UI layouts

## Chat/Message Handling

### Message Display Settings

Controls how messages are loaded and displayed in the chat interface. These settings affect the overall chat experience and performance.
* **# Messages to Load**: Number of chat history messages to load before pagination (0 = All)
* **Streaming FPS**: Update speed of streamed text (5-100 FPS)
* **Example Messages Behavior**:
    - Gradual push-out
    - Always include examples
    - Never include examples
* **Image Swipe Behavior** (controls swipe actions for images in gallery style):
    - Generate new: Allows generating new images with the Image Generation extension
    - Roll over: Cycles through existing images, wrapping around at the ends

### Input & Response Controls

Settings that determine how messages are sent and how the AI continues its responses.
* **Enter to Send**: Choose between Disabled, Automatic (PC), or Enabled
* **"Send" to Continue**: Use Send button to continue AI responses
* **Quick "Continue" button**: Show button to extend AI's last message
* **Quick "Impersonate" button**: Show button for single-message character impersonation
* **Swipes**: Show arrow buttons for alternative AI responses (PC and mobile)
* **Gestures**: Enable swipe gestures for generation (Mobile only)

### Auto-Management

Automated features that help manage chat flow and content.
* **Auto-load Last Chat**: Automatically load the most recent chat on startup
* **Auto-scroll Chat**: Automatically scroll to newest messages
* **Auto-save Message Edits**: Save message edits without confirmation
* **Confirm message deletion**: Prompt before deleting messages
* **Auto-fix Markdown**: Automatically correct markdown formatting

#### Auto-swipe

Automatically reject and regenerate AI messages based on configurable criteria.
* **Enable Auto-swipe**: Master toggle for the auto-swipe function
* **Minimum generated message length**: Triggers an auto-swipe if the message is shorter than this value
* **Blacklisted words**: List of words that can trigger auto-swipe, separated by commas
* **Blacklisted word count to swipe**: Minimum number of blacklisted words that must be detected to trigger an auto-swipe

#### Auto-Continue

Automatically continues a response if the model stopped before reaching a certain length.

This lets your AI write a long response in multiple parts, so that you can have a short response length setting while still getting long replies. 

It will not make the AI write more than it would have otherwise. Asking the AI to continue a message that it considers "finished" does not usually work. See How to make the AI write more? for other ideas.

* **Enable Auto-continue**: Master toggle for automatic continuation
* **Allow for Chat Completion APIs**: Enables auto-continue functionality for Chat Completion API endpoints
* **Target length (tokens)**: The desired message length in tokens - will trigger continue if message is shorter than this value (0-1024)

### Message Formatting & Display

Controls how messages are formatted and what content is displayed.
* **Forbid External Media**: Block embedded media from external domains
* **Show {\{char}}: in responses**: Retain character name prefix in responses if generated
* **Show {\{user}}: in responses**: Retain user name prefix in responses if generated
* **Experimental Macro Engine**: Enables advanced macro processing that supports nesting
* **Show tags in responses**: Allow (some) HTML tags in responses to be displayed as HTML 
* **Relax message trim in Groups**: Allow AI to speak for other characters in group chats, rather than stopping the response generation
* **Show group chat queue**: Display response order in the character list for group chats
* **Pin greeting message styles**: Always render style tags from greetings, even if the message is unloaded due to lazy loading.

### Prompt Inspection and Debugging

* **Log prompts to console**: Output prompts to browser console
* **Request token probabilities**: Request token probabilities for AI responses from the API. Where available, these can be viewed in <i class="fa-solid fa-bars" title="Burger Menu icon"></i> Token Probabilities.

### AutoComplete

- Auto-hide details
- Matching style (Starts with/Includes/Fuzzy)
- Visual style (Theme/Dark/Light)
- Keyboard selection options
- Font scaling
- Width controls

## STscript Settings

Configuration options for the STscript parser.

### STRICT_ESCAPING

* Pipes don't need to be escaped in quoted values.
* A backslash in front of a symbol can be escaped to provide the literal backslash followed by the functional symbol.

See Strict Escaping for more information.

### REPLACE_GETVAR

Helps to avoid double-substitutions when the variable values contain text that could be interpreted as macros.

See Replace Variable Macros for more information.

## Clean-Up Menu

The Clean-Up menu provides a data maintenance tool that helps you identify and remove unnecessary files from your SillyTavern installation. This feature helps keep your data directory organized and can free up significant disk space.

**"Important Warning"**

The Clean-up tool will permanently delete files. **This action cannot be undone!**

Manual uploads to the `/data/user/files/` and `/data/user/images/` directories will be deleted if they are not associated with chat messages or Data Bank entries.

If unsure, make a backup of your data before using the Clean-up menu.

**### How to Use Clean-Up**

1. Click the **Clean-Up** button under the **Miscellaneous** section
2. Click **Scan** to analyze your installation. This may take some time depending on the size of your data directory
3. Review the categories of files found
4. Use **View** to preview file contents before deletion
5. Use **Download** to save files before deletion
6. Delete individual files or entire categories as needed

### Clean-Up Categories

The Clean-Up tool scans for loose files into the following categories:

#### Files

* **What it finds**: Files that are not associated with chat messages or Data Bank entries
* **Location**: `/data/<user-handle>/user/files/`
* **Risk**: ⚠️ **WILL DELETE MANUAL UPLOADS** that aren't referenced in chats
* **When to clean**: Safe to delete if you don't need unreferenced files

#### Images

* **What it finds**: Images that are not associated with chat messages
* **Location**: `/data/<user-handle>/user/images/`
* **Risk**: ⚠️ **WILL DELETE MANUAL UPLOADS** that aren't referenced in chats
* **When to clean**: Safe to delete if you don't need unreferenced images

#### Chats

* **What it finds**: Chat files associated with deleted characters
* **Location**: `data/<user-handle>/chats/`
* **Risk**: ⚠️ **Orphaned chats will be permanently lost**
* **When to clean**: Safe to delete if you've intentionally deleted characters and no longer need their chat histories

#### Group Chats

* **What it finds**: Chat files associated with deleted groups
* **Location**: `data/<user-handle>/group chats/`
* **Risk**: ⚠️ **Orphaned group chats will be permanently lost**
* **When to clean**: Safe to delete if you've intentionally deleted groups and no longer need their chat histories

#### Avatar Thumbnails

* **What it finds**: Thumbnails for avatars of missing or deleted characters
* **Location**: `data/<user-handle>/thumbnails/avatar`
* **Risk**: ✅ **Safe to delete** - thumbnails are automatically regenerated when needed
* **When to clean**: Always safe to clean, helps free up space

#### Background Thumbnails

* **What it finds**: Thumbnails for missing or deleted backgrounds
* **Location**: `data/<user-handle>/thumbnails/bg`
* **Risk**: ✅ **Safe to delete** - thumbnails are automatically regenerated when needed
* **When to clean**: Always safe to clean, helps free up space

#### Chat Backups

* **What it finds**: Automatically generated chat backups
* **Location**: `data/<user-handle>/backups/chat_*`
* **Risk**: ⚠️ **Backup files will be permanently lost**
* **When to clean**: Consider keeping recent backups, but older ones can be safely deleted

#### Settings Backups

* **What it finds**: Automatically generated settings backups
* **Location**: `data/<user-handle>/backups/settings_*`
* **Risk**: ⚠️ **Settings backup files will be permanently lost**
* **When to clean**: Consider keeping recent backups, but older ones can be safely deleted

## Debug menu

**These functions are intended for advanced users only.**

Do not use them unless you fully understand their consequences.

**The Debug Menu provides functionality for troubleshooting, maintenance, and development purposes. These functions should be used with caution as they can significantly impact your SillyTavern installation.**

Because extensions can add debug functions, the available options will vary depending on the extensions you have installed.

### Translation & Locale Functions
* **Get missing translations**: Analyzes the current locale (or all locales if English is selected) for missing translations and outputs results to browser console
* **Apply locale**: Forces a refresh of the current language settings by reapplying the selected locale
### Cache & Storage Management
* **Clear WebSearch cache**: Removes all stored search results from local cache
* **Purge all vector indices**: Completely removes all stored vectors across all sources
* **Reset token cache**: Clears stored token counts, forcing complete re-tokenization of all chats
* **Delete itemized prompts**: Removes all itemized prompts from local storage
### Data & Statistics
* **Refresh Stat File**: Rebuilds the statistics file using existing chat data
* **Backfill token counters**: Recalculates token counts for all messages in current chat
    - Useful when switching between models with different tokenizers
    - Triggers chat reload after completion
    - Visual changes only, does not modify chat content
### API & Extension Testing
* **Change Mancer base URL**: Modify the base URL for Mancer API server
* **Test WebSearch extension**: Performs a test search using current settings
* **Send a generation request**: Tests text generation using the currently selected API
### System & Debug Tools
* **Force onboarding**: Restarts the onboarding process
* **Toggle event tracing**: Enables/disables event tracking for debugging
* **Copy ST setup**: [Work in Progress] Copies system configuration data to clipboard for bug reports

Each function can be executed using the "Execute" button beneath its description. Consider backing up your data before using these tools, as some operations cannot be undone.

# SECTION: SillyTavern_Usage_User_Settings_uicustomization

# UI Customization

## UI Theme

### Theme Management

Theme files allow you to save, share, and reuse your UI customizations. You can maintain multiple themes for different moods or purposes, and switch between them instantly.

* Import/Export theme files
* Delete existing themes
* Save changes to current theme
* Save as new theme

All the settings in this section are saved to the current theme. If you switch themes, the settings will be replaced by the settings of the new theme.

### Display Settings

These display options affect how characters and messages are presented in the chat interface.

#### Avatar Style

Choose between Circle, Square, Rectangle, or Rounded Square. This setting applies to both user and AI avatars.

#### Chat Style

| Style        | Description                                                                                                                                                    | Slash command |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| **Flat**     | Clean and continuous "chat log" style, a flat canvas for your AI interactions to come to life.                                                                 | `/flat``/default`                                      |
| **Bubbles**  | "Instant messenger" style with distinct bubbles for each message, delightful rounded corners, and a subtle 3D effect.                                          | `/bubble``/bubbles`                                    |
| **Document** | Compact, document-like appearance with a text-focused layout. Hides avatars, timestamps, and message control buttons for past messages. | `/single``/story`                                      |

### Notifications

Set a position where the notification popups (toast messages) will appear on the screen.

* Top Left
* Top Center (default)
* Top Right
* Bottom Left
* Bottom Center
* Bottom Right

### Media Style

Default display style for media attachments (images, audio, video) in chat messages. Extensions that append media to chat messages may override this setting. It can also be changed manually per message using "Toggle media display style" action in the message context menu.

* **List**: Display all media attachments at once in a grid-like layout.
* **Gallery**: Display media attachments in a carousel-style gallery.

**This setting also affects how the inline media attachments are sent to supported Chat Completion sources: list sends all attachments at once, while gallery sends the selected attachment.**

**### Theme Colors**

Customize the color scheme of every UI element to create your perfect theme. Colors can be selected using a color picker, and include transparency options where applicable.

* Main Text
* Italics Text
* Underlined Text
* Quote Text
* Text Shadow
* Chat Background
* UI Background
* UI Border
* User Message
* AI Message

### Layout & Visual Settings

Fine-tune the visual presentation of the interface with these sliders.

* **Chat Width**: Adjust chat window width (25-100% of screen)
* **Font Scale**: Customize text size (0.5-1.5x)
* **Blur Strength**: Control UI panel blur (0-30)
* **Shadow Width**: Adjust text shadow intensity (0-5)

### Theme Toggles

These switches control various UI features and behaviors. Some options can improve performance on lower-end devices, while others add useful information or functionality to the chat interface.

* **Reduced Motion**: Disable animations and transitions
* **No Blur Effect**: Remove background blur for better performance
* **No Text Shadows**: Disable text shadow effects
* **Visual Novel mode**: Compact chat with background sprite
* **Expand Message Actions**: Always show full message context menu
* **Zen Sliders**: Simplified parameter controls
* **Mad Lab Mode**: Unrestricted parameter ranges
* **Message Timer**: Show AI response generation time
* **Chat Timestamps**: Display message timestamps
* **Model Icons**: Show AI model icons for messages
* **Message IDs**: Display sequential message numbers
* **Hide Chat Avatars**: Remove avatars from chat
* **Message Token Count**: Show token counts per message
* **Compact Input Area**: Single-row input (Mobile only)
* **Swipe # for All Messages**: Show swipe numbers on all messages
* **Characters Hotswap**: Quick-select buttons for favorite characters
* **Avatar Hover Magnification**: Zoom effect on avatar hover
* **Tags as Folders**: Organize characters using tags as folders
* **Click to Edit**: Click on messages to quickly open a message editor

### Custom CSS

Allows you to apply custom CSS styles to further customize the appearance of the chat interface.

Use <i class="fa-fw fa-solid fa-maximize" title="Expand icon"></i> **Expand** to expand the editor window for better visibility and editing.

If you switch themes, your custom CSS will be replaced by the custom CSS of the new theme. Ensure you save your custom CSS to a theme if you want to keep it when switching themes.

If you use a lot of custom CSS, or want to use the same custom CSS with several themes, the unofficial CSS Snippets extension (https://github.com/LenAnderson/SillyTavern-CssSnippets) can help you manage and organize your custom CSS.

---

## Message Sound

To play your own custom sound on receiving a new message from bot, replace the following MP3 file in your SillyTavern folder:

`public/sounds/message.mp3`

Plays at 80% volume.

If the "Background Sound Only" option is enabled, the sound plays only if SillyTavern window is **unfocused**.

## Formulas Rendering

To enable math formulas rendering, use the LaTeX extension (https://github.com/SillyTavern/Extension-LaTeX). To get the extension, you need to install it via the "Download Extensions & Assets" menu in SillyTavern.

Type your formulas in code blocks with `latex` or `asciimath` language identifiers for LaTeX and AsciiMath respectively. The extension uses KaTeX (https://katex.org/) for rendering.

<pre><code>```latex
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
```

```asciimath
int_{-oo}^{oo} e^{-x^2} dx = sqrt{pi}
```</code></pre>

**Deprecation notice**

The legacy `$` and `$$` wrapper syntax is no longer supported. Please use the following regex scripts to polyfill the old syntax:

* $$ - LaTeX (https://github.com/SillyTavern/Extension-LaTeX/raw/refs/heads/main/assets/$$_-_latex.json)
* $ - AsciiMath (https://github.com/SillyTavern/Extension-LaTeX/raw/refs/heads/main/assets/$_-_asciimath.json)

# SECTION: SillyTavern_Usage_User_Settings_Visual-Novel

# Visual Novel (VN) Mode

Visual Novel Mode is a special screen layout in SillyTavern that allows you to chat to characters with sprites (or their character card image) that resembles that of a visual novel like Doki Doki Literature Club, The Fruits of Grisaia, Fate: Stay/night and other famous VN games.

## Toggling Visual Novel Mode

### Enabling Visual Novel Mode

Visual Novel Mode comes built in with SillyTavern and can be toggled by going to *User Settings* (User Settings Icon) and checking **Visual Novel Mode** below *No Text Shadows*.

### Disabling Visual Novel Mode

Disabling Visual Novel Mode is the same steps as enabling it. Untoggle Visual Novel Mode and you should be back to the normal chat screen itself.

**Regarding VN Mode with VN Extensions**

Some extensions (like the Prome VN Extension) will toggle 'Visual Novel Mode' on if you use their own respective VN modes. Enabling/Disabling VN Mode from the *User Settings* menu will also affect these extensions as well.

**## The Visual Novel UI**

In Visual Novel Mode, the UI is altered slightly in order to accommodate character sprites (or the character card image) which is shown in the center. In a group chat with multiple characters however, the character sprites will spread themselves out, accommodating for each other as shown below.

### VN Mode with MovingUI

To toggle MovingUI, go to *User Settings* and check on **MovingUI**. Do note that this feature **only** works on Desktops.

**If **MovingUI** is enabled in *User Settings*, the sprites (or character card image) can be moved around if you wish to move them around or place them in a more specific area on the screen.**

**Regarding Sprite Sizes**

If the size of your character sprites is relatively big it will be a challenge to try to move certain sprites around with MovingUI as the button to drag sprites around might be covered underneath an existing sprite. You will probably have to move them around a bit more than normal, especially if there is more characters on the screen for better placement.

**## Obtaining Character Sprites**

Obtaining character sprites can be done by browsing the internet for existing sprites, for say, an existing character from a Visual Novel or a game that uses a Visual Novel feature such as DDLC or CounterSide. If the character you desire sprites from does not come with sprites already, you have several options remaining.

1. Search the character post for any sprite ZIP package or link to a sprite pack.

    Some bot creators may release their bots with a sprite pack (either within the same post or in a sprites channel). Search those posts if someone hasn't made sprites of the character you want already.

**2. Create your own using LoRAs and Stable Diffusion.**

    Generating sprites from scratch is time-consuming (especially if no LoRAs exist for your character and/or for the Stable Diffusion model you want to use) and will require decent hardware in order to generate them, more so if you plan on making 28 sprite expressions than 6 and if you are using SDXL and/or upscaling sprites to a higher resolution.

**3. Use the character card image. It might not be like a sprite, but at least you have something to look at on-screen. However, multiple character cards cannot be used in VN mode.**

**Character Card Images with the Prome Visual Novel Extension**

    With the Prome Visual Novel Extension 1.0.6+, there is a feature called `Emulate Character Card as Sprite` that allows you to have a group chat with both sprite and non-sprite characters by using their character card as a sprite in chat.

**## VN Extensions**

### Prome Visual Novel Extension

The Prome Visual Novel Extension is an endorsed third-party extension from Bronya Rand and Prometheus that enhances the visual novel experience in SillyTavern even further with features such as Letterbox Mode which makes the visual novel UI more "cinematic", Focus Mode with Darken Character Sprites, Traditional VN Mode where only the last message in chat appears in chat and more planned to come!

|                              Letterbox Mode                              |                          Traditional VN Mode                           |
|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|

|                 Hide Sheld (Message Box)                  |                      Focus Mode (w/ Darken Sprites)                      |
|:---------------------------------------------------------:|:------------------------------------------------------------------------:|

To install the Prome Visual Novel Extension, you can either install by going to `Download Extensions & Assets` and finding *Prome Visual Novel Extension*, or follow the installation instructions on the Prome Visual Novel Extension (https://github.com/Bronya-Rand/Prome-VN-Extension?tab=readme-ov-file#installation-and-usage) Github page. Adjusting Prome's settings can be found either in *Extensions* -> **Prome (Visual Novel Extension)** or via the 🪄 (Wand) menu.

# SECTION: SillyTavern_Usage_welcome-assistants

# Welcome Page Assistants

SillyTavern features a Welcome Screen that can greet you with a designated "Assistant" character. This screen appears when you launch SillyTavern without an active chat or after you close your last chat session.

If you don't see a Welcome Screen on app startup, make sure the "Auto-Load Last Chat" option is disabled in the "Chat/Message Handling" section of the **<i class="fa-solid fa-user-cog"></i> User Settings** panel. If this option is enabled, SillyTavern will automatically load your last chat instead of showing the Welcome Screen.

**## The Welcome Screen**

When no chat is active, the Welcome Screen provides several useful elements:

* **SillyTavern Version:** Displays the application's logo and current version.
* **Quick Links:** Easy access to:
  * **Docs:** Opens the official SillyTavern documentation (you're already here!).
  * **GitHub:** Takes you to the SillyTavern GitHub repository (<https://github.com/SillyTavern/SillyTavern>).
  * **Discord:** Provides a link to the official SillyTavern Discord server (<https://discord.gg/sillytavern>).
* **Temporary Chat Button:** Allows you to quickly start a new, temporary chat session with the default neutral assistant, which won't be saved to your chat history unless you explicitly save it.
* **Recent Chats Section:** Lists your recent conversations for quick access. You can:
  * Show or hide this section.
  * Expand the list if more than 3 chats are available (up to 15 recent chats).

## Temporary Chat

Due to a technical limitation, the Temporary Chat feature will not use your customized Welcome Page Assistant. It will always start an empty chat without any additional prompts or character information.

**The Temporary Chat button allows you to quickly start a new chat session without saving it to your chat history. This is useful for testing or casual conversations without cluttering your saved chats. This chat will be deleted as soon as you close it or switch to another chat.**

* **Save** button will allow you to export the temporary chat as a JSONL file, which you can then import later.
* **Load** button will allow you to restore a previously saved temporary chat file.

## What is a Welcome Page Assistant?

A Welcome Page Assistant is a character you choose to be featured on the Welcome Screen. This allows for a personalized greeting and a quick way to start a chat with a familiar character right from the start.

### Setting and Unsetting an Assistant

You can choose any of your characters to act as your Welcome Page Assistant.

**To set an assistant:**

1. Navigate to the **Character Management** panel (usually found in the right-hand sidebar via the <i class="fa-solid fa-address-card"></i> icon).
2. Find the character you wish to set as your assistant in the list.
3. Click on "More..." and select **"Set / Unset as Welcome Page Assistant"** from the dropdown menu.
4. A small icon (<i class="fa-solid fa-user-graduate"></i>) will appear next to the character's name, indicating they are now your active Welcome Page Assistant.

**To unset an assistant:**

1. Go to the Character Management panel.
2. Locate your current Welcome Page Assistant (they will have the <i class="fa-solid fa-user-graduate"></i> icon).
3. Click on "More..." and select **"Set / Unset as Welcome Page Assistant"** again.
4. The character will no longer be your assistant, and the <i class="fa-solid fa-user-graduate"></i> icon will disappear.
5. SillyTavern will revert to using the Default Assistant (see below).

### Interacting with the Assistant

Once the Welcome Screen is displayed with your chosen assistant, simply type your message into the chat input bar at the bottom of the screen and press Enter or click the send button. This will start a new chat session with your Welcome Page Assistant.

To open a previous chat with the assistant, use the Recent Chats section or find the chat in the **Manage chat files** dialog (accessible via the **<i class="fa-solid fa-bars"></i> Options** menu).

## Default Assistant

SillyTavern will automatically create a default character named "Assistant" when you interact with the Welcome Screen for the first time. This character serves as a fallback option if you haven't set a specific character as your Welcome Page Assistant.

The default assistant doesn't have any specific prompts attached to it, and you're free to customize it as you like (e.g. renaming, adding a picture, or setting a personality).

* If you haven't explicitly set a character as your Welcome Page Assistant, this default assistant will be used.
* If you unset your chosen assistant, the system will revert to this default assistant.
* If a character you had set as an assistant is deleted, the system will also revert to the default assistant.

**Note:** You cannot "unset" the default system assistant in the same way you unset a character you've chosen. To change from the default assistant, you must set one of your other characters as the assistant.

# SECTION: SillyTavern_Usage_worldinfo

# World Info

**World Info (also known as Lorebooks or Memory Books) is a powerful tool available in ST to insert prompts dynamically into your chat to help guide the AI replies.**

Commonly, World Info (WI for short) is used to  enhance the AI's understanding of the details in your fictional world, however you could use a World Info entry to insert ANYTHING that you would like to insert into the prompt.

It functions like a dynamic dictionary that only inserts relevant information from World Info entries when keywords associated with the entries are present in the message text.

The SillyTavern engine activates and seamlessly integrates the appropriate lore into the prompt, providing background information to the AI.

*It is important to note that while World Info helps guide the AI toward the desired content, it does not guarantee its appearance in the generated output messages. That depends on how good your model is at making use of additional information!*

## Pro Tips

* The World Info engine is a very powerful prompt management tool. Don't fixate on adding character lore alone, feel free to experiment.
* Activation keywords, titles, and other information that is not in the **Content** field is not inserted into context, so each World Info entry should have a comprehensive, standalone description.
* To create rich and detailed world lore, entries can be interlinked and reference one another by using recursive activation. See more on Recursion below.
* SillyTavern offers flexible context budgeting for inserted background information. To conserve prompt tokens, it is advisable to keep entry contents concise.

## Further reading

* World Info Encyclopedia (https://rentry.co/world-info-encyclopedia): Exhaustive in-depth guide to World Info and Lorebooks. By kingbri, Alicat, Trappu.

## Character Lore

Optionally, World Info files can be assigned to a character to serve as dedicated lore sources across all chats with that character (including groups).

One primary World Info can be bound to the character. To do that, navigate to the Character Management panel and click the globe button, then pick World Info from a dropdown list and click "Ok". When exporting the character, this file will also get embedded in the character card data.

To unbind, change, or assign additional World Info files as character lore, shift-click the globe button or click "More..." then "Link World Info". Note that only the primary World Info file gets exported with the character.

### Character Lore Insertion Strategy

When generating an AI reply, entries from the character World Info will be combined with the entries from a global World Info selector using one of the following strategies:

#### Sorted Evenly (default)

All entries will be sorted according to their Insertion Order as if they were a part of one big file, ignoring the source.

#### Character Lore First

Entries from the Character World Info would be included first by their Insertion Order, then entries from the Global World Info.

#### Global Lore First

Entries from the Global World Info would be included first by their Insertion Order, then entries from the Character World Info.

### World Info Entry

#### Key

A list of keywords that trigger the activation of a World Info entry. Keys are not case-sensitive by default (this is configurable).

##### Regular Expression (Regex) as Keys

Keys allow a more flexible approach to matching by supporting regex. This makes it possible to match more dynamic content with optional words or characters, spacing, and all the other utilities that regex provides.  
If a defined key is a valid regex (Javascript regex style, with `/` as delimiters. All flags are allowed), it will be treated as such when checking whether an entry should be triggered. Multiple regexes can be entered as separate keys and will work alongside each other. Inside a regex, commas are possible. Plaintext keys do not support commas, as they are treated as key separators.  

An example of a use-case for advanced regex matching:  
An entry/instruction that should be inserted, when char is doing a weather-related action

```js
/(?:{{char}}|he|she) (?:is talking about|is noticing|is checking whether|observes) (?:the )?(rainy weather|heavy wind|it is going to rain|cloudy sky)/i
```

For more information on Regex syntax and possibilities: Regular expressions - JavaScript | MDN (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)

###### Advanced Regex Per-Message Matching

ST prefixes every chat message in the WI scan buffer with `character name:` and after v1.12.6, prepends them using the character value 1 (`\x01`).  
This means you can match specific input or output from a certain character using a regex tied to that separation character.

For example, to match only the user saying "hello", you could use the following regex:

```js
/\x01{{user}}:[^\x01]*?hello/
```

##### Key Input

There are two modes to enter keywords, each with a slightly different UI. In ⌨️ *plaintext mode* (default), keys can be entered as a comma-separated list in a single text field. Regexes can be included too, but they don't have any special highlighting. In ✨ *fancy mode*, the keys appear as separate elements and regexes will be highlighted as such. The control supports editing and deleting keys. The mode can be switched via the inline button inside the input control.

#### Optional Filter

Comma-separated list of additional keywords in conjunction with the primary key.
If no arguments are provided, this flag is ignored.
Supports logic for AND ANY, NOT ANY, or NOT ALL

1. AND ANY = Activates the entry only if the primary key and Any one of the optional filter keys are in scanned context.
2. AND ALL = Activates the entry only if the primary key and ALL of the optional filter keys are present.
3. NOT ANY = Activates the entry only if the primary key and None of the optional filter keys are in scanned context.
4. NOT ALL = Prevents activation of the entry despite primary key trigger, if all of the optional filters are in scanned context.

These keys also support regex.

#### Entry Content

The text that is inserted into the prompt upon entry activation.

#### Insertion Order

Numeric value. Defines a priority of the entry if multiple were activated at once. Entries with larger order numbers will be inserted closer to the end of the context as they will have more impact on the output. For example, an entry with Order number 100 will appear in the context before an entry with Order number 250.

#### Insertion Position

* **Before Char Defs:** World Info entry is inserted before the character's description and scenario. Has a moderate impact on the conversation.
* **After Char Defs:** World Info entry is inserted after the character's description and scenario. Has a greater impact on the conversation.
* **Before Example Messages:** The World Info entry is parsed as an example dialogue block and inserted before the examples provided by the character card.
* **After Example Messages:** The World Info entry is parsed as an example dialogue block and inserted after the examples provided by the character card.
* **Top of AN:** World Info entry is inserted at the top of Author's Note content. Has a variable impact depending on the Author's Note position.
* **Bottom of AN:** World Info entry is inserted at the bottom of Author's Note content. Has a variable impact depending on the Author's Note position.
* **@ D:** World Info entry is inserted at a specific depth in the chat (Depth 0 being the bottom of the prompt).
  * ⚙️ - as a system role message
  * 👤 - as a user role message
  * 🤖 - as an assistant role message
* **Outlet:** World Info entry is not injected automatically. Instead, its content is stored under a named outlet so you can decide exactly where it appears in the prompt by calling it with the `{{outlet::Name}}` macro.

Example Message entries will be formatted according to the prompt-building settings: Instruct Mode or Chat Completion prompt manager. They also follow the Example Messages Behavior rules: being gradually pushed out on full context, always kept, or disabled altogether.

If your Author's Note is disabled (Insertion Frequency = 0), World Info entries in A/N positions will be ignored!

#### Outlet Name

When the **Outlet** insertion position is selected, an additional **Outlet Name** field becomes available for the entry. The name that you provide here groups entries together and defines the token that you will use to pull them into the prompt manually.

Use the `{{outlet::YourName}}` macro in the Prompt Manager or Advanced Formatting prompt fields. When the prompt is built, the macro is replaced with the combined content of every World Info entry that shares the same outlet name, separated by newlines, sorted by their Insertion Order value.

If an outlet entry is missing a name it will be skipped during generation, so make sure to fill in the field. Outlet names support autocomplete based on the names you have already used to make it easy to reuse consistent labels.

##### Limitations and caveats

* Placing outlet macros inside World Info entries is not supported and will not work. This conflicts with the evaluation order of World Info and may lead to infinite loops.
* Nesting outlets is not supported. You cannot place an outlet macro inside another outlet's content. Same as above, this may lead to infinite loops.
* Character card fields (Description, Personality, Scenario, etc.) cannot expand outlets. Those fields are parsed early so they can act as additional matching sources for World Info triggers, which means outlets are not available when their text is processed. Use another macro-aware field if you need to place outlet content in the prompt body instead.
* The Author's Note editor also cannot resolve outlets. To place outlet content around the Author's Note, assign the entries to **Top of AN** or **Bottom of AN** insertion positions instead of relying on the macro.
* Outlet names are case-sensitive. The `{{outlet::}}` macro must use exactly the same capitalization as the entry's **Outlet Name**, otherwise no content is returned.
* Leading or trailing spaces in an outlet name are ignored when you call the macro, so names saved with extra whitespace will not match. Avoid padding names so they can be resolved correctly.
* Outlet macros that have no content assigned to them will be replaced with an empty string.

#### Entry Title / Memo

A text field for your convenience to label your entries, which is not utilized by the AI or any of the trigger logics.

If empty, can be backfilled using the entries' first key by clicking on the "Fill empty memos" button.

#### Strategy

1. 🔵 (Blue Circle) = The entry would always be present in the prompt.
2. 🟢 (Green Circle) = The entry will be triggered only in the presence of the keyword.
3. 🔗 (Chain Link) = The entry is allowed to be inserted by embedding similarity.

Each Entry also has a toggle that allows you to enable or disable the entry.

#### Probability (Trigger %)

This value acts like an additional filter that adds a chance for the entry NOT to be inserted when it is activated by any means (constant, primary key, recursion).

1. Probability = 100 means that the entry will be inserted on every activation.
2. Probability = 50 means that the entry will be inserted with a 1:1 chance.
3. Probability = 0 means that the entry will NOT be inserted (essentially disabling it).

Use this to create random events in your chats. For example, every message could have a 1% chance of waking up an Elder God if its name is mentioned in the message.

#### Inclusion Group

Inclusion groups control how entries are selected when multiple entries with the same group label are triggered simultaneously. If multiple entries having the same group label were activated, only one will be inserted into the prompt.

By default, the chosen entry is selected randomly based on their Group Weight (default is 100 points) — the higher the number, the higher the probability of selection. This allows for a random selection among the triggered entries, adding an element of surprise and variety to interactions.

A single entry can be part of multiple inclusion groups if they are defined as a comma-separated list. The same logic as explained above will apply. If that entry is triggered, it will *disable* all other entries that are part of any of its groups. Therefore, if any of the groups are activated, this entry will not be activated.

#### Prioritize Inclusion

To provide more control over which entries are activated via Inclusion Group, you can use the 'Prioritize Inclusion' setting. This option allows you to specify deterministically which entry to choose instead of randomly rolling Group Weight chances.

If multiple entries having the same group label and this setting turned on were activated, the one with the highest 'Order' value will be selected. This is useful for creating fallback sequences via inclusion groups. For example to prioritize low-depth entries with more emphasis, or to choose a specific instruction on setting the scene over another if both are valid.

#### Use Group Scoring

When this setting is enabled globally or per entry, the number of activated entry keys determines the group winner selection. Only the subset of a group with the highest number of key matches will be left to be activated by Group Weight or Inclusion Priority - the rest will be deactivated and removed from the group.

Use this to give more specificity for individual entries in large groups. For example, they can have a common key and a specific key. A random entry will be inserted when a specific key is not provided, and vice versa.

The score calculation logic for primary keys is 1 match = 1 point.

For secondary keys, the interaction depends on the chosen Selective Logic:

1. AND ANY: 1 secondary match = 1 point.
2. AND ALL: 1 point for every secondary key if they all match.
3. NOT ANY and NOT ALL: no change.

Example:

* Entry 1. Keys: song, sing, Black Cat. Group: songs
* Entry 2. Keys: song, sing, Ghosts. Group: songs

The input `sing me a song` can activate either entry (both activated 2 keys), but `sing me a song about Ghosts` will activate only Entry 2 (activated 3 keys).

#### Automation ID

Allows to integrate World Info entries with STscripts from Quick Replies extension. If both the quick reply command and the WI entry have the same Automation ID, the command will be executed automatically when the entry with a matching ID is activated.

Automations are executed in the order they are triggered, adhering to your designated sorting strategy, combining the Character Lore Insertion Strategy with the 'Priority' sorting. Which leads to Blue Circle entries processed first, followed by others in their specified 'Order'. Recursively triggered entries will be processed after in the same order.

The script command will run only once if multiple entries with the same Automation ID are activated.

#### Character Filter

A list of character names for which this entry can be activated. If this list is not empty, the entry will only be activated for characters whose names are on the list. When a tag is selected, the entry will only be activated for characters that have that specific tag.

"Exclude" mode inverts the filter, meaning that the entry will be activated for all characters except those that are added to the list or that have the selected tag(s).

#### Triggers

The generation types for which this World Info entry can be activated. If nothing is selected, the entry can be activated for all generation types. If one or more are selected, the entry will only be activated for those specific generation types:

* **Normal:** Regular message generation request.
* **Continue:** When the Continue button is pressed.
* **Impersonate:** When the Impersonate button is pressed.
* **Swipe:** When the generation is triggered by swiping.
* **Regenerate:** When the Regenerate button is pressed in solo chats.
* **Quiet:** Background generation requests, usually triggered by extensions or STscript commands.

**The "Regenerate" trigger is not available in group chats as it uses different regeneration logic: all messages from the last reply are deleted, and messages are queued using the "Normal" generation type according to the chosen Group reply strategy.**

**#### Additional matching sources**

By default World Info Entries are matched only against content from the current conversation. These options allow you to match the entry against different character information that does not show up in the chat, or even persona information. This is useful when you want to have a wide range of entries that are to be used between several characters but don't want to have to manage large lists of tags, or don't want to have to update character filter lists every time you create a new one. This also allows you to match entries based on the persona you have active.

* **Character Description**: Matches against the character description.
* **Character Personality**: Matches against the character personality summary, found under Advanced Definitions.
* **Scenario**: Matches against the character specified scenario, found under Advanced Definitions.
* **Persona Description**: Matches against the current selected persona's description.
* **Character's Note**: Matches against the character's note, which can be found under Advanced Definitions.
* **Creator's Notes**: Matches against the character creator's notes, which can be found under Advanced Definitions. The creator's notes are usually not included in the prompt.

## Vector Storage Matching

The Vector Storage extension provides an alternative to keyword matching by using the similarity between the recent chat messages and World Info entry contents.

To enable and use this, the following prerequisites need to be met:

1. Vector Storage extension is enabled and is configured to use one of the available embedding sources.
2. The "Enable for World Info" checkbox is ticked in the Vector Storage extension settings.
3. Either the World Info entries that are allowed for keyless matching have the "Vectorized" (🔗) status or the "Enabled for all entries" option is checked in the Vector Storage settings.

The choice of the vectorization model in the extension and the theoretical meaning behind the term "embeddings" won't be covered here. Check out the Data Bank guide if you require more info on this topic.

Vector Storage matching adheres to this set of rules:

* The maximum number of entries that are allowed to be matched with the Vector Storage can be adjusted with the "Max Entries" setting. This number only sets the limit and does not influence the token budget set in the activation settings for World Info. All of the budgeting rules still apply.
* This feature only replaces the check for keywords. All additional checks must be met for the entry to be inserted: trigger%, character filters, inclusion groups, etc.
* The "Scan Depth" setting from Activation Settings or entry overrides is not used. The Vector Storage "Query messages" value is utilized instead to get the text to match against. This allows for a configuration like "Scan Depth" set to 0, so no regular keyword matches will be made, but entries still can be activated by vectors.
* A "Vectorized" status is only an additional marker. The entry would still behave like a normal, enabled, non-constant record that will be activated by keywords if they are set. Remove the keywords if you want them to be activated only by vectors.

**Note**

Since the retrieval quality depends entirely on the outputs of the embedding model, it's impossible to predict exactly what entries will be inserted. If you want deterministic and predictable results, stick to keyword matching.

**## Timed Effects**

Usually, World Info evaluation is stateless, meaning that the result of the evaluation is the same, only depending on the current chat context. However, with the introduction of Timed Effects, you can create entries that have an activation delay, stay active after being triggered, or can't be triggered after the activation.

### Timed Effects Rules

1. The time frames for the effects are measured in messages (not pairs of messages/exchanges), with 0 meaning there is no effect.
2. Effects only apply in the chat where the entry was activated. Branches inherit the state of the parent chat.
3. Active timed effects are removed if the chat doesn't advance, e.g. if the last message was swiped or deleted.
4. Making any changes to the entry that is currently on timed effect will cause the effect to be forcibly removed.
5. Consequent triggering of keywords does not refresh the effect duration if it's already active.

### Types of Timed Effects

1. Sticky - the entry stays active for N messages after being activated. Stickied entries ignore probability checks on consequent scans until they expire.
2. Cooldown - the entry can't be activated for N messages after being activated. Can be used together with sticky: the entry goes on cooldown when the sticky duration ends.
3. Delay - the entry can't be activated unless there are at least N messages in the chat at the moment of evaluation.
    * Delay = 0 -> The entry can be activated at any time.
    * Delay = 1 -> The entry can't be activated if the chat is empty (no greeting).
    * Delay = 2 -> The entry can't be activated if there is zero or only one message in the chat, etc.

### Timed Effects Example

Entry configuration: sticky = 3, cooldown = 2, delay = 2.

```txt
Message 0: delay
Message 1: entry activated
Message 2: sticky
Message 3: sticky
Message 4: sticky
Message 5: cooldown
Message 6: cooldown
Message 7: entry can be activated again
```

## Activation Settings

Collapsible menu at the top of the World Info screen.

### Scan Depth

> Can be overridden on an entry level.

Defines how many messages in the chat history should be scanned for World Info keys.

* If set to 0, then only recursed entries and Author's Note are evaluated.
* If set to 1, then SillyTavern only scans the last message.
* 2 = two last messages, etc.

### Include Names

Defines if the names of the chat participants should be included in the scanned text buffer as message prefixes. This allows activating entries that use names as keywords without directly mentioning the names in messages.

See an example of the text to be scanned below, assuming the chat participants are named Alice and Bob.

Enabled (default):

```txt
Alice: Hello! Good to see you.
Bob: How is the weather today?
```

Disabled:

```txt
Hello! Good to see you.
How is the weather today?
```

### Context % / Budget

**Defines how many tokens could be used by World Info entries at once.**
You can define a threshold relative to your API's max-context settings (Context %) or an objective token threshold (Budget)

If the budget is exhausted, then no more entries are activated even if the keys are present in the prompt.

Constant entries will be inserted first. Then entries with larger order numbers.

Entries inserted by directly mentioning their keys have higher priority than those that were mentioned in other entries' contents.

### Min Activations

**This setting is mutually exclusive with Max Recursion Steps.**

Minimum Activations: If set to a non-zero value, this will disregard the limitation of "scan-depth", seeking all of the chat log backward from the latest message for keywords until as many entries as specified in min activations have been triggered. This will still be limited by the Max Depth setting or your overall Budget cap.

*Additional scan sweeps triggered by Min Activations will not check entries added by recursion on previous steps. Only chat messages and extension prompts can trigger these additional activations. However, the entries activated by Min Activations can trigger other entries as usual.*

### Max Depth

Maximum Depth to scan for when using the Min Activations setting.

### Recursive scanning

Recursive scanning allows for entries to activate other entries or be activated by others, enabling complex interactions and dependencies between different World Info entries. This feature can significantly enhance the dynamic nature of your creative scenarios.  
Whether recursive scanning is enabled can be controlled with the global setting **Recursive Scan**.  
There are three options available to control recursion for each entry:

8 **Non-recursable**: When this checkbox is selected, the entry will not be activated by other entries. This is useful for static information that should not change or be influenced by other world info entries.
  
* **Prevent further recursion**: Selecting this option ensures that once this entry is activated, it will not trigger any other entries. This is helpful to avoid unintended chains of activations.

* **Delay until recursion**: This entry will only be activated during recursive checks, meaning it won't be triggered in the initial pass but can be activated by other entries that have recursion enabled. Now, with the added **Recursion Level** for those delays, entries are grouped by levels. Initially, only the first level (smallest number) will match. Once no matches are found, the next level becomes eligible for matching, repeating the process until all levels are checked. This allows for more control over how and when deeper layers of information are revealed during recursion, especially in combination with criteria as NOT ANY or NOT ALL combination of key matches.

**Entries can activate other entries by mentioning their keywords in the content text.**

For example, if your World Info contains two entries:

```txt
Entry #1
Keyword: Bessie
Content: Bessie is a cow and is friends with Rufus.
```

```txt
Entry #2
Keyword: Rufus
Content: Rufus is a dog.
```

**Both** of them will be pulled into the context if the message text mentions **just Bessie**.

### Max Recursion Steps

**This setting is mutually exclusive with Min Activations.**

When set to zero, recursion nesting is only limited by your prompt budget. When set to a non-zero value, limits the total number of scan sweeps to desired maximum "nesting level".

Example values:

* 1 effectively disables recursion as the check stops after the first step.
* 2 can only activate recursive entries once.
* 3 can trigger recursion twice...

### Case-sensitive keys

> Can be overridden on an entry level.

**To get pulled into the context, entry keys need to match the case as they are defined in the World Info entry.**

This is useful when your keys are common words or parts of common words.

For example, when this setting is active, keys 'rose' and 'Rose' will be treated differently, depending on the inputs.

### Match whole words

> Can be overridden on an entry level.

Entries with keys containing only one word will be matched only if the entire word is present in the search text. Enabled by default.

For example, if the setting is enabled and the entry key is "king", then text such as "long live the king" would be matched, but "it's not to my liking" wouldn't.

**Important:** this setting can have a detrimental effect when used with languages that don't use whitespace to separate words (e.g. Japanese or Chinese). If you write entries in these languages, it is advised to keep it off.

### Alert on overflow

Shows an alert if the activated World Info exceeds the allocated token budget.

# SECTION: SillyTavern_Administration_config-yaml

# Configuration File

**Disclaimer**

This documentation may be obsolete, incomplete, or incorrect. Please refer to the default config.yaml (https://github.com/SillyTavern/SillyTavern/blob/release/default/config.yaml) in your installation for the most up-to-date list of settings.

**WARNING: DO NOT EDIT THE DEFAULT CONFIG DIRECTLY. THIS WON'T HAVE ANY POSITIVE EFFECT. EDIT ITS COPY IN THE REPOSITORY ROOT INSTEAD.**

**`config.yaml` is the main configuration file for the SillyTavern server which you can find in the repository root directory after completing the installation. It is a YAML file that contains various settings, such as network, security, and backend-specific options. **The changes made to this file will take effect after restarting the server.****

New settings that are added upstream are automatically populated with default values when you run `npm install` (specifically, the `post-install.js` script) after updating the repository. You can then modify these settings as needed.

For nested settings, dot notation is used to indicate the hierarchy. For example, `protocol.ipv6: false` refers to the `ipv6` setting under the `protocol` section with a value of `false`.

```yaml
protocol:
  ipv6: false
```

## Command-Line Arguments

You can pass command-line arguments when starting the SillyTavern server to override some settings in config.yaml.

### Examples

```shell
node server.js --port 8000 --listen false
# or
npm run start -- --port 8000 --listen false
# or (Windows only)
Start.bat --port 8000 --listen false
```

### Supported arguments

None of the arguments are required. If you don't provide them, SillyTavern will use the settings in `config.yaml`.

| Option                          | Description                                                          | Type     |

|---------------------------------|----------------------------------------------------------------------|----------|
| `--version`                     | Shows the version number                                             | boolean  |
| `--global`                      | Forces the use of system-wide paths for application data             | boolean  |
| `--configPath`                  | Overrides the path to the config.yaml file (standalone mode only)    | string   |
| `--dataRoot`                    | Sets the root directory for data storage (standalone mode only)      | string   |
| `--port`                        | Sets the port under which SillyTavern will run                       | number   |
| `--listen`                      | Makes SillyTavern listen on all network interfaces                   | boolean  |
| `--whitelist`                   | Enables whitelist mode                                               | boolean  |
| `--basicAuthMode`               | Enables basic authentication                                         | boolean  |
| `--enableIPv4`                  | Enables the IPv4 protocol                                            | boolean  |
| `--enableIPv6`                  | Enables the IPv6 protocol                                            | boolean  |
| `--listenAddressIPv4`           | Specifies the IPv4 address to listen on                              | string   |
| `--listenAddressIPv6`           | Specifies the IPv6 address to listen on                              | string   |
| `--dnsPreferIPv6`               | Prefers IPv6 for DNS                                                 | boolean  |
| `--ssl`                         | Enables SSL                                                          | boolean  |
| `--certPath`                    | Sets the path to your certificate file                               | string   |
| `--keyPath`                     | Sets the path to your private key file                               | string   |
| `--browserLaunchEnabled`        | Automatically launches SillyTavern in the browser                    | boolean  |
| `--browserLaunchHostname`       | Sets the browser launch hostname                                     | string   |
| `--browserLaunchPort`           | Overrides the port for browser launch                                | string   |
| `--browserLaunchAvoidLocalhost` | Avoids using 'localhost' for browser launch in auto mode             | boolean  |
| `--corsProxy`                   | Enables the CORS proxy                                               | boolean  |
| `--requestProxyEnabled`         | Enables the use of a proxy for outgoing requests                     | boolean  |
| `--requestProxyUrl`             | Sets the request proxy URL (HTTP or SOCKS protocols)                 | string   |
| `--requestProxyBypass`          | Sets the request proxy bypass list (space-separated list of hosts)   | array    |
| `--disableCsrf`                 | Disables CSRF protection (NOT RECOMMENDED)                           | boolean  |

## Environment Variables

Configuration may also be set via environment variables, which will override the values in the `config.yaml` file.

The environment variables should be prefixed with `SILLYTAVERN_` and use uppercase letters for the setting names. For example, the `dataRoot` setting can be overridden with the `SILLYTAVERN_DATAROOT` environment variable.

The nested settings should be separated by underscores. For example, `protocol.ipv6` can be overridden with the `SILLYTAVERN_PROTOCOL_IPV6` environment variable.

Configurations that expect arrays or objects should be JSON-stringified. For example, to override the `whitelist` setting with the `SILLYTAVERN_WHITELIST` environment variable, you should set it as a JSON string: `SILLYTAVERN_WHITELIST='["127.0.0.1", "::1"]'`.

**If you are using Node.js v20 or later, you can also store environment variables in a `.env` file and pass it to the server with the `--env-file` flag. For example, to use the `.env` file located in the repository root, you can start the server with the following command:**

```bash
node --env-file=.env server.js
```

Alternatively, pass the environment variables directly via the command line:

```bash
SILLYTAVERN_LISTEN=true SILLYTAVERN_PORT=8000 node server.js
```

See more about using environment variables in the Node.js documentation (https://nodejs.org/en/learn/command-line/how-to-read-environment-variables-from-nodejs).

## Data Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `dataRoot` | Root directory for user data storage (standalone mode only) | `./data` | Any valid directory path |
| `skipContentCheck` | Skip checks for new default content | `false` | `true`, `false` |
| `enableDownloadableTokenizers` | Enable on-demand tokenizer downloads | `true` | `true`, `false` |
| `whitelistImportDomains` | List of trusted domains for importing web-hosted character cards and assets | See here (https://github.com/SillyTavern/SillyTavern/blob/d118eee014330c37978cc0226f4ca74a1f321eea/default/config.yaml#L220) | Array of strings |

## Logging Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|------------------|
| `logging.minLogLevel` | Minimum log level to display in the terminal | `0` (DEBUG) | (DEBUG = 0, INFO = 1, WARN = 2, ERROR = 3) |
| `logging.enableAccessLog` | Write server access logs to a file and the console | `true` | `true`, `false` |

## Network Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `listen` | Enable listening for incoming connections | `false` | `true`, `false` |
| `port` | Server listening port | `8000` | Any valid port number (1-65535) |
| `heartbeatInterval` | Interval in seconds to write a heartbeat file for Docker healthchecks. Set to 0 to disable | `0` | `0` (disabled), positive integer |
| `protocol.ipv4` | Enable listening on the IPv4 protocol | `true` | `true`, `false`, `auto` |
| `protocol.ipv6` | Enable listening on the IPv6 protocol | `false` | `true`, `false`, `auto` |
| `listenAddress.ipv4` | Listen on a specific IPv4 address | `0.0.0.0` | Valid IPv4 address |
| `listenAddress.ipv6` | Listen on a specific IPv6 address | `'[::]'` | Valid IPv6 address |
| `dnsPreferIPv6` | Prefer IPv6 for DNS resolution | `false` | `true`, `false` |

## SSL Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|------------------|
| `ssl.enabled` | Enable SSL/TLS encryption and HTTPS protocol | `false` | `true`, `false` |
| `ssl.keyPath` | Path to SSL private key (relative to the server directory) | `"./certs/privkey.pem"` | Valid file path |
| `ssl.certPath` | Path to SSL certificate (relative to the server directory) | `"./certs/cert.pem"` | Valid file path |
| `ssl.keyPassphrase` | Passphrase for the SSL private key. Leave empty if not required | `""` | Any string |

## Security Configuration

### IP Whitelisting

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `whitelistMode` | Enable IP whitelist filtering | `true` | `true`, `false` |
| `enableForwardedWhitelist` | Check forwarded headers for whitelisted IPs | `true` | `true`, `false` |
| `whitelist` | List of allowed IP addresses | `["::1", "127.0.0.1"]` | Array of valid IP addresses |
| `whitelistDockerHosts` | Automatically whitelist Docker host IPs | `true` | `true`, `false` |

### Host Whitelisting

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `hostWhitelist.enabled` | Enable host whitelisting | `false` | `true`, `false` |
| `hostWhitelist.scan` | Log incoming requests from untrusted hosts | `true` | `true`, `false` |
| `hostWhitelist.hosts` | List of trusted hostnames | `[]` | Array of valid hostnames |

### Security Overrides

**DISABLING SECURITY MEASURES IS HIGHLY DISCOURAGED. PLEASE MAKE SURE YOU UNDERSTAND WHAT YOU ARE DOING BEFORE MAKING CHANGES.**

| Setting | Description | Default | Permitted Values |

|---------|-------------|---------|------------------|
| `allowKeysExposure` | Allow unmasked API key exposure in the UI | `false` | `true`, `false` |
| `disableCsrfProtection` | Disable CSRF protection (not recommended) | `false` | `true`, `false` |
| `securityOverride` | Disable startup security checks (not recommended) | `false` | `true`, `false` |

## User Authentication

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `basicAuthMode` | Enable basic authentication | `false` | `true`, `false` |
| `basicAuthUser.username` | Basic auth username | `"user"` | Any string |
| `basicAuthUser.password` | Basic auth password | `"password"` | Any string |
| `enableUserAccounts` | Enable multi-user mode | `false` | `true`, `false` |
| `enableDiscreetLogin` | Hide the user list on the login screen | `false` | `true`, `false` |
| `sessionTimeout` | User session timeout in seconds | `-1` (disabled) | Any number (-1 to disable, 0 for browser close, >0 for timeout) |
| `perUserBasicAuth` | Use account credentials for basic auth | `false` | `true`, `false` |

### SSO Auto-Login

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|------------------|
| `sso.autheliaAuth` | Enable Authelia-based auto-login. See: SSO | `false` | `true`, `false` |
| `sso.authentikAuth` | Enable Authentik-based auto-login. See: SSO | `false` | `true`, `false` |

## Rate Limiting Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|------------------|
| `rateLimiting.preferRealIpHeader` | Use the X-Real-IP header instead of the socket IP for rate limiting | `false` | `true`, `false` |

## Request Proxy Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `requestProxy.enabled` | Enable proxy for outgoing requests | `false` | `true`, `false` |
| `requestProxy.url` | Proxy server URL | `null` | Valid proxy URL (e.g., `"socks5://username:password@example.com:1080"`) |
| `requestProxy.bypass` | Hosts to bypass the proxy | `["localhost", "127.0.0.1"]` | Array of hostnames/IPs |

## CORS Proxy Configuration

**An enabled CORS proxy may be required by some extensions. It is not required by any built-in features.**

| Setting | Description | Default | Permitted Values |

|---------|-------------|---------|-----------------|
| `enableCorsProxy` | Enable CORS proxy middleware | `false` | `true`, `false` |

## CORS Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `cors.enabled` | Enable or disable CORS middleware | `true` | `true`, `false` |
| `cors.origin` | Allowed origins. `"null"` matches the default browser file origin | `["null"]` | `"*"` (any origin), array of allowed origins |
| `cors.methods` | Allowed HTTP methods | `["OPTIONS"]` | Array of HTTP methods |
| `cors.allowedHeaders` | Allowed request headers | `[]` | Array of header names |
| `cors.exposedHeaders` | Exposed response headers | `[]` | Array of header names |
| `cors.credentials` | Allow credentials (cookies, authorization headers) | `false` | `true`, `false` |
| `cors.maxAge` | Preflight cache max age in seconds | `null` | `null`, positive integer |

## Browser Launch Configuration

> Previously known as "Autorun" settings.

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `browserLaunch.enabled` | Open the browser automatically on server startup | `true` | `true`, `false` |
| `browserLaunch.browser` | Browser to use for opening the URL | `"default"` | `"default"`, `"chrome"`, `"firefox"`, `"edge"`, `"brave"` |
| `browserLaunch.hostname` | Override the hostname for browser launch | `"auto"` | `"auto"`, any valid hostname (e.g., `"localhost"`, `"st.example.com"`) |
| `browserLaunch.port` | Override the port for browser launch | `-1` | `-1` (use server port), any valid port number |
| `browserLaunch.avoidLocalhost` | Avoid using 'localhost' in the launch URL | `false` | `true`, `false` |

## Performance Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|------------------|
| `performance.lazyLoadCharacters` | Lazy-load character data | `true` | `true`, `false` |
| `performance.useDiskCache` | Enable disk caching for character cards | `true` | `true`, `false` |
| `performance.memoryCacheCapacity` | Maximum memory cache capacity | `100mb` | Human-readable size (e.g., `100mb`, `1gb`) |

## Cache Buster Configuration

Requires localhost or a domain with HTTPS, otherwise will not work!

| Setting | Description | Default | Permitted Values |

|---------|-------------|---------|------------------|
| `cacheBuster.enabled` | Clear browser cache on first load or after uploading image files | `false` | `true`, `false` |
| `cacheBuster.userAgentPattern` | Only clear the cache for user agents matching the specified regex pattern. Example: `'firefox'` (case-insensitive). | `''` | Any valid regex string |

## Thumbnailing Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `thumbnails.enabled` | Enable thumbnail generation | `true` | `true`, `false` |
| `thumbnails.quality` | JPEG thumbnail quality | `95` | 0-100 |
| `thumbnails.format` | Image format for thumbnails | `jpg` | `jpg`, `png` |
| `thumbnails.dimensions.bg` | Background thumbnails size | `[160, 90]` | Array of two numbers (width, height) |
| `thumbnails.dimensions.avatar` | Avatar thumbnails size | `[96, 144]` |  Array of two numbers (width, height) |
| `thumbnails.dimensions.persona` | Persona thumbnails size | `[96, 144]` |  Array of two numbers (width, height) |

## Backup Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `backups.chat.enabled` | Enable automatic chat backups | `true` | `true`, `false` |
| `backups.chat.checkIntegrity` | Verify integrity of chat files before saving | `true` | `true`, `false` |
| `backups.common.numberOfBackups` | Number of backups to keep | `50` | Any positive integer |
| `backups.chat.throttleInterval` | Backup throttle interval (ms) | `10000` | Any positive integer |
| `backups.chat.maxTotalBackups` | Maximum total chat backups to keep | `-1` | Any positive integer or -1 |

## Extensions Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `extensions.enabled` | Enable UI extensions | `true` | `true`, `false` |
| `extensions.autoUpdate` | Auto-update extensions (if enabled by the extension manifest) | `true` | `true`, `false` |
| `extensions.models.autoDownload` | Enable automatic model downloads | `true` | `true`, `false` |
| `extensions.models.classification` | HuggingFace model ID for classification | `"Cohee/distilbert-base-uncased-go-emotions-onnx"` | Valid model ID |
| `extensions.models.captioning` | HuggingFace model ID for image captioning | `"Xenova/vit-gpt2-image-captioning"` | Valid model ID |
| `extensions.models.embedding` | HuggingFace model ID for embeddings | `"Cohee/jina-embeddings-v2-base-en"` | Valid model ID |
| `extensions.models.speechToText` | HuggingFace model ID for speech-to-text | `"Xenova/whisper-small"` | Valid model ID |
| `extensions.models.textToSpeech` | HuggingFace model ID for text-to-speech | `"Xenova/speecht5_tts"` | Valid model ID |

## Server Plugins

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `enableServerPlugins` | Enable server-side plugins | `false` | `true`, `false` |
| `enableServerPluginsAutoUpdate` | Attempt to automatically update server plugins on startup | `true` | `true`, `false` |

## API Integration Settings

### OpenAI Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `promptPlaceholder` | Default message for empty prompts | `"[Start a new chat]"` | Any string |
| `openai.randomizeUserId` | Randomize the user ID for API calls | `false` | `true`, `false` |
| `openai.captionSystemPrompt` | System message for caption completion | `""` | Any string |

### MistralAI Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `mistral.enablePrefix` | Enable reply prefilling. **The prefix will be echoed in the response** | `false` | `true`, `false` |

### Ollama Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `ollama.keepAlive` | Model keep-alive duration (seconds) | `-1` | `-1` (indefinite), `0` (immediate unload), positive integer |
| `ollama.batchSize` | Controls the "num_batch" (batch size) parameter of the generation request | `-1` | `-1` (model default), positive integer |

### Claude Configuration

****IMPORTANT!****

Use with caution and only when the prompt prefix is static and doesn't change between requests. \{\{random\}\} macro, lorebooks, vectors, summaries, etc. will likely invalidate the cache and you'll just waste money on cache misses. The provider may have a minimum prompt size requirement for caching. Behavior may be unpredictable and no guarantees can or will be made, please review the API documentation.

See: Prompt Caching (https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

| Setting | Description | Default | Permitted Values |

|---------|-------------|---------|-----------------|
| `claude.enableSystemPromptCache` | Enable system prompt caching | `false` | `true`, `false` |
| `claude.cachingAtDepth` | Enable message history caching | `-1` | `-1` (disabled), `0` or positive integer |
| `claude.extendedTTL` | Use 1h TTL instead of the default 5m. Note that this also increases the cost of the request. | `false` | `true`, `false` |

### Google Gemini Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `gemini.apiVersion` | API endpoint version (AI Studio only) | `v1beta` | `v1beta`, `v1alpha` |
| `gemini.thoughtSignatures` | Adds thought signatures to requests (if available). Only for Gemini 3 and above | `true` | `true`, `false` |
| `gemini.enableSystemPromptCache` | Enables caching of the system prompt (OpenRouter only) | `false` | `true`, `false` |
| `gemini.image.personGeneration` | See: <https://ai.google.dev/gemini-api/docs/imagen#imagen-configuration> | `allow_adult` | `dont_allow`, `allow_adult`, `allow_all` |

### DeepL Configuration

| Setting | Description | Default | Permitted Values |
|---------|-------------|---------|-----------------|
| `deepl.formality` | Translation formality level | `"default"` | `"default"`, `"more"`, `"less"`, `"prefer_more"`, `"prefer_less"` |

# SECTION: SillyTavern_Administration_index

# Administration

Despite following many security best practices, the SillyTavern server is not secure enough for exposure to the public internet.

**NEVER HOST ANY INSTANCES ON THE OPEN INTERNET WITHOUT ENSURING PROPER SECURITY MEASURES FIRST.**

**WE ARE NOT RESPONSIBLE FOR ANY DAMAGE OR LOSSES RESULTING FROM UNAUTHORIZED ACCESS DUE TO IMPROPER OR INADEQUATE SECURITY IMPLEMENTATION.**

**:::callout**

**config.yaml**

The main configuration file for SillyTavern. It contains various settings, such as network, security, and backend-specific options.

**:::callout**

**Multi-user**

To share your SillyTavern instance with others, you can create multiple user accounts. Each user has their own settings, extensions, and data. User accounts can also be password-protected.

**:::callout**

**Remote access**

You can access your SillyTavern instance from your phone, tablet, or another computer.

**:::callout**

**VPNs and Tunneling**

To access your SillyTavern instance from the internet, you can use a VPN or a tunneling service like Cloudflare Zero Trust, ngrok, or Tailscale.

**:::callout**

**Reverse proxying**

Enthusiasts can set up a reverse proxy to access their SillyTavern instance from the internet.

**## Security checklist**

**These are just recommendations. Please consult a web application security specialist before making your ST instance live.**

1. Keep your operating system and runtime software, such as Node.js, up to date. This ensures your system has the latest security patches and fixes, which helps prevent potential vulnerabilities.
2. Use a whitelist and a network firewall. Only allow trusted IP ranges to access the server.
3. Enable basic authentication. It acts as a "master password" before you can access the front-end app.
4. Alternatively, configure external authentication. Some known services for this are Authelia (https://www.authelia.com/) and authentik (https://goauthentik.io/). See the SSO guide for details.
5. Never leave admin accounts without passwords. The server will warn you on startup if you have any unprotected admin accounts.
6. Use the discreet login setting outside the local network. This hides the user list from potential outsiders.
7. Check the access logs often. They are written to the server console and to the `access.log` file and provide information about incoming connections, such as IP address and user agent.
8. Configure HTTPS. For a localhost server, you can generate and use a self-signed certificate. Otherwise, you may need to deploy a reverse-proxy web server such as Traefik (https://traefik.io/) or Caddy (https://caddyserver.com/docs/getting-started).
9. Configure and enable host whitelisting, especially if you're not using HTTPS encryption on a local network.

Find more information about secure proxying in the following guide: Reverse Proxying SillyTavern.

# SECTION: SillyTavern_Administration_multi-user

Multi-user mode allows several people to use one SillyTavern server. Each user has their own settings, extensions, and data. User accounts can also be password-protected.

User passwords provide basic privacy between users of a multi-user setup. They are not a security feature and should not be considered as such. All user data (including chat history, API keys, and other sensitive information) is stored in plain text on the server. It can be viewed and modified by anyone with access to the server's filesystem. **Do not use SillyTavern on a public server or with untrusted users.**

**## Configuration**

To enable and use the multi-user mode, edit the `config.yaml` file:

```yaml
# Enable multi-user mode
enableUserAccounts: true
# Enable discreet login mode: hides user list on the login screen
enableDiscreetLogin: true
```

1. When the user account setting is disabled, a `default-user` fallback admin account is utilized for storing the user data.
2. When the discreet login setting is disabled, a list of active users is displayed on the login screen. If enabled, a user must enter their handle manually.

You can't _delete_ the `default-user` account from the users list because it is used for serving the user data in case if `enableUserAccounts` is set to `false`. But you can _disable_ it to hide it from the list and disallow logins.

**## User handles**

A handle is the unique identifier of a user. It can consist only of lowercase letters, numbers, and dashes.

A path to the user data directory assumes using the following pattern: `%DATA_ROOT%/%USER_HANDLE%`.

Examples of valid user handles:

- default-user
- juan555
- flux-the-cat
- cool-guy1337

## Roles

- **Admin** - can manage (create, delete, modify) other users. Can install extensions for all users.
- **User** - can't manage other users. Can install extensions only for themselves.

Except for having admin panel access, both user roles are functionally identical and can use a full range of SillyTavern features without any restrictions. An implementation of user permissions is TBD.

All user accounts are created as regular users first, and then could be promoted to admins if needed.

### Login screen

There you can select a user account to use. Has two styles, depending on the `enableDiscreetLogin` config value.

The login screen is bypassed and not displayed when you have only one active user and it is not password protected.

### User profile

You can access an account self-management menu using an "Account" button under the "User settings" panel in the top menu bar.

1. Display name - used in the login screen, can be changed. Does not correlate with personas and is not visible for the AI APIs - you can still use as many personas as you want.
2. Profile picture - used in the login screen. You can either use a custom picture, the default persona picture (if set), or the last used persona otherwise.
3. Password - a lock icon reflects the account protection status (open lock = no password). A password can be set, changed, or removed using the "Change Password" button.
4. Settings Snapshots - access and review the backups of your `settings.json` file, with the ability to create or restore snapshots.
5. Download Backup - download an archive of your user data folder.
6. Reset Settings - reset factory default settings, while leaving other data (character, chats) intact.

## Password recovery

1. A password can be recovered from a login screen. You need access to the server console to get a one-time recovery code (consisting of 4 digits).
2. Alternatively, you can use a utility script in the SillyTavern server to reset a password by providing the user handle.

```txt
Usage: node recover.js [account] (password)
Example: node recover.js admin SecurePassword
```

## Content scaffolding

To add custom content for users, you can use the content scaffolding feature. This feature allows you to define a set of files that will be copied to each user's data directory when the server starts up.

You must create an `index.json` file in the `/default/scaffold` directory for this feature to work. The syntax is the same as for default content. All file paths should be relative to the `/default/scaffold` directory, and you can organize files using subdirectories.

Scaffolded files are copied before default files, which means they will override any default files (presets/settings/etc.) that have the same file name.

Every user data directory has a `content.log` file that lists all files copied from the scaffold and default directories. Remove this file to force the server to sync the content again on the next restart.

**### Recognized content types**

| Type                          | Value                |
|-------------------------------|----------------------|
| settings.json                 | `'settings'`         |
| Character card                | `'character'`        |
| Character sprites             | `'sprites'`          |
| Background image              | `'background'`       |
| World Info file               | `'world'`            |
| Persona avatar                | `'avatar'`           |
| UI theme                      | `'theme'`            |
| ComfyUI workflow              | `'workflow'`         |
| KoboldAI Classic preset       | `'kobold_preset'`    |
| Chat Completion preset        | `'openai_preset'`    |
| NovelAI preset                | `'novel_preset'`     |
| Text Completion preset        | `'textgen_preset'`   |
| Instruct Mode template        | `'instruct'`         |
| Context Formatting template   | `'context'`          |
| MovingUI preset               | `'moving_ui'`        |
| Quick Replies set             | `'quick_replies'`    |
| System Prompt template        | `'sysprompt'`        |
| Reasoning Formatting template | `'reasoning'`        |

### Example (`/default/scaffold/index.json`)

```json
[
    {
        "filename": "themes/Midnight.json",
        "type": "theme"
    },
    {
        "filename": "backgrounds/city.png",
        "type": "background"
    },
    {
        "filename": "characters/Charlie.png",
        "type": "character"
    }
]
```

# SECTION: SillyTavern_Administration_remote-connections

# Remote connections

Most often this is for people who want to use SillyTavern on their mobile phones while their PC runs the ST server within the same WiFi network.

It is also the first step for allowing remote connections from outside the local network.

You should not use port forwarding to expose your ST server to the internet. Instead, use a VPN or a tunneling service like Cloudflare Zero Trust, ngrok, or Tailscale. See the VPN and Tunneling guide for more information.

**!!!danger Disclaimer**

**NEVER HOST ANY INSTANCES ON THE OPEN INTERNET WITHOUT ENSURING PROPER SECURITY MEASURES FIRST.**

**WE ARE NOT RESPONSIBLE FOR ANY DAMAGE OR LOSSES IN CASES OF UNAUTHORIZED ACCESS DUE TO IMPROPER OR INADEQUATE SECURITY IMPLEMENTATION.**

**## Allowing remote connections**

By default, the ST server only accepts connections from the machine that it's running on (localhost). To allow it to listen for connections from other devices, set the `listen` option in `config.yaml` to `true`.

**If you search for `config.yaml` directly in the SillyTavern folder, you may find two files.**

All modifications to `config.yaml` in this document refer to the one in the SillyTavern root directory (/SillyTavern/config.yaml), not `/SillyTavern/default/config.yaml`.

```yaml

# Listen for incoming connections
listen: true
```

When ST is listening for remote connections, you should see this message in the console:

```txt
SillyTavern is listening on IPv4: 0.0.0.0:8000
```

and some explanation about what that means.

When ST is **not** listening for remote connections, you should see this message in the console:

```txt
SillyTavern is listening on IPv4: 127.0.0.1:8000
```

## Access control configuration

After enabling remote connection listening, you must configure at least one access control method. Otherwise, the server will not start.

### Whitelist-Based access control

To enable access control via a whitelist, edit the `config.yaml` file in the SillyTavern root directory (`/SillyTavern/config.yaml`):

1. Start SillyTavern at least once to generate the necessary configuration files.
2. Open `/SillyTavern/config.yaml` in a text editor.
3. Find the `whitelist` section and add the IP addresses you wish to allow:
    * List each IP address separately.
    * Ensure `127.0.0.1` is included, or you will be unable to connect from the host machine.
    * Supports individual IPs, CIDR masks (e.g., `10.0.0.0/24`), and wildcard (`*`) ranges.
4. Save the `config.yaml` file.
5. **Restart your SillyTavern server.**

#### Example `config.yaml` whitelist configuration

1. Allow any device on the local network:

    ```yaml
    whitelist:
      - ::1
      - 127.0.0.1
      - 10.0.0.0/8
      - 172.16.0.0/12
      - 192.168.0.0/16
    ```

    If unsure about your local network's address range, use the whitelist above.

2. Allows two specific devices to connect:

    ```yaml
    whitelist:
      - ::1
      - 127.0.0.1
      - 192.168.0.2
      - 192.168.0.5
    ```

3. Allows any device on the `192.168.0.*` subnet to connect:

    ```yaml
    whitelist:
      - ::1
      - 127.0.0.1
      - 192.168.0.*
    ```

4. Allow network connections for all IPv4 devices:

    ```yaml
    whitelist:
      - 0.0.0.0/0
    ```

### Disabling whitelist-based access control

To disable access control via a whitelist:

* Set `whitelistMode` to `false` in `/SillyTavern/config.yaml`.
* Remove or rename `whitelist.txt` (if it exists) in the SillyTavern base installation folder.
* Restart your SillyTavern server.

### Not recommended: using `whitelist.txt`

If `whitelist.txt` exists, it takes precedence over the whitelist settings in `config.yaml`.

However, since all other configurations are managed within `config.yaml`, and `whitelist.txt` may encounter permission issues or become locked, the system could silently revert to using the `config.yaml` whitelist.

**Editing config.yaml directly is both simpler and more reliable.**

**If you still prefer using whitelist.txt:**

1. Create a new text file named `whitelist.txt` in the SillyTavern base installation folder.
2. Open it in a text editor and add the allowed IP addresses.
3. Save the file and restart your SillyTavern server.

#### Example `whitelist.txt` configuration

```txt
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
127.0.0.1
::1
```

This allows any device on the local network to connect.

### Access control by HTTP Basic Authentication

HTTP Basic Authentication does not provide strong security.

There is no rate-limiting to prevent brute-force attacks. If this is a concern, it is recommended to use a reverse proxy with TLS and rate-limiting, and a dedicated authentication service.

**The server will ask for username and password whenever a client connects via HTTP. **This only works if the Remote connections (listen: true) are enabled.****

To enable HTTP BA, Open `config.yaml` in the SillyTavern base directory and search for `basicAuthMode`. Set basicAuthMode to true and set username and password. Note: `config.yaml` will only exist if ST has been executed before at least once.

```yaml
basicAuthMode: true
basicAuthUser:
  username: "MyUsername"
  password: "MyPassword"
```

Alternatively you can enable basic auth as follows:

```yaml
basicAuthMode: true
enableUserAccounts: true
perUserBasicAuth: true
```

In this `perUserBasicAuth` mode the basic auth's username and password will be the same as any valid multi user account that has a password. Additionally SillyTavern will login directly to that account. **Ensure you have an account with a password prior to enabling `perUserBasicAuth`.**

Save the file and restart SillyTavern if it was already running. You should be prompted for username and password when connecting to your ST. Both username and password are transmitted in plain text. If you are concerned about this, you can serve ST via HTTPS.

### Host whitelisting

When hosting a server over the network without HTTPS, it is highly recommended to enable request host verification. This helps prevent various attacks, such as DNS rebinding. By default, the SillyTavern server will log a console message on a first connection from an unrecognized host.

### Toggle host whitelisting

To enable host whitelisting, edit the `config.yaml` file in the SillyTavern root directory:

```yaml
hostWhitelist:
    enabled: true
```

### Add trusted hosts

To add a host name to a list of trusted hosts, include it in the `hostWhitelist.hosts` section:

**Tips**

Do not add `localhost` or IPs (such as `127.0.0.1` or `::1`). These are always considered trusted.

To add a range of hosts, use a leading dot. For example, adding `.trycloudflare.com` will trust `trycloudflare.com` as well as any subdomain like `example.trycloudflare.com`.

```yaml

hostWhitelist:
  hosts:
    - "example.com"
    - ".trycloudflare.com"
```

### Toggle console messages

To disable console messages for unrecognized hosts, set the `hostWhitelist.scan` option to `false`:

```yaml
hostWhitelist:
    scan: false
```

## Connecting to your SillyTavern instance

### Getting the IP address for the ST host machine

After the whitelist has been setup, you'll need the IP of the ST-hosting device.

If the ST-hosting device is on the same wifi network, you will use the ST-host's internal wifi IP:

* For Windows: windows button > type `cmd.exe` in the search bar > type `ipconfig` in the console, hit Enter > look for `IPv4` listing.

If you (or someone else) wants to connect to your hosted ST while not being on the same network, you will need the public IP of your ST-hosting device.

* While using the ST-hosting device, access this page (https://whatismyipaddress.com/) and look for for `IPv4`. This is what you would use to connect from the remote device.

### Connecting to the ST server

Whatever IP you ended up with for your situation, you will put that IP address and port number into the remote device's web browser.

A typical address for an ST host on the same wifi network would look like:

`http://192.168.0.5:8000`

Use http:// NOT https://

### Connection logging

New connections to the server are displayed in the console window and logged in the `access.log` file in the SillyTavern data directory.

A console message for a browser on the same machine as the server looks like:

```txt
New connection from 127.0.0.1; User Agent: ...
```

A console message for a browser on a different machine on the same network as the server might look like:

```txt
New connection from 192.168.116.187; User Agent: ...
```

If a connection is refused, the console message will look like:

```txt
New connection from 192.168.116.211; User Agent: ...

Forbidden: Connection attempt from 192.168.116.211. If you are attempting to connect, 
please add your IP address in whitelist or disable whitelist mode in config.yaml in 
root of SillyTavern folder.
```

`access.log` will contain the connection information, with timestamps, but not whether the connection was accepted or refused.

### Troubleshooting

Still unable to connect?

* If the connection attempt appears in the console, but is forbidden, it is a whitelist issue.
* If ST is listening for remote connections but the connection attempt does not appear in the console, it is a network issue.
* If ST is not listening for remote connections, it is a reading issue.

#### Network issues

* On Windows, the application may be blocked by the application firewall. The quickest way to fix this is to uninstall and reinstall node.js, and when prompted by the firewall, allow it to access the network. Otherwise, you will need to manually allow the node.js application through the Windows application firewall.
* On Windows 11, enable the Private Network profile type in Settings > Network and Internet > Ethernet. This is VERY important for Windows 11, otherwise, you would be unable to connect even with the aforementioned firewall rules.
* On Linux, you may need to allow the port through the firewall. The command to do this is `sudo ufw allow 8000`. This will allow traffic on port 8000.

Do not modify the port forwarding settings on your router. This is not necessary for accessing ST within your local network, and can expose your server to the internet.

If you are trying to access your ST server from outside your local network, and it's not working, identify whether the problem is between the remote device and the tunnel/VPN endpoint, or between the tunnel endpoint on the server and the ST service. Otherwise you will spend a lot of time troubleshooting the wrong thing.

## HTTPS

### Start SillyTavern with TLS/SSL

SSL can also be configured using the `config.yaml` file: SSL Configuration.

**To encrypt traffic from and to your ST instance, start the server with the `--ssl` flag.**

Example:

```bash
node server.js --ssl
```

As per default, ST will search for your certificates inside the `certs` folder. If your files are located elsewhere, you can use the `--keyPath` and `--certPath` arguments.

Example:

```bash
node server.js --ssl --keyPath /home/user/certificates/privkey.pem --certPath /home/user/certificates/cert.pem
```

The user you're running SillyTavern with requires read permissions on the certificate files.

### How to get a certificate

The simplest, quickest way to get a certificate is by using certbot (https://letsencrypt.org/getting-started/).

### Certificates in Docker

For security and privacy reasons, do not include your SSL certificates inside the Docker image if you are building one. Instead, use volume mounts to provide the certificates at runtime.

**When running SillyTavern in Docker, the recommended way to provide SSL certificates is by placing them in the `/config` volume mount. This allows you to manage certificates without rebuilding the container image.**

1. Place your certificate files (e.g., `privkey.pem` and `cert.pem`) in your local config directory that is mounted to `/config` in the container.

2. Update your `config.yaml` to reference the certificates:

    ```yaml
    ssl:
      enabled: true
      certPath: ./config/cert.pem
      keyPath: ./config/privkey.pem
    ```

3. Restart your Docker container to apply the changes.

# SECTION: SillyTavern_Administration_reverse-proxying

**Note**

This section does **not** refer to OpenAI/Claude reverse proxies. This refers exclusively to **HTTP/HTTPS Reverse Proxies**.

**Is Termux confusing to set up? Are you tired of updating and installing ST on every device you have? Want organization of your chats and characters? Well you are in luck. This guide will _hopefully_ cover how to host SillyTavern on your PC where you can connect from anywhere and chat to your bots on the same PC you use to run AI models!**

**Warning**

This guide is **not meant** for beginners. This will be very technical.

**## Fair Warning**

**For Windows Users**

This guide is not for Windows users. We recommend using a Linux VM or WSL2 to follow this guide.

**!!!info For Linux Users**

You must have prior knowledge of

- Linux console commands
- DNS Records
- Public IP addresses
- Docker (https://www.docker.com)

****You will have to buy a domain for yourself and configure a `CNAME` for your SillyTavern page. We suggest adding or buying the domain on Cloudflare (https://www.cloudflare.com) as this guide will cover how to do this with Cloudflare itself.****

## Installation

### Linux (Bare-Metal SillyTavern)

For Linux, we will be reverse proxying SillyTavern through Traefik (https://traefik.io/traefik/). There are other options such as _NGINX_ or _Caddy_, but for this guide, we will use Traefik as it is what we use ourselves.

1. Get the private IP of your computer using `ifconfig` or from your router.

**Tip**

   It is recommended to set your private IP to a Static IP. Refer to your router's manual or Google to configure static IPs.

**2. Get your public IP of your modem by Googling `what's my ip`.**

**About Public IPs**

   Most residential/home networks use **Dynamic IPs** which are renewed after months of use. If you have a dynamic IP, use either DDClient or remember to check and change your public IP ever so often on the Cloudflare Dashboard.

**3. Install Docker by following the Docker installation guide here (https://docs.docker.com/engine/install/).**

**Note**

   **Do not** install Docker Desktop.

**4. Follow the steps in **Manage Docker as a non-root user** in the Docker post-installation guide here (https://docs.docker.com/engine/install/linux-postinstall/).**

5. Go to your root folder in Linux and make a new folder named `docker`.
    ```sh
    cd /
    sudo mkdir docker && cd docker
    ```
6. Execute `chown`, replacing _<USER>_ with your Linux username to set the permissions in the docker folder.
    ```sh
    sudo chown -R <USER>:<USER> .
    ```
7. Make a folder inside the _docker_ folder, that being `secrets` and inside _secrets_ being `cloudflare`.
    ```sh
    mkdir secrets && mkdir secrets/cloudflare
    ```
8. Make a folder inside the _docker_ folder, that being `appdata` and inside _appdata_ being `traefik`. Enter the `appdata/traefik` folder afterwards.
    ```sh
    mkdir appdata && mkdir appdata/traefik
    cd appdata/traefik
    ```
9. Create an _acme.json_ file using `touch` and set the permissions of it to 600.
    ```sh
    touch acme.json
    chmod 600 acme.json
    ```
10. Using `nano` or a similar editor, create a file named _traefik.yml_ and paste the following. Replace the template email with your own, then save the file.
    ```yml
    api:
        dashboard: true
        debug: true
        insecure: true
    entryPoints:
        http:
            address: ":80"
            http:
                redirections:
                    entryPoint:
                        to: https
                        scheme: https
        https:
            address: ":443"
    serversTransport:
        insecureSkipVerify: true
    providers:
        docker:
            endpoint: "unix:///var/run/docker.sock"
            exposedByDefault: false
        file:
            filename: /config.yml
            watch: true
    certificatesResolvers:
        cloudflare:
            acme:
                email: YOUR_CLOUDFLARE_EMAIL@DOMAIN.com
                storage: acme.json
                dnsChallenge:
                    provider: cloudflare
                    #disablePropagationCheck: true  # uncomment this if you have issues pulling certificates through cloudflare, By setting this flag to true disables the need to wait for the propagation of the TXT record to all authoritative name servers.
                    resolvers:
                        - "1.1.1.1:53"
                        - "1.0.0.1:53"
    ```
11. Return back to the `docker` folder.
    ```sh
    cd /docker
    ```
12. Using `nano` or a similar editor, create a file named _docker-compose.yaml_ and paste the following. Save the file afterwards.

    ```yaml
    secrets:
        CF_DNS_API_KEY:
            file: ./secrets/cloudflare/CF_DNS_API_KEY

    services:
        traefik:
            image: traefik:latest
            container_name: traefik
            restart: unless-stopped
            secrets:
                - CF_DNS_API_KEY
            ports:
                - 80:80
                - 443:443
                - 8080:8080
            environment:
                CLOUDFLARE_DNS_API_TOKEN_FILE: /run/secrets/CF_DNS_API_KEY
                CLOUDFLARE_ZONE_API_TOKEN_FILE: /run/secrets/CF_DNS_API_KEY
            volumes:
                - /var/run/docker.sock:/var/run/docker.sock:ro
                - ./appdata/traefik/traefik.yml:/traefik.yml:ro
                - ./appdata/traefik/config.yml:/config.yml:ro
                - ./appdata/traefik/acme.json:/acme.json
                - /etc/localtime:/etc/localtime:ro

    networks:
        internal:
            driver: bridge
    ```

13. Login to Cloudflare and click on your Domain, followed by **Get your API token**.
14. Click on _Create Token_ then _Create Custom Token_ and make sure you give your token the following permissions.

**Token Permissions**

    **Zone -> DNS -> Edit**

    **Zone -> Zone -> Read**

**Click on _Continue to summary_ followed by _Create Token._**

15. Copy the Token Key given to you and store it somewhere secure.
16. `cd` into `secrets/cloudflare` and using `nano` or a similar editor, create a file named **CF_DNS_API_KEY** and paste your key inside.
17. Return to your domain page and go to **DNS**. Create a new record using **Add record** and create two _A_ type keys like the ones below. Replace `PUBLIC_IP` with your own public IP, then click _Save_.

    | Type | Name (required) | Target (required) | Proxy Status | TTL  |
    |------|-----------------|-------------------|--------------|------|
    | A    | DOMAIN.com      | PUBLIC_IP         | Proxied      | Auto |
    | A    | www             | PUBLIC_IP         | Proxied      | Auto |

18. Create another record of the **`CNAME`** type, then click _Save_. Here is an example on how it should appear on the Cloudflare dashboard.

    | Type  | Name (required) | Target (required) | Proxy Status | TTL |
    |-------|-----------------|-------------------|--------------|-----|
    | CNAME | silly           | DOMAIN.com        | Proxied      | N/A |

19. `cd` into _appdata/traefik_ and using `nano` or a similar editor, create a file named _config.yml_ and paste the following. Replace `PRIVATE_IP` with the private IP you obtained, and `silly.DOMAIN.com` with the name of your subdomain and domain page, then save the file.

    ```yml
    http:
        routers:
            sillytavern:
                entryPoints:
                    - "https"
                rule: "Host(`silly.DOMAIN.com`)"
                middlewares:
                    - https-redirectscheme
                tls: {}
                service: sillytavern

        services:
            sillytavern:
                loadBalancer:
                    servers:
                        - url: "http://PRIVATE_IP:8000"
                    passHostHeader: true

        middlewares:
            https-redirectscheme:
                redirectScheme:
                    scheme: https
                    permanent: true
    ```

20. Run Docker Compose using the following commands:
    ```sh
    cd /docker
    docker compose up -d
    ```
21. Go to your SillyTavern folder and edit `config.yaml` to enable listen mode and basic authentication, whilst disabling `whitelistMode`.

    ```yaml
    listen: yes
    whitelistMode: false
    basicAuthMode: true
    ```

**Tip**

    Make sure to change the default username and password to something strong that you can remember.

**Or to use the SillyTavern accounts as usernames and passwords:**

    ```yaml
    basicAuthMode: true
    enableUserAccounts: true
    perUserBasicAuth: true
    ```

**Tip**

    Before enabling perUserBasicAuth ensure you have a valid multi-user setup with working passwords.

**22. Wait a few minutes, then open the domain page you made for ST. At the end of it, you should be able to open SillyTavern from anywhere you go just with one URL and one account.**

**Tip**

    If nothing happens after several minutes, check the container logs for Traefik for any possible errors.

**23. Enjoy! :D**

### Linux (Docker SillyTavern)

**Note**

Do note that we run SillyTavern on bare-metal over Docker. This is a rough idea of what we would do on Docker with other Docker containers we tend to use with ST.

**1. Follow Steps 1-11 of **Linux (Bare-Metal SillyTavern)**.**

2. Login to Cloudflare and click on your Domain, followed by **Get your API token**.
3. Click on _Create Token_ then _Create Custom Token_ and make sure you give your token the following permissions.

**Token Permissions**

   **Zone -> DNS -> Edit**

    **Zone -> Zone -> Read**

**Click on _Continue to summary_ followed by _Create Token._**

4. Copy the Token Key given to you and store it somewhere secure.
5. `cd` into `secrets/cloudflare` and using `nano` or a similar editor, create a file named **CF_DNS_API_KEY** and paste your key inside.
6. Return to your domain page and go to **DNS**. Create a new record using **Add record** and create two _A_ type keys like the ones below. Replace `PUBLIC_IP` with your own public IP and the example domain with your domain, then click _Save_.

    | Type | Name (required) | Target (required) | Proxy Status | TTL  |
    |------|-----------------|-------------------|--------------|------|
    | A    | DOMAIN.com      | PUBLIC_IP         | Proxied      | Auto |
    | A    | www             | PUBLIC_IP         | Proxied      | Auto |

7. Create another record of the **`CNAME`** type, then click _Save_. Here is an example on how it should appear on the Cloudflare dashboard.

    | Type  | Name (required) | Target (required) | Proxy Status | TTL |
    |-------|-----------------|-------------------|--------------|-----|
    | CNAME | silly           | DOMAIN.com        | Proxied      | N/A |

8. Git clone SillyTavern into the `docker` folder.
    ```sh
    cd /docker && git clone https://github.com/SillyTavern/SillyTavern
    ```
9. Using `nano` or a similar editor, create a file named _docker-compose.yaml_ and paste the following. Replace `silly.DOMAIN.com` with the subdomain you added above, then save the file afterwards.

    ```yaml
    secrets:
        CF_DNS_API_KEY:
            file: ./secrets/cloudflare/CF_DNS_API_KEY

    services:
        traefik:
            image: traefik:latest
            container_name: traefik
            restart: unless-stopped
            secrets:
                - CF_DNS_API_KEY
            ports:
                - "80:80"
                - 443:443
                - 8080:8080
            environment:
                CLOUDFLARE_DNS_API_TOKEN_FILE: /run/secrets/CF_DNS_API_KEY
                CLOUDFLARE_ZONE_API_TOKEN_FILE: /run/secrets/CF_DNS_API_KEY
            volumes:
                - /var/run/docker.sock:/var/run/docker.sock:ro
                - ./appdata/traefik/traefik.yml:/traefik.yml:ro
                - ./appdata/traefik/config.yml:/config.yml:ro
                - ./appdata/traefik/acme.json:/acme.json
                - /etc/localtime:/etc/localtime:ro
        sillytavern:
            build: ./SillyTavern
            container_name: sillytavern
            hostname: sillytavern
            image: ghcr.io/sillytavern/sillytavern:latest
            volumes:
                - "./appdata/sillytavern/config:/home/node/app/config"
                - "./appdata/sillytavern/data:/home/node/app/data"
            restart: unless-stopped
            labels:
                - "traefik.enable=true"
                - "traefik.http.routers.sillytavern.entrypoints=http"
                - "traefik.http.routers.sillytavern.rule=Host(`silly.DOMAIN.com`)"
                - "traefik.http.middlewares.sillytavern-https-redirect.redirectscheme.scheme=https"
                - "traefik.http.routers.sillytavern.middlewares=sillytavern-https-redirect"
                - "traefik.http.routers.sillytavern-secure.entrypoints=https"
                - "traefik.http.routers.sillytavern-secure.rule=Host(`silly.DOMAIN.com`)"
                - "traefik.http.routers.sillytavern-secure.tls=true"
                - "traefik.http.routers.sillytavern-secure.service=sillytavern"
                - "traefik.http.services.sillytavern.loadbalancer.server.port=8000"

    networks:
        internal:
            driver: bridge
    ```

10. Run Docker Compose using the following commands:
    ```sh
    docker compose up -d
    ```
11. Stop the SillyTavern Docker container.
    ```sh
    docker compose stop sillytavern
    ```
12. Go to your SillyTavern folder (`appdata/sillytavern/config`) and edit `config.yaml` to enable listen mode and basic authentication, whilst disabling `whitelistMode`.

    ```yaml
    listen: yes
    whitelistMode: false
    basicAuthMode: true
    ```

**Tip**

    Make sure to change the default username and password to something strong that you can remember.

**13. Start the SillyTavern Docker container again.**

    ```sh
    docker compose up -d sillytavern
    ```
14. Wait a few minutes, then open the domain page you made for ST. At the end of it, you should be able to open SillyTavern from anywhere you go just with one URL and one account.

**Tip**

    If nothing happens after several minutes, check the container logs for Traefik for any possible errors.

**15. Enjoy! :D**

## Updating your Cloudflare DNS

**DDClient** (https://ddclient.net/) allows you to sync your public IP to Cloudflare in the situation that your ISP changes it, allowing you to continue accessing your ST instance as if nothing ever happened.

# SECTION: SillyTavern_Administration_sso

# Single Sign-On (SSO)

SSO allows you to create users and secure many different pages using a login portal presented on sites you want to secure. While it is complex to setup, it is a good way to both learn SSO and secure your ST instance out on the internet more.

SSO can also replace HTTP Basic Authentication as an access control mechanism for remote connections.

This is recommended because SSO provides better security and functionality than HTTP Basic Authentication.

**Authelia** (https://www.authelia.com/) and **Authentik** (https://goauthentik.io/) are open-source SSO providers that can be used with SillyTavern.

## Sign in with SSO

If your SSO-provided username **exactly** matches the user handle of a SillyTavern user account, you can sign in to SillyTavern as that user by SSO. To enable this feature, change one of the following options to your config.yaml file:

### Authelia

```yaml
sso:
  autheliaAuth: true
```

### Authentik

```yaml
sso:
  authentikAuth: true
```

Both options augment or replace the built-in password management component of a multi-user mode setup.

# SECTION: SillyTavern_Administration_tunneling

VPNs and tunnels are a secure way to access your home network from anywhere in the world. This guide will show you how to use a VPN or a tunnel to access your SillyTavern instance from anywhere.

## Methods

1. Use a **home-made VPN**.

   Several routers come with the ability to host a VPN server (primarily OpenVPN or WireGuard) in the router administration page. Refer to your router's manual to setup a VPN and add your devices to the VPN. Once connected, just go to the private IP you have set for SillyTavern and you can connect just fine. Easier for users and for Windows use.

2. Use **Cloudflare Zero Trust** (https://developers.cloudflare.com/cloudflare-one/).

   Cloudflare Zero Trust is a free organizational feature in Cloudflare that allows you to add 50 users. This will proxy your traffic through Cloudflare and by adding your ST PC as a tunnel using `cloudflared`, you can connect to your ST instance as if you were home.

   Do note that after making a tunnel, you will have to add a route to your router's private IP addresses and calculate IP CIDR values to have full local access on the go using Cloudflare Zero Trust.

3. Use a standalone **Cloudflare** or **ngrok (https://ngrok.com)** tunnel.

   Similar to how AI backends can connect, you can also connect your ST instance via a Cloudflare Tunnel and open the Cloudflare Tunnel page. However, you will have to copy and paste each new link generated by Cloudflare/NGROK each time you want to use ST on-the-go.

4. Use **Tailscale**.

   Tailscale is a VPN provider enabling a secure remote connection to your PC.

## Tailscale setup

Tailscale is a VPN provider enabling a secure remote connection to your PC. An open-source implementation of the Tailscale server exists and you can also host the server using Headscale (https://github.com/juanfont/headscale), but that is outside of the scope of this tutorial.

### 1. Creating an account

* Go to Tailscale's website (https://tailscale.com/) and create a new account.

**NOTE:** For everyday use by a single person Tailscale will be permanently free. If you fear hidden costs, just don't add any payment options.

### 2. Setting up clients

* Go to Tailscale's download page (https://tailscale.com/download) and download the client/app on the device you have SillyTavern running on and on the device you want to use from a remote location.
* Log in on both devices with your previously created account.
* Go to Tailscale's admin page (https://login.tailscale.com/admin/machines) and approve both devices.
* Take note of both of the connected devices' names.

### 3. Adding your devices to the whitelist

* Add your connecting device's machine name (the one you want to use SillyTavern with) to SillyTavern's whitelist by following Managing whitelisted IPs.

### 4. Connecting

Now whenever you want to use SillyTavern from anywhere all you have to do is:

* Have Tailscale turned on on both the PC hosting SillyTavern and your device that wants to use it remotely.
* Open a browser on the device that wants to connect and go to `http://<machine name of PC running st>:8000/`

### 5. Sharing SillyTavern instance with a friend (optional)

* Tell your friend to create their own Tailscale account and download the client on their device.
* Go to Tailscale's admin page (https://login.tailscale.com/admin/machines).
* Hover over the three-dot button on your PC hosting SillyTavern and press "Share..." or press the three-dot button and press "Sharing settings...".
* Uncheck "Allow use as an exit node" (unless you want your friend to be able to route all their internet traffic through your PC).
* Either send the link as an email or change the tab to "Copy share link", press the big blue button with the same text, and send it to your friend in any other way.
* After clicking your share link, your friend will see your PC pop up in their Tailscale network.
* Send your friend the same link you use to access SillyTavern as explained in the last step.

**NOTE:** This will give your friend full access to any services running locally on your PC like SillyTavern, automatic1111, etc. Only do this if you truly trust your friend.

# SECTION: SillyTavern_extensions_AllTalk

# AllTalk TTS V2

AllTalk is a voice cloning system based on Coqui XTTS, F5-TTS, VITS, Piper and other TTS model engines, designed to produce high-quality voice reproduction (either zero shot voice cloning or built-in voices). In AllTalk V2, significant updates enhance functionality and ease of use, including multiple TTS engine support, expanded customization, and performance optimizations. For a comprehensive list of features, refer to the AllTalk Wiki here (https://github.com/erew123/alltalk_tts/wiki).

---

## 🟩 Key Features in AllTalk V2
- **Multi-engine Support**: Easily switch between Coqui XTTS, VITS, Piper, Parler, F5, and custom engines.
- **Voice Conversion (RVC)**: Enhanced retrieval-based voice cloning pipeline.
- **Customizable Settings**: Adjust per-engine settings and save startup configurations.
- **Narrator Functionality**: Specify separate voices for narration and characters.
- **Standalone and Integrated Use**: Seamless integration with SillyTavern.
- **DeepSpeed and Low VRAM Modes**: Performance optimization for resource-limited environments.
- **Screenshots**: See AllTalk V2’s interface here (https://github.com/erew123/alltalk_tts/discussions/237).

---

## 🟨 Setup and Installation Options

AllTalk offers both standalone and integrated installation methods. The fastest setup involves using one of the quick installation options provided, with scripts automating most of the process.

- **Standalone Installation**: Recommended for most users (Standalone Guide (https://github.com/erew123/alltalk_tts/wiki/Install-%E2%80%90-Standalone-Installation))
- **Text-generation-webui Integration**: For integration into Text-generation-webui (TGWUI Installation Guide (https://github.com/erew123/alltalk_tts/wiki/Install-%E2%80%90-Text%E2%80%90generation%E2%80%90webui-Installation))

#### 🟩 Automated Installation
**This method is for Windows users only.**
For new users who want a quick setup, the automated installation uses the SillyTavern-Launcher. 
Note: This assumes you have already installed the SillyTavern-Launcher. If you haven’t, visit https://github.com/SillyTavern/SillyTavern-Launcher and follow the instructions in the readme.md file to install it.
Once the SillyTavern-Launcher is installed:
1. Run Launcher.bat
2. Go to: `Home > Toolbox > App Installer > Voice Generation`
3. Select the option labeled: **Install AllTalk V2**

#### 🟩 Manual Installation
For advanced users requiring detailed control, follow the Manual Installation Guide (https://github.com/erew123/alltalk_tts/wiki/Install-%E2%80%90-Manual-Installation-Guide) for a step-by-step setup on Windows, Linux, or Mac (untested).

#### 🟩 Google Colab Installation
Run AllTalk in a cloud environment with the Google Colab Installation (https://github.com/erew123/alltalk_tts/wiki/Google-COLAB) for users who prefer not to install locally.

---

## 🟨 Using AllTalk within SillyTavern

Once AllTalk is loaded, select it within SillyTavern on the TTS page, ensuring to select the correct AllTalk server version in the settings.

- **Settings Management**: AllTalk may enable or disable specific settings based on your selected configuration.
- **Loading Sequence**: If SillyTavern is loaded before AllTalk, reload the TTS extensions page.
- **Performance Optimization**: Enable DeepSpeed and Low VRAM modes selectively to improve performance based on system resources.
- **Narrator function**: Details of the Narrator function can be found on the AllTalk Wiki (https://github.com/erew123/alltalk_tts/wiki/Narrator-Function).

Full details of the SillyTavern AllTalk Extension will be updated on the AllTalk Wiki page for SillyTavern (https://github.com/erew123/alltalk_tts/wiki/SillyTavern-Extension)

TGWUI Users who use the AllTalk extension for TGWUI need to disable `Enable TGWUI TTS` in the TGWUI chat interface, otherwise you will have duplicate TTS audio generated.

---

## 🟨 Troubleshooting

If you experience issues that you believe are specific to AllTalk within SillyTavern, please refer to the AllTalk Wiki page for SillyTavern (https://github.com/erew123/alltalk_tts/wiki/SillyTavern-Extension) for the latest information.

---

### 🟪 Support, Assistance, and Feature Requests

For further assistance:
- Refer to the Wiki (https://github.com/erew123/alltalk_tts/wiki) and built-in documentation.
- Join discussions on the Discussion Board (https://github.com/erew123/alltalk_tts/discussions/245).
- Submit bugs or feature requests through the Issue Tracker (https://github.com/erew123/alltalk_tts/issues).

---

# SECTION: SillyTavern_extensions_Blip

# Blip

This guide will walk you through setting up and customizing blip extension for your SillyTavern experience. This extension animates the text of messages with variable speed and plays sound along the animation. You can use an audio file or generate the sound.

## Prerequisites

Before you begin, ensure you've met the following prerequisites:

- Make sure you're on the latest version of SillyTavern.
- Install the "Blip" extension from the "Download Extensions & Assets" menu in the Extensions panel (stacked blocks icon).

## Blip global settings

1. **Blip user message**:
   - Enable checkbox to play animation on user message.
   - Set a profile for the user or a default profile if you want blip animation for user.

2. **Blip only for certain text**:
   - Enable checkbox to only blip for text inside quotes.
   - Enable checkbox to ignore everything inside asterisks.

3. **Automatic scroll down**:
   - Enable checkbox to make the chat go down to follow the text animation, disable it if you want to scroll freely during animation.

4. **Audio volume**
   - Mute the audio if just the animation of the text is desired.
   - You can adjust the global volume of blip audio.

## Character animation/voice profile

You can save a profile for each character:
   - including the user and an optional default profile that will be used when character have no profile. 
   - If only the current chat characters are shown in the list, click the checkbox to show all your characters.

1. **Select the character to assign/update profile**:
   - Select a character. If it has a profile, it will be loaded.
   - If it does not have a profile yet the current parameters will become his profile settings.
   - Any profile can be deleted using the remove button.
   - Use refresh button if your character does not appear in the list.

2. **Text animation settings**:
   - Set the text speed: the delay in milliseconds between each letter printed.
   - Set Min/max speed multiplier different to 1.0 for randomness of speed animation.
   - Set comma/phrase delay superior to 0 to add a pause when special characters are printed, can add more liveliness to animation. Audio is paused too in this case.

3. **Audio parameters**:
   - Set a volume multiplier that will only affect this voice profile if needed.
   - Set audio speed: the delay between each blip sound, independent of text speed.

4. **Blip origin: Generated sound**:
   - Use the min/max frequency slider to customize the blip sound played.
   - If min/max are different a random sound in this range is played each time.

5. **Blip origin: file**:
   - Choose a file in the list.
   - You can get official ST blip assets from the assets extension menu.
   - Or put file directly into: `\SillyTavern\data\<user-handle>\assets\blip`.
   - Enable the checkbox to force waiting until the entire file is played before playing again if needed.

Thank you for following this guide! Your SillyTavern experience is now enriched with text animation and blip voices.

# SECTION: SillyTavern_extensions_captioning

# Image Captioning

Image Captioning allows SillyTavern to automatically generate text descriptions for images used in chats. 

Use Image Captioning when you want your AI character to "see" and respond to visual content in your conversations.

- Create captions for images you upload or paste into messages
- Add context to existing images in the chat history
- Use various sources for generation, including local models, cloud APIs, and crowdsourced networks

There are options that require no setup, no money, and no GPU. There are also options that require some or all of those things. Choose the one that fits your needs and resources.

The image captioning extension is built-in to SillyTavern and does not need to be installed separately.

## Quick start

1. Set up:
    - Open the **Image Captioning** panel in the **<i class="fa-solid fa-cubes"></i> Extensions** panel
    - Choose a captioning source (most likely "Local" or "Multimodal")
    - For "Multimodal" ensure you've set up the connection in the **<i class="fa-solid fa-plug"></i> API Connections** tab
2. Generate a caption:
    - Choose "**Generate Caption**" from the **<i class="fa-solid fa-magic-wand-sparkles"></i> Extensions** popup menu
    - Select an image file when prompted
    - Wait for the caption to be generated
3. Review and send:
    - The captioned image will be inserted into your message
    - See the caption using the image tooltip
    - Click **<i class="fa-solid fa-paper-plane"></i> Send** to see what your character thinks of the image!

## Panel controls

### Source Selection

Choose the source for image captioning. Supported options:

| Source                           | Description                                                                                                                                                                                                  |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Multimodal | **Cloud**: OpenAI, Anthropic, Google, MistralAI, and others. **Local**: Ollama, llama.cpp, KoboldCpp, Text Generation WebUI, and vLLM. Supports custom prompts so you can ask your images questions. |
| Local           | Uses transformers.js (https://huggingface.co/docs/transformers.js/en/index) running locally inside your SillyTavern server. Zero setup!                                                                     |
| Horde                            | Uses the AI Horde (https://aihorde.net/) network, a crowdsourced distributed network of image generation models. Nothing to download, configure, or pay for. Variable response times.                       |
| Extras                           | The Extras project was discontinued in April 2024 and is not maintained or supported.                                                                                                                        |

### Caption Configuration
- **Caption Prompt**: Enter a custom prompt for captioning. The default prompt is "What's in this image?"
- **Ask every time**: Toggle to request a custom prompt for each image caption

### Message Template
- **Message Template**: Customize the caption message template. Use `{{caption}}` macro to insert the generated caption. The default template is `[{{user}} sends {{char}} a picture that contains: {{caption}}]`

### Auto-captioning
- **Automatically caption images**: Toggle to enable automatic captioning of images pasted or attached to messages
- **Edit captions before saving**: Toggle to allow editing captions before they are saved

## Captioning images

All the ways to caption images in SillyTavern:

* Choose "**Generate Caption**" from the **<i class="fa-solid fa-magic-wand-sparkles"></i> Extensions** popup menu and select an image file when prompted
* Click the <i class="fa-solid fa-envelope-open-text"></i> **Caption** icon at the top of an image already in a message
* Paste an image directly into the chat input with auto-captioning enabled
* Attach an image file to a message using the <i class="fa-solid fa-paperclip"></i> **Embed File or Image** button in the actions of a message.
* Send a message with an embedded image
* Use the `/caption` slash command

## Auto-Captioning
The auto-captioning feature allows you to automatically generate captions for images as they are added to the chat, without manually triggering the captioning process each time.

To enable, select the "Automatically caption images" checkbox in the Image Captioning panel. You can also choose to edit captions before they are saved by checking the "Edit captions before saving" box.

Once enabled, auto-captioning will trigger in the following scenarios:

- When an image is pasted directly into the chat input.
- When an image file is attached to a message.
- When a message with an embedded image is sent.

The system will use your selected captioning source (Local, Extras, Horde, or Multimodal) and the configured settings to generate a caption for the image.

### Editing captions before saving (Refine Mode)

If you've enabled the "Edit captions before saving" option:
1. After an image is added, a popup will appear with the generated caption.
2. You can review and edit the caption as needed.
3. Click "OK" to apply the caption, or "Cancel" to discard the caption without saving.

### Caption sending
The generated (and optionally edited) caption will be automatically inserted into the prompt using the Message Template you've configured. By default, it will be sent in this format:

```
[BaronVonUser sends Seraphina a picture that contains: ...]
```

## Slash Command: /caption
The extension provides a `/caption` slash command to use in the chatbox or in scripts. 

### Usage

```
/caption [quiet=true|false]? [mesId=number]? [prompt]
```

- `prompt` (optional): A custom prompt for the captioning model. Only supported by multimodal sources.
- `quiet=true|false`: If set to true, suppresses sending a captioned message to the chat. Default is false.
- `mesId=number`: Specifies a message ID to caption an image from an existing message instead of uploading a new one.

If no `mesId` is provided, the command will prompt you to upload an image. When `quiet` is false (default), a new message with the captioned image will be sent to the chat. The generated caption can be used as input for other commands.

### Examples
Caption a new image with the default settings:

```
/caption
```

Caption a new image with a custom prompt:

```
/caption Describe the main colours and shapes in this image
```

Caption an image from message #5 without sending a new message:

```
/caption mesId=5 quiet=true
```

Caption an image from message #10 with a custom prompt then generate a new image based on the caption:

```
/caption mesId=10 Describe this image using comma-separated keywords | /imagine 
```

## Local source

You can change the model in config.yaml. The key is called `extensions.models.captioning`. Enter the Hugging Face model ID you want to use. The default is `Xenova/vit-gpt2-image-captioning`. 

You can use any model that supports image captioning (`VisionEncoderDecoderModel` or "image-to-text" pipeline). The model needs be to compatible with the transformers.js library. That is, it needs ONNX weights. Look for models with the `ONNX` and `image-to-text` tags, or that have a folder called `onnx` full of `.onnx` files. 

## Multimodal source

### General configuration

- **Model**: Choose the model for image captioning. Options vary based on the selected API.
- **Allow reverse proxy**: Toggle to allow using a reverse proxy if defined and valid (OpenAI, Anthropic, Google, Mistral, xAI)

API keys and endpoint URLs for captioning sources are managed in the API Connections panel. Set the connection up in API Connections first, then select it as your captions source in Captioning.

**Set it up in the API Connections panel first**

One last time: configure the API key/address/port in **<i class="fa-solid fa-plug"></i> API Connections** and use the connection in Captioning.

You can still use Claude for chats and Google AI Studio for image captioning, or whatever. Just set them *both* up in the 'API Connections' tab first. Then flip your Chat Completion source to Claude and your Captioning source to Google AI Studio.

**For most local backends, you will need to set some options in the model backend rather than in SillyTavern. If your backend can only run one model at a time and doesn't support automatic switching, you have several options to use different models for chat and captioning:**

1. **Secondary endpoints:** Use the secondary endpoint feature (see Secondary endpoints section below) to connect to a different API server for captioning
2. **Multiple connection types:** Connect to your backend using both Text Completion and Chat Completion modes in API Connections - this gives you two separate connections to the same backend type

### Sources

To use one of these caption sources, select Multimodal in the Source dropdown.

* "I want the best captioning possible, and I don't mind paying for it": Anthropic
* "I don't want to pay anything or run anything": Google AI Studio free tier
* "I want to caption images locally and have it just work": Ollama
* "I want to keep the dream of local AI alive": KoboldCpp
* "I want to complain when it doesn't work": ~~Extras~~

| API Provider                      | Description                                                                                                                                                                   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AI/ML API                         | Cloud, paid, various GPT, Claude, and Gemini models with vision capabilities                                                                                                  |
| Chutes                            | Cloud, various models with vision capabilities                                                                                                                                |
| Claude                            | Cloud, paid, all Claude models with vision capabilities                                                                                                                       |
| Cohere                            | Cloud, paid, Aya Vision 8B / 32B                                                                                                                                              |
| Custom (OpenAI-compatible)        | For custom OpenAI-compatible APIs, uses currently configured model in API Connections tab                                                                                     |
| Electron Hub                      | Cloud, paid, various models with vision capabilities.                                                                                                                         |
| Google AI Studio                  | Cloud, free tier then paid, Gemini Flash/Pro                                                                                                                                  |
| Google Vertex AI                  | Cloud, free tier, Gemini Flash/Pro                                                                                                                                            |
| Groq                              | Cloud, llama-4 scout/maverick                                                                                                                                                 |
| KoboldCpp                         | Local, must configure model in KoboldCpp                                                                                                                                      |
| llama.cpp                         | Local, must configure model in llama.cpp                                                                                                                                      |
| MistralAI                         | Cloud, paid, pixtral-large, pixtral-12B, magistral, mistral-large, etc.                                                                                                       |
| Moonshot AI                       | Cloud, paid, moonshot-vision                                                                                                                                                  |
| NanoGPT                           | Cloud, paid, various GPT/Claude/Google models with vision capabilities                                                                                                        |
| Ollama                            | Local, can switch between available models and download additional vision models (https://ollama.com/search?c=vision) within Captioning after configuring in API Connections |
| OpenAI                            | Cloud, paid, GPT-4 Vision, 4-turbo, 4o, 4o-mini                                                                                                                               |
| OpenRouter                        | Cloud, paid (maybe free options), many models, pick from what's available within Captioning after configuring in API connections                                              |
| Pollinations                      | Cloud, free                                                                                                                                                                   |
| Text Generation WebUI (oobabooga) | Local, must configure model in ooba                                                                                                                                           |
| vLLM                              | Local                                                                                                                                                                         |
| xAI (Grok)                        | Cloud, paid, grok-vision                                                                                                                                                      |
| Z.AI (GLM).                       | Cloud, paid, GLM Vision models                                                                                                                                                |

### Secondary endpoints

By default, the Multimodal source uses the primary endpoint configured in the API Connections tab.
You can also set up a secondary endpoint specifically for multimodal captioning.

- Open the **Image Captioning** panel in the **<i class="fa-solid fa-cubes"></i> Extensions** panel.
- Select "Multimodal" as the captioning source and a preferred API provider.
- Enter a valid URL for the secondary endpoint in the "Secondary captioning endpoint URL" field.
- Check the "Use secondary URL" box to enable the secondary endpoint.

Do not append `/v1` or `/chat/completions` to the end of the URL. The extension will handle that automatically.

**This is only supported by the following APIs:**

- KoboldCpp
- llama.cpp
- Ollama
- Text Generation WebUI (oobabooga)
- vLLM

### Source-specific guides

#### KoboldCpp

For general information on installing and using KoboldCpp (https://github.com/LostRuins/koboldcpp), see the KoboldCpp documentation (https://github.com/LostRuins/koboldcpp/wiki).

To use KoboldCpp for multimodal captioning:

* get a multimodal-capable model, trained to process text and image prompts at the same time.
* also get the multimodal projections for the model. These weights allow the model to understand how the text and image parts of the input relate to each other.
* load the model and projections in the KoboldCpp launch GUI or command line interface.

The original and classic local multimodal model is LLaVA. GGUF-format files for the model and projections are available from Mozilla/llava-v1.5-7b-llamafile (https://huggingface.co/Mozilla/llava-v1.5-7b-llamafile). To load them from the command line, set the model and projections with the `--model` and `--mmproj` flags. For example:

```shell
./koboldcpp \
--model="models/llava-v1.5-7b-Q4_K.gguf" \
--mmproj="models/ llava-v1.5-7b-mmproj-Q4_0.gguf" \
... other flags ...
```

Some LLaVA finetunes you can try: xtuner/llava-llama-3-8b-v1_1-gguf (https://huggingface.co/xtuner/llava-llama-3-8b-v1_1-gguf), xtuner/llava-phi-3-mini-gguf (https://huggingface.co/xtuner/llava-phi-3-mini-gguf).

You can use multimodal projections for the base model that your particular finetune was built from. Projections for some common base models are available from koboldcpp/mmproj (https://huggingface.co/koboldcpp/mmproj/tree/main).

# SECTION: SillyTavern_extensions_Chat-vectorization

# Chat Vectorization

**Disclaimer**

The use of this extension does not guarantee a better chatting experience or improved memory of any sort. Only use if you understand all the implications of vector database utilization.

**Chat vectorization searches for messages in your current chat history that seem relevant to your most recent messages.**

It temporarily shuffles the most relevant messages to the beginning or end of the chat history. 
This happens when the model's reply to your last message is generated.

The messages at the start and end of the chat history tend to have the greatest impact on the model's reply. 
Therefore, shuffling relevant messages to these locations can help the model focus on relevant information in its reply. 

In particular, chat vectorization can find relevant messages that are too far back in the message history to fit 
into the request context. Shuffling these messages into context provides the model with information that it would not have otherwise.

Chat vectorization is a kind of retrieval-augmented generation (RAG). Retrieval-augmented generation increases the 
quality of responses generated by a model, by providing additional relevant information in the prompt.

* Retrieval: the most recent messages are used to retrieve relevant past messages
* Augmented: the model's context is augmented by inserting past messages in a useful way
* Generation: the model is instructed to use the past messages when generating the response

**Some terms:**

A *vector* is a set of numbers that could represent the themes, content, style, or other characteristics of a piece of text. 

*Vectorization* is calculating the vector that represents a piece of text. This is done by a vectorizing model.
Just as text generation models make text from text, vectorizing models make vectors from text.

*Vector search* finds relevant results by comparing vectors rather than, say, keywords. If we calculate the vector 
for a search query, we can compare it to the stored vectors for a collection of pieces of text. This finds the texts 
in our collection that are most similar to the text in the search query. In the case of chat vectorization, the 
"search query" is the most recent 2 messages, and the "texts in our collection" are all the other messages in the chat.

**## Setting up**

**Prompt Caching Compatibility**

Like any dynamic prompt source (World Info, Summarization, etc.), Chat Vectorization restructures the prompt prefix between the LLM calls, which can lead to frequent cache misses. When used with caching, vectorization is often counter-productive, as the modified prompts rarely hit the cache – effectively making caching useless. You have to choose one or the other, but not both.

**To enable Chat vectorization, select "Extensions" > "Vector Storage" > "Enabled for chat messages".**

Configure a vectorization source and vectorization model. Chat vectorization uses the same vector source as Data Bank, 
so you may have set this up already. The settings for the Vectorization Source and Vectorization Model are documented in Data Bank.

Chat vectorization uses the same vector storage as Data Bank, but this does not need to be set up or configured. 
There is also information about Vector Storage in Data Bank.

Chat vectorization does not use Data Bank to store the chat messages. The messages are stored in the chat. 

## Preparing chat messages for search (vector storage)

So that chat messages can be searched, a vector is calculated for each message and stored.

Vectorizing occurs in the background, whenever you send or receive a message.

Each message is stored individually, so that it can be found and shuffled individually during generation.

Large messages are split into "chunks" so that the model can be given the most relevant part of a long message. The chunk size is 400 characters. 
You can change this with "Chunk size (chars)". 

Messages are divided into chunks by finding a chunk boundary such as a paragraph break, line break, or space between words. This is so that 
all the chunks make sense, as far as possible. If your chat messages have some other way to mark natural splitting points, such as `----`, 
you can add this to "Chunk boundary". The setting for "Chunk boundary" is shared with Data Bank.

### Vector storage controls

To calculate vectors for all messages in the current chat, without waiting for them to be processed in the background, choose "Vectorize All" from the settings.

To see how many messages in the current chat have been vectorized, choose "View Stats". This displays the total number of vectors stored. 
It also indicates the specific chat messages that have been vectorized, by marking them with a green ball.

To remove all the vectors for messages in the current chat, choose "Purge Vectors".

**The controls for "Vectorize All" and "Purge Vectors" **within Chat vectorization** only affect the stored vectors for the current chat.**

However, there are identical buttons in File vectorization that affect the vectors for files in Data Bank. Ensure that you are purging the vectors that you intend to purge.

**## Finding relevant messages to shuffle (vector retrieval)**

To find the most relevant messages in the chat history, the most recent messages are converted (vectorized) into a query vector. By default, the 2 most recent messages are used. To change this, change the value of "Query messages". This value is also used when finding relevant content from Data Bank. 

Past messages must have a relevance score of at least 25% to be included. You can change this with "Score threshold". The setting for score threshold is shared with Data Bank.

The 3 most relevant messages from chat history are shuffled. You can change this with "Insert#".

To avoid disturbing the most recent events in the chat, the 5 most recent messages are not shuffled. To change this, change the value of "Retain#".

## Shuffling messages (augmented generation)

The messages are shuffled to one of 3 places:

* The top of the chat, after the Main Prompt / Story String (the default)
* The top of the chat and *before* the Main Prompt / Story String
* The end of the chat, before the last 2 messages ("In-chat @ Depth 2"). Since you just sent a message, this position is usually just before the previous reply from the model.

You can change this with "Injection Position" and "Depth".

The messages are included in order of relevance, with more relevant messages shown after less relevant messages.

The name of the person or character who sent each message is included. 

The messages are shown to the model as "past events". This assists the model to understand that the messages contain information from a different point in the chat history than the point at which they are inserted. You can change this with "Injection Template".

You can see the final prompt to the model using the Prompt Itemization popup, the terminal logs, or the browser console logs. The browser console logs are useful for understanding what all the steps in Chat vectorization are doing.

## Vector summarization

**Warning**

The Vector summarization feature is experimental.

**Vector summarization does not create summaries of your chat. It does not turn the retrieved messages into summaries. It does not make your chat history shorter. It is not "like Summarize but better".**

**Vector summarization is intended to make vector search of chat messages more effective. It does this by introducing a summarizing step prior to vectorizing. The summarizing step extracts the most important parts of the message, so that the resulting vector is a better indicator of what the message relates to.**

Vector summarization may make vector search less effective. 

To summarize the messages in the chat history, and generate a vector for each summarized message, choose "Summarize chat messages for vector generation". 

The summarized message does not replace the original message in chat. If a vector search matches the vector of a summarized message, the original message is retrieved from chat history and shuffled into context. The summarized versions of the messages are retained in Vector Storage, which may be of interest for debugging.

To summarize the content of the messages used to search the chat history (the last 2 messages by default), choose "Summarize chat messages when sending".

Each time a message is summarized for vectorizing, a separate request is made to the summarizing model. You can choose which summarizing source is used with "Summarize with". Choosing "Main API" will generate the summaries using the same model and connection settings that you use for generating chat or text completions.

The request consists of the raw message content and an instruction about how the model should produce the summary. You can change the instruction with "Summary Prompt".

# SECTION: SillyTavern_extensions_Dynamic-Audio

# Dynamic Audio

This guide will walk you through setting up and customizing dynamic audio assets for your SillyTavern experience.

## Prerequisites

Before you begin, ensure you've met the following prerequisites:

- Make sure you're on the latest version of SillyTavern.
- Install the "Dynamic Audio" extension from the "Download Extensions & Assets" menu in the Extensions panel (stacked blocks icon).

## Dynamic Audio Setup (Browser)

1. **Connect to the Assets Repository**:
   - Launch SillyTavern and navigate to **Extensions** > **Assets**.
   - Click on the "Connect" button to establish a connection to the official assets repository.
   - Download the desired audio assets, such as background music (BGM) or ambient sounds, that correspond to the backgrounds you intend to use.

2. **Enable Dynamic Audio Extension**:
   - In SillyTavern, go to **Extensions** > **Dynamic Audio**.
   - Enable the extension, unmute and adjust the volume of BGM and ambient sounds to your preference.
   - When bgm ends another one will play randomly, click on loop button to keep current bgm playing
   - Click on roll button to pick another bgm randomly

3. **Expression based BGM**:
   - Enable expression BGM switch if you want BGM to follow character expression (requires BGM in character folder see below).
   - Adjust the cooldown timer (in seconds) between BGM updates. Increase it if you find the BGM changes too frequently in group chats or when using character-specific BGM with emotion detection.

## Importing Music for Characters

To set up custom music for your characters' emotions, follow these steps:

1. **Navigate to Character Folder**:
   - Go to the characters folder, e.g., `\SillyTavern\data\<user-handle>\characters\Seraphina`.

2. **Create BGM Folder**:
   - Inside the character folder, create a subfolder named `bgm`.

3. **Import Emotion Music**:
   - Within the `bgm` folder, import the music files for each emotion. Supported audio extensions include `.mp3`, `.ogg`, and `.wav`.
   - Naming convention: `[emotion]_[number].mp3`, e.g., `anger_0.mp3`, `joy_0.mp3`.

4. **Multiple Tracks for Emotions**:
   - You can import multiple tracks for the same emotion by incrementing the number, e.g., `neutral_1.mp3`, `neutral_2.mp3`.

5. **Default Music Selection**:
   - When no emotion is detected, a random neutral track will play as the default. Emotions are detected similarly to updating sprites; refer to the expression images documentation for details.

## Changing Default BGM Music

If a character doesn't have custom BGM in their folder, a default track will play. Here's how you can change it:

1. **Navigate to BGM Folder**:
   - Go to the following folder: `\SillyTavern\data\<user-handle>\assets\bgm`.

2. **Replace/Add Music**:
   - Replace or add music files (`.mp3`, `.ogg`, `.wav`) to this folder.
   - These are the official audio assets downloaded using the assets extension.
   - One of these tracks will play randomly when no character-specific BGM is found (solo or group chat).

## Changing Ambient Sounds

Ambient sounds add depth to your scenes. Here's how you can customize them:

1. **Navigate to Ambient Folder**:
   - Go to the following folder: `\SillyTavern\data\<user-handle>\assets\ambient`.

2. **File Naming Convention**:
   - Ambient audio filenames correspond to background image filenames, replacing spaces with dashes.
   - Example: `"bedroom-clean.mp3"` corresponds to the "bedroom clean.jpg" background.
   - If the lock button is unlocked the audio file corresponding to the background will play. Activating lock will keep current ambient playing.

3. **Custom Ambients**:
   - You can add your own ambient sounds for custom or existing backgrounds by following the same naming pattern.

Thank you for following this guide! Your SillyTavern experience is now enriched with dynamic audio.

# SECTION: SillyTavern_extensions_EmulatorJS

# EmulatorJS

This extension allows you to play retro console games right from the SillyTavern chat.

## Installation

**Prerequisites:**

- Latest release version of SillyTavern.
- ROM files downloaded from the net. You can find them anywhere (https://archive.org/details/ni-romsets).

**How to install:**

1. Install using SillyTavern's extensions downloader.
2. Or use this link: `https://github.com/SillyTavern/SillyTavern-EmulatorJS`

## Usage

- Open the "EmulatorJS" extension menu.
- Click "Add ROM file". ROMs are saved to your browser storage and not stored on a server.
- Select the game file to add. Input the name and core (if it wasn't auto-detected). If the core requires a BIOS file, add it too.
- Click the "Play" button in the list or launch via the wand menu.
- You can customize controls and other settings in the emulator frame after launching the game.
- Use save/load state functions if you need to take a break.

Check the EmulatorJS docs to see the list of available cores and their requirements: Cores (https://emulatorjs.org/docs4devs/cores).

## Comments mode

With the power of multimodal models, your AI bots can see your gameplay and provide witty in-character comments.

### Requirements

1. A browser that supports ImageCapture (https://developer.mozilla.org/en-US/docs/Web/API/ImageCapture#browser_compatibility). Tested on desktop Chrome. Firefox requires enabling it via config. Safari won't work.
2. Chat Completion API with image inlining mode is recommended. Check the API documentation to see if the chosen model supports multimodal prompts.
3. If image inlining is disabled, make sure that the Image Captioning extension is enabled, then select the "Multimodal" captioning source.

### How to enable comments

1. Make sure you set the interval of providing comments in the EmulatorJS extension settings. This setting defines how often the character is queried for comments using an image of your current gameplay. A value of 0 indicates that no comments are provided.
2. Select a character chat and launch the game. For the best performance, make sure that the ROM file is properly named so that AI can have more background context.
3. Start playing as you normally would. The vision model will be queried periodically to write a comment based on the latest screenshot it "sees".

### Settings

1. Caption template - a prompt used to describe the in-game screenshot.`{{game}}` and `{{core}}` additional macros are supported.
2. Comment template - a prompt used to write a comment based on the generated caption. `{{game}}`, `{{core}}`, `{{caption}}` additional macros are supported. For image inlining mode, `{{caption}}` is replaced with `see included image`.
3. Force captions - will force the use of multimodal captioning even if image inlining is supported and enabled.

### Why am I not seeing any comments?

Comments are temporarily paused (interval step skipped) if:

1. Emulator is paused (with a pause button, not in-game).
2. The browser window is out of focus.
3. The user input area is not empty. This is to let you type your reply in peace.
4. Another reply generation is currently in progress.
5. TTS voice is being read aloud. Comment is held off (30 seconds maximum) until it finishes, but not skipped.
6. A character card or group is currently open. Comment mode is disabled when starting the game from a welcome screen.

Other common issues:

1. Make sure you've set a commenting interval before launching the game.
2. Make sure you have set a multimodal API key and there are no errors in the ST server console.

Still doesn't work? Send us your browser debug console logs (press F12).

## Credits

- EmulatorJS engine (GPLv3): <https://github.com/EmulatorJS/EmulatorJS>

# SECTION: SillyTavern_extensions_Expression-Images

# Character Expressions

## What is it?

Expression images are images (aka 'sprites') of your AI character which are shown next to (or behind) the chat window.

Expression images can automatically change based on a classification, adjusting to the sentiment expressed in the AI's most recent chat response.

## Adding Character Expression Images

1. Open the Extensions Panel and expand the 'Character Expressions' section. If you have the character chat open, you will see a grid of image placeholders.

2. Click the 'Upload image' button at the top left of each image in the grid, and select the image you want to apply to that emotion. This will save the image with the correct filename inside the `/data/<user-handle>/characters/(character_name_here)/` folder.
3. Repeat this for all expressions you want to assign an image to.

### Importing an Expression images ZIP file

Using the '<i class="fa-solid fa-file-zipper"></i> Upload sprite pack (ZIP)' button, you can import a zip file that contains a collection of expression images, and those images will automatically be added to the correct folder for your **currently selected character**. The ZIP file must contain all images in a flat structure (no subfolders) and correctly named files. Importing a zip will not automatically rename any images to make them match the emotions.

## Change Expressions Manually

1. Click on any of the uploaded expression images (sprites) to display them near the chat interface (with default UI mode) or at the center of the screen (in Visual Novel mode).
2. Use the `/expression-set (name)` slash command or matching Quick Reply to set the sprite without opening the extensions menu.

## Change Expressions Automatically

To automatically set expressions when the character replies, you have multiple options.
Expressions change per message or at regular intervals when message streaming is enabled.

### How does the classify module work?

The `classify` module uses a small 'sentiment parsing' model that runs alongside the SillyTavern server. This model takes the new output from the AI and detects what kind of sentiment, or emotion, the text is expressing. While multiple sentiments may be expressed in a single message, the model only picks the most likely one and returns that to the SillyTavern. The frontend extension then displays the image that is associated with that sentiment.

### Setup Instructions (Local)

1. Open the extensions panel and expand the "Character Expressions" extension menu.
2. Select "Local" in the classification source dropdown.
3. This will start a one-time download of the classification model from HuggingFace Hub (about ~100 Mb).
4. Generate any message to verify that the classification works and the sprite appears. You may also check the server console for debug logs.

Local classification defaults to 28 possible image labels: Cohee/distilbert-base-uncased-go-emotions-onnx (https://huggingface.co/Cohee/distilbert-base-uncased-go-emotions-onnx)

To use the 6-option classification model, change the value of `extensions.models.classification` variable in the `config.yaml` file to: Cohee/bert-base-uncased-emotion-onnx (https://huggingface.co/Cohee/bert-base-uncased-emotion-onnx)

### Setup Instructions (with LLM)

1. Connect to any of the supported and properly configured APIs via **<i class="fa-solid fa-plug"></i> API Connections**.
2. Import the expression images the same way as mentioned above.
3. Select "Main API" in the classification source dropdown.
4. Optionally, configure the classification instruction prompt.
5. Generate any message to verify that the classification works and the sprite appears. You may also check the server console for debug logs.

#### Prompt Building Strategies

Main LLM source allows to choose how the classification prompt will be built:

* **Limited Context**: Only the last message and a system instruction prompt are sent.
* **Full Context**: The entire chat history, including the character card are sent.

### Setup Instructions (WebLLM)

1. Install the official WebLLM extension (https://github.com/SillyTavern/Extension-WebLLM).
2. Import the expression images the same way as mentioned above.
3. Select "WebLLM" in the classification source dropdown.
4. Optionally, configure the classification instruction prompt.
5. Generate any message to verify that the classification works and the sprite appears. You may also check the server console for debug logs.

### Setup Instructions (with Extras)

> [!WARNING]  
> Extras is deprecated and may be removed in future updates.

1. Have Extras installed and running with the `classify` module enabled: `python server.py --enable-modules=classify`
2. Import the expression images the same way as mentioned above.
3. Select "Extras" in the classification source dropdown.
4. The appropriate expression image will display automatically whenever the AI sends you a response.

Extras API uses a classification model with 6 options by default: nateraw/bert-base-uncased-emotion (https://huggingface.co/nateraw/bert-base-uncased-emotion)

There is also a model with 28 options: joeddav/distilbert-base-uncased-go-emotions-student (https://huggingface.co/joeddav/distilbert-base-uncased-go-emotions-student)

To use this model you need to change your Extras command line to include the following argument (with a space before and after): `--classification-model=joeddav/distilbert-base-uncased-go-emotions-student`

## Custom Expressions

How to get more expression options than provided by default? You can set up **Custom Expressions** in the extension settings. You can assign any name to Custom Expressions. They will appear in the expression image list and can be assigned images like other expressions. They will have an indicator showing that those are custom.

> [!TIP]
> Both Local and Extras only support a limited list of expressions.
>
> If you want Custom Expressions to be displayed, you either need to train a classification model with supported labels (outside the scope of this guide), or you can use LLM or WebLLM as classification source, which both will automatically use all existing expressions - both the default and any custom ones.

## What image formats are supported for Expressions?

Any image format is allowed, including webp and animated gifs.

The most common format is a PNG file with a transparent background.

## Using Default Expressions

If you don't have expression images for all expressions of a character, or no images at all, there are multiple options on what to display by default.  
All of those can be selected via the dropdown under 'Default / Fallback Expression'.

1. **Choose a Fallback Expression**: If an expression gets chosen where you don't have an image for, the fallback expression gets shown instead. Simply select one of the available expressions from the dropdown.
2. **[No Fallback]**: When no image exists, show nothing.
3. **[Default emojis]**: You can use the built-in default expressions which are included within SillyTavern. These are simple emoji-style images.

## Using Multiple Images per Expression

It is possible to add multiple images per expression to allow for more variety in displayed expressions.  
To enable this, simply toggle **Allow multiple sprites per expression**.  
You can now upload more than one image, and any additional images will be displayed with a small marker.

Individual images can be manually chosen by selecting them with a click, or via `/expression-set type=sprite`, which will list available sprite images, instead of expressions.

Whenever an expression with multiple images gets automatically chosen, one of the existing images will be selected at random.  
If you want to force a new image of that expression to be chosen when the same expression gets used multiple times, you can enable **Re-roll if same sprite is used again**.

### Naming Convention for Multiple Images per Expression

In case of multiple images per expression, files need to be named a specific way.
The files need to start with the name of the expression, and then followed by a suffix, either separated by a dot or a dash. Examples: `joy.png`, `joy-1.png`, `joy.expressive.png`  
File names must follow this format for both direct uploads and ZIP imports.

## Sprite Folder Override

> [!NOTE]
> Display names (not character card filenames) dictate which image set is used

If you have more than one character with the same display name, they will both use the same set of expression images.

If you want a different image set to be used for each version of the same-named character, you can use the sprites folder override.  
Folder overrides can also be used to define different sprite sets (outfits, etc.) of the same character.

### How to set an override

1. Create a folder in the `/data/<user-handle>/characters` with any name and put images there, e.g. `/data/<user-handle>/characters/Boris`.
2. Open the chat with the character whose sprites you'd like to override.
3. Enter the name of the override folder into the "Sprite Folder Override" input and click "Submit".
4. The Sprites list will reload and the "Sprite set" indicator should show the override folder.
5. Alternatively, you can use the `/costume` slash command to achieve the same result: `/costume Boris`.
6. By prepending a backslash to the override folder name, it will resolve to a subfolder in the current character sprites folder, e.g. `/costume \tracksuit` for the character named Boris will resolve to the `/data/<user-handle>/characters/Boris/tracksuit` folder.

# SECTION: SillyTavern_extensions_Extras_index

**Discontinued**

The Extras project was discontinued in April 2024 and won't receive any new updates or modules. The vast majority of modules are available natively in the main SillyTavern application. You may still install and use it but don't expect to get immediate support if you face any issues.

# SECTION: SillyTavern_extensions_Extras_Smart-Context

# Smart Context

## **THIS EXTENSION IS NO LONGER MAINTAINED AND NOT RECOMMENDED TO USE. CONSIDER CHAT VECTORIZATION AS A POSSIBLE ALTERNATIVE.**

**Disclaimer**

The use of this extension does not guarantee a better chatting experience or improved memory of any sort. Only use if you understand all the implications of vector database utilization.

**### What is it?**

Smart Context is a SillyTavern extension that uses the ChromaDB library (https://www.trychroma.com) to give your AI characters access to information that exists outside the normal chat history context limit.

### How is that useful?

If you have a very long chat, the majority of the contents are outside the usual context window and thus unavailable to the AI when it comes to writing a response.

Smart Context automatically takes the entire history of the chat file and puts it into a vector database. This database is then searched each time you input something new into the chat, and if messages with matching keywords are found, those chat messages are placed into the context so the AI can see them when writing its next reply.

***

### Setup Instructions

1. Update SillyTavern to at least version 1.10.6.
2. Install the "Smart Context" extension from the "Download Extensions & Assets" menu in the Extensions panel (stacked blocks icon).
3. Install or Update Extras (https://github.com/SillyTavern/SillyTavern-extras) to the latest version. Alternatively, use the Colab notebook (https://colab.research.google.com/github/SillyTavern/SillyTavern/blob/release/colab/GPU.ipynb).
4. *Local installs only:* Install requirements-complete.txt for Extras (even if you did it once before in a prior install).
5. Run Extras with the chromadb module enabled: `python server.py --enable-modules=chromadb`

#### Getting an error when installing ChromaDB?

```
ERROR: Could not build wheels for hnswlib, which is required to install pyproject.toml-based projects
```

Installing chromadb package requires one of the following:

- Have Visual C++ build tools installed: <https://visualstudio.microsoft.com/visual-cpp-build-tools/>
- Installing hnswlib from conda: `conda install -c conda-forge hnswlib`

***

### Configuration

Once Smart Context is enabled, you should configure it in the SillyTavern UI.
Smart Context configuration can be done from within the Extensions menu 

There are 4 main concepts to be aware of:

- Chat History Preservation
- Memory Injection Amount
- Individual Memory Length
- Injection Strategy

***

#### SmartContext only starts after 10 messages are in the chat history

- At the start of a new chat, ChromaDB is inactive.
- Once the chat has accumulated 10 messages, it will begin recording all messages into the database, and recalling messages as needed.

#### Chat History Preservation ('kept messages')

By default, ChromaDB will keep as many recent natural chat history messages as specified in the slider.
Any messages beyond this amount will be removed from your sent prompt, and if 'memories' exist in the database they will be added in place of the older chat history messages (see Strategy below).

***

#### Memory Injection Amount

The maximum number of 'memories' Smart Context will insert into the context.
Not every injection attempt will get this full amount.
If you send an input related to 'dogs' and only one other message in the DB is related to dogs, then only 1 item will be inserted.

***

#### Individual Memory Length

This is the maximum length allowed for each injected 'memory'.
This is in **CHARACTERS** (not tokens).
If set too small, the memory could be cut off midway.

Example:

`Ross: I like dogs with long fur and fluffy tails. I dislike dogs with short fur and short tails.`

This database 'memory' is 103 characters long, so you would need to set the slider to at least `103` in order to pull it entirely into the context.

If the slider is less than 103, the message would be cut off and injected like that.

***

### Injection Strategy

#### Replace oldest history

This strategy keeps X recent messages, removes all message before that, and replaces them with 'memories'.

Advantage

- less likely to overflow your context limit
- memories existing near the top of the context will have less immediate impact on the response while still providing 'background information'.

Disadvantage

- old messages are inserted directly into the chat history with no special demarcation, and usually have no immediate natural relevance to the preserved natural chat history messages. This can confuse less intelligent AI models.

#### Add to Bottom

This strategy leaves the chat history in its natural state and adds 'memories' **after** it inside a formatted [bracket header].
This means the 'kept messages' slider is effectively disabled.

Advantage

- does not shorten or alter the current natural chat history
- 'memories' exist after chat and have a stronger impact on the next AI response

Disadvantage

- because no chat items are being removed/replaced, there is a higher chance you will overflow your context limit.
- because the memories exist very close to the end of the prompt they can have TOO MUCH effect on the AI's response.

#### Custom Depth

This strategy leaves the chat history in its natural state and adds 'memories' at the depth you determine within the template you specify.
This means the 'kept messages' slider is effectively disabled.
The custom injection message should include the `{{memories}}` template word which is where all queried memories will be placed.

Advantage

- flexibility to experiment with memory placement 
- customizable introductions to memory within context

Disadvantage

- because no chat items are being removed/replaced, there is a higher chance you will overflow your context limit.

#### Use % Strategy

Note: This is not compatible with the 'Add to Bottom' strategy, which does not remove any messages at all.

While using the 'Replace Oldest History' strategy, checking this box will enable the slider for selecting a percentage of the in-context chat history to replace with SmartContext memories. It will also disable the two sliders for manually selecting the number of messages.

This strategy automatically calculates a percentage of the chat history to be replaced with SmartContext memories, instead of a fixed number of messages.

Advantage

- easier than manually calculating the number of messages yourself
- adjusts with the available context size, applying the same percentage to small and large prompt spaces

Disadvantage

- calculations for how much history to remove can be slightly inaccurate as they are based on estimated tokens per message
- it rounds the number of messages to remove to the nearest number divisible by 5 (0, 5, 10, 15, 20, etc), so it is not as fine grained as manual numeric selection.

***

### Memory Recall Strategy

#### Recall only from this chat

This is the default behavior of smart-context and pulls 'memories' only from the ChromaDB collection for this specific chat.

#### Recall from all character chats

This is an experimental behavior of smart-context which pulls 'memories' from all ChromaDB collections for the selected character.
Hypothetically this should allow for the development of a more robust memory set spanning many interactions. 
Recommended that this be used with 'Add to Bottom' or 'Custom Depth' strategies and 'kept messages' set to a low number so that ChromaDB will pull from memory sooner.

### Using Smart Context

Once it is enabled and configured, Smart Context happens automatically.

ChromaDB makes a new database for each chat that is opened inside SillyTavern.
This database is automatically filled with the entire chat history.

You can also manually insert text files into the database.

These text files do not have to be chats. They can be anything (wikipedia entries, fanfic, etc).

#### Purging the Database

You can use the 'Purge DB' button to clear the database for the current chat.

This can be helpful if you find inaccurate memories have been stored (such as chat message you have since deleted or edited).

***

### FAQ

#### What happens to the databases when I'm done chatting? Can I save them?

For locally installed Extras servers, Smart Context saves the databases. There is no need to save them manually in usual use cases.

For colab users, the databases are wiped when the extras server shuts down. Use the export button to save the database as a JSON file, and import it next time you want to use it.

**Usually there is no need to save Smart Context databases.**

Currently we have an Import/Export feature, which allows you to save the chat's DB and use it again at a later date.

#### Can I make one big database for all of my chats to reference?

This would not be a good use of Smart Context's capabilities.
We recommend using World Info for this purpose.

# SECTION: SillyTavern_extensions_Extras_Talkinghead

# talkinghead

**THE SUPPORT FOR TALKINGHEAD WAS DROPPED IN SILLYTAVERN 1.12.13. THIS PAGE IS KEPT FOR HISTORICAL PURPOSES.**

**### What is it?**

An implementation of Talking Head Anime 3 Demo for AITuber. It possesses the following features:

- Generates random Live 2D-like motion actions from a single static image.
- Lip-syncs to the sound output from any TTS output.

This extension contains the original demo programs for the Talking Head(?) Anime from a Single Image 3: Now the Body Too project. As the name implies, the project allows you to animate anime characters, and you only need a single image of that character to do so. There are two demo programs:

The manual_poser lets you manipulate a character's facial expression, head rotation, body rotation, and chest expansion due to breathing through a graphical user interface, so you can save them as default expressions e.g., Happy, sad, joy, etc.
ifacialmocap_puppeteer lets you transfer your facial motion to an anime character.

### Hardware Requirements

You can use either CPU or GPU Modes (CPU is default). However, in CPU mode expect about 1 FPS, and in GPU mode on an RTX3060 I am getting about 9-10 FPS. 

The ifacialmocap_puppeteer requires an iOS device that is capable of computing blend shape parameters from a video feed. This means that the device must be able to run iOS 11.0 or higher and must have a TrueDepth front-facing camera. (See this page for more info.) In other words, if you have the iPhone X or something better, you should be all set.

### How to use

You must launch extras with the following modules for talkinghead to work: `classify` and `talkinghead`!
classify is required for the handling of the talkinghead.png file. Additionally, you may also use `--talkinghead-gpu` to load the blend models into GPU memory and make the animations 10x faster. It is highly recommended to use GPU acceleration! By default, once the program starts it will load a default image SillyTavern-extras\talkinghead\tha3\images\lambda_00.png. You can verify it is working by going to http://localhost:5100/api/talkinghead/result_feed or `YOUR EXT URL:PORT/api/talkinghead/result_feed`. 

- Once the server has started go to the Extension API tab and connect. Then simply select a character card to load. (`--enable-modules=classify,talkinghead --talkinghead-gpu` when starting server.py)

- Now select the Character Expressions, if you check the image type talkinghead box the script will replace your current character expression with the result of `YOUR EXT URL:PORT/api/talkinghead/result_feed` unchecking the box SHOULD return the image back to the original expression, however sometimes you have to send a new message to the chat to "reload" the image.

- If you do not have a talkinghead.png file in the character directory it will simply show either the default image or the last character card that had a talkinghead.png file. The animation source image is changed when the character card is changed. 

- Now open the character expressions scroll down to the talkinghead image and upload an image file that meets the requirements in the section below called "Constraints on Input Images".

- Then check and uncheck the talkinghead box to reload the character. If the image is funny looking it is probably because it is not transparent / has no alpha layer. Otherwise, follow the instructions and template below. 

### Constraints on Input Images
In order for the system to work well, the input image must obey the following constraints:

It should be of resolution 512 x 512. (If the program receives an input image of any other size, it will resize the image to this resolution and also output at this resolution.)
It must have an alpha channel.
It must contain only one humanoid character.
The character should be standing upright and facing forward.
The character's hands should be below and far from the head.
The head of the character should roughly be contained in the 128 x 128 box in the middle of the top half of the image.
The alpha channels of all pixels that do not belong to the character (i.e., background pixels) must be 0.

### ADVANCED SECTION

### Python Environment

In addition to the base feature (app.py), both manual_poser and ifacialmocap_puppeteer are available as desktop applications. To run them, you need to set up an environment for running programs written in the Python language. The environment needs to have the following software packages:

* Python >= 3.8
* PyTorch >= 1.11.0 with CUDA support
* SciPY >= 1.7.3
* wxPython >= 4.1.1
* Matplotlib >= 3.5.1

One way to do so is to install Anaconda and run the following commands in your shell:

> conda create -n talking-head-anime-3-demo python=3.8
> conda activate talking-head-anime-3-demo
> conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
> conda install scipy
> pip install wxpython
> conda install matplotlib

### Additional Blend Models

There is only one (lightest) model included, if you want the additional blend models you need to download the model files from https://www.dropbox.com/s/y7b8jl4n2euv8xe/talking-head-anime-3-models.zip?dl=0 and unzip it to the SillyTavern-extras\talkinghead\tha3\models folder. In the end, the data folder should look like:

+ tha3
  + models
    + separable_float
      - editor.pt
      - eyebrow_decomposer.pt
      - eyebrow_morphing_combiner.pt
      - face_morpher.pt
      - two_algo_face_body_rotator.pt
    + separable_half
      - editor.pt
          :
      - two_algo_face_body_rotator.pt
    + standard_float
      - editor.pt
          :
      - two_algo_face_body_rotator.pt
    + standard_half
      - editor.pt
          :
      - two_algo_face_body_rotator.pt

The model files are distributed with the Creative Commons Attribution 4.0 International License, which means that you can use them for commercial purposes. However, Pramook Khungurn. Talking Head(?) Anime from a Single Image 3: Now the Body Too. <https://github.com/pkhungurn/talking-head-anime-3-demo>, is the creator.

### Running the manual_poser Desktop Application
Open a shell. Change your working directory to the repository's root directory. Then, run:

> python tha3/app/manual_poser.py
Note that before running the command above, you might have to activate the Python environment that contains the required packages. 

> conda activate extras
if you have not already activated the environment.

# SECTION: SillyTavern_extensions_index

# Extensions

SillyTavern comes with many extensions that can be enabled or disabled in the Extensions panel. Extensions can add new
features, change the behavior of existing features, or provide additional content for your AI to use. More extensions
can be installed from the "Download Extensions & Assets" menu in the Extensions panel.

## Extensions panel

To open or close the Extensions panel, choose **<i class="fa-solid fa-cubes fa-fw"></i> Extensions** in the top bar.

- **<i class="fa-solid fa-cubes"></i> Manage extensions**: Activate, deactivate, and update extensions
- **Download Extensions & Assets**: Install more extensions, characters, sounds, and backgrounds from the SillyTavern repository
- **Notify on extension updates**: Check to be notified when there are updates available for installed extensions
- **<i class="fa-solid fa-cloud-arrow-down"></i> Install extension**: Import a third-party extension from a Git repository URL

## Built-in extensions

These extensions are built into SillyTavern and do not need to be installed. They can be enabled or disabled in the Extensions panel.

**Chat Translation**

Translate chat messages to a different language

**:::callout**

**Image Captioning**

Generates text from images so your AI can "see" and respond to visual content in your conversations

**:::callout**

**Image Generation**

Use local or cloud-based Stable Diffusion, FLUX or DALL-E APIs to generate images

**:::callout**

**Expression Images**

Images (aka 'sprites') of your AI character, shown next to or behind the chat window

**:::callout**

**Summarize**

Auto-summary of the chat history

**:::callout**

**Chat Vectorization**

Finds relevant messages from chat history and adds them into the context

**:::callout**

**Text To Speech**

Voice narration for your chat messages via ElevenLabs, Silero, your system TTS, **AllTalk**, **XTTS**, and more

**:::callout**

**Quick Reply**

Reply to chat messages with a single click, run commands and STscripts, and more

**:::callout**

**Token Counter**

Converts text into tokens and counts the number of tokens

**---**

## Installable extensions

You **must** have git installed to download extensions. Follow the instructions on the Git installation page (https://git-scm.com/downloads) if you don't have it installed.

**You can browse a list of all available extensions directly from the app by going to the **<i class="fa-solid fa-cubes"></i> Extensions** => **Download Extensions & Assets** menu and clicking the **<i class="fa-solid fa-plug-circle-exclamation"></i> Load Asset List** button. To install an extension, click the **<i class="fa-solid fa-download"></i> Download** button. To read more about an extension, click the **<i class="fa-solid fa-arrow-up-right-from-square"></i> Link** button next to its name to open its GitHub page.**

**Extensions are not Extras**

The Extras project was discontinued in April 2024. You do not need to install Extras to use extensions.

**:::callout**

**Blip**

Animate the text of character messages with variable speed and play sound along the animation.

**:::callout**

**Dynamic Audio**

Adds immersive background music and ambient sounds to your chats.

**:::callout**

**EmulatorJS**

Play retro console games directly in SillyTavern chats.

**:::callout**

**Live2d**

Adds support for live2d models. Customizable expressions, animations and interactions.

**:::callout**

**Objective**

Set an Objective for the AI to aim for during the chat.

**:::callout**

**RVC**

Adds Realtime Voice Cloning capabilities to the Text-to-Speech module.

**:::callout**

**Speech Recognition**

Convert your speech to text using browser or extras.

**:::callout**

**VRM**

Adds support for VRM models. Customizable expressions, animations and interactions.

**:::callout**

**Web Search**

Adds web search results to LLM prompts.

**:::callout**

**AccuWeather (https://github.com/SillyTavern/Extension-AccuWeather)**

Provides weather information using the AccuWeather API as a slash command or a function tool.

**:::callout**

**Chat Top Bar (https://github.com/SillyTavern/Extension-TopInfoBar)**

Adds a top bar to the chat window with shortcuts to quick actions.

**:::callout**

**Chess (https://github.com/SillyTavern/SillyTavern-Chess)**

Play the game of chess with the LLM.

**:::callout**

**Code Runner (https://github.com/SillyTavern/Extension-CodeRunner)**

Allows running JavaScript and STscript code from code blocks in chat.

**:::callout**

**D&D Dice (https://github.com/SillyTavern/Extension-Dice)**

A set of 7 classic D&D dice for all your dice rolling needs.

**:::callout**

**Duplicate Finder (https://github.com/SillyTavern/Extension-DupeFinder)**

Adds an ability to cluster characters by similarity groups to easily find duplicates.

**:::callout**

**Emoji Picker (https://github.com/SillyTavern/Extension-EmojiPicker)**

Adds a button to quickly insert emojis into a chat message.

**:::callout**

**Group Greetings (https://github.com/SillyTavern/Extension-GroupGreetings)**

Allows setting alternate greetings that are specific to group chats.

**:::callout**

**Group SendAs (https://github.com/SillyTavern/SillyTavern-GroupSendAs)**

Adds a button to quickly insert a /sendas command template for the selected group member.

**:::callout**

**HypeBot (https://github.com/SillyTavern/Extension-HypeBot)**

Show personalized suggestions based on your recent chats using the NovelAI's HypeBot engine. Requires an active NovelAI subscription.

**:::callout**

**Idle (https://github.com/SillyTavern/Extension-Idle)**

Adds "idle prompting" after the user has been idle for some time to organically continue the conversation.

**:::callout**

**Image Metadata Viewer (https://github.com/SillyTavern/Extension-ImageMetadataViewer)**

View metadata of enlarged images attached to a chat.

**:::callout**

**LaTeX (https://github.com/SillyTavern/Extension-LaTeX)**

Render LaTeX and AsciiMath formulas in chat messages.

**:::callout**

**Mermaid (https://github.com/SillyTavern/Extension-Mermaid)**

Adds Mermaid diagrams & flowcharts rendering to SillyTavern chats.

**:::callout**

**Notebook (https://github.com/SillyTavern/Extension-Notebook)**

Adds a place to store your notes. Supports rich text formatting.

**:::callout**

**Parameter Randomizer (https://github.com/SillyTavern/Extension-Randomizer)**

Adds ability to randomize API settings sliders with every generation.

**:::callout**

**Prome Visual Novel Extension (https://github.com/Bronya-Rand/Prome-VN-Extension)**

Enhances the current visual novel experience with more features (Focus Mode, Letterbox Mode, and more)!

**:::callout**

**Prompt Inspector (https://github.com/SillyTavern/Extension-PromptInspector)**

Adds an option to inspect and edit output prompts before sending them to the server.

**:::callout**

**Push Notifications (https://github.com/SillyTavern/SillyTavern-PushNotifications)**

Allows to receive push notifications for incoming chat messages.

**:::callout**

**Quick Persona (https://github.com/SillyTavern/Extension-QuickPersona)**

Adds a dropdown menu for selecting user personas from the chat bar.

**:::callout**

**RSS (https://github.com/SillyTavern/Extension-RSS)**

Gets the latest news from RSS feeds as a slash command or a function tool.

**:::callout**

**Screen Share (https://github.com/SillyTavern/Extension-ScreenShare)**

Provides the screen image for multimodal models when you send a message.

**:::callout**

**Silence Player (https://github.com/SillyTavern/Extension-Silence)**

Adds a silence audio player to the extensions menu. Can help if the browser tab is being killed in a background.

**:::callout**

**Timelines (https://github.com/SillyTavern/SillyTavern-Timelines)**

Adds a timeline navigation to the chat history.

**:::callout**

**Variable Viewer (https://github.com/LenAnderson/SillyTavern-Variable-Viewer)**

Easy way to view and modify variables.

**:::callout**

**WebLLM (https://github.com/SillyTavern/Extension-WebLLM)**

Provides an interface for extensions to use language models directly in the browser.

**## Third-party extensions**

Using third-party extensions can have unintended side effects and may pose security risks. 
Always make sure you trust the source before importing an extension via **<i class="fa-solid fa-cloud-arrow-down"></i> Install extension**. 
We are not responsible for any damage caused by third-party extensions.

**To install a third-party extension, go to the **<i class="fa-solid fa-cubes"></i> Extensions** => **<i class="fa-solid fa-cloud-arrow-down"></i> Install Extension** menu and paste the URL of the extension repository. Optionally, specify the branch and (in multi-user scenarios) the installation target: all users or just the current user. The extension will be downloaded and loaded automatically.**

# SECTION: SillyTavern_extensions_Live2d

# Live2D

This guide will walk you through the process of setting up and customizing the Live2D extension for your SillyTavern experience. This extension allows you to use Live2D animated models for your character, providing a dynamic and interactive element to your virtual character.

## Prerequisites

Before you begin, ensure you've met the following prerequisites:

1. **Branch Selection**: Make sure you're using the latest version of SillyTavern to access the latest features and updates.

2. **Extension Installation**: Install the "Live2D" extension from the "Download Extensions & Assets" menu in the Extensions panel (represented by the stacked blocks icon).

3. **Model Folder Placement**: Place your Live2D model folders into the `/data/<user-handle>/assets/live2d` directory. A properly organized `live2d` assets folder might look like this:

    

    - A Live2D model folder should include all necessary components for the Live2D model, such as expressions, motions, textures, sounds, and settings files. Notably the `***.model.json` file must be at the root of the Live2D model folder for the model to be detected by the extension. In this example the `shizuku` live2d model folder may look like this:

    

    - Note: Models can also be placed in character-specific folders, such as `/data/<user-handle>/characters/Shizuku/live2d/`. However, models in character folders will only be accessible for that specific character.

## Extension Settings

The Live2D extension offers various settings to customize the behavior of your animated model. Here are the key settings:

### Global Settings

1. **Enabled**:
   - Enable this checkbox to activate the extension, allowing your Live2D model to interact within SillyTavern.
   - You can disable the extension if you want to use normal sprites only.
   - You can disable the extension when you want to move normal sprites in a group chat and enable it again when you're ready to use Live2D models.

2. **Follow Cursor**:
   - Enable this checkbox to make the Live2D model follow your cursor, provided that the model supports this feature.

3. **Auto-send Interaction**:
   - Enable this checkbox to automatically trigger character interactions when you click on areas with mapped messages (refer to the hit areas section for details).

## Debug Settings

These settings help you control the behavior and visibility of your Live2D model for debugging purposes.

1. **Reset Model Before Animation**:
   - Enable this checkbox to reload the model before any animation. This forces the animation to start and allows you to spam clicks if necessary. Some models may require this to ensure that animations begin from a compatible state.

2. **Show Model Frames**:
   - Enable this checkbox to display the model frame, making it easier to identify where to click to drag the model around. It also shows the hit area, if available. Hovering over a hit area will show its name.

3. **Reload button**
    - Click this button to reload every live2d model. Use it in case something glitches.

## Character Selection

These settings allow you to manage characters and assign Live2D models to them.

1. **Refresh Button**:
   - Click the refresh button to update the list of characters in the current chat.

2. **Select Character**:
   - Use the drop-down list to choose a character to assign a Live2D model to.

3. **Remove Button**:
   - Click this button to delete all assigned models for a character. A confirmation prompt will appear to confirm the deletion.

## Model Selection

1. **Refresh Button**:
   - Click the refresh button if your Live2D model does not appear in the list.

2. **Select Model**:
   - Choose a model from the list to assign it to the selected character.
   - The model can be located in the asset folder or the current character's folder.
   - The list displays the model folder name, its origin (asset or character), and the name of the detected model setting file.
   - Note that some model folders may contain different versions of the same model. You can try different model files to see which one works best.
   - Selecting none will use normal sprites if there are any
   - Settings are saved per character and model

## Model Settings

1. **Model Scale**:
   - Use the slider to adjust the size of the model, making it larger or smaller.

2. **Model Center X Offset**:
   - Use the slider to change the horizontal position of the model relative to the window center.

3. **Model Center Y Offset**:
   - Use the slider to adjust the vertical position of the model relative to the window center.

### Remarks
- The settings are saved and carry over different chats.
- You can also drag the model with your mouse, and those settings will be updated and saved.
- Use these UI settings to bring your model back on the screen if you somehow made it out of view. Also, check the "Show frame" checkbox to see clearly where you can click to drag the model.

## Model Talk

1. **Param mouth open Y id**
    - Select from the list the ID of the parameter corresponding to the model's mouth Y value. Not all models have one, and names may vary from model to model. Usually something like "PARAM_MOUTH_OPEN_Y" or "ParamMouthOpenY". Check the model when selecting an element from the list; it will try to run the speak animation. If the mouth moves, you got it!

2. **Mouth movement speed**
    - Adjust the slider to change the movement speed of the mouth animation.

3. **Time per character**
    - Set the time duration of each character. The duration of the talk animation will be this time multiplied by the number of characters of the message.

### Remarks
- This mouth animation does not work on every model and every animation. Even if your model has animations where the mouth moves, it does not mean the mouth animation can be controlled by this extension. If nothing shows in the parameter list, your model is probably made with a too old version of Live2D to access the parameters properly.

## Model Animations

1. **Starter animation**
    - Select an expression and motion from the lists that will play when starting a chat with the character. You can also add a delay during which the model will be invisible if you need to hide the character for some time to achieve a perfect effect.

2. **Default animation**
    - Select an expression and motion from the list that will play when the character sends a message. Use a fallback animation when using the classify expression extension.

### Remarks
- Animations will play when you select one in the lists.
- Use the replay button to replay the selected animation.
- Some models have expressions defined as motions.
- If nothing shows in the lists, it's probable your model's setting file has no expressions/motions defined.

## Hit areas mapping

1. **Default click animation**
    - Select an expression and motion from the list that will play when you click on the model. You can also set a message that will be sent as a user message.

2. **Hit areas**
    - If the model has hit areas, they will be listed, and you can assign an animation/message to each of them.

### Remarks
- Some models have no hit areas, but the default click is detected for all.
- The default click will trigger if you click on a hit area with nothing mapped or if you click outside of any hit area.
- Hit areas have priority defined in the model; for example, "mouth" is inside "head." If it does not behave properly, it may be due to the model file.
- For some models, animations need to be finished before starting another one. Use the debug checkbox if you want to force the refresh and spam animations.

## Classified Expressions Mapping

1. **Requirements**
    - Requires the use of the classify expression extension; otherwise, it will fall back to the default animation.

2. **Mapping**
    - For each detected emotion by the classify extension, you can assign an expression/motion animation.

### Remarks
- If the previous animation did not finish when a new message is received, it's possible that the new animation will not play. This behavior is dependent on the Live2D model. Use the debug checkbox if you want to force the animation to play.

Thank you for following this guide! Your SillyTavern experience is now enriched with animated and interactive Live2D models.

# SECTION: SillyTavern_extensions_MiniMaxTTS

# MiniMax TTS

This page will teach you how to properly use the MiniMax TTS provider.

## Prerequisites

1. MiniMax account with API access
2. Valid API Key and Group ID from MiniMax

## Getting API Credentials

### 1. Create a MiniMax Account

1. Visit the MiniMax website (International) (https://www.minimax.io/)
2. Click "Sign Up" or "Login"
3. Complete the account registration process

**Regional Differences**

MiniMax has separate Chinese and International versions. Please note:
- The Chinese version does not support voice cloning features
- The Chinese version only supports the `api.minimax.chat` API host

**### 2. Obtain API Key and Group ID**

1. Log into the MiniMax console (International) (https://www.minimax.io/platform/user-center/basic-information)
2. You can find your GroupId on the Basic Information page
3. Go to Settings → API Keys on the left sidebar to create and obtain your API Key

## Configuration in SillyTavern

### 1. Basic Setup

1. Open SillyTavern
2. Navigate to "Extensions" → "TTS"
3. Select "MiniMax" as your TTS provider
4. Configure the following settings:
    - **API Key**: Your MiniMax API key
    - **Group ID**: Your MiniMax Group ID
    - **API Host**: Choose the appropriate server based on your region:
        - `api.minimax.io` (Official international server)
        - `api.minimaxi.chat` (Another international server host)
        - `api.minimax.chat` (China mainland server)

### 2. Model Selection

Available models include:
- **Speech-02-HD**: High-quality voice synthesis (recommended)
- **Speech-02-Turbo**: Fast voice synthesis
- **Speech-01**: Legacy model
- **Speech-01-240228**: Legacy model (specific version)

### 3. Voice Parameters

Adjust the following parameters to customize voice output:
- **Speed**: 0.5 - 2.0 (1.0 = normal speed)
- **Volume**: 0.1 - 2.0 (1.0 = normal volume)
- **Pitch**: 0.5 - 2.0 (1.0 = normal pitch)
- **Audio Format**: MP3, WAV, FLAC

## Custom Voices

### 1. Obtaining Voice IDs

1. Access the MiniMax TTS page (International) (https://www.minimax.io/audio/text-to-speech)
2. Click "Voice" on the right side to enter the Voice Selection interface
3. Find the voice you want to use
4. Click the copy button next to the voice name to copy the Voice ID

### 2. Adding Custom Voices

1. In the MiniMax TTS settings, locate the "Custom Voice Management" section
2. Fill in the following information:
    - **Voice Name**: Choose any name for identification
    - **Voice ID**: The voice ID obtained from the MiniMax platform
    - **Language**: Select the corresponding language for the voice
3. Click "Add Custom Voice"

## Custom Models

### 1. Adding Custom Models

1. In the "Custom Model Management" section
2. Fill in:
    - **Model ID**: Model identifier
    - **Model Name**: Display name for the model
3. Click "Add Custom Model"

### 2. Obtaining Model IDs

1. Check the model list in the official MiniMax documentation (https://www.minimax.io/platform/document/Model?key=684261f14c5738213294faa7)
2. Or view available custom models in the console
3. Copy the corresponding Model ID

## Troubleshooting

### Common Issues

1. **API Authentication Failed**
    - Verify that the API Key corresponds to the correct API Host
    - Confirm that the Group ID is correct
    - Check if your account has sufficient balance

2. **Voice Generation Failed**
    - Verify that the selected Voice ID is valid
    - Ensure the voice is compatible with your selected model

3. **Connection Timeout**
    - Try switching to a different API Host
    - Check your network connection
    - Verify firewall settings

4. **Audio Quality Issues**
    - Try using a different model (Speech-02-HD for best quality)
    - Adjust voice parameters (speed, pitch, volume)
    - Check audio format compatibility

# SECTION: SillyTavern_extensions_Objective

# Objective

### What is it?

The Objective extension lets the user specify an Objective for the AI to strive towards during the chat. This objective is broken down into step-by-step tasks. Tasks may be branched, where child tasks can be created automatically or manually. This gives the ability to create complex task trees. The completion status of each task in the list will be checked at certain intervals.

This differs from adding static direction through prompting in that it adds sequential and paced directives for the AI to follow without user intervention. It gives a more genuine experience of the AI autonomously striving to reach a goal.

### Prerequisites

Before you begin, ensure you've met the following prerequisites:

- Make sure you're on the latest version of SillyTavern.
- Install the "Objective" extension from the "Download Extensions & Assets" menu in the Extensions panel (stacked blocks icon).

### Common Use Cases

Your imagination is the limit, you can give the AI any objective you wish and it will plan out how to achieve it. You can ask it to plan how to slay a demon, rob a temple, throw a lavish party, or even take over the world.

### Configuration

- The extension is found in the Extensions menu under Objective.

- Type an objective into the top text box, then click on `Auto-Generate Tasks`. This sends a request to the connected API and asks it to provide  a list of tasks which match the objective you have typed in.

*Note: Clicking Auto-Generate Tasks will delete all existing tasks for the currently selected Objective before adding new ones.*

- Upon receiving the response from the AI, a list of tasks will be created automatically in the space below the Objective input box. Tasks can be edited after creation.

- At the bottom of the panel are two boxes: `Position in Chat` and `Task Check Frequency`
  - `Position in Chat` - This is how 'deep' in the chat section of the prompt you want the current task to be inserted. The lower the number, the more attention the AI will give to the task. Setting to 0 will make the task the primary thing in the AI's mind. Setting at high values will put the task in the background and allow the AI to focus on the conversation at hand, but setting it too high may cause the AI to never 'get around' to the task at all.
  - `Task Check Frequency` - This is how often you want the AI to check if the task has been completed. If it is set to `3`, the AI will be asked if the current task has been completed every 3rd message.

-  Objectives, tasks, and their descriptions are saved in real-time to the current chat session. Custom prompts are saved globally.

### Custom Prompts
You can customize the prompts sent to the LLM to generate tasks, check task completion, and for prompt injection. Editing prompts will save them for the current session. Custom prompts can be saved and loaded for persistence.

- Click Edit Prompts to open the prompt editor window. You can edit your prompts as desired.
- To save prompts, enter a name and click Save Prompt.
- To load prompts, select the prompt from the dropdown list.
- To delete a saved prompt, select it from the dropdown list and click Delete Prompt

**WARNING: Task Checking happens in a separate API request. Setting Task Check Frequency to 1 will double your API calls to the LLM service. Be careful with this if you are using a paid service.**

### Usage

By default the Objective extension will keep track of all tasks and their respective completion status automatically.

The User can also manually create, update, delete, and complete tasks at any time.

#### Current Task Selection

The current task will always be the first listed incomplete task. Any manual updates to tasks will trigger a check for what the current task should be. So if you add a task above a bunch of completed tasks, it will be set as the current task. Once it's completed, previously completed tasks will be skipped and the next incomplete task will be selected as 'Current'.

When using parent/child tasks in a task tree, tasks are selected depth-first, meaning all child tasks will be selected in order first, then continue down the list of tasks for the current Objective/Task.

#### Branch Tasks

Click the Branch Task button to set the current task as an Objective where you can auto generate or manually create tasks as child tasks. You can continue to turn any child task into an Objective and keep generating to your heart's content.

Marking a parent task as complete will cause the extension to skip all subtasks. When all child tasks are complete, the parent task will be marked as complete

#### Manually Complete Tasks

You can manually toggle the completion status of a task by `clicking the checkbox` next to it. This will set the next incomplete task to be selected.

#### Manual Task Check

If you want to manually trigger the AI to check for task completion, click on the Extras Extension button (the `magic wand` on the right side of the chat input bar) and select `Manual Task Check`.

#### Manually Add Tasks

When no tasks are present, an `Add Task` button is visible, allowing you to manually create the first task.

If other tasks are already present, click the `+` button to the right of any task to insert a new task after it.

#### Delete Tasks

Click the red `x` to delete an existing task. The next incomplete task will be selected as the current task automatically.

Deleting a task with child tasks will delete all child tasks and their descendants. 

#### Hiding Tasks

If you want to remain unaware of what tasks the AI is attempting to complete, check the `Hide Tasks` box to hide the task list and make the AI's intentions a mystery. For 100% mysteriousness, do this before clicking `Auto-Generate Tasks`!

# SECTION: SillyTavern_extensions_Regex

# Regex

## What is it?

The Regex extension lets the user automatically detect specific patterns in a string of text (called 'sequences') and apply manipulations (replacements) to them. It can be a powerful tool when used in conjunction with other SillyTavern features such as Quick Replies or STscript, or simply a way to remove certain words from a chat.

## Helpful Links

**This document will not explain the process of writing a RegEx sequence in depth. There are many online resources to assist you with that.**

- https://regexr.com (https://regexr.com)

- https://regex101.com (https://regex101.com)

- https://extendsclass.com/regex-tester.html (https://extendsclass.com/regex-tester.html)

- https://en.wikipedia.org/wiki/Regular_expression (https://en.wikipedia.org/wiki/Regular_expression)

## Prerequisites

Regex is a built-in extension of SillyTavern, so no additional setup is required.

You may find its settings in the **<i class="fa-solid fa-cubes"></i> Extensions** panel.

## Common Use Cases

RegEx is often used to apply a find-replace function on certain words in the chat, to add markdown styles to certain words or sentence types, or to return a boolean value to an STscript.

## Script List

- The buttons at the top are used to make a new script.
  - 'Global' scripts will apply to all characters and will be saved into `settings.json`.
  - 'Scoped' scripts will only apply to the currently active character, and will be saved into the character card's data.
- 'Import' lets you import RegEx scripts which were exported from another instance of SillyTavern.

Below this is a list of your scripts with some action buttons.

- Drag handles (three horizontal bars to the left of the script name) let you drag/drop the scripts into any order you like.
- Primary on/off switch can be quickly toggled to enable or disable the script without changing anything else. Disabled scripts are shown with ~~strikethrough~~ styling. **If a script is disabled here, it will be untriggerable by a Quick Reply or STscript.**
- 'Edit' (pencil) button will open the RegEx script editor.
- 'Move to scoped' (down arrow) will convert a global script to a scoped script and apply it to the current character. In reverse (up arrow), it would convert a scoped script to global.
- 'Export' will cause your browser to download an exported `.json` file of the Script, which can then be shared and imported into another instance of SillyTavern.
- 'Delete' (trashcan) deletes the script.

## RegEx Editor

- **Test Mode** : This will open a comparison view at the top of the editor. Type some text into the 'Input' box, and the results of your RegEx script will be shown in the Output box. It is a valuable debug tool as it will update the Output box in real time as you make changes to the script settings.

- **Name** : The label for the script shown on the extension's script list. **This is also used to target the script when triggering it via slash command or STscript.**

- **Find Regex** : This is the Regular Expression that is used to detect your targeted text pattern. This is usually the most complex part of any RegEx script, and is the easiest place to make mistakes. Refer to the links at the top of the page for information how to write a RegEx sequence. This box can resolve the values of common SillyTavern macros (such as \{\{user\}\}, \{\{char\}\}, etc) if the 'Macros in Find Regex' is set to do so (see below).

- **Replace With**: This is what will replace the matched sequence. In a very simple example, if your 'Find Regex' is `apple`, and your 'Replace With' is `orange`, the first occurrence of 'apple' would be automatically changed to 'orange' in any text where the script is applied.

  - Adding the extension-specific macro \{\{match\}\} in this box will insert the full matched sequence of text. This is commonly used to apply styles to specific words. Going back to the above example, if \*\*\{\{match\}\}\*\* were put into the 'Replace With' box instead, all occurrences of the word 'apple' would be replaced with `**apple**`, which would apply the bold markdown style to it.

  - Variables such as $1, $2, $3 etc can be used to insert what are called 'Capture Groups'. These are substrings located in the text sequence matched by the 'Find Regex' sequence. **Note that using these variables requires the matching expression to contain sets of parentheses to define which part of the matched string counts as a captured group.** Refer to the links at the top for reference on how to set up Capture Groups.

- **Trim Out** : text put in this box will be removed from the matched text sequence before the 'Replace With' process is applied. For example, if our match was 'apple', and the Trim Out box contains 'le', then the letters 'le' would be removed first before the 'Replace With' process is applied. Since our 'Replace With' box contains \*\*\{\{match\}\}\*\* it would result in `**app**` being put in as the replacement for 'apple' (first 'le' is removed, and the remaining matched text is given the bold markdown style). Multiple trims can be applied by adding a newline between each string you want to remove.

- **Affects** : This list of checkboxes defines the text sources to which the RegEx script will be applied.
  - 'User Input': script will be run against the contents of the user's typed input after they hit Send.
  - 'AI Response': script will be run against the contents of the AI's response after it is received.
  - 'Slash Commands': script will be run against the values inserted into prompt/chat by slash commands.
  - 'World Info': script will be run on against contents of World Info entries as they are injected into the prompt. **Requires 'Alter Outgoing Prompt' to be checked (or both ephemerality boxes to be unchecked).**
  - 'Reasoning': script will be run against the contents of the 'reasoning' object returned by Chat Completion API's like Gemini or Deepseek. If 'Alter Outgoing Prompt' is checked under Ephemerality, the script will also be applied to any reasoning blocks that are added into prompt in subsequent chat turns.
  - **If everything here is unchecked the script will never activate during normal chatting, but it can still be activated via slash command or STscript.**

- **Other Options** :
  - 'Disabled' prevents the script from running. This is used as an override to prevent the script from running when you simply don't want to change any of the script's settings and/or don't want to disable it entirely via the switch on the script list (as doing so would prevent slash commands from triggering it).
  - 'Run on Edit' makes the script also run after a chat message has been edited. If this is unchecked, the contents of edited chat messages will not trigger the script.

- **Macros in Find Regex** : Select whether or not to replace macros (such as \{\{user\}\}, \{\{char\}\}, etc) that are present in the Find Regex box's sequence.
  - 'Don't Substitute' will cause any SillyTavern macros to be ignored so the RegEx script will treat them literally when searching.
  - 'Raw' will send in the value of the macro verbatim. This might alter the way your RegEx script searches the text if the value of the macro contains certain special characters.
  - 'Escaped' will add a RegEx escape slash `\` before each character to ensure they do not accidentally alter the overall RegEx sequence. This can be useful if you have certain special characters in the values of the macro.

### Depth Settings

The Min/Max Depth settings provide precise control over which messages in the chat history your regex pattern will affect:

- **Min Depth**: Only affects messages that are at least N levels deep in the chat history
  - 0 = last message
  - 1 = second-to-last message
  - etc.
  - When blank (set to 'Unlimited'), or -1, will also affect the message to continue on the Continue action

- **Max Depth**: Only affects messages no deeper than N levels in the chat history
  - Must be greater than Min Depth for the regex to apply
  - System prompts and utility prompts are not affected by these settings

For example, setting Min Depth to 0 and Max Depth to 2 would only apply your regex to the three most recent messages in the chat.

### Flags

By default the Find Regex pattern is case-sensitive and applies only to the first match. To adjust this behavior, as well as other RegEx flags, you can add them like so:

```txt
/yourpattern/flags
```

Example: `/yourpattern/gi` will match all instances of 'yourpattern' in the text, regardless of case.

Some of the most common flags are:

- `i` : case-insensitive
- `g` : global (applies to all matches, not just the first)
- `s` : dotAll (treats the input as a single line, so `.` will match newlines)
- `m` : multi-line (treats the input as multiple lines, so `^` and `$` match the start/end of each line, not just the whole string)
- `u` : unicode (treats the input as unicode, so `\d`, `\w`, etc. will match unicode characters)

For more information on RegEx flags, see the following MDN page: Advanced searching with flags (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions#advanced_searching_with_flags)

### Ephemerality

By default (when neither box here is checked) a RegEx script will directly edit the text values stored inside the chat's JSONL file. This ensures both the outgoing prompt and the chat display will always contain the same values. However, these changes to the chat file are irreversible.

If you do not want this to happen, you can enable either of the checkboxes here to limit the RegEx script's affects to only the display or the outgoing prompt.

If only one of the boxes is checked, there will be no changes made to the chat file, but **only the checked item** will be changed. This means you will be seeing one thing, but the LLM will be seeing another. Use this carefully.

If both are selected, the script will function as normal in all ways EXCEPT it will not write any changes to the chat file.

## Advanced Use

While RegEx is commonly used as a simple Find/Replace tool, it can also be used in more complex ways.

For example the 'Replace With' box could include a set of CSS rules and HTML to add a specific styled HTML element into your chat whenever a certain word is found. This will require the `Show <tags> in responses` box to be unchecked in the User Settings panel.

The script can also be set to never trigger during normal use, but could instead be triggered via slash command as part of a logic check inside an STscript. The 'Replace With' box would include a unique value the script recognizes to indicate if a logic check is true or false. This expands the utility of RegEx to the full capabilities of all slash commands, allowing for truly unlimited levels of control and automation based on the contents of the chat.

# SECTION: SillyTavern_extensions_RVC

# Retrieval-based Voice Conversion (RVC)

This guide will walk you through using RVC, a technique that allows transferring voice features from one audio clip to another, enabling voices to speak in different tones and styles.

Ever enjoyed those famous "Presidents Play X" videos? They were created using RVC. With the RVC extension, you can make your SillyTavern characters speak in any voice you desire, be it anime, movie, or even your own unique voice.

RVC is NOT TTS: it's more like speech-to-speech. It takes an audio clip as its input. In the background, what RVC does is work in tandem with SillyTavern's TTS extension: it waits for TTS to generate an audio file (which TTS would've done regardless of whether you use RVC or not), then RVC will perform a second pass that takes the TTS audio file and transforms it into the cloned voice from your RVC configuration.

## RVC Setup

SillyTavern's RVC supports several API sources that perform audio conversion:

* rvc-python (https://github.com/daswer123/rvc-python)
* SillyTavern Extras (https://github.com/SillyTavern/SillyTavern-Extras) (deprecated)

### Common prerequisites

Before you begin, ensure you've met the following prerequisites.

#### ffmpeg

Make sure you have `ffmpeg` binary in your PATH environment variable. This tool is used to convert incoming audio.

**Windows**:

* Use the Toolbox in SillyTavern Launcher script to install ffmpeg automatically: <https://github.com/SillyTavern/SillyTavern-Launcher>
* Or download the build here: <https://www.gyan.dev/ffmpeg/builds/>
* How to modify PATH variable: <https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/>
* To test whether you did things correctly, open a command prompt and run ```ffmpeg```. It should print the ffmpeg version and info.

**Linux**:

Install ffmpeg using your package manager.

```shell
# Debian/Ubuntu
sudo apt install ffmpeg
# Arch Linux
sudo pacman -S ffmpeg
# Fedora
sudo dnf install ffmpeg
```

**macOS**:

Install ffmpeg using Homebrew (https://brew.sh/):

```shell
brew install ffmpeg
```

#### Make sure TTS is enabled and works

RVC depends on TTS; you need to enable a TTS extension. Your TTS has to be already working properly and narrating your chats before you try to add RVC to the mix!

Please note that:

* System TTS engine does not support voice conversion at all.
* Streaming TTS will wait for the audio stream to end before conversion.

#### Install the extension

Install the "RVC" extension from the "Download Extensions & Assets" menu in the Extensions panel (stacked blocks icon).

#### Enable RVC in SillyTavern*

In SillyTavern, navigate to **Extensions** > **RVC** and enable it.

#### Pick the source

In the extension settings, choose an RVC source to use. Then proceed to the source-specific installation instructions.

### rvc-python Setup

#### 1. Install the package

Follow the installation instructions from the GitHub page: rvc-python Installation (https://github.com/daswer123/rvc-python?tab=readme-ov-file#installation). It is recommended to follow CUDA installation instructions if you have an Nvidia GPU.

If you're experiencing problems when installing on Windows (e.g. building fairseq step fails), make sure the following software is installed on your PC:

* Windows 10 SDK (https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/)
* Visual Studio Build Tools 2022 (https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022)

#### 2. Prepare the models

Create a directory for storing RVC models. By default it is named `rvc_models` and is picked up from your current directory when starting up the server. Every model is a subfolder (its name will be visible in the UI) that should contain `.pth` (required) and `.index` (optional) files.

Read more: rvc-python Model Management (https://github.com/daswer123/rvc-python?tab=readme-ov-file#model-management)

#### 3. Start the API server

Start the API server by running the following command:

```shell
python -m rvc_python api -p 5050 -l -md models_path
```

**Arguments:**

* `5050` - sets a listening port for the server. Change if you want to host on a different port.
* `models_path` - sets a path for models. Remove if you want to use the default `rvc_models` directory.
* `-l` - sets the server to listen on all network interfaces. Remove to only listen on localhost.

#### 4. Connect to the server

* In the RVC extension settings, set an appropriate **rvc-python API URL**. By default, it will be `http://localhost:5050`.
* Check the **Use CUDA** checkbox if you have installed rvc-python to support CUDA acceleration.
* Press "Refresh" to load a list of available voices.

#### 5. Configure a voice map

**Voice map defines voice conversion settings for every character or user persona.**

* To set up a voice map, choose your character or persona name from the "Character" dropdown, then choose an RVC "Voice", then click Apply.
* Optionally, you can also configure other related settings such as pitch correction or filtering.
* If you did everything correctly, the Voice Map debug area will show something like 'Betty:MyVoice(rmvpe)'.

### SillyTavern Extras Setup

#### 1. Prepare RVC Model Files

* In a file browser, navigate to: `\SillyTavern-extras\data\models\rvc`.
* Create a subfolder like 'Betty' and place the `.pth` and `.index` files into it. (Hint: you can download voice files from https://voice-models.com, make sure the voice name says it's RMVPE.)

#### 2. Install Requirements

Install the necessary requirements using the command:

```shell
pip install -r requirements-rvc.txt`
```

#### 3. Run SillyTavern-extras with RVC enabled

Launch SillyTavern-extras with the RVC module enabled. This example invocation assumes you used Edge TTS which comes pre-installed with SillyTavern-extras:

```shell
python server.py --enable-modules=rvc,edge-tts
```

Optionally, you may wish to run RVC on your GPU if you have a capable one, by adding ```--cuda``` to the startup command. Based on a quick test, VRAM usage was 3.4GB for narrating 50 tokens (~36 words), and 7.6GB for 200 tokens (~150 words).

#### 4. Set Up Voice Mapping

Create a Voice map for RVC. Set your Character to your desired SillyTavern character name, and set Voice to the RVC folder you created at step 1, then click Apply. If you did things correctly, the Voice Map will show something like 'Betty:MyVoice(rmvpe)'.

#### 5. Select Pitch Extraction

* Choose "rmvpe" as the pitch extraction method.
* If you have trouble with "rmvpe" try other methods (for example, "harvest" or "torchcrepe").

#### 6. (Optional) Configure RVC to save your generations to file

If for testing or troubleshooting purposes you wish to save the generated RVC audio, add ```--rvc-save-file``` to your startup command. This will save the last generation under `SillyTavern-extras/data/tmp/rvc_output.wav`:

```shell
python server.py --enable-modules=rvc,edge-tts --rvc-save-file
```

#### Expression-Based Dynamic Voice

##### 1. Configure RVC Models

In your RVC model folder, have separate `.pth` and `.index` files for each classified expression (e.g., anger, fear, joy, love, sadness, surprise).

##### 2. Enable Modules

Enable both RVC and classify modules:

```shell
python server.py --enable-modules=rvc,classify
```

##### 3. Use RVC Module

The remaining setup is similar to using the RVC module alone (as explained above).

## Train Your Own RVC Model

### Using RVC Easy Menu by Deffcolony (Windows Only)

Automatically install and launch Mangio-RVC: https://github.com/deffcolony/rvc-easy-menu

#### 1. Clone Repository

Clone the repository to your desired location:

```shell
git clone https://github.com/deffcolony/rvc-easy-menu.git
```

#### 2. Launch RVC-Launcher.bat

* Open the `RVC-Launcher.bat` file.
* Choose option 1 to install RVC.

#### 3. Complete Installation

When prompted, install required packages and dependencies.

#### 4. Open WebUI for Voice Training

After installation, choose option 2 to open the WebUI for voice training.

### Mangio-RVC: Training a Voice Model

***Dataset Preparation***:

**1. Prepare Audio**:

* Place the audio you want to train in the `datasets` folder.
* Ensure the audio is free of background noise – only raw voice is needed.
* Longer audio makes a better output quality.

***WebUI Training***:

**1. Access Training Tab**:

* Click on the training tab in the WebUI.

**2. Configure Experiment**:

* Enter an experiment name (e.g., `my-epic-voice-model`).
* Set version to v2.

**3. Process Data and Extract Features**:

* Click "Process data" and "Feature extraction".
* Set "Save frequency" to 50.

**4. Training Parameters**:

* Set "Total training epochs" to 300.
* Click "Train feature index" and "Train model".

# SECTION: SillyTavern_extensions_Speech-Recognition

# Speech Recognition

This guide will walk you through setting up speech recognition to transcribe your voice into text within SillyTavern.

## Prerequisites

Before you begin, ensure you've met the following prerequisites:

- Make sure you're on the latest version of SillyTavern.
- Install the "Speech Recognition" extension from the "Download Extensions & Assets" menu in the Extensions panel (stacked blocks icon).

## Speech Recognition Setup (Browser)

1. **Configure SillyTavern**:
   - Launch SillyTavern and go to **Extensions** > **Speech Recognition**.
   - Select "Browser" from the dropdown options.
   - If your browser doesn't support voice recognition, an error popup will appear.

2. **Select Message Mode**:
   - Choose the "Message Mode" you want:
     - **Append**: Your message will be appended to the current user message text area.
     - **Replace**: Your message will replace the current user message in the text area.
     - **Auto send**: Your message will automatically be sent once the end of speech is detected.

3. **Enable Message Mapping** *(Optional)*:
   - Setup phrases mapping for vocal shortcuts.
   - For instance, by adding "command delete = /del2", the "/del2" command will replace your voice message when "command delete" is detected.
   - Useful when combined with auto send mode for full voice control. Enable this by checking "Enable messages mapping".

4. **Select Language**:
   - Choose the language you want to speak (Note: not every browser supports all languages).

5. **Recording**:
   - To start recording, click the microphone button to the right of the message area next to the send button. Click again to stop recording. Recording may stop automatically if no voice is detected.

## Speech Recognition Setup (API Sources)

Supports sources like OpenAI, MistralAI, Groq, Chutes, Z.AI, and others that provide speech-to-text APIs.

To set up:

1. Provide an API key for the chosen provider in the Chat Completion API settings.
2. Launch SillyTavern and go to **Extensions** > **Speech Recognition**.
3. Select the desired API source from the dropdown options.
4. Configure additional settings as needed, similar to the "Browser" provider setup.

## Speech Recognition Setup (Extras) - Deprecated

**Requires ffmpeg binary installed. See RVC setup for more details.**

**1. **Enable Provider**:**

   - Enable the desired speech recognition provider on the extras server using the following command:
     ```shell
     python server.py --enable-modules=whisper-stt
     ```
     or
     ```shell
     python server.py --enable-modules=vosk-stt
     ```
   - You can also use a custom model by adding the option `--stt-vosk-model-path` or `--stt-whisper-model-path` with the path to the model.

2. **Configure SillyTavern**:
   - Launch SillyTavern and go to **Extensions** > **Speech Recognition**.
   - Select "Vosk" or "Whisper" from the dropdown options (whisper is more accurate).
   - The settings are similar to the "Browser" provider setup (except for language) see above.

## Speech Recognition Setup (Streaming) - Deprecated

**Requires ffmpeg binary installed. See RVC setup for more details.**

**1. **Enable Provider**:**

   - Enable the streaming speech recognition module on Sillytavern-extras with the following command:
     ```shell
     python server.py --enable-modules=streaming-stt
     ```

2. **Configure SillyTavern**:
   - (Optional) Specify a custom Whisper model as in the Whisper setup above.
   - (Optional but recommended) Set up trigger words in SillyTavern. Only messages starting with these trigger words will be sent to SillyTavern as actual messages. This prevents random speech or noise from being transcribed. Enable this with the checkbox. The trigger words can be included/excluded from the actual message using a checkbox.
   - Other settings are similar to other providers.

You're now ready to transcribe your voice into text using speech recognition in SillyTavern.

# SECTION: SillyTavern_extensions_Stable-Diffusion

# Image Generation

Use local or cloud-based Stable Diffusion, FLUX or DALL-E APIs to generate images.

Automatically generate images as replies to your messages for full immersion, 
generate from chat history and character information from the wand menu or slash commands, 
or use the `/sd (anything_here)` command in the chat input bar to make an image with your own prompt.

Most common Stable Diffusion generation settings are customizable within the SillyTavern UI.

- Supports multiple image generation sources, both local and cloud-based
- Various generation modes for characters, scenes, and custom prompts
- Slash commands for easy image generation within chats
- Interactive mode to trigger image generation based on natural language requests
- Customizable prompt templates and prefixes for consistent style and quality
- Character-specific prompt prefixes for tailored character images
- Style presets to quickly switch between different image generation settings
- Flexible visibility options for generated images in chat
- Advanced ComfyUI integration for highly customizable workflows
- Ability to view all generated images in a character gallery
- Image swipes feature to regenerate images while keeping the same prompt
- Options to edit prompts before generation and extend free-mode prompts
- Integration with AI function calling for automatic image generation detection
  
## Supported sources

| Source                                                                                            | Remarks                                                                                         |
|:--------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| AI/ML API (https://aimlapi.com/)                                                                 | Cloud, paid                                                                                     |
| Black Forest Labs (https://bfl.ai/)                                                              | Cloud, paid                                                                                     |
| Chutes (https://chutes.ai/)                                                                      | Cloud                                                                                           |
| ComfyUI (https://github.com/comfyanonymous/ComfyUI)                                              | Local, open source (GPL3), free of charge, see ComfyUI Configuration. |
| Draw Things (https://drawthings.ai/)                                                             | Local, Mac/iOS, free of charge                                                                  |
| Electron Hub (https://electronhub.ai/)                                                           | Cloud, paid                                                                                     |
| FAL.AI (https://fal.ai/)                                                                         | Cloud, paid                                                                                     |
| Google AI Studio (https://aistudio.google.com/) / Google Vertex AI (https://cloud.google.com/vertex-ai) | Cloud, paid. Imagen model series. AI Studio supports less models.                       |
| HuggingFace Serverless (https://huggingface.co/docs/api-inference/index)                         | Cloud, free of charge                                                                           |
| NanoGPT (https://nano-gpt.com/)                                                                  | Cloud, paid                                                                                     |
| NovelAI Diffusion (https://novelai.net/)                                                         | Cloud, requires an active subscription                                                          |
| OpenAI (https://platform.openai.com/)                                                            | Cloud, paid                                                                                     |
| OpenRouter (https://openrouter.ai/)                                                              | Cloud                                                                                           |
| Pollinations (https://pollinations.ai/)                                                          | Cloud, open source (MIT), free of charge                                                        |
| SD.Next / vladmandic (https://github.com/vladmandic/automatic)                                   | Local, open source (AGPL3), free of charge                                                      |
| SillyTavern Extras (https://github.com/SillyTavern/SillyTavern-Extras)                           | Deprecated, not recommended                                                                     |
| stable-diffusion.cpp (https://github.com/leejet/stable-diffusion.cpp)                             | Local, open source (MIT), free of charge                                                        |
| Stability AI (https://platform.stability.ai/)                                                    | Cloud, paid                                                                                     |
| Stable Diffusion WebUI / AUTOMATIC1111 (https://github.com/AUTOMATIC1111/stable-diffusion-webui) | Local, open source (AGPL3), free of charge                                                      |
| Stable Horde (https://stablehorde.net/)                                                          | Cloud, open source (AGPL3), free of charge                                                      |
| TogetherAI (https://docs.together.ai/docs/serverless-models#image-models)                        | Cloud                                                                                           |
| x.AI (https://x.ai/)                                                                             | Cloud, paid                                                                                     |
| Z.AI (https://z.ai/)                                                                             | Cloud, paid                                                                                     |

## Generation modes

| Wand menu item     | Slash command argument | Description                                    | Remarks                               |
|:-------------------|:-----------------------|:-----------------------------------------------|:--------------------------------------|
| "Yourself"         | `you`                  | A full-body portrait of the current character. | -                                     | 
| "Your Face"        | `face`                 | A close-up portrait of the current character.  | Forces a portrait aspect ratio.       |
| "Me"               | `me`                   | A portrait of the user persona.                | -                                     |
| "The Whole Story"  | `scene`                | A visual recap of the chat events.             | -                                     |
| "The Last Message" | `last`                 | A visual recap of the last chat message.       | -                                     |
| "Raw Last Message" | `raw_last`             | Last message used as a prompt verbatim.        | -                                     |
| "Background"       | `background`           | A chat background based on story context.      | Forces a wide landscape aspect ratio. |

## How to generate an image

1. Use the "Image Generation" item in the extensions context menu (wand).
2. Type a `/sd (argument)` slash command with an argument from the Generation modes table. Anything else would trigger a "free mode" to make SD generate whatever you prompted. Example: `/sd apple tree` would generate a picture of an apple tree.
3. Look for a paintbrush icon in the context actions for chat messages. This will force the "Raw Message" mode for the selected message.

Every generation mode besides raw message and free mode will trigger a prompt generation using your currently selected main generation API to convert chat context into the SD prompt.
You can configure the instruction template for generating prompts for every generation mode using the "SD Prompt Templates" settings drawer in the extensions panel.

### Tips and tricks for the `/sd` command usage

#### View all generated images

To view all saved images for a character (including other chats), open a gallery from a "More..." dropdown menu on a character info panel, or use a `/show-gallery` slash command.

#### Specify a negative prompt

Use a `negative` named argument before the prompt to enforce a specific negative prompt for this generation.

```stscript
/sd negative="fries" cute tater farmer holding a tayto in a spud-field
```

#### Include a character-specific prefix

Use a special `{{charPrefix}}` macro in free-prompt mode to include positive and negative prompt prefixes (if defined) for the current character.

```stscript
/sd {{charPrefix}}, riding a bike
```

#### Suppress a chat message

You can avoid posting a generated image into the chat by passing a `quiet=true` named argument. The image will still be added into the character gallery, and the command will produce a relative URL to the image that can be consumed by other commands.

The example below will send the generated image using Markdown as a user persona.

```stscript
/sd quiet=true me | /send Here's a picture of me: 
```

### Image swipes

Image swipes allow rerolling the image generation while keeping the same prompt. If a fixed seed is set, it will be randomized for the next generation. 

To cycle through images, hover a mouse cursor (tap on mobile) over a generated image to reveal arrow buttons and swipes counter. Tapping the right arrow on the latest image will generate a new one.

*'Swipes' here is just a name, don't try the actual swiping gesture, as this will regenerate the message itself, not the attached image.*

## Options

### Edit prompts before generation

Allow to edit the automatically generated prompts manually before sending them to the Stable Diffusion API.

### Use function tool

Uses function calling to automatically detect the intention to generate an image.

**Requirements:**

1. Must have image generation configured with a supported source.
2. Must use a supported Chat Completion API model and have function tool calling enabled in the AI Response settings.
3. The "Use function tool" option must be enabled in the Image Generation settings.
4. The user should express an intent to generate an image in the chat message, e.g. "Send me a picture of a cat".

The interactive mode will not trigger when the function tool is enabled.

**### Use interactive mode**

Allows you to trigger an image generation instead of text as a reply to a user message that follows the special pattern:

1. Contains one of the following verbs: send, mail, imagine, generate, make, create, draw, paint, render
2. Followed by one of the following nouns (not further than 10 characters away): pic, picture, image, drawing, painting, photo, photograph
3. Followed by a target subject of image generation, could be optionally preceded by phrases like "of a" or "of this".

Examples of valid requests and captured subjects:

* `Can you please send me a picture of a cat` => `cat`
* `Generate a picture of the Eiffel tower` => `Eiffel tower`
* `Let's draw a painting of Mona Lisa` => `Mona Lisa`

Some special subjects trigger a predefined generation mode:

* 'you, 'yourself' => "Yourself"
* 'your face', 'your portrait', 'your selfie' => "Your Face"
* 'me', 'myself' => "Me"
* 'story', 'scenario', 'whole story' => "The Whole Story"
* 'last message' => "The Last Message"
* 'background', 'scene background', 'scene', 'scenery', 'surroundings', 'environment' => "Background"

### Extend free-mode prompts

When using the interactive mode of the slash command, automatically extend free-mode generation subject descriptions by prompting your main API.

### Minimal prompt processing

When enabled, reduces the processing applied to prompts returned by the LLM for image generation. Only normalization and whitespace reduction are performed, skipping the aggressive sanitization that is done by default. This is useful when working with advanced workflows (e.g., ComfyUI) that accept structured prompt formats like JSON.

### Snap auto-adjusted resolutions

Snap image generation requests with a forced aspect ratio (portraits, backgrounds) to the nearest known resolution, while trying to preserve the absolute pixel counts. Refer to the "Resolution" dropdown for the list of possible options.

**Recommended for SDXL models**.

## Common prompt prefix

**Pro Tip**

Use `{prompt}` macro to specify where exactly the generated prompt will be inserted.

**Added before every generated or free-mode prompt. Commonly used for setting the overall style of the picture.**

Example: `best quality, anime lineart`.

## Negative prompt

Characteristics of the image you don't want to be present in the output.

Example: `bad quality, watermark`.

## Character-specific prompt prefix

**Pro Tip**

If supported by the generation source, you can also use LoRAs/embeddings here, for example: `<lora:DonaldDuck:1>`.

**Any characteristics that describe the currently selected character. Will be added after a common prefix.**

Example: `female, green eyes, brown hair, pink shirt`.

You can also specify a negative prompt prefix for any unwanted content. It will be combined with the general negative prompt.

Limitations:
1. Works only in 1-to-1 chats. Will not be used in groups.
2. Won't be used for backgrounds and free mode generations.

To force include a character prefix into a free mode prompt, use the `{{charPrefix}}` macro anywhere in the prompt.

**If you want to share the prefixes with others, tick the "Shareable" checkbox. This will save them with the character data, rather than your local settings.**

## Styles

Use this to quickly save and restore your favorite style/quality presets to use them later or when switching between models. The following is included in the Style preset:

1. Common Prompt Prefix
2. Negative Prompt

You can also switch between styles using the `/imagine-style` command (or `/sd-style` or `/img-style`).

## Chat Message Visibility

Generated images inserted into the chat are hidden in the main API prompts by default, but this can be overriden individually per generation initiator ("Magic wand" icon, slash command, interactive mode). This can be used for making the experience more immersive by letting the characters "acknowledge" the images. Multimodal models in Chat Completions API may also 'see' the images if "Send inline images" is enabled.

A text message can be customized by changing the "Chat Message Template" under Image Prompt Templates. All regular macros can be used in this template, plus a special `{{prompt}}` macro to specify where the image prompt will be added.

## ComfyUI Configuration

ComfyUI (https://github.com/comfyanonymous/ComfyUI) is a fast and very flexible option for image generation. 

If you're familiar with ComfyUI, the tl;dr is: make your workflow in ComfyUI, download it **in API format**, and paste it into the SillyTavern ComfyUI Workflow Editor. ST will submit your workflow to ComfyUI's API and you will get an image in your chat. But with great power comes great responsibility, and the main responsibility is inserting placeholders in your workflow JSON so you can change settings from SillyTavern.

If you're not familiar with ComfyUI, you can still use it to generate images in SillyTavern using the default workflow. Later, when you want great power, you can learn how to use ComfyUI...

### Controls

This panel allows you to configure and manage your ComfyUI integration with SillyTavern.

#### Server Type

* Standard Server is when you call ComfyUI directly whether on your local machine or hosted elsewhere.
* RunPod Serverless Endpoint is for running ComfyUI through RunPod's serverless API (https://www.runpod.io/product/serverless). Serverless can be a good option for remote generation as you can get the same control over workflows as a standard server but can take advantage of more powerful hosted GPUs and only be charged when you're actively generating images. The majority of the usage is the same. Differences from standard server setup and behavior is described below.

#### Standard Server setup

Enter the URL of your ComfyUI server in the **ComfyUI URL** input field. The default value is `http://127.0.0.1:8188`. 
If you are using SwarmUI (https://github.com/mcmonkeyprojects/SwarmUI), the default port for the 
managed ComfyUI server (https://github.com/mcmonkeyprojects/SwarmUI/blob/master/src/BuiltinExtensions/ComfyUIBackend/README.md) is `7821`, 
20 ports higher than the default port for SwarmUI.

After entering the URL, choose <i class="fa-solid fa-check"></i> **Connect** to validate and establish a connection. The ComfyUI server must be accessible from the SillyTavern host machine.
 
#### ComfyUI RunPod Setup

* You'll need a RunPod account and to add some money to it. You can probably expect around 2 cents per image for Qwen image generation on an RTX 4090 though YMMV. $5 in credits should last a while.
* <https://console.runpod.io/hub/runpod-workers/worker-comfyui> is a flux1 dev configuration that you can use to create your own serverless endpoint.
  * There is information there on creating your own configuration if you want to use a different model or add LoRAs.
* Create an API key for access to the serverless endpoint: <https://console.runpod.io/user/settings>

* In ST, select **ComfyUI** as the **Source** and **RunPod Serverless Endpoint** as the **Server Type**.
* Set the **ComfyUI RunPod URL** to the URL of your endpoint.
* Set the API key.
* Click **Connect**. If the API key and URL are correct, you should get toasts indicating success.
* The ComfyUI workflow configuration flow is the same as local.
  * Use the "Export (API)" option.
  * Depending on your local setup, you may need to/want to pick a variation of the model for use on RunPod. For example, if you use a quantized GGUF locally, but want to use an fp16 version on RunPod. The JSON workflow you use in ST needs to have this change.
  * Model, samplers, VAE, etc cannot be determined dynamically so your workflow needs to have these hard coded (no `%model%` substitution).
  * Other substitutions should work the same as local.

**Note**

The serverless configuration does not currently embed the workflow into the output image. i.e., you won't be able to drag/drop the image into local ComfyUI to see the seed or prompt. This is just a limitation of the RunPod handler and is a capability that could be added on that side.

**### Workflow Management**

Select a ComfyUI workflow from the dropdown menu. Two default workflows are provided:

- Default_Comfy_Workflow.json: A basic text-to-image workflow supporting the most common image generation settings.
- Char_Avatar_Comfy_Workflow.json: A sample image-to-image workflow that uses the character avatar, plus the prompt, to generate an image.

Use the following buttons to manage your workflows:

- <i class="fa-solid fa-pen-to-square"></i> **Open workflow editor** to view and modify the selected workflow.
- <i class="fa-solid fa-plus"></i> **Create new workflow** to create a new workflow with a custom name.
- <i class="fa-solid fa-trash-can"></i> **Delete workflow** to remove the selected workflow.

### Workflow Editor

The ComfyUI Workflow Editor allows you to view and modify ComfyUI workflows for use with SillyTavern.

The main component of the editor is a large text area where you can insert or edit your ComfyUI workflow in JSON format.

To add a ComfyUI workflow to the editor, follow these steps:

1. Enable 'Dev Mode' in ComfyUI settings.
2. Use the 'Save (API Format)' option in ComfyUI to download the JSON data.
3. Create a new workflow in SillyTavern and open the editor.
4. Paste the downloaded JSON data into the text area.
5. Replace specific values with placeholders as needed for your use case.

**Tips**

You can add the API-format JSON file directly to the `data/default-user/user/workflows` directory in your SillyTavern installation. This will save you from steps 3 and 4.

Retain the original JSON file. If you need to open the workflow again in ComfyUI to make changes, it is much more convenient to edit the original file than the one with all the placeholders.

**### Placeholders**

The editor provides a list of predefined placeholders that can be used in your workflow JSON. These placeholders are replaced with dynamic values when the workflow is executed in SillyTavern.

Placeholders marked with ✅ are present in your workflow JSON. Placeholders marked with ❌ are not present in your workflow JSON. You can add these placeholders to your workflow JSON as needed. You do not need to add all the placeholders, only the ones that your workflow uses and you want to replace dynamically.

#### Prompts

The `%prompt%` and `%negative_prompt%` placeholders are used to insert the image generation prompts into the workflow. These contain the final prompts generated by SillyTavern, including the generated prompt for your chosen `/sd` mode, the common prompt prefix, negative prompt, and character-specific prompt prefix.

For example, you may have tested your workflow with a prompt like "forest elf" in ComfyUI. To use this workflow in SillyTavern, you can replace the "forest elf" prompt with the `%prompt%` placeholder:

+++ JSON with placeholder
```json
{
    "class_type": "CLIPTextEncode",
    "inputs": {
        "clip": ["4", 1],
        "text": "%prompt%"
    }
}
```
+++ Original JSON
```json
{
    "class_type": "CLIPTextEncode",
    "inputs": {
        "clip": ["4", 1],
        "text": "forest elf"
    }
}
```
+++

Notice that the placeholder is wrapped in double quotes. This is important for the JSON format, and required by SillyTavern's placeholder replacement system. Even for numbers, you must use double quotes in the template JSON.

Sometimes the prompt (or other value) doesn't appear where you might expect. ComfyUI will remove nodes from the API version of the workflow if they are not necessary for the workflow to function in API mode. 

For instance, this workflow uses a LoRA tag loader node (https://github.com/badjeff/comfyui_lora_tag_loader) with a prompt primitive so the workflow is clearer in UI mode:

The prompt primitive node will be removed from the API version of the workflow, so you insert the placeholder in the LoraTagLoader node. Find the text "apple tree" in the workflow and replace it with the `%prompt%` placeholder:

+++ JSON with placeholder
```json
{
    "inputs": {
      "text": "%prompt%",
      "model": ["112", 0],
      "clip": ["112", 1]
    },
    "class_type": "LoraTagLoader",
    "_meta": {"title": "Load LoRA Tag"}
}
```
+++ Original JSON
```json
{
    "inputs": {
      "text": "apple tree",
      "model": ["112", 0],
      "clip": ["112", 1]
    },
    "class_type": "LoraTagLoader",
    "_meta": {"title": "Load LoRA Tag"}
}
``` 
+++

In some cases you may need to make several replacements in the workflow JSON, even if the prompt appears only once in the UI. 

#### Model

The `%model%` placeholder will insert the value of the selected model in the image generation settings. 

An example from the default text-to-image workflow:

+++ JSON with placeholder
```json
{
    "class_type": "CheckpointLoaderSimple",
    "inputs": {
        "ckpt_name": "%model%"
    }
}
```
+++ Original JSON
```json
{
    "class_type": "CheckpointLoaderSimple",
    "inputs": {
        "ckpt_name": "sd15.safetensors"
    }
}
```
+++

To load GGUF-quantized UNets, use a UNet Loader (GGUF) (https://github.com/city96/ComfyUI-GGUF) node in your workflow, 
choose a `GGUF` model in the SillyTavern model dropdown, and use the `%model%` placeholder in the node's settings like this:

+++ JSON with placeholder
```json
{
    "inputs": {
      "unet_name": "%model%"
    },
    "class_type": "UnetLoaderGGUF",
    "_meta": {
      "title": "Unet Loader (GGUF)"
    }
}
```
+++ Original JSON
```json
{
    "inputs": {
      "unet_name": "flux1-dev-Q4_0.gguf"
    },
    "class_type": "UnetLoaderGGUF",
    "_meta": {
      "title": "Unet Loader (GGUF)"
    }
}
```
+++

**If you have model types other than the usual SD checkpoints in ComfyUI**

Stable Diffusion checkpoints, SD UNets, and GGUF-quantized UNets all appear in the Model dropdown.
Models of one type will not work with workflows/loader nodes expecting another type.
If you choose an incompatible model type in ST, ComfyUI will report a problem with the loader node.

**#### Avatar images**

Use the `%user_avatar%` and `%char_avatar%` placeholders to include the user and character avatars in the workflow. These placeholders are replaced with the PNG data of the avatars when the workflow is executed. The image data is encoded in base64 format, so you must decode it in your workflow. A popular choice for this task is the Load image (Base64) (https://github.com/Acly/comfyui-tooling-nodes) node.

In this example, the character avatar is loaded with a `Load Image (Base64)` node. It also uses an Image Resize node to rescale the image to whatever size is specified in the image generation settings:

Insert the `%char_avatar%`, `%width%`, and `%height%` placeholders into the JSON for the Load Image (Base64) and Image Resize nodes:

```json
{
    "97": {
        "inputs": {
            "image": "%char_avatar%"
        },
        "class_type": "ETN_LoadImageBase64",
        "_meta": {"title": "Load Image (Base64)"}
    },
    "98": {
        "inputs": {
            "mode": "resize",
            "resize_width": "%width%",
            "resize_height": "%height%",
            "image": ["97", 0]
        },
        "class_type": "Image Resize",
        "_meta": {"title": "Resize image"}
    }
}
```

To get a base64-encoded image string for testing your workflow in ComfyUI, use any online tool that converts images to base64 strings. 
Here's an example string you can use for initial testing: sd-comfy-base64-test-string.txt.

#### Other placeholders

Most other placeholders use the values of the corresponding controls in image generation settings, or the values that you specify with the `/sd` command:

- `%vae%`, but most SD models include a VAE so the default workflows do not use this placeholder. Use it with custom workflows to load a VAE alongside a UNet, override the default VAE, etc.
- `%sampler%`
- `%scheduler%`
- `%steps%`
- `%scale%`
- `%width%`
- `%height%`
- `%denoise%`: for the sample image-to-image workflow, vary the denoise amount between about 0.5 (barely-noticeable changes to the source image) and 1.0 (a completely different image as if no source image was used). Not used by the default text-to-image workflow because there's no point using a value other than 1.0 for text-to-image.
- `%clip_skip%`: not used by the default workflows but available for custom workflows.

The `%seed%` placeholder will insert the seed value from the control if you have specified one. If you set the seed to `-1`, SillyTavern will generate a new random seed for each image in `%seed%`. 

#### Custom placeholders

You can add custom placeholders to your workflow:

1. Look for the "Custom" section below the predefined placeholders.
2. Click the "+" button to add a new custom placeholder.
3. Enter a name for the placeholder in the `find` field.
4. Enter the value that you want to replace the placeholder with in the `replace` field.

Custom placeholders will appear in a separate list below the predefined ones.

For example, you could replace the "SillyTavern" prefix for saved image filenames in the default workflow with a custom placeholder. Add a new custom placeholder with `find` set to `filename_prefix` and `replace` set to `ServiceTensor`. Insert the new `%filename_prefix%` placeholder into your workflow JSON. Now you can change the filename prefix from SillyTavern to ServiceTensor by changing the value of the custom placeholder.

+++ JSON with placeholder
```json
{
    "class_type": "SaveImage",
    "inputs": {
        "filename_prefix": "%filename_prefix%",
        "images": ["8", 0]
    }
}
```
+++ Original JSON
```json
{
    "class_type": "SaveImage",
    "inputs": {
        "filename_prefix": "SillyTavern",
        "images": ["8", 0]
    }
}
```
+++

### Comfy tricks

Read all the general information on this page so you're familiar with the image generation options. Options such as switchable styles and common prompt prefixes, when combined with the total flexibility of ComfyUI workflows, allow you to create a wide variety of image generation setups.

#### Loading LoRAs

Use a LoRA tag loader node (such as Load LoRA Tag (https://github.com/badjeff/comfyui_lora_tag_loader)) to load any LoRAs specified in the prompt. 
Now you can add as many LoRAs as you like to your prompt with tags like `<lora:CroissantStyle:0.8>`, and they will be loaded into your workflow. 
This will also make the "pro-tip" of using LoRAs in character-specific prompt prefixes work with ComfyUI.

#### Setting workflow values from styles or slash-commands

You can use macros in custom placeholder values. As a practical example, 
let's say you sometimes want to generate images without a background, and you'd like this to be switchable with a 
slash-command or image style. Here's how you could do it:

1. Make a ComfyUI workflow that removes the image background, or not, depending on the value of an input
2. Use a custom placeholder to set the value of that input, but use `{{getvar::remove_background}}` as the replace value
3. Now you can set the value of `remove_background` with `/setvar key=remove_background true` or `/setvar key=remove_background false` before generating an image
4. The workflow will use the value you set to determine whether to remove the background
5. Make an image style "No background" with common prompt prefix `{{setvar::remove_background::true}}`
6. Use the style control or `/imagine-style No background` to set the value of `remove_background` to `true` before generating an image

# SECTION: SillyTavern_extensions_Summarize

# Summarize

## What is it?

This extension allows you to create, store, and utilize automatically generated summaries based on the events happening in your chats. Summarization can help with outlining general details of what is happening in the story, which *could* be interpreted as a long-term memory, but take that statement with a grain of salt. Since the summaries are generated by language models, the outputs may lose some important details or contain hallucinations, so you're always advised to keep track of the summary state and correct it manually if needed.

## Common configuration

The summarization extension is installed in SillyTavern by default, thus it will show up in ST's Extensions panel (stacked cubes icon) list like this:

- **Current summary** - displays and provides an ability to modify the current summary. The summary is updated and embedded into the chat file's metadata for the message that was the last in context when the summary was generated. Deleting or editing a message from the chat that has a summary attached to it, will revert the state to the last valid summary.
- **Restore Previous** - removes the current summary, rolling it back to the previous state. This is useful if the summarizer does a poor job at any given point.
- **Pause** - check this to prevent the summary from being automatically updated. This is useful if you want to provide a custom summary of your own or to effectively disable the summary by clearing the box and stopping updates.
- **Popup window** - allows to detach the summary into a movable UI panel on the sidebar. Useful for the desktop layout to easily have access to summarization settings without having to navigate through the extensions menu.
- **Injection Template** - defines how the summary will be wrapped when being inserted into regular chat prompts. A special \{\{summary\}\} macro should be used to denote the exact location of the current summary state in the prompt injection text.
- **Injection Position** - sets the location of the prompt injection. The options are the same as for Author's Notes: before or after the main prompt, or in-chat at designated depth.

## Supported summary sources

### Main API

Summarization will be powered by your currently selected AI backend, model and settings. This method requires no additional setup, just a working API connection.

This option has the following sub-modes that differ depending on how the summary prompt is built:

1. Raw, blocking. The summary will be generated using nothing but the summarization prompt and the chat history. Subsequent prompts will also include the previous summary with messages that were sent after the summary was generated (see example). This mode can (and will) generate prompts that have a lot of variability between them, so it is not recommended to use it with backends that have slow prompt processing times, such as llama.cpp and its derivatives.
2. Raw, non-blocking. Same as above, but the chat generation will not be blocked during the summary generation. Not every backend supports simultaneous requests, so switch to blocking mode if summarization fails.
3. Classic, blocking. The summarization prompt will be sent at the end of your usual generation prompt, as a neutral system instruction, not omitting the character card, main prompt, example dialogues and other parts of chat prompts. This usually results in prompts that play nicely with reusing processed prompts, so it is recommended to use with llama.cpp and its siblings.

#### Summary Settings explained

1. **Summary Prompt** - defines the prompt that will used for creating a summary. May include any of the known macros, as well as a special \{\{words\}\} macro (see below).
2. **Target summary length (words)** - defines the value of the \{\{words\}\} macro that can be inserted into the Summary Prompt. This setting is completely optional and has no effect at all if the macro is not used.
3. **API response length (tokens)** - allows to set an override API response length for generating summaries that are different from the globally set value.
4. **Max messages per request _(raw modes only)_** - set to limit the maximum number of messages that will be included in one summarization prompt. `0` means no explicit limitation, but the resulting number of messages to summarize will still depend on the maximum context size, calculated using the formula: `max summary buffer = context size - summarization prompt - previous summary - response length`. Use this when you want to get more focused summaries on models with large context sizes.
5. **No WI/AN** - omit World Info and Author's Note from text to be summarized. Only has an effect when using the Classic prompt builder. The Raw prompt builder always omits WI/AN.
6. **Update every X messages** - sets the interval at which the summary is generated. `0` means that the automatic summarization is disabled, but you can still trigger it manually by clicking the "Summarize now" button. This should be adjusted based on how quickly the prompt buffer entirely fills with chat messages. Ideally, you'd want to have the first summary generated when the messages are starting to get dropped out of the prompt.
7. **Update every X words** - same as above, but using words (not tokens!) instead of messages, theoretically can be a more accurate measurement due to how unpredictable the contents of chat messages usually are, but your mileage may vary.

If both "Update every" sliders are set to a non-zero value, then both will trigger summary updates at their respective intervals, depending on what happens first. It is strongly advised to update these values accordingly when you switch to another model that has differing context sizes, otherwise, the summary generation may trigger too often, or never at all.

If you're unsure about the interval settings, you can click the "magic wand" button above the "Update every" sliders to try and guess the optimal values based on some simple heuristics. A brief description of the algorithm is as follows:

1. Calculate token and word counts for all chat messages
2. Determine target summary length based on desired prompt words
3. Calculate the maximum number of messages that can fit in the prompt based on the average message length
4. If "Max messages" is set, adjust the average to account for messages that don't fit the summary limit
5. Round down the adjusted average messages per prompt to a multiple of 5

#### Example prompts

**Raw prompt**
```
System:
[Summarization prompt]

Previous summary.

User:
Message foo.

Char:
Message bar.
```

**Classic prompt**
```
[Main prompt]

[Character card]

[Example dialogues]

User:
Message foo.

Char:
Message bar.

System:
[Summarization prompt]
```

### Extras API

Extras server with the `summarize` module could run an auxiliary summarization model (BART).

It has a very small context size (~1024 tokens), so its ability to handle large summaries is quite limited.

To configure the Extras summary source, do the following:

1. Install or Update Extras (https://github.com/SillyTavern/SillyTavern-extras) to the latest version.
2. Run Extras with the `summarize` module enabled: `python server.py --enable-modules=summarize`

#### Changing Summary Model

By default, Summarize uses the Qiliang/bart-large-cnn-samsum-ChatGPT_v3 (https://huggingface.co/Qiliang/bart-large-cnn-samsum-ChatGPT_v3) model for summarization purposes.

This can be changed by using the command line argument `--summarization-model=(###Hugging-Face-Model-URL-Here###)`

A known alternate Summarize model is `Qiliang/bart-large-cnn-samsum-ElectrifAi_v10`.

# SECTION: SillyTavern_extensions_Translation

# Chat Translation

## Overview

The Chat Translation Extension enables real-time translation of chat messages between
different languages using various translation providers. It supports both manual and
automatic translation modes.

+++ English

+++ 简体中文

+++ 繁體中文

+++ 한국어

+++ Русский

+++

## Usage

All the ways to translate chat messages:

**<i class="fa-solid fa-language"></i> Translate Chat** button in the **<i class="fa-solid fa-magic-wand-sparkles"></i>
Extensions** menu

- Translates the entire chat history at once

**<i class="fa-solid fa-keyboard"></i> Translate Input** button in the **<i class="fa-solid fa-magic-wand-sparkles"></i>
Extensions** menu

- Translates just the current input text
- Useful before sending a message

**<i class="fa-solid fa-language"></i> Translate Message** icon in the **<i class="fa-solid fa-ellipsis"></i> Message
Actions**
toolbar of any message

- Click to translate just that message
- Click again to revert to original text

**Auto-mode** configuration in the **Chat Translation** drawer of the **<i class="fa-solid fa-cubes"></i>
Extensions** panel

- Automatically translates user inputs, AI responses, or both

**/translate** slash command

- Use `/translate [target=language_code] text` to translate text

## Configuration

Configuration options are available in the **Chat Translation** drawer of the **<i class="fa-solid fa-cubes"></i>
Extensions** panel.

#### Provider

- Choose your preferred translation service
- Click the **<i class="fa-solid fa-key"></i> API Key** icon, if it appears, to enter an API key
- Click the **<i class="fa-solid fa-link"></i> Custom URL** icon, if it appears, to enter a custom API URL

#### Target Language

Select the language you want to write your messages in, or read AI responses in.

#### Auto-mode

Configure automatic translation behavior.

- **None**: No automatic translation
- **Translate responses**: Automatically translates AI responses into the target language
- **Translate inputs**: Automatically translates user inputs into English
- **Translate both**: Translates both user inputs and AI responses

#### Clear Translations

The **<i class="fa-solid fa-trash-can"></i> Clear Translations** button removes all translations from messages in the
current chat. The original messages are preserved.

### Configuration Example: Chinese to English Chatting

To set up a workflow where a Chinese-speaking user can chat in Chinese with an AI that operates in English:

1. Set Auto-mode to "Translate both"
2. Set Target Language to "Chinese (Simplified)" or "Chinese (Traditional)"
3. Choose a translation provider with good language auto-detection (e.g., Google or DeepL)

This setup will:

- Translate user's Chinese input to English for the AI
- Translate AI's English responses back to Chinese for the user

This setup relies on automatic language detection for input. For more precise control, future updates may include
explicit source language selection.

## Translation providers

**:icon-cloud:** Cloud-based
**<i class="fa-solid fa-link"></i>** Local, custom URL
**<i class="fa-solid fa-key"></i>** Requires API key

| Provider                                                            | Location                                                                      | Features                                                                                               |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Libre Translate (https://libretranslate.com/)                      | :icon-cloud: <i class="fa-solid fa-key"></i> <i class="fa-solid fa-link"></i> | Self-hosted (AGPL-3.0) alternative to proprietary translation services, with cloud-hosted Pro tier     | 
| Google Translate (https://cloud.google.com/translate)              | :icon-cloud:                                                                  | Widely used, supports many languages, good accuracy                                                    |
| Lingva Translate (https://lingva.ml/)                              | <i class="fa-solid fa-link"></i>                                              | Alternative front-end for Google Translate, open source (AGPL-3.0), privacy-focused                    |
| DeepL (https://www.deepl.com/)                                     | :icon-cloud: <i class="fa-solid fa-key"></i>                                  | High-quality translations, especially for European languages                                           |
| DeepLX (https://github.com/OwO-Network/DeepLX)                     | <i class="fa-solid fa-link"></i>                                              | Self-hosted DeepL proxy, open source (MIT), free but proxying DeepL Pro requires DeepL API key         |
| Bing Translator (https://www.bing.com/translator)                  | :icon-cloud:                                                                  | Microsoft's translation service, integrates with Azure services                                        |
| OneRing Translator (https://github.com/janvarev/OneRingTranslator) | <i class="fa-solid fa-link"></i>                                              | Self-hosted front-end to Google Translate and other providers, privacy-focused, open source (AGPL-3.0) |
| Yandex Translate (https://translate.yandex.com/)                   | :icon-cloud:                                                                  | Good for Russian and Eastern European languages                                                        |

### DeepL-specific configuration

- Formality levels available for German, French, Italian, Spanish, Dutch, Japanese, and Russian
- Configure via `deepl.formality` in config.yaml

## Slash Commands

Use `/translate` command for quick translations. Syntax: `/translate [target=language_code] text`. If target language is
not provided, the value from the extension settings will be used.

### Basic usage

Translate text to the current target language and show it in a popup:

```
/translate Welcome to the Tavern | /echo 
```

Translate text to Spanish and add it to the chat:

```
/translate target=es Hello world | /send
```

### Testing, pipeline translation, localization

Prompt the user for a message and a language, translate the message into that language, then re-translate it into the
configured target language and show both translations in a popup. This example uses the `/input` and `/buttons` commands
to gather user input:

```shell
/input default="Hello, world!" <span data-i18n="Test Message">Sample text</span> | 
/let key=input ||
/buttons labels=["zh-CN", "zh-TW", "es", "hu", "en"] <span data-i18n="UI Language">Language</span> | 
/let key=lang ||
/translate target={{var::lang}} {{var::input}} | /let key=tx_target | 
/translate | /let key=tx_orig ||
/echo escapeHtml=false cssClass=wider_dialogue_popup
<b data-i18n="Test Message">Test message</b>: {{var::input}} 
<b data-i18n="Output">Output</b> ({{var::lang}}): {{var::tx_target}} 
<b data-i18n="Output">Output</b> (<span data-i18n="ext_translate_target_lang">target language</span>): {{var::tx_orig}} 
```

This is useful for checking the quality of a translation into a language that you don't speak, before writing it
somewhere important.

The UI controls are shown in the current locale, independent of the configured target language.

| `/input`                                                                                        | `/buttons`                                                                          |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|

Input language detection is relatively effective in the following examples:

## Technical Notes

- UTF-8 encoding, special characters, and emojis are supported
- Handles large messages by splitting into chunks when needed
- Preserves formatting and embedded images in messages
- Caches translations to avoid redundant API calls

### AI input language

`internal_language` controls the language into which user messages are auto-translated before being sent to the AI. It
is hardcoded to 'en' in the default settings and cannot be changed through the UI. Thus, the translation target language
for messages *to the AI* is always English. Previous testing showed that AI performance was better when receiving
English messages, but this may change as more LLMs are being trained on more varied language data. I suppose one could
change `internal_language` in `settings.json` and find out.

### Chinese variant handling

The extension supports both Simplified and Traditional Chinese, but not all translation providers do. The UI presents
these as 'Chinese (Simplified)' and 'Chinese (Traditional)' respectively, with language codes 'zh-CN' and 'zh-TW'. They
are mapped to the following language codes for translation providers:

* Libre Translate: 'zh-CN' to 'zh' and 'zh-TW' to 'zt'.
* DeepL and DeepLX: both variants to 'ZH'.
* Bing: 'zh-CN' to 'zh-Hans', 'zh-TW' as-is.
* Other providers use 'zh-CN' and 'zh-TW' as provided.

### Text length limits

Some providers have character limits per request:

- Yandex: 5000 characters
- DeepLX: 1500 characters
- Bing: 1000 characters
- Google: 5000 characters

Longer texts are automatically split into chunks for translation.

# SECTION: SillyTavern_extensions_TTS

# TTS

SillyTavern has a wide range of TTS (text-to-speech) options that are used to have a voice narrate parts of your chat. This page explains the setup and use.

## Configuring TTS

### TTS Provider Selection

Used to select which TTS service you want to use. Some of the options are free, some require a paid subscription, and some run locally on your PC.

Available options (list may change over time):

- **AllTalk** - free, open source local installation, offers a variety of TTS engines. See the AllTalk page for setup instructions.
- **Azure TTS** - same voices as Microsoft Edge. Requires an Azure account and a paid subscription.
- **Coqui-TTS** (deprecated) - free, requires Extras API to run. High-performance Text2Speech models (Tacotron, Tacotron2, Glow-TTS, SpeedySpeech) as well as Bark.
- **Edge** - free, runs via Azure. When running with "Plugin" selected as the provider, you also need to install this server plugin (https://github.com/SillyTavern/SillyTavern-EdgeTTS-Plugin). Other option requires Extras API (deprecated) to run.
- **Electron Hub** - reuses your Electron Hub (https://electronhub.ai/) API key to access cloud voices (GPT-4o Mini TTS, Microsoft neural voices, etc.) with per-model controls.
- **ElevenLabs** - paid subscription required. Get an API key from ElevenLabs (https://elevenlabs.io/).
- **Google Translate** - a free voice provided by Google, one per language, quality can vary widely.
- **Google Gemini TTS** - requires an API key from either Vertex AI or AI Studio, uses Gemini TTS (https://cloud.google.com/text-to-speech/docs/gemini-tts) models.
- **Kokoro** - free, uses kokoro.js (https://www.npmjs.com/package/kokoro-js) to run the model locally in your browser. However, some browsers (https://caniuse.com/webgpu) may not support WebGPU for the device option.
- **MiniMax** - requires an API key from MiniMax (https://www.minimax.io/). See the MiniMax TTS page for setup instructions.
- **Novel** - requires a paid NovelAI subscription, generated by NovelAI's TTS engine
- **OpenAI** - paid API key required, uses OpenAI's TTS models.
- **Pollinations** - free of charge access to OpenAI TTS models, but with a rate limit. Website (https://pollinations.ai/).
- **Silero** - free, runs on your PC, quality can vary widely. Requires a dedicated API server (https://github.com/ouoertheo/silero-api-server) installation or Extras API (deprecated).
- **System** - uses your OS TTS engine, if one exists. Quality can vary widely depending on the OS.
- **XTTS** - free, requires a dedicated API server installation. See the XTTS page for setup instructions.

### Checkboxes

- **Enabled** - turns TTS playback on/off
- **Auto Generation** - lets TTS start playing automatically when a new message enters the chat
- **Only narrate "quotes"** - Limits TTS playback to only include text within `"quotation marks"`. This will `*include "quotes" within asterisk lines*` (internal variable name = `narrate_quoted_only`)
- **Ignore \*text, even "quotes", inside asterisks\*** - TTS will not play any text within `*asterisks*`, even "quotes" (internal variable name = `narrate_dialogues_only`)
- *having both "only narrate quotes" and "ignore asterisks" checkboxes both checked will result in the TTS only reading "quotes" which are not in asterisks, and ignoring everything else.*
- **Narrate only the translated text** - this will make the TTS only narrate the translated text.
- **Apply regex** - applies a provided regex pattern to the text before sending it to the TTS provider. Useful for removing unwanted parts from the input text, such as emojis or non-native language characters that the TTS engine doesn't handle well.

Given the example text: `*Cohee approaches you with a faint "nya"* "Good evening, senpai", she says.`
Here's a table showing how the text will be modified based on the boolean states of **Ignore \*text, even "quotes", inside asterisks\*** and **Only narrate "quotes"**:

| **Ignore \*text, even "quotes", inside asterisks\*** 	 | **Only narrate "quotes"**	 | **Output**                                                                |
|:-------------------------------------------------------|:---------------------------|:--------------------------------------------------------------------------| 
| Disabled                                               | 	Disabled	                 | Cohee approaches you with a faint "nya" "Good evening, senpai", she says. |
| Disabled                                               | Enabled	                   | "nya"... "Good evening, senpai"                                           |
| Enabled	                                               | Disabled	                  | "Good evening, senpai", she says.                                         |
| Enabled	                                               | Enabled	                   | "Good evening, senpai"                                                    |

### Sliders

These will change depending on the API you select.

### Buttons

- **Apply** - this must be clicked after setting a TTS API and after editing the voice map.
- **Refresh** - reloads the list of voices from the selected TTS API.
- **Available voices** - loads a popup with all voices available for your selected API, and lets you preview them with sample dialogues.

## Using TTS

1. Click the "Enable" checkbox, or nothing will ever happen.
2. Click the "Auto-generation" checkbox if you want the TTS to start automatically every time a new message arrives in chat.
3. Optionally, click the megaphone icon inside the top-right of any message to playback on demand.
4. Click the lower right "Stop" button (found inside the wand menu) to stop any playback.

### Voice Map

You must provide a voice map for the TTS to use, otherwise, it won't know what voices should be used for each character. To setup the voice map, first open a chat with a character that you'd like to assign a voice to and/or select a user persona to assign a voice to, then select a voice listed by a TTS provider from the dropdown. If you don't see a list of voices and/or characters, make sure that your TTS provider is configured correctly and click "Refresh". Some providers (like OpenAI-compatible or NovelAI) require you to populate the voice list manually.

# SECTION: SillyTavern_extensions_VRM

# VRM

This guide will walk you through the process of setting up and customizing the VRM extension for your SillyTavern experience. This extension allows you to use VRM animated models for your character, providing a dynamic and interactive element to your virtual character.

## Prerequisites

Before you begin, ensure you've met the following prerequisites:

1. **Branch Selection**: Make sure you're using the latest version branch of SillyTavern to access the latest features and updates.

2. **Extension Installation**: Install the "VRM" extension from the "Download Extensions & Assets" menu in the Extensions panel (represented by the stacked blocks icon).

3. **Model Folder Placement**: Place your VRM model files (.vrm) into the `/data/<user-handle>/assets/vrm/model` directory and your animation files into the `/data/<user-handle>/assets/vrm/animation` directory. The currently supported animation file formats are .fbx and .bvh that are compatible with VRM models. This includes any animation you can get from Mixamo (https://www.mixamo.com/) and any animation you can export from tools like XR Animator (https://github.com/ButzYung/SystemAnimatorOnline).

## Extension Settings

The VRM extension offers various settings to customize the behavior of your animated model. Here are the key settings:

### Global Settings

1. **Enabled**:
   - Enable this checkbox to activate the extension, allowing your VRM model to interact within SillyTavern.
   - You can disable the extension if you want to use normal sprites only.

2. **Look at camera**:
   - Enable this checkbox to make the VRM model eyes look at the camera.

3. **Blink**:
   - Enable this checkbox to make the VRM model eyes blink at random intervals. Model expressions should define properly blinking weight property otherwise model can blink with closed eyes for example, if that happens either:
    - correct the model if you have the .vroid file
    - don't use that incorrect face expression
    - disable blinking completely with this checkbox

4. **TTS Lip sync**
    - Enable this checkbox to have the VRM mouth movement follow the sound of your TTS when it's played. Only works with TTS whose sound is played by Sillytavern itself like XTTS (not in streaming mode). If disabled, mouth will be animated according to the message text length when a new character message is received.

5. **Auto-send Interaction**:
   - Enable this checkbox to automatically trigger character interactions when you click on areas with mapped messages (refer to the hit areas section for details).

### Performance Settings

1. **Body hitboxes**
    - Enable this checkbox to activate detection of click on several part of the VRM model depending on the model the following area can be detected: head/chest/hands/groin/butt/legs/feet. Hitbox locations are computed at each frame and follow the body animation, disabling this option can improve performance.

2. **Use model cache**
    - Enable this checkbox to keep the VRM model in memory when switching models, allows to switch back to previous model faster. Useful if you use different model for the same character to change outfit or form for example. Can affect performance.

3. **Use animation cache**
    - Enable this checkbox to keep in memory all animations played during the session. All animation assigned to a model will also be loaded the first time the model appears. Will increase the time you load the model the first time but make all animation switch instant. Can affect performance.

### Debug Settings

1. **Show grid**
    - Enable this checkbox to visualize the 3d grid, model dragging box and body hitboxes.

2. **Reload button**
    - Click this button to reload the 3d scene, clear the cache and all VRM models. Use it if some bug occurs or if cache starts to hit performance.

### Scene Settings

1. **Light Color**
    - Set the color of the light in the 3d scene. Click on the reset button to set it back to the default white color. Depending on your browser you can use a color picker, for example you can color pick the color of your background image to add more immersion.

2. **Light intensity**
    - Set the light intensity in percent using the slider. Click on the reset button to set it back to the default value of 100%. VRM model can react differently to light depending on the baked shaders into the model, play with the value and see how it goes.

## Character Selection

These settings allow you to manage characters and assign VRM models to them.

1. **Refresh Button**:
   - Click the refresh button to update the list of characters in the current chat.

2. **Select Character**:
   - Use the drop-down list to choose a character to assign a VRM model to.

3. **Remove Button**:
   - Click this button to delete the assigned model for a character.

## Model Selection

1. **Refresh Button**:
   - Click the refresh button if your VRM model does not appear in the list.

2. **Select Model**:
   - Choose a model from the list to assign it to the selected character.
   - The model has to be located in `/data/<user-handle>/assets/vrm/model` directory.

3. **Reset button**
    - Click this button to reset the model settings to its default. If you have animation files that correspond to the default value they will be auto mapped. See the naming mapping at the end of this README.

## Model Settings

1. **Model Scale**:
   - Use the slider to adjust the size of the model, making it larger or smaller.

2. **Model Center X/Y Offset**:
   - Use those sliders to change the horizontal/vertical position of the model relative to the window center.

3. **Model X/Y Rotation**
    - Use those sliders to change the horizontal/vertical rotation of the model relative to the model hips.

### Remarks
    - The settings are saved per model not per character and carry over different chats.
    - If you want to use the same model for two different characters with different settings make a copy of the .vrm file.
    - You can also drag the model with your mouse, and those settings will be updated and saved. Left click and hold to drag a model around the screen. Middle mouse Click and hold to rotate the model or use shift-left click. Use mouse wheel with cursor on the model to scale it up or down or use ctrl+left click.
    - Use these UI settings to bring your model back on the screen if you somehow made it out of view. Also, check the "Show frame" checkbox to see clearly where you can click to drag the model.

## Hitboxes mapping

    - Depending on the model bones definition some hitbox areas can be generated, they will be listed in this part of the ui, and you can assign an expression/animation/message to each of them that will trigger when you click the area.

## Classified Expressions Mapping

1. **Requirements**
    - Requires the use of the classify expression extension; otherwise, it will fall back to the default animation.

2. **Mapping**
    - For each detected emotion by the classify extension, you can assign an expression/motion/message. The message can contain commands.

## Commands

1. **/vrmlightcolor**
    - set the light color
    - arguments: color
    - example: "/vrmlightcolor white" or "/vrmlightcolor purple".
2. **/vrmlightintensity**
    - set the light intensity in percent
    - arguments: intensity
    - example: "/vrmlightintensity 0" or "/vrmlightintensity 100
3. **/vrmmodel**
    - assign the vrm model to the character
    - arguments: character, model
    - example: "/vrmmodel Seraphina.vrm" in solo chat or "/vrmmodel character=Seraphina model=Seraphina.vrm" in group chat
4. **/vrmexpression**
    - change the expression of the model
    - arguments: character, expression
    - example: "/vrmexpression happy" in solo chat or "/vrmexpression character=Seraphina expression=happy" in group chat

5. **/vrmmotion**
    - change the animation of the model
    - arguments: character, motion, loop, random
    - "/vrmmotion idle" or "/vrmmotion character=Seraphina motion=idle loop=true random=false"

## Animations default mapping
If your animation files are named in the following way they will be mapped automatically when resetting a model settings. For example the files named "assets/vrm/animation/neutral.bvh" and "assets/vrm/animation/neutral1.fbx" will be automatically mapped as a group for default and neutral classified animation. Same goes for the hitboxes. 

    // Fallback
    "default": "assets/vrm/animation/neutral",

    // Classify class
    "admiration": "assets/vrm/animation/admiration",
    "amusement": "assets/vrm/animation/amusement",
    "anger": "assets/vrm/animation/anger",
    "annoyance": "assets/vrm/animation/annoyance",
    "approval": "assets/vrm/animation/approval",
    "caring": "assets/vrm/animation/caring",
    "confusion": "assets/vrm/animation/confusion",
    "curiosity": "assets/vrm/animation/curiosity",
    "desire": "assets/vrm/animation/desire",
    "disappointment": "assets/vrm/animation/disappointment",
    "disapproval": "assets/vrm/animation/disapproval",
    "disgust": "assets/vrm/animation/disgust",
    "embarrassment": "assets/vrm/animation/embarrassment",
    "excitement": "assets/vrm/animation/excitement",
    "fear": "assets/vrm/animation/fear",
    "gratitude": "assets/vrm/animation/gratitude",
    "grief": "assets/vrm/animation/grief",
    "joy": "assets/vrm/animation/joy",
    "love": "assets/vrm/animation/love",
    "nervousness": "assets/vrm/animation/nervousness",
    "neutral": "assets/vrm/animation/neutral",
    "optimism": "assets/vrm/animation/optimism",
    "pride": "assets/vrm/animation/pride",
    "realization": "assets/vrm/animation/realization",
    "relief": "assets/vrm/animation/relief",
    "remorse": "assets/vrm/animation/remorse",
    "sadness": "assets/vrm/animation/sadness",
    "surprise": "assets/vrm/animation/surprise",

    // Hitboxes
    "head": "assets/vrm/animation/hitarea_head",
    "chest": "assets/vrm/animation/hitarea_chest",
    "groin": "assets/vrm/animation/hitarea_groin",
    "butt": "assets/vrm/animation/hitarea_butt",
    "leftHand": "assets/vrm/animation/hitarea_hands",
    "rightHand": "assets/vrm/animation/hitarea_hands",
    "leftLeg": "assets/vrm/animation/hitarea_leg",
    "rightLeg": "assets/vrm/animation/hitarea_leg",
    "rightFoot": "assets/vrm/animation/hitarea_foot",
    "leftFoot": "assets/vrm/animation/hitarea_foot"

Thank you for following this guide! Your SillyTavern experience is now enriched with animated and interactive 3D models.

## Remarks
    - The VRM model loaded by this extension are the .vrm files not the .vroid files.
    - Animation files should be VRM compatible, you can use a tool like XR animation (https://github.com/ButzYung/SystemAnimatorOnline) to convert fbx/bvh animation file.
    - You can create animation groups by having file with same name ending with different numbers for example: "idle1.bvh", "idle2.bvh", "idle3.bvh" will be considered as one group "idle" and when selected in a mapping a random one will played when triggered, can be used to add variety to animations.
    - You can get curated animations from this repository: https://github.com/test157t/VRM-Animations-Pack-For-Silly-Tavern
    - Nitral has some tutorial video about how to use the extension and the animation repo: https://www.youtube.com/@nitralai

# SECTION: SillyTavern_extensions_WebSearch

# Web Search

Adds web search results to LLM prompts.

Some Chat Completion sources provide built-in web search functionality. In this case, this extension will be largely redundant. Check the **<i class="fa-solid fa-sliders"></i> AI Response Configuration** panel for the "Enable web search" toggle. For example, this is available for Claude, Google AI Studio / Vertex AI, xAI, and OpenRouter backends.

**## Available sources**

### Selenium Plugin

Requires an official server plugin to be installed and enabled.

See SillyTavern-WebSearch-Selenium (https://github.com/SillyTavern/SillyTavern-WebSearch-Selenium) for more details.

Supports Google and DuckDuckGo engines.

### Extras API

Requires a `websearch` module and Chrome/Firefox web browser installed on the host machine.

Supports Google and DuckDuckGo engines.

### SerpApi

Requires an API key.

Get the key here: <https://serpapi.com/dashboard>

### SearXNG

Requires a SearXNG instance URL (either private or public). Uses HTML format for search results.

SearXNG preferences string: obtained from SearXNG - preferences - COOKIES - Copy preferences hash

Learn more: <https://docs.searxng.org/>

### Tavily AI

Requires an API key.

Get the key here: <https://app.tavily.com/>

### KoboldCpp

KoboldCpp URL must be provided in Text Completion API settings. KoboldCpp version must be >= 1.81.1 and WebSearch module must be enabled on startup: enable Network => Enable WebSearch in the GUI launcher or add `--websearch` to the command line.

See: <https://github.com/LostRuins/koboldcpp/releases/tag/v1.81.1>

### Serper

Requires an API key.

Get the key here: <https://serper.dev/>

### Z.AI

Requires an API key, set it in the Chat Completion API settings first. Not compatible with the Coding API subscription!

Get the key here: <https://z.ai/manage-apikey/apikey-list/>

Docs: <https://docs.z.ai/api-reference/tools/web-search>

## How to use

1. Make sure you use the latest version of SillyTavern.
2. Install the extension via the "Download Extensions & Assets" menu in SillyTavern.
3. Open the "Web Search" extension settings, set your API key or connect to Extras, and enable the extension.
4. The web search results will be added to the prompt organically as you chat. **Only user messages trigger the search.**
5. To include search results more organically, wrap search queries with single backticks: ```Tell me about the `latest Ryan Gosling movie`.``` will produce a search query `latest Ryan Gosling movie`.
6. Optionally, configure the settings to your liking.

## Settings

### General

1. Enabled - toggles the extension on and off.
2. Sources = sets the search results source.
3. Cache Lifetime - how long (in seconds) the search results are cached for your prompt. Default = one week.

### Prompt Settings

1. Prompt Budget - sets the maximum capacity of the inserted text (in characters of text, NOT tokens). Rule of thumb: 1 token ~ 3-4 characters, adjust according to your model's context limits. Default = 1500 characters.
2. Insertion Template - how the result gets inserted into the prompt. Supports the usual macro + special macro: \{\{query\}\} for search query and \{\{text\}\} for search results.
3. Injection Position - where the result goes in the prompt. The same options as for the Author's Note: as in-chat injection or before/after system prompt.

### Search Activation

1. Use function tool - uses function calling to activate search or scrape web pages. Must use a supported Chat Completion API and be enabled in the AI Response settings. **Disables all other activation methods when engaged.**
2. Use Backticks - enables search activation using words encased in single backticks.
3. Use Trigger Phrases - enables search activation using trigger phrases.
4. Regular expressions - provide a JS-flavored regex to match the user message. If the regex matches, the search with a given query will be triggered. Search query supports `{{macros}}` and $1-syntax to reference the matched group. Example: `/what is happening in (.*)/i` regex for search query `news in $1` will match a message containing `what is happening in New York` and trigger the search with the query `news in New York`.
5. Trigger Phrases - add phrases that will trigger the search, one by one. It can be anywhere in the message, and the query starts from the trigger word and spans to "Max Words" total. To exclude a specific message from processing, it must start with a period, e.g. `.What do you think?`. Priority of triggers: first by order in the textbox, then the first one in the user message.
6. Max Words - how many words are included in the search query (including the trigger phrase). Google has a limit of about 32 words per prompt. Default = 10 words.

### Page Scraping

1. Visit Links - text will be extracted from the visited search result pages and saved to a file attachment.
2. Visit Count - how many links will be visited and parsed for text.
3. Visit Domain Blacklist - site domains to be excluded from visiting. One per line.
4. File Header - file header template, inserted at the start of the text file, has an additional \{\{query\}\} macro.
5. Block Header - link block template, inserted with the parsed content of every link. Use \{\{link\}\} macro for page URL and \{\{text\}\} for page content.
6. Save Target - where to save the results of scraping. Possible options: trigger message attachments, or chat attachments of Data Bank, or just images (if the source supports them).
7. Include Images - attach relevant images to the chat. Requires a source that supports images (see below).

## More info

Search results from the latest query will stay included in the prompt until the next valid query is found.
If you want to ask additional questions without accidentally triggering the search, start your message with a period.

Web Search function tool always overrides other triggers if enabled and available.

**Priority of triggers (if multiple are enabled):**

1. Backticks.
2. Regular expressions.
3. Trigger phrases.

To discard all previous queries from processing, start the user message with an exclamation mark, for example, a user message `!Now let's talk about...` will discard this and every message above it.

This extension also provides a `/websearch` slash command to use in STscript. More info here: STscript Language Reference

```stscript
/websearch (links=on|off snippets=on|off [query]) – performs a web search query. Use named arguments to specify what to return - page snippets (default: on), full parsed pages (default: off) or both.

Example: /websearch links=off snippets=on how to make a sandwich
```

### What can be included in the search result?

**Thesaurus:**

- Answer box: Direct answer to the question.
- Knowledge graph: Encyclopedic knowledge about the topic.
- Page snippets: Relevant extracts from the web pages.
- Relevant questions: Questions and answers to similar topics.
- Images: Relevant images.

#### SerpApi

1. Answer box.
2. Knowledge graph.
3. Page snippets (max 10).
4. Relevant questions (max 10).
5. Images (max 10).

#### Selenium Plugin and Extras API

1. Google - answer box, knowledge graph, page snippets.
2. DuckDuckGo - page snippets.

**Selenium Plugin** can additionally provide images.

#### SearXNG

1. Infobox.
2. Page snippets.
3. Images.

#### Tavily AI

1. Answer.
2. Page contents.
3. Images (up to 5).

#### KoboldCpp

1. Page titles.
2. Page snippets.

#### Serper

1. Answer box.
2. Knowledge graph.
3. Page snippets.
4. Relevant questions.
5. Images.

#### Z.AI

1. Page titles.
2. Page snippets.

# SECTION: SillyTavern_extensions_XTTS

# XTTS with voice cloning

Greetings! So, you've been blown away by those Reddit posts showcasing how far the technology went for the AI text-to-speech?

Feeling excited to give your robotic waifu/husbando a new shiny voice modulator?

Fear not, this stunning groundbreaking technology is already available at your local SillyTavern, you just need a simple...

## Prerequisites

1. Latest version of SillyTavern.
2. Miniconda (https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) installed.
3. (Windows) Visual C++ Build Tools (https://visualstudio.microsoft.com/visual-cpp-build-tools/) installed.
4. WAV files with voice clips to clone from (~10 seconds per file). File requirements: PCM, Mono, 22050Hz, 16-bit (convert via Audacity).
5. Create a folder with "speakers" and "output" subfolders. Put WAV files into "speakers".

Example folder structure:
```
C:\xtts
  - speakers
    - alice.wav
    - bob.wav
  - output
```

## Installing 

daswer123 (https://github.com/daswer123) made an API server that runs the XTTSv2 model on your computer and connects to SillyTavern's TTS extension.

It's completely independent of Extras API and would use a separate environment.

**Very important:** Don't install the following requirements to your Extras environment or system Python.
It will break your other packages, do unnecessary downgrades, etc.

The following instruction is provided using Miniconda, but you can also do it with venv (not covered here).
Open the Anaconda command prompt and follow the instructions line by line.

### Getting the server up and running

1. Navigate to the folder you've created at step 4 of prerequisites.
    ```
    cd C:\xtts
    ```
2. Create a new conda env. From now on, we'll call it `xtts`.
    ```
    conda create -n xtts
    ```
3. Activate a newly created env.
    ```
    conda activate xtts
    ```
4. Install Python 3.10 to your env. Confirm with "y" when prompted.
    ```
    conda install python=3.10
    ```
5. Install the XTTS server with its requirements.
    ```
    pip install xtts-api-server pydub
    ```
6. Install PyTorch. This can take some time. The following line installs PyTorch with GPU acceleration support (CUDA).
If you want to use just the CPU inference, drop the last part that starts with `--index-url`.
    ```
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    ```
7. Start the XTTS server on the default host and port: <http://localhost:8020>
    ```
    python -m xtts_api_server
    ```
8. During your first startup, the model will be downloaded (about ~2 GB).
Don't forget to read the legal notice from Coqui AI very carefully. Lol, I'm kidding, just hit "y" again.

### Connecting to SillyTavern

1. Open the extensions panel, expand the TTS menu, and pick "XTTSv2" in the provider list.
2. Choose your text-to-speech language in the Language dropdown (I'll be sad if it's not Polish).
3. Verify that the provider endpoint points to <http://localhost:8020> and "Available voices" shows a list of your voice samples.
4. Pick any character and set a mapping between the voice sample and the character.
If the characters list is empty, hit "Reload" a couple of times.
5. Configure the rest of the TTS settings according to your preferences.

### You're all set now!

Click on the bullhorn icon in the context actions menu for any message and hear the beautiful cloned voice emanating
from your speakers. The generation takes some time and it's not real-time even on high-end RTX GPUs.

### Streaming?

It's possible to use HTTP streaming with the latest version of the XTTS server to get the chunks of generated audio as soon as it is available!

#### This doesn't work with RVC!

The audio will still be generated (assuming you're using the latest version of the RVC extension) and converted, *but not streamed* as RVC requires to have the full audio file before initiating the conversion. Streamed RVC is still being investigated...

#### How to get streaming support?

1. Update SillyTavern to the latest version.
2. Update the XTTS server to the latest version.

    ```bash
    conda activate xtts
    pip install xtts-api-server --upgrade
    ```

3. Start and connect XTTS to ST as usual.
4. Enable the "Streaming" XTTS extension setting in SillyTavern.

### Choppy audio?

Try increasing the "chunk size" setting.

For reference: with a chunk size of 200, RTX 3090 can produce uninterrupted audio at the cost of slightly increased audio latency.

### How to restart the TTS server?

Just do steps 1, 3 and 7 from the installation instruction.

### Android??

Unlikely, it can't run apps that require PyTorch without some arcane black magic that we don't provide support for. You can try it out at your own risk, but no support will be provided if you face any problems.

Your best solution is to host the TTS API on your PC over the local network, just don't forget to specify the host and port to listen on - see README (https://github.com/daswer123/xtts-api-server/blob/main/README.md).

# SECTION: SillyTavern_For_Contributors_Writing-Extensions

# UI Extensions

UI extensions expand SillyTavern's functionality by hooking into its events and API. They run in a browser context and have practically unrestricted access to the DOM, JavaScript APIs, and the SillyTavern context. Extensions can modify the UI, call internal APIs, and interact with chat data. This guide explains how to create your own extensions (JavaScript knowledge is required).

**Just want to install extensions?**

Go here: Extensions.

**To extend the functionality of the Node.js server, see the Server Plugins page.**

**Can't write JavaScript?**

* Consider STscript as a simpler alternative to writing a full-fledged extension.
* Go through the MDN Course (https://developer.mozilla.org/en-US/docs/Learn/JavaScript) and come back when you're done.

## Extension submissions

Want to contribute your extensions to the official content repository (https://github.com/SillyTavern/SillyTavern-Content)? Contact us!

To ensure that all extensions are safe and easy to use, we have a few requirements:

1. Your extension must be open-source and have a libre license (see Choose a License (https://choosealicense.com/licenses/)). If you are unsure, AGPLv3 is a good choice.
2. Extensions must be compatible with the latest release version of SillyTavern. Please be ready to update your extension if something in the core changes.
3. Extensions must be well-documented. This includes a README file with installation instructions, usage examples, and a list of features.
4. Extensions that have a server plugin requirement to function will not be accepted.

## Examples

See live examples of simple SillyTavern extensions:

* <https://github.com/city-unit/st-extension-example> - basic extension template. Showcases manifest creation, local script imports, adding a settings UI panel, and persistent extension settings usage.
* <https://github.com/search?q=topic%3Aextension+org%3ASillyTavern&type=Repositories> - a list of all official SillyTavern extensions on GitHub.

## Bundling

Extensions can also utilize bundling to isolate themselves from the rest of the modules and use any dependencies from NPM, including UI frameworks like Vue, React, etc.

* <https://github.com/SillyTavern/Extension-WebpackTemplate> - template repository of an extension using TypeScript and Webpack (no React).
* <https://github.com/SillyTavern/Extension-ReactTemplate> - template repository of a bare-bones extension using React and Webpack.

To use relative imports from the bundle, you may need to create an import wrapper. Here's an example for Webpack:

```js
/**
 * Import a member from a module by URL, bypassing webpack.
 * @param {string} url URL to import from
 * @param {string} what Name of the member to import
 * @param {any} defaultValue Fallback value
 * @returns {Promise<any>} Imported member
 */
export async function importFromUrl(url, what, defaultValue = null) {
    try {
        const module = await import(/* webpackIgnore: true */ url);
        if (!Object.hasOwn(module, what)) {
            throw new Error(`No ${what} in module`);
        }
        return module[what];
    } catch (error) {
        console.error(`Failed to import ${what} from ${url}: ${error}`);
        return defaultValue;
     }
}

// Import a function from 'script.js' module
const generateRaw = await importFromUrl('/script.js', 'generateRaw');
```

## manifest.json

Every extension must have a folder in `data/<user-handle>/extensions` and a `manifest.json` file, which contains metadata about the extension and a path to a JS script file that is the entry point of the extension.

Downloadable extensions are mounted into the `/scripts/extensions/third-party` folder when serving over HTTP, so relative imports should be used based on that. To ease local development, consider placing your extension repository in the `/scripts/extensions/third-party` folder (the "Install for all users" option).

```json
{
    "display_name": "The name of the extension",
    "loading_order": 1,
    "requires": [],
    "optional": [],
    "dependencies": [],
    "js": "index.js",
    "css": "style.css",
    "author": "Your name",
    "version": "1.0.0",
    "homePage": "https://github.com/your/extension",
    "auto_update": true,
    "minimum_client_version": "1.0.0",
    "i18n": {
        "de-de": "i18n/de-de.json"
    }
}
```

### Manifest fields

* `display_name` is required. It is displayed in the "Manage Extensions" menu.
* `loading_order` is optional. A higher number loads later.
* `js` is the main JS file reference and is required.
* `css` is an optional style file reference.
* `author` is required. It should contain the name or contact info of the author(s).
* `auto_update` is set to `true` if the extension should auto-update when the version of the ST package changes.
* `i18n` is an optional object that specifies the supported locales and their corresponding JSON files (see below).
* `dependencies` is an optional array of strings specifying other **extensions** that this extension depends on.
* `generate_interceptor` is an optional string that specifies the name of a global function called on text generation requests.
* `minimum_client_version` is an optional string that specifies the minimum SillyTavern version required for this extension to work.

### Dependencies

Extensions can also depend on other SillyTavern extensions. The extension will not load if any of these dependencies are missing or disabled.

Dependencies are specified by their **folder name** as it appears in the `public/extensions` directory.

Examples:

* Built-in extensions: `"vectors"`, `"caption"`
* Third-party extensions: `"third-party/Extension-WebLLM"`, `"third-party/Extension-Mermaid"`

### Deprecated fields

* `requires` is an optional array of strings specifying required **Extras modules**. The extension won't be loaded if the connected Extras API doesn't provide all listed modules.
* `optional` is an optional array of strings specifying optional **Extras modules**. The extension will still load if these are missing, and the extension should handle their absence gracefully.

To check which modules are currently provided by the connected Extras API, import the `modules` array from `scripts/extensions.js`.

## Scripting

### Using getContext

The `getContext()` function in the `SillyTavern` global object gives you access to the SillyTavern context, which is a collection of all the main app state objects, useful functions, and utilities.

```js
const context = SillyTavern.getContext();
context.chat; // Chat log - MUTABLE
context.characters; // Character list
context.characterId; // Index of the current character
context.groups; // Group list
context.groupId; // ID of the current group
// And many more...
```

You can find the full list of available properties and functions in the SillyTavern source code (https://github.com/SillyTavern/SillyTavern/blob/staging/public/scripts/st-context.js).

**If you're missing any of the functions/properties in `getContext`, please get in touch with the developers or send us a pull request!**

**### Shared libraries**

Most of the npm libraries used internally by the SillyTavern frontend are shared in the `libs` property of the `SillyTavern` global object.

* `lodash` - Utility library. Docs (https://lodash.com/).
* `localforage` - Browser storage library. Docs (https://localforage.github.io/localForage/).
* `Fuse` - Fuzzy search library. Docs (https://www.fusejs.io/).
* `DOMPurify` - HTML sanitization library. Docs (https://github.com/cure53/DOMPurify).
* `Handlebars` - Templating library. Docs (https://handlebarsjs.com/).
* `moment` - Date/time manipulation library. Docs (http://momentjs.com/).
* `showdown` - Markdown converter library. Docs (https://showdownjs.com/).

You can find the full list of exported libraries in the SillyTavern source code (https://github.com/SillyTavern/SillyTavern/blob/staging/public/lib.js).

**Example:** Using the DOMPurify library.

```js
const { DOMPurify } = SillyTavern.libs;

const sanitizedHtml = DOMPurify.sanitize('<script>"dirty HTML"</script>');
```

### TypeScript notice

If you want access to autocomplete for all methods in the `SillyTavern` global object (and you probably do), including `getContext()` and `libs`, you should add a TypeScript `.d.ts` module declaration. This declaration should import global types from SillyTavern's source, depending on your extension's location. Below is an example that works for both installation types: "all users" and "current user."

**global.d.ts** - place this file in the root of your extension directory (next to `manifest.json`):

```ts
export {};

// 1. Import for user-scoped extensions
import '../../../../public/global';
// 2. Import for server-scoped extensions
import '../../../../global';

// Define additional types if needed...
declare global {
    // Add global type declarations here
}
```

### Importing from other files

Using imports from SillyTavern code is unreliable and can break at any time if the internal structure of ST's modules changes. `getContext` provides a more stable API.

**Unless you're building a bundled extension, you can import variables and functions from other JS files.**

For example, this code snippet will generate a reply from the currently selected API in the background:

```js
import { generateQuietPrompt } from "../../../../script.js";

async function handleMessage(data) {
    const text = data.message;
    const translated = await generateQuietPrompt({ quietPrompt: text });
    // ...
}
```

## State management

### Persistent settings

When an extension needs to persist its state, it can use the `extensionSettings` object from the `getContext()` function to store and retrieve data. An extension can store any JSON-serializable data in the settings object and must use a unique key to avoid conflicts with other extensions.

To persist the settings, use the `saveSettingsDebounced()` function, which will save the settings to the server.

```js
const { extensionSettings, saveSettingsDebounced } = SillyTavern.getContext();

// Define a unique identifier for your extension
const MODULE_NAME = 'my_extension';

// Define default settings
const defaultSettings = Object.freeze({
    enabled: false,
    option1: 'default',
    option2: 5
});

// Define a function to get or initialize settings
function getSettings() {
    // Initialize settings if they don't exist
    if (!extensionSettings[MODULE_NAME]) {
        extensionSettings[MODULE_NAME] = structuredClone(defaultSettings);
    }

    // Ensure all default keys exist (helpful after updates)
    for (const key of Object.keys(defaultSettings)) {
        if (!Object.hasOwn(extensionSettings[MODULE_NAME], key)) {
            extensionSettings[MODULE_NAME][key] = defaultSettings[key];
        }
    }

    return extensionSettings[MODULE_NAME];
}

// Use the settings
const settings = getSettings();
settings.option1 = 'new value';

// Save the settings
saveSettingsDebounced();
```

### Chat metadata

To bind some data to a specific chat, you can use the `chatMetadata` object from the `getContext()` function. This object allows you to store arbitrary data associated with a chat, which can be useful for storing extension-specific state.

To persist the metadata, use the `saveMetadata()` function, which will save the metadata to the server.

Do not save the reference to `chatMetadata` in a long-lived variable, as the reference will change when the chat is switched. Always use `SillyTavern.getContext().chatMetadata` to access the current chat metadata.

```js

const { chatMetadata, saveMetadata } = SillyTavern.getContext();

// Set some metadata for the current chat
chatMetadata['my_key'] = 'my_value';

// Get the metadata for the current chat
const value = chatMetadata['my_key'];

// Save the metadata to the server
await saveMetadata();
```

The `CHAT_CHANGED` event is emitted when the chat is switched, so you can listen to this event to update your extension's state accordingly. See more in the Listening to events section.

**### Character cards**

SillyTavern fully supports Character Cards V2 Specification (https://github.com/malfoyslastname/character-card-spec-v2/blob/main/spec_v2.md), which allows to store arbitrary data in the character card JSON data.

This is useful for extensions that need to store additional data associated with the character and make it shareable when exporting the character card.

To write data to the character card extensions (https://github.com/malfoyslastname/character-card-spec-v2/blob/main/spec_v2.md#extensions) data field, use the `writeExtensionField` function from the `getContext()` function. This function takes a character ID, a string key, and a value to write. The value must be JSON-serializable.

**Weirdness Ahead**

Despite being called `characterId`, it's not a "real" unique identifier but rather an index of the character in the `characters` array.

The index of the current character is provided by the `characterId` property in the context. If you want to write data to the currently selected character, use `SillyTavern.getContext().characterId`. If you need to store data for another character, find the index by searching for the character in the `characters` array.

**Caution: `characterId` is `undefined` in group chats or when no character is selected!**

```js

const { writeExtensionField, characterId } = SillyTavern.getContext();

// Write some data to the character card
await writeExtensionField(characterId, 'my_extension_key', {
    someData: 'value',
    anotherData: 42
});

// Read the data back from the character card
const character = SillyTavern.getContext().characters[characterId];
// The data is stored in the `extensions` object of the character's data
const myData = character.data?.extensions?.my_extension_key;
```

### Settings presets

Arbitrary JSON data can be stored in the settings presets of the main API types. It will be exported and imported along with the preset JSON, so you can use it to store extension-specific settings for the preset. The following API types support data extensions in settings presets:

* Chat Completion
* Text Completion
* NovelAI
* KoboldAI / AI Horde

To read or write the data, you first need to get the PresetManager instance from the context:

```js
const { getPresetManager } = SillyTavern.getContext();

// Get the preset manager for the current API type
const pm = getPresetManager();

// Write data to the preset extension field:
// - path: the path to the field in the preset data
// - value: the value to write
// - name (optional): the name of the preset to write to, defaults to the currently selected preset
await pm.writePresetExtensionField({ path: 'hello', value: 'world' });

// Read data from the preset extension field:
// - path: the path to the field in the preset data
// - name (optional): the name of the preset to read from, defaults to the currently selected preset
const value = pm.readPresetExtensionField({ path: 'hello' });
```

The `PRESET_CHANGED` and `MAIN_API_CHANGED` events are emitted when the preset is changed or the main API is switched, so you can listen to these events to update your extension's state accordingly. See more in the Listening to events section.

**## Internationalization**

**For general information on providing translations, see the Internationalization page.**

**Extensions can provide additional localized strings for use with the `t`, `translate` functions and the `data-i18n` attribute in HTML templates.**

See the list of supported locales here (`lang` key): <https://github.com/SillyTavern/SillyTavern/blob/release/public/locales/lang.json>

### Direct `addLocaleData` call

Pass a locale code and an object with the translations to the `addLocaleData` function. Overrides of existing keys are *NOT* allowed. If the passed locale code is not a currently chosen locale, the data will be silently ignored.

```js
SillyTavern.getContext().addLocaleData('fr-fr', { 'Hello': 'Bonjour' });
SillyTavern.getContext().addLocaleData('de-de', { 'Hello': 'Hallo' });
```

### Via the extension manifest

Add an i18n object with a list of supported locales and their corresponding JSON file paths (relative to your extension's directory) to the manifest.

```json
{
  "display_name": "Foobar",
  "js": "index.js",
  // rest of the fields
  "i18n": {
    "fr-fr": "i18n/french.json",
    "de-de": "i18n/german.json"
  }
}
```

## Registering slash commands (new way)

While `registerSlashCommand` still exists for backward compatibility, new slash commands should now be registered through `SlashCommandParser.addCommandObject()` to provide extended details about the command and its parameters to the parser (and, in turn, to autocomplete and the command help).

```javascript
SlashCommandParser.addCommandObject(SlashCommand.fromProps({ name: 'repeat',
    callback: (namedArgs, unnamedArgs) => {
        return Array(namedArgs.times ?? 5)
            .fill(unnamedArgs.toString())
            .join(isTrueBoolean(namedArgs.space.toString()) ? ' ' : '')
        ;
    },
    aliases: ['example-command'],
    returns: 'the repeated text',
    namedArgumentList: [
        SlashCommandNamedArgument.fromProps({ name: 'times',
            description: 'number of times to repeat the text',
            typeList: ARGUMENT_TYPE.NUMBER,
            defaultValue: '5',
        }),
        SlashCommandNamedArgument.fromProps({ name: 'space',
            description: 'whether to separate the texts with a space',
            typeList: ARGUMENT_TYPE.BOOLEAN,
            defaultValue: 'off',
            enumList: ['on', 'off'],
        }),
    ],
    unnamedArgumentList: [
        SlashCommandArgument.fromProps({ description: 'the text to repeat',
            typeList: ARGUMENT_TYPE.STRING,
            isRequired: true,
        }),
    ],
    helpString: `
        <div>
            Repeats the provided text a number of times.
        </div>
        <div>
            <strong>Example:</strong>
            <ul>
                <li>
                    <pre><code class="language-stscript">/repeat foo</code></pre>
                    returns "foofoofoofoofoo"
                </li>
                <li>
                    <pre><code class="language-stscript">/repeat times=3 space=on bar</code></pre>
                    returns "bar bar bar"
                </li>
            </ul>
        </div>
    `,
}));
```

All registered commands can be used in STscript in any possible way.

## Events

### Listening to events

Use `eventSource.on(eventType, eventHandler)` to listen for events:

```js
const { eventSource, event_types } = SillyTavern.getContext();

eventSource.on(event_types.MESSAGE_RECEIVED, handleIncomingMessage);

function handleIncomingMessage(data) {
    // Handle message
}
```

The main event types are:

* `APP_INITIALIZED`: the app is initialized and close to being ready, but the loader is still visible. UI modifications can be done here. It will auto-fire every time a new listener is attached after the app is initialized.
* `APP_READY`: the app is fully loaded and ready to use. It will auto-fire every time a new listener is attached after the app is ready.
* `MESSAGE_RECEIVED`: the LLM message is generated and recorded into the `chat` object but not yet rendered in the UI.
* `MESSAGE_SENT`: the message is sent by the user and recorded into the `chat` object but not yet rendered in the UI.
* `USER_MESSAGE_RENDERED`: the message sent by a user is rendered in the UI.
* `CHARACTER_MESSAGE_RENDERED`: the generated LLM message is rendered in the UI.
* `CHAT_CHANGED`: the chat has been switched (e.g., switched to another character, or another chat was loaded).
* `GENERATION_AFTER_COMMANDS`: the generation is about to start after processing slash commands.
* `GENERATION_STOPPED`: the generation was stopped by the user.
* `GENERATION_ENDED`: the generation has been completed or has errored out.
* `SETTINGS_UPDATED`: the application settings have been updated.

The rest can be found in the source (https://github.com/SillyTavern/SillyTavern/blob/staging/public/scripts/events.js).

**Event data**

The way each event passes its data to the listener is not uniform. Some events don't emit any data; some pass an object or a primitive value. Please refer to the source code where the event is emitted to see what data it passes, or check with the debugger.

**### Emitting events**

You can produce any application events from extensions, including custom events, by calling `eventSource.emit(eventType, ...eventData)`:

```js
const { eventSource } = SillyTavern.getContext();

// Can be a built-in event_types field or any string.
const eventType = 'myCustomEvent';

// Use `await` to ensure all event handlers complete before continuing execution.
await eventSource.emit(eventType, { data: 'custom event data' });
```

## Prompt Interceptors

Prompt Interceptors provide a way for extensions to perform any activity such as modifying the chat data, adding injections, or aborting the generation before a text generation request is made.

Interceptors from different extensions are run sequentially. The order is determined by the `loading_order` field in their respective `manifest.json` files. Extensions with lower `loading_order` values run earlier. If `loading_order` is not specified, `display_name` is used as a fallback. If neither is specified, the order is undefined.

### Registering an Interceptor

To define a prompt interceptor, add a `generate_interceptor` field to your extension's `manifest.json` file. The value should be the name of a global function that will be called by SillyTavern.

```json
{
    "display_name": "My Interceptor Extension",
    "loading_order": 10, // Affects execution order
    "generate_interceptor": "myCustomInterceptorFunction",
    // ... other manifest properties
}
```

### Interceptor Function

The `generate_interceptor` function is a global function that will be called upon generation requests that are not dry runs. It must be defined in the global scope (e.g., `globalThis.myCustomInterceptorFunction = async function(...) { ... }`) and can return a `Promise` if it needs to perform any asynchronous operations.

The interceptor function receives the following arguments:

* `chat`: An array of message objects representing the chat history that will be used for prompt building. You can modify this array directly (e.g., add, remove, or alter messages). Please note that messages are mutable, so any changes you make to the array will be reflected in the actual chat history. If you want the changes to be ephemeral, use `structuredClone` to create a deep copy of the message object.
* `contextSize`: A number indicating the current context size (in tokens) calculated for the upcoming generation.
* `abort`: A function that, when called, will signal to prevent the text generation from proceeding. It accepts a boolean parameter that prevents any subsequent interceptors from running if `true`.
* `type`: A string indicating the type or trigger of the generation (e.g., `'quiet'`, `'regenerate'`, `'impersonate'`, `'swipe'`, etc.). This helps the interceptor apply logic conditionally based on how the generation was initiated.

**Example Implementation:**

```javascript
globalThis.myCustomInterceptorFunction = async function(chat, contextSize, abort, type) {
    // Example: Add a system note before the last user message
    const systemNote = {
        is_user: false,
        name: "System Note",
        send_date: Date.now(),
        mes: "This was added by my extension!"
    };
    // Insert before the last message
    chat.splice(chat.length - 1, 0, systemNote);
}
```

## Generating text

SillyTavern provides several functions to generate text in different contexts using the currently chosen LLM API. These functions allow you to generate text in the context of a chat, raw generation without any context, or with structured outputs.

### Within a chat context

The `generateQuietPrompt()` function is used to generate text in the context of a chat with an added "quiet" prompt (post-history instruction) in the background (the output is not rendered in the UI). This is useful for generating text without interrupting the user experience while also keeping the relevant chat and character data intact, such as generating a summary or an image prompt.

```js
const { generateQuietPrompt } = SillyTavern.getContext();

const quietPrompt = 'Generate a summary of the chat history.';

const result = await generateQuietPrompt({
    quietPrompt,
});
```

### Raw generation

The `generateRaw()` function is used to generate text without any chat context. It is useful when you want to fully control the prompt-building process.

It accepts a `prompt` as a Text Completion string or an array of Chat Completion objects, constructing the request with an appropriate format depending on the selected API type, e.g., converting between chat/text modes, applying instruct formatting, etc. You can also pass an additional `systemPrompt` and a `prefill` to the function for even more control over the generation process.

```js
const { generateRaw } = SillyTavern.getContext();

const systemPrompt = 'You are a helpful assistant.';
const prompt = 'Generate a story about a brave knight.';
const prefill = 'Once upon a time,';

/*
In Chat Completion mode, will produce a prompt like this:
[
  {role: 'system', content: 'You are a helpful assistant.'},
  {role: 'user', content: 'Generate a story about a brave knight.'},
  {role: 'assistant', content: 'Once upon a time,'}
]
*/

/*
In Text Completion mode (no instruct), will produce a prompt like this:
"You are a helpful assistant.\nGenerate a story about a brave knight.\nOnce upon a time,"
*/

const result = await generateRaw({
    systemPrompt,
    prompt,
    prefill,
});
```

### Structured Outputs

Currently only supported by the Chat Completion API. The availability varies based on the selected source and model. If the selected model does not support structured outputs, the generation will either fail or will return an empty object (`'{}'`). Check the documentation for the specific API you are using to see if structured outputs are supported.

**You can use the structured outputs feature to ensure the model produces a valid JSON object that adheres to a provided JSON Schema (https://json-schema.org/learn). This is useful for extensions that require structured data, such as state tracking, data classification, etc.**

To use structured outputs, you must pass a JSON schema object to `generateRaw()` or `generateQuietPrompt()`. The model will then generate a response that matches the schema, and it will be returned as a stringified JSON object.

The outputs are not validated against the schema, you must handle the parsing and validation of the generated output yourself. If the model fails to generate a valid JSON object, the function will return an empty object (`'{}'`).

Zod (https://zod.dev/json-schema) is a popular library to generate and validate JSON schemas. Its use will not be covered here.

```js

const { generateRaw, generateQuietPrompt } = SillyTavern.getContext();

// Define a JSON schema for the expected output
const jsonSchema = {
    // Required: a name for the schema
    name: 'StoryStateModel',
    // Optional: a description of the schema
    description: 'A schema for a story state with location, plans, and memories.',
    // Optional:  the schema will be used in strict mode, meaning that only the fields defined in the schema will be allowed
    strict: true,
    // Required: a definition of the schema
    value: {
        '$schema': 'http://json-schema.org/draft-04/schema#',
        'type': 'object',
        'properties': {
            'location': {
                'type': 'string'
            },
            'plans': {
                'type': 'string'
            },
            'memories': {
                'type': 'string'
            }
        },
        'required': [
            'location',
            'plans',
            'memories'
        ],
    },
};

const prompt = 'Generate a story state with location, plans, and memories. Output as a JSON object.';

const rawResult = await generateRaw({
    prompt,
    jsonSchema,
});

const quietResult = await generateQuietPrompt({
    quietPrompt: prompt,
    jsonSchema,
});
```

## Registering custom macros

You can register custom macros that can be used anywhere where macro substitutions are supported, e.g. in the character card fields, STscript commands, prompt templates, etc.

To register a macro, use the `registerMacro()` function from the `SillyTavern.getContext()` object. The function accepts a macro name that should be a unique string, and a string or a function that returns a string. The function will be called with a unique `nonce` string that will be different between each `substituteParams` call.

```js
const { registerMacro } = SillyTavern.getContext();

// Simple string macro
registerMacro('fizz', 'buzz');
// Function macro
registerMacro('tomorrow', () => {
    return new Date(Date.now() + 24 * 60 * 60 * 1000).toLocaleDateString();
});
```

When a custom macro is no longer needed, remove it using the `unregisterMacro()` function:

```js
const { unregisterMacro } = SillyTavern.getContext();

// Unregister the 'fizz' macro
unregisterMacro('fizz');
```

**Important details and known limitations regarding custom macros:**

1. Currently only simple string replacement macros are supported. We're working on adding support for more complex macros in the future.
2. Macros that use functions to provide a value *must* be synchronous. Returning a `Promise` will not work.
3. You do not need to wrap the macro name in double curly braces (`{{ }}`) when registering it. SillyTavern will do that for you.
4. Since macros are plain regular expression substitutions, registering a lot of macros will cause performance issues, so use them sparingly.

## Do Extras request

The Extras API is deprecated. It's not recommended to use it in new extensions.

**The `doExtrasFetch()` function allows you to make requests to your SillyTavern Extras API server.**

For example, to call the `/api/summarize` endpoint:

```js
import { getApiUrl, doExtrasFetch } from "../../extensions.js";

const url = new URL(getApiUrl());
url.pathname = '/api/summarize';

const apiResult = await doExtrasFetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Bypass-Tunnel-Reminder': 'bypass',
    },
    body: JSON.stringify({
        // Request body
    })
});
```

`getApiUrl()` returns the base URL of the Extras server.

The `doExtrasFetch()` function:

* Adds the `Authorization` and `Bypass-Tunnel-Reminder` headers
* Handles fetching the result
* Returns the result (the response object)

This makes it easy to call your Extras API from your extension.

You can specify:

* The request method: GET, POST, etc.
* Additional headers
* The body for POST requests
* Any other fetch options

## Best Practices

### Security

**Never store API keys or secrets in `extensionSettings`**

Extension settings are accessible to all other extensions and are stored in plain text. Do not store sensitive data client-side:

```js
// BAD - Don't do this!
extensionSettings[MODULE_NAME].apiKey = 'secret_key_123';

// NOTE: There is no secure way to store secrets in client-side extensions.
// If you need to handle sensitive data, use server plugins instead.
// See: https://docs.sillytavern.app/for-contributors/server-plugins/
```

**Sanitize user inputs**

Always validate and sanitize data from user inputs before using it in commands, API calls, or DOM manipulation:

```js
// Validate input type first
if (typeof userInput !== 'string') {
    toastr.error('Invalid input type');
    return;
}
// Use DOMPurify to sanitize HTML input
const { DOMPurify } = SillyTavern.libs;
const cleanInput = DOMPurify.sanitize(userInput);
```

**Avoid using `eval()` or `Function()` constructors**

These can execute arbitrary code and pose security risks. If you need dynamic evaluation, use safer alternatives or restrict the input carefully.

### Performance

**Don't store large data in `extensionSettings`**

Extension settings are loaded into memory and saved frequently. Large data can cause performance issues:

```js
// BAD - Don't store large data
extensionSettings[MODULE_NAME].largeDataset = { /* megabytes of data */ };

// GOOD - Use localforage (abstraction over IndexedDB/localStorage)
const { localforage } = SillyTavern.libs;
await localforage.setItem(`${MODULE_NAME}_data`, largeData);

// Or use localStorage for smaller data
localStorage.setItem(`${MODULE_NAME}_data`, JSON.stringify(smallData));
```

**Clean up event listeners**

Remove event listeners when they're no longer needed to prevent memory leaks:

```js
function cleanup() {
    eventSource.removeListener(event_types.MESSAGE_RECEIVED, handleMessage);
    document.getElementById('myElement').removeEventListener('click', handleClick);
}
```

**Don't block the UI thread**

For heavy operations, use async/await or web workers:

```js
// Use async for I/O operations
async function processData() {
    const result = await fetch('/api/process');
    return result.json();
}

// Break up heavy computations
async function heavyComputation(data) {
    for (let i = 0; i < data.length; i++) {
        // Process chunk
        if (i % 1000 === 0) {
            await new Promise(resolve => setTimeout(resolve, 0)); // Yield to UI
        }
    }
}
```

### Compatibility

**Prefer `getContext()` over direct imports**

The context API is more stable and less likely to break with SillyTavern updates:

```js
// GOOD - Stable API
const { chat, characters, saveSettingsDebounced } = SillyTavern.getContext();

// AVOID - May break with internal changes
import { chat, characters } from '../../../../script.js';
```

**Use unique module names**

Prevent conflicts with other extensions by using a descriptive, unique module name:

```js
// GOOD - Specific and unique
const MODULE_NAME = 'my_extension_name';

// BAD - Too generic, likely to conflict
const MODULE_NAME = 'settings';
```

### User Experience

**Provide clear feedback**

Use toastr notifications to inform users of actions and errors:

```js
const { Popup } = SillyTavern.getContext();

// Success message
toastr.success('Data imported successfully');

// Error message
toastr.error('Failed to connect to API');

// Warning message
toastr.warning('This feature is experimental');

// For important messages, use popups
const result = await Popup.show.confirm('Confirm', 'Are you sure?');
const userInput = await Popup.show.input('Input', 'Please enter a value:', 'default value');
await Popup.show.text('Info', 'Operation completed successfully.');
```

**Provide helpful console messages**

Use a consistent prefix for your console logs. But do not spam the console with excessive logs in production:

```js
const MODULE_NAME = 'MyExtension';

console.log(`[${MODULE_NAME}] Extension loaded`);
console.debug(`[${MODULE_NAME}] Processing data:`, data);
console.error(`[${MODULE_NAME}] Error occurred:`, error);
```

### Code Quality

**Use bundled libraries from `lib.js`**

SillyTavern bundles several useful libraries that extensions can be used directly:

```js
// Utility functions
const { lodash } = SillyTavern.libs;
const uniqueItems = lodash.uniq([1, 2, 2, 3]);
const grouped = lodash.groupBy([{ category: 'A', name: 'foo' }, { category: 'B', name: 'bar' }], 'category');

// Fuzzy search
const { Fuse } = SillyTavern.libs;
const fuse = new Fuse(items, { keys: ['name', 'description'] });
const results = fuse.search('query');

// Template rendering
const { Handlebars } = SillyTavern.libs;
const template = Handlebars.compile('<div>{{name}}</div>');
const html = template({ name: 'Example' });

// Date/time manipulation
const { moment } = SillyTavern.libs;
const formatted = moment().format('YYYY-MM-DD HH:mm:ss');
```

Other available libraries include: `DOMPurify`, `localforage`, `hljs`, `showdown`, `yaml`, and more. Check lib.js (https://github.com/SillyTavern/SillyTavern/blob/release/public/lib.js) for the full list.

**Initialize settings properly**

Always provide defaults and handle missing keys:

```js
function loadSettings() {
    // Merge with defaults to handle new keys after updates and initialize if it doesn't exist.
    extensionSettings[MODULE_NAME] = SillyTavern.libs.lodash.merge(
        structuredClone(defaultSettings),
        extensionSettings[MODULE_NAME]
    );
}
```

# SECTION: SillyTavern_For_Contributors_Function-Calling

# Function Calling

Function Calling allows adding dynamic functionality to your extensions by letting the LLM use structured data that you then can use to trigger a specific functionality of the extension.

## Example use cases

1. Query external APIs for additional information (news, weather, web search, etc.).
2. Perform calculations or conversions based on user input.
3. Store and recall important memories or facts, including RAG and database queries.
4. Introduce true randomness into the conversation (dice rolls, coin flips, etc.).

## Officially supported extensions using function calling

1. Image Generation (built-in) - generate images based on user prompts.
2. Web Search - trigger a web search for a query.
3. RSS (https://github.com/SillyTavern/Extension-RSS/) - fetch the latest news from RSS feeds.
4. AccuWeather (https://github.com/SillyTavern/Extension-AccuWeather) - fetch the weather information from AccuWeather.
5. D&D Dice (https://github.com/SillyTavern/Extension-Dice) - roll dice for D&D games.

## Prerequisites and limitations

1. This feature is only available for certain Chat Completion sources: OpenAI, Claude, MistralAI, Groq, Cohere, OpenRouter, AI21, Google AI Studio, Google Vertex AI, DeepSeek, AI/ML API, NanoGPT and Custom API sources.
2. Text Completion APIs don't support function calls, but some locally-hosted backends like Ollama and TabbyAPI may run in Custom OpenAI-compatible mode under Chat Completion.
3. The support for function calling must be explicitly allowed by the user first. This is done by enabling the "Enable function calling" option in the AI Response Configuration panel.
4. There is no guarantee that an LLM will perform any function calls at all. Most of them require an explicit "activation" through the prompt (e.g., the user asking to "Roll a dice", "Get the weather", etc.).
5. Not all prompts can trigger a tool call. Continuations, impersonation, background ('quiet') prompts are not allowed to trigger a tool call. They can still use past successful tool calls in their responses.

## How to make a function tool

### Check if the feature is supported

To determine if the function tool calling feature is supported, you can call `isToolCallingSupported` from the `SillyTavern.getContext()` object. This will check if the current API supports function tool calling and if it's enabled in the settings. Here is an example of how to check if the feature is supported:

```ts
if (SillyTavern.getContext().isToolCallingSupported()) {
    console.log("Function tool calling is supported");
} else {
    console.log("Function tool calling is not supported");
}
```

### Register a function

To register a function tool, you need to call the `registerFunctionTool` function from the `SillyTavern.getContext()` object and pass the required parameters. Here is an example of how to register a function tool:

```ts
SillyTavern.getContext().registerFunctionTool({
    // Internal name of the function tool. Must be unique.
    name: "myFunction",
    // Display name of the function tool. Will be shown in the UI. (Optional)
    displayName: "My Function",
    // Description of the function tool. Must describe what the function does and when to use it.
    description: "My function description. Use when you need to do something.",
    // JSON schema for the parameters of the function tool. See: https://json-schema.org/
    parameters: {
        $schema: 'http://json-schema.org/draft-04/schema#',
        type: 'object',
        properties: {
            param1: {
                type: 'string',
                description: 'Parameter 1 description',
            },
            param2: {
                type: 'string',
                description: 'Parameter 2 description',
            },
        },
        required: [
            'param1', 'param2',
        ],
    },
    // Function to call when the tool is triggered. Can be async.
    // If the result is not a string, it will be JSON-stringified.
    action: async ({ param1, param2 }) => {
        // Your function code here
        console.log(`Function called with parameters: ${param1}, ${param2}`);
        return "Function result";
    },
    // Optional function to format the toast message displayed when the function is invoked.
    // If an empty string is returned, no toast message will be displayed.
    formatMessage: ({ param1, param2 }) => {
        return `Function is called with: ${param1} and ${param2}`;
    },
    // Optional function that returns a boolean value indicating whether the tool should be registered for the current prompt.
    // If no shouldRegister function is provided, the tool will be registered for every prompt.
    shouldRegister: () => {
        return true;
    },
    // Optional flag. If set to true, the function call will be performed, but the result won't be recorded to the visible chat history.
    stealth: false,
});
```

### Unregister a function

To deactivate a function tool, you need to call the `unregisterFunctionTool` function from the `SillyTavern.getContext()` object and pass the name of the function tool to disable. Here is an example of how to unregister a function tool:

```ts
SillyTavern.getContext().unregisterFunctionTool("myFunction");
```

## Tips and tricks

1. Successful tool calls are saved as a part of the visible history and will be displayed in the chat UI, so you can inspect the actual parameters and results. If that is not desirable, set the `stealth: true` flag when registering a function tool.
2. If you don't want to see the tool call in the chat history. If you want to stylize or hide them with custom CSS, target a `toolCall` class on `.mes` elements, i.e. `.mes.toolCall { display: none; }` or `.mes.toolCall { color: #999; }`.

# SECTION: SillyTavern_For_Contributors_i18n

# Internationalization (i18n)

SillyTavern supports multiple languages. This guide explains how to add and manage translations.

You're probably here because some piece of text is untranslated in your language, and it's driving you nuts. First I'll
show you how I fixed some missing translations in the Chinese (Traditional) locale. Each was missing for a different
reason, so you'll get a good idea of how to fix your own missing translations.

In the second half, we look at

- how i18n works in SillyTavern,
- writing translations and code to use them,
- debug functions to find missing translations,
- adding a new language,
- and contributing your changes.

If you're developing an extension or modifying the core code, write your HTML and JavaScript with i18n in mind. This way
your work is ready for other people to translate it into their language.

Nobody knows 15 languages by themselves. We work together to make SillyTavern accessible to everyone.

**Everyone in the world should be able to use their own language on phones and computers.**

--- 

## Let's fix some missing translations!

All 3 of these issues required code changes to fix. If you're adding a new translation, you might not need to touch
the code at all. Just add the translation to the JSON file. It just so happens that somebody recently added a large number
of missing translations to the Chinese (Traditional) JSON file, so the remaining issues were all in the code. In other locales
there are plenty of missing translations you can fix without touching the code.

**### `Generate Image`**

The text "Generate Image" is untranslated in the Chinese (Traditional) locale. Why?

Right-click on the element and inspect it. You'll see the HTML:

```html
<!--rendered HTML-->
<div class="list-group-item flex-container flexGap5 interactable" id="sd_gen" tabindex="0">
    <div data-i18n="[title]Trigger Stable Diffusion" title="觸發 Stable Diffusion"
         class="fa-solid fa-paintbrush extensionsMenuExtensionButton"></div>
    <span>Generate Image</span>
</div>
```

Where is its `data-i18n` attribute? It's missing! Let's add it. We find it in the source code:

```html
<!--public/scripts/extensions/stable-diffusion/button.html-->
<div id="sd_gen" class="list-group-item flex-container flexGap5">
    <div class="fa-solid fa-paintbrush extensionsMenuExtensionButton" title="Trigger Stable Diffusion"
         data-i18n="[title]Trigger Stable Diffusion"></div>
    <span>Generate Image</span>
</div>
<div id="sd_stop_gen" class="list-group-item flex-container flexGap5">
    <div class="fa-solid fa-circle-stop extensionsMenuExtensionButton" title="Abort current image generation task"
         data-i18n="[title]Abort current image generation task"></div>
    <span>Stop Image Generation</span>
</div>
```

We are in luck, that string `Generate Image` is in many of the language files, including in Chinese (Traditional).

```json
{
    "Generate Image": "生成图片"
}
```

Why isn't it showing up? We have to wire the element up correctly:

```html
<!--public/scripts/extensions/stable-diffusion/button.html-->
<div id="sd_gen" class="list-group-item flex-container flexGap5">
    <div class="fa-solid fa-paintbrush extensionsMenuExtensionButton" title="Trigger Stable Diffusion"
         data-i18n="[title]Trigger Stable Diffusion"></div>
    <span data-i18n="Generate Image">Generate Image</span>
</div>
<div id="sd_stop_gen" class="list-group-item flex-container flexGap5">
    <div class="fa-solid fa-circle-stop extensionsMenuExtensionButton" title="Abort current image generation task"
         data-i18n="[title]Abort current image generation task"></div>
    <span>Stop Image Generation</span>
</div>
```

Now it works! Reload the page and see.

But while we have the HTML open, what's with `Stop Image Generation` just under it? The HTML doesn't look right.

If we generate an image and then open the wand menu while it's generating, we see untranslated text.

First fix the HTML:

```html
<!--public/scripts/extensions/stable-diffusion/button.html-->
<div id="sd_gen" class="list-group-item flex-container flexGap5">
    <div class="fa-solid fa-paintbrush extensionsMenuExtensionButton" title="Trigger Stable Diffusion"
         data-i18n="[title]Trigger Stable Diffusion"></div>
    <span data-i18n="Generate Image">Generate Image</span>
</div>
<div id="sd_stop_gen" class="list-group-item flex-container flexGap5">
    <div class="fa-solid fa-circle-stop extensionsMenuExtensionButton" title="Abort current image generation task"
         data-i18n="[title]Abort current image generation task"></div>
    <span data-i18n="Stop Image Generation">Stop Image Generation</span>
</div>
```

This isn't enough to fix the issue. There are no translations for "Stop Image Generation" in the Chinese (Traditional)
file. We can add it! Here's one possible translation:

```json
{
    "Stop Image Generation": "停止生成图片"
} 
```

... which we can add to the JSON file just after the "Generate Image" translation.

```json
{
    "Generate Image": "生成图片",
    "Stop Image Generation": "停止生成图片"
} 
```

After some discussion with Claude, we're actually going to go with the following translations:

- Traditional Chinese: "Stop Image Generation": "終止圖片生成"
- Simplified Chinese: "Stop Image Generation": "中止图像生成"
- Japanese: "Stop Image Generation": "画像生成を停止"

### `Generate Caption`

"Generate Caption" is untranslated in the Chinese (Traditional) locale. Let's fix it!

Where is it? Inspect the element.

```html
<!--rendered HTML-->
<div id="send_picture" class="list-group-item flex-container flexGap5 interactable" tabindex="0">
    <div class="fa-solid fa-image extensionsMenuExtensionButton"></div>
    Generate Caption
</div>
```

Turns out that this HTML is produced by JavaScript. Let's find the source code.

```js
// public/scripts/extensions/caption/index.js
const sendButton = $(`
        <div id="send_picture" class="list-group-item flex-container flexGap5">
            <div class="fa-solid fa-image extensionsMenuExtensionButton"></div>
            Generate Caption
        </div>`);
```

We will first have to fix the code:

```js
// public/scripts/extensions/caption/index.js
const sendButton = $(`
        <div id="send_picture" class="list-group-item flex-container flexGap5">
            <div class="fa-solid fa-image extensionsMenuExtensionButton"></div>
            <span data-i18n="Generate Caption">Generate Caption</span>
        </div>`);
``` 

There are also no translations for "Generate Caption" in the Chinese (Traditional) file. Let's add it!

```json
{
    "Generate Caption": "生成圖片說明"
}
```

We will use the following translations:

- Traditional Chinese: "Generate Caption": "生成圖片說明"
- Simplified Chinese: "Generate Caption": "生成图片说明"
- Japanese: "Generate Caption": "画像説明を生成"

### `Inspect Prompts`

The text "Inspect Prompts" is untranslated in the Chinese (Traditional) locale. Why?
This one is a bit more complicated. The text is generated by JavaScript, and the translation is missing.

```js
// Extension-PromptInspector/index.js
const enabledText = 'Stop Inspecting';
const disabledText = 'Inspect Prompts';
```

Well wouldn't you know it... neither phrase is in the i18n files. Let's add them.

```json
{
    "Stop Inspecting": "停止檢查",
    "Inspect Prompts": "檢查提示"
}
```

Now we have to fix the JavaScript code. It has to use the `t` function to get the translation.

```js
// Extension-PromptInspector/index.js
import {t} from '../../../i18n.js';

const enabledText = t`Stop Inspecting`;
const disabledText = t`Inspect Prompts`;
```

We got these suggestions from Claude. Keep the strings, ignore the code. They have to be added to the JSON files.

```js
// 1. Simplified Chinese (zh-cn):
const enabledText = t`停止检查`;
const disabledText = t`检查提示词`;
// 2. Traditional Chinese (zh-tw):
const enabledText = t`停止檢查`;
const disabledText = t`檢查提示詞`;
// 3. Japanese (ja-jp):
const enabledText = t`検査を停止`;
const disabledText = t`プロンプトを検査`;
```

We will merge those into the JSON files.

```json
{
    "Stop Inspecting": "停止检查",
    "Inspect Prompts": "检查提示词"
}
```

```json
{
    "Stop Inspecting": "停止檢查",
    "Inspect Prompts": "檢查提示詞"
}
```

```json
{
    "Stop Inspecting": "検査を停止",
    "Inspect Prompts": "プロンプトを検査"
}
```

A pity about that tooltip. The problem is that the code doesn't use
the `t` function.

```js
launchButton.title = 'Toggle prompt inspection';
```

We will have to fix that in the extension code.

```js
launchButton.title = t`Toggle prompt inspection`;
```

We also need to add the translations to the JSON files.

```json
{
    "Toggle prompt inspection": "切换提示检查"
}
```

```json
{
    "Toggle prompt inspection": "切换提示词检查"
}
```

```json
{
    "Toggle prompt inspection": "プロンプト検査の切り替え"
}
```

Prompt inspector is a separate extension, so we will PR the code fixes to that
repo: https://github.com/SillyTavern/Extension-PromptInspector/pull/1

The translations will be added to the main SillyTavern repo. https://github.com/SillyTavern/SillyTavern/pull/3198

## Language files

Each language has a JSON file in `public/locales/` named with its language code (e.g., `ru-ru.json`).

The file contains key-value pairs where:

- Keys are either the original English text or unique identifiers
- Values are the translated text

Example:

```json
{
    "Save": "Сохранить",
    "Cancel": "Отмена",
    "Could not find proxy with name '${0}'": "Не удалось найти прокси с названием '${0}'"
}
```

## How translations work

There are two ways translations are used in the application:

1. **HTML Elements**: Using `data-i18n` attributes
   ```html
   <div data-i18n="some_key">Default Text</div>
   ```
   The default text in the HTML will be replaced with the translated text if available.

2. **Template Strings**: In the JavaScript code using the `t` function
   ```javascript
   t`Some text with ${variable}`
   ```
   These strings should be translated keeping the `${0}`, `${1}`, etc. placeholders intact.

SillyTavern uses HTML elements with `data-i18n` attributes to mark translatable content. There are several ways to use
this:

### 1. Translating Element Text

For simple text content:

```html
<span data-i18n="Role:">Role:</span>
```

```json
{
    "Role:": "Роль:"
}
```

This replaces the element's text content with the translation of "Role:".

### 2. Translating Attributes

To translate an attribute like a title or placeholder:

```html
<a class="menu_button fa-chain fa-solid fa-fw"
   title="Insert prompt"
   data-i18n="[title]Insert prompt"></a>
```

```json
{
    "Insert prompt": "Вставить промпт"
}
```

The `[title]` prefix indicates which attribute to translate. The rest of the attribute value is the text that will
be used as a lookup key in the JSON file. It is common for coders to use the English text as the key, but it is not
required. The key can be any unique identifier.

The original English text must be present in the corresponding attribute (`title="Insert prompt"`) though. It's used as
a fallback if the translation is missing. Most notably, there is no translation file for English.

Here is an example of using a unique identifier `no_items_text` as the key, rather than the English text:

```html
<!--suppress HtmlUnknownAttribute -->
<div class="openai_logit_bias_list" no_items_text="No items"
     data-i18n="[no_items_text]openai_logit_bias_no_items"></div>
```

```json
{
    "openai_logit_bias_no_items": "没有相关产品"
}   
```

### 3. Multiple Translations Per Element

Some elements need both content and attribute translations, separated by semicolons. The most common pattern is
translating both the element's text content and its title attribute:

```html
<div data-source="openrouter" class="menu_button menu_button_icon openrouter_authorize"
     title="Get your OpenRouter API token using OAuth flow. You will be redirected to openrouter.ai"
     data-i18n="Authorize;[title]Get your OpenRouter API token using OAuth flow. You will be redirected to openrouter.ai">
    Authorize
</div>
```

```json
{
    "Authorize": "Авторизоваться",
    "Get your OpenRouter API token using OAuth flow. You will be redirected to openrouter.ai": "Получите свой OpenRouter API токен используя OAuth. У вас будет открыта вкладка openrouter.ai"
}
```

This translates:

- The element's text content using the key "Authorize"
- The title attribute using the key "Get your OpenRouter API token using OAuth flow. You will be redirected to
  openrouter.ai"

Note that both the `title` attribute and the element's text content are provided in English as fallbacks.

You can also translate multiple attributes:

```html
<!--suppress HtmlUnknownAttribute -->
<textarea id="send_textarea" name="text" class="mdHotkeys"
          data-i18n="[no_connection_text]Not connected to API!;[connected_text]Type a message, or /? for help"
          placeholder="Not connected to API!"
          no_connection_text="Not connected to API!"
          connected_text="Type a message, or /? for help"></textarea>
```

The corresponding translations in your language file would look like:

```json
{
    "Not connected to API!": "Нет соединения с API!",
    "Type a message, or /? for help": "Введите сообщение или /? для помощи"
}
```

When the page loads, the system:

1. Finds all elements with `data-i18n` attributes
2. Parses any attribute prefixes like `[title]` or `[placeholder]`
3. Looks up each key in your language's JSON file
4. Replaces the element's content or attributes with the translated text

### Dynamic Text

For dynamic text in JavaScript code, translations use either:

1. Template literals with the `t` function:
    ```javascript
    toastr.warn(t`Tag ${tagName} not found.`);
    ```
2. Direct translation function:
    ```javascript
    translate("Some text", "optional_key")
    ```

### Variable Placeholders

Some strings contain placeholders for dynamic values using `${0}`, `${1}`, etc:

```js
toastr.error(t`Could not find proxy with name '${presetName}'`);
```

```json
{
    "Could not find proxy with name '${0}'": "Не удалось найти прокси с названием '${0}'"
}
```

Keep the placeholders the same for key and translation. The system will replace `${0}` with the value of `presetName`, etc.

## Finding missing translations

Let's say you don't just want to fix one annoying missing translation, you want to find them all.

That's a big ambition! Even fixing one translation is worth it. But if you want to catch 'em all, you need a tool.

### SillyTavern-i18n

https://github.com/SillyTavern/SillyTavern-i18n

Tools for working with frontend localization files.

Features:

- Automatically add new keys to translate from HTML files.
- Prune missing keys from localization files.
- Use automatic Google translation to auto-populate missing values.
- Sort JSON files by keys.

### Inbuilt debug functions

These are under <i class="fa-fw fa-solid fa-user-cog"></i> **User Settings** > **Debug Menu**.

#### Get missing translations

Detects missing localization data in the current locale and dumps the data into the browser console. If the current
locale is English, searches all other locales.

The console will show a table of missing translations with:

- key: The text or identifier needing translation
- language: Your current language code
- value: The English text to translate

#### Apply locale

Reapplies the currently selected locale to the page

**Neither of these tools are perfect**

- they don't catch missing translations in JavaScript code
- they don't catch missing data-i18n attributes in HTML, they just catch untranslated keys
- there are bugs in the code for `getMissingTranslations`: keys should not be prefixed with `[title]` or `[placeholder]`

**## Adding a new language**

To add support for a new language:

1. Add your language to `public/locales/lang.json`:

   ```json
   {
     "lang": "xx-xx",
     "display": "Language Name (English Name)"
   }
   ```

2. Create `public/locales/xx-xx.json` with your translations

## Contributing

When your translations are ready:

1. Verify your JSON file is valid
2. Test thoroughly in the application
3. Submit via GitHub pull request

# SECTION: SillyTavern_For_Contributors_index

# Development and Automation

SillyTavern's default package only provides a barebones platform that can be extended in a multitude of ways.

**STscript**

STscript is a powerful scripting language based on batched chat commands that can be approached without any prior coding knowledge.

**:::callout**

**Function Calling**

Add more dynamic capabilities by letting the LLM use external sources of data or trigger specific functionality of the extension.

**:::callout**

**UI Extensions**

UI extensions run in a browser environment and expand the functionality of SillyTavern by hooking into its events and API.

**:::callout**

**Server Plugins**

Server plugins allow adding functionality such as new API endpoints by running code in the NodeJS environment.

**:::callout**

**Internationalization (i18n)**

Learn how to translate SillyTavern's UI into your language.

# SECTION: SillyTavern_For_Contributors_Server-Plugins

# Server Plugins

These plugins allow for adding functionality that is impossible to achieve using UI extensions alone, such as creating new API endpoints or using Node.JS packages that are unavailable in a browser environment.

Plugins are contained in the `plugins` directory of SillyTavern and are loaded on server startup, but *only* if `enableServerPlugins` is set to `true` in the `config.yaml` file.

**Warning**

 **Server Plugins are not sandboxed. This means they can potentially gain access to your entire file system, or introduce a wide range of security vulnerabilities in a way that normal UI extensions cannot. Only install server plugins from developers you trust!**

**For a list of all official server plugins, see the GitHub organization list: <https://github.com/search?q=topic%3Aplugin+org%3ASillyTavern&type=Repositories>**

## Types of plugins

### Files

An executable JavaScript file with a ".js" (for CommonJS modules) or ".mjs" (for ES modules) extension containing a module that exports an `init` function. This function accepts an Express router (created specifically for your plugin) as an argument and returns a Promise.

The module should also export an `info` object containing information about the plugin (`id`, `name`, and `description` strings). This will provide information about the plugin to the loader.

You can register routes via the router that will be registered under the `/api/plugins/{id}/{route}` path. For example, `router.get('/foo')` for the `example` plugin will produce a route like this: `/api/plugins/example/foo`.

A plugin can also *optionally* export an `exit` function that performs clean-up when shutting down the server. It should have no arguments and must return a Promise.

TypeScript contract for plugin exports:

```ts
interface PluginInfo {
    id: string;
    name: string;
    description: string;
}

interface Plugin {
    init: (router: Router) => Promise<void>;
    exit: () => Promise<void>;
    info: PluginInfo;
}
```

See below for a "Hello world!" plugin example:

```js
/**
 * Initialize plugin.
 * @param {import('express').Router} router Express router
 * @returns {Promise<any>} Promise that resolves when plugin is initialized
 */
async function init(router) {
    // Do initialization here...
    router.get('/foo', req, res, function () {
       res.send('bar');
    });
    console.log('Example plugin loaded!');
    return Promise.resolve();
}

async function exit() {
    // Do some clean-up here...
    return Promise.resolve();
}

module.exports = {
    init,
    exit,
    info: {
        id: 'example',
        name: 'Example',
        description: 'My cool plugin!',
    },
};
```

### Directories

You can load a plugin from a subdirectory in the `plugins` directory in one of the following ways (in order of precedence):

1. A `package.json` file that contains a path to an executable file in the "main" field.
2. An `index.js` file for CommonJS modules.
3. An `index.mjs` file for ES modules.

A resulting file must export an `init` function and an `info` object with the same requirements as for individual files.

Example of a directory plugin (with an `index.js` file): <https://github.com/SillyTavern/SillyTavern-DiscordRichPresence-Server>

### Bundling

It is preferable to use a bundler (such as Webpack or Browserify) that will package all the requirements into one file. Make sure to set "Node" as a build target.

Template repository for plugins using Webpack and TypeScript: <https://github.com/SillyTavern/Plugin-WebpackTemplate>

# SECTION: SillyTavern_For_Contributors_st-script

# STscript Language Reference

## What is STscript?

It's a simple yet powerful scripting language that could be used to expand the functionality of SillyTavern without serious coding, allowing you to:

- Create mini-games or speed run challenges
- Build AI-powered chat insights
- Unleash your creativity and share with others

STscript is built using the slash commands engine, utilizing command batching, data piping, macros, and variables.
These concepts are going to be described in the following document.

### Security precaution

With great power comes great responsibility. Be careful and always inspect the scripts before executing them.

## Hello, World!

To run your first script, open any SillyTavern chat and type the following into the chat input bar:

```stscript
/pass Hello, World! | /echo
```

|-------------------------------------------------|

You should see the message in the toast on top of the screen. Now let's break it down bit by bit.

A script is a batch of commands, each one starting with the slash, with or without named and unnamed arguments, and terminated with the command separator character: `|`.

Commands are executed sequentially, one after another, and transfer data between each other.

1. The `/pass` command accepts a constant value of "Hello, World!" as an unnamed argument and writes it to the pipe.
2. The `/echo` command receives the value through the pipe from the previous command and displays it as a toast notification.

**Hint:** To see a list of all available commands, type `/help slash` into the chat.

**As constant unnamed arguments and pipes are interchangeable, we could rewrite this script simply as:**

```stscript
/echo Hello, World!
```

## User input

Now let's add a little bit of interactivity to the script. We will accept the input value from the user and display it in the notification.

```stscript
/input Enter your name |
/echo Hello, my name is {{pipe}}
```

1. The `/input` command is used to display an input box with the prompt specified in the unnamed argument and then writes the output to the pipe.
2. Because `/echo` already has an unnamed argument that sets the template for the output, we use the `{{pipe}}` macro to specify a place where the pipe value will be rendered.

|-----------------------------------------------------|-------------------------------------------------------|

### Other input/output commands

- `/popup (text)` — shows a blocking popup, supports lite HTML formatting, e.g: `/popup <font color=red>I'm red!</font>`.
- `/setinput (text)` — replaces the contents of the user input bar with the provided text.
- `/speak voice="name" (text)` — narrates the text using the selected TTS engine and the character name from the voice map, e.g. `/speak name="Donald Duck" Quack!`.
- `/buttons labels=["a","b"] (text)` — shows a blocking popup with the specified text and button labels. `labels` must be a JSON-serialized array of strings or a variable name containing such an array. Returns the clicked button label into the pipe or empty string if canceled. The text supports lite HTML formatting.
- `/beep` — plays the message notification sound.

#### Arguments for `/popup` and `/input`

`/popup` and `/input` support the following additional named arguments:
- `large=on/off` - increases the vertical size of the popup. Default: `off`.
- `wide=on/off` - increases the horizontal size of the popup. Default: `off`.
- `okButton=string` - adds ability to customize the text on the "Ok" button. Default: `Ok`.
- `rows=number` - (only for `/input`) increases the size of the input control. Default: 1.

Example:
```stscript
/popup large=on wide=on okButton="Accept" Please accept our terms and conditions....
```

#### Arguments for `/echo`

`/echo` supports the following values for the additional `severity` argument that sets the style of the displayed message.
  - `warning`
  - `error`
  - `info` (default)
  - `success`

Example:

```stscript
/echo severity=error Something really bad happened.
```

## Variables

Variables are used to store and manipulate data in scripts, using either commands or macros. The variables could be one of the following types:

- Local variables — saved to the metadata of the current chat, and unique to it.
- Global variables — saved to the settings.json and exist everywhere across the app.

1. `/getvar name` or `{{getvar::name}}` — gets the value of the local variable.
2. `/setvar key=name value` or `{{setvar::name::value}}` — sets the value of the local variable.
3. `/addvar key=name increment` or `{{addvar::name::increment}}` — adds the `increment` to the value of the local variable.
4. `/incvar name` or `{{incvar::name}}` — increments a value of the local variable by 1.
5. `/decvar name` or `{{decvar::name}}` — decrements a value of the local variable by 1.
6. `/getglobalvar name` or `{{getglobalvar::name}}` — gets the value of the global variable.
7. `/setglobalvar key=name` or `{{setglobalvar::name::value}}` — sets the value of the global variable.
8. `/addglobalvar key=name` or `{{addglobalvar::name:increment}}` — adds the `increment` to the value of the global variable.
9. `/incglobalvar name` or `{{incglobalvar::name}}` — increments a value of the global variable by 1.
10. `/decglobalvar name` or `{{decglobalvar::name}}` — decrements a value of the global variable by 1.
11. `/flushvar name` — deletes the value of the local variable.
12. `/flushglobalvar name` — deletes the value of the global variable.

- The default value of previously undefined variables is an empty string or a zero of it is first used in the `/addvar`, `/incvar`, `/decvar` command.
- Increment in the `/addvar` command performs an addition or subtraction of the value if both increment and the variable value can be converted to a number, or otherwise does the string concatenation.
- If a command argument accepts a variable name and both local and global variables exist with the same name, then the *local variable* takes priority.
- All *slash commands* for variable manipulation write the resulting value into the pipe for the next command to use.
- For *macros*, only the "get", "inc", and "dec" type macro returns the value, "add" and "set" are replaced with an empty string instead.

Now, let's consider the following example:

```stscript
/input What do you want to generate? |
/setvar key=SDinput |
/echo Requesting an image of {{getvar::SDinput}} |
/getvar SDinput |
/imagine
```

1. The value of the user input is saved in the local variable named `SDinput`.
2. The `getvar` macro is used to display the value in the `/echo` command.
3. The `getvar` command is used to retrieve the value of the variable and pass it through the pipe.
4. The value is passed to the `/imagine` command (provided by the Image Generation plugin) to be used as its input prompt.

Since the variables are saved and not flushed between the script executions, you can reference the variable in other scripts and via macros, and it will resolve to the same value as during the execution of the example script. To guarantee that the value will be discarded, add the `/flushvar` command to the script.

### Arrays and objects

Variable values can contain JSON-serialized arrays or key-value pairs (objects).

Examples:
- Array: `["apple","banana","orange"]`
- Object: `{"fruits":["apple","banana","orange"]}`

The following modifications can be applied to commands to work with these variables:

- `/len` command gets a number of items in the array.
- `index=number/string` named argument can be added `/getvar` or `/setvar` and their global counterparts to get or set sub-values by either a zero-based index for arrays or a string key for objects.
  - If a numeric index is used on a nonexistent variable, the variable will be created as an empty array `[]`.
  - If a string index is used on a nonexistent variable, the variable will be created as an empty object `{}`.
- `/addvar` and `/addglobalvar` commands support pushing a new value to array-typed variables.

## Flow control - conditionals

You can use the `/if` command to create conditional expressions that branch the execution based on the defined rules.

```stscript
/if left=valueA right=valueB rule=comparison else={: /echo (command on false) :} {: /echo (command on true) :}
```

Note that

```stscript
/if left=valueA right=valueB rule=comparison else="(command on false)" "(command on true)"
```

syntax is also supported, however `{: closures :}` will help you write cleaner scripts.

Let's review the following example:

```stscript
/input What's your favorite drink? |
/if left={{pipe}} right="black tea" rule=eq else={: /echo You shall not pass | /abort :} {: /echo Welcome to the club, {{user}} :}
```

This script evaluates the user input against a required value and displays different messages, depending on the input value.

### Arguments for `/if`

1. `left` is the first operand. Let's call it A.
2. `right` is the second operand. Let's call it B.
3. `rule` is the operation to be applied to the operands.
4. `else` is the optional string of subcommands to be executed if the result of boolean comparison is false.
5. Unnamed argument is the subcommand to be executed if the result of boolean comparison is true.

The operand values are evaluated in the following order:

1. Numeric literals
2. Local variable names
3. Global variable names
4. String literals

String values of named arguments could be escaped with quotes to allow multi-word strings. Quotes are then discarded.

### Boolean operations

Supported rules for boolean comparison are the following. An operation applied to the operands results in either a true or false value.

1. `eq` (equals) => A = B
2. `neq` (not equals) => A != B
3. `lt` (less than) => A < B
4. `gt` (greater than) => A > B
5. `lte` (less than or equals) => A <= B
6. `gte` (greater than or equals) => A >= B
7. `not` (unary negation) => !A
8. `in` (includes substring) => A includes B, case insensitive
9. `nin` (not includes substring) => A not includes B, case insensitive

### Subcommands

A subcommand is a string containing a list of slash commands to execute.

1. To use command batching in subcommands, the command separator character should be escaped (see below).
2. Since macro values are executed when the conditional is entered, not when the subcommand is executed, a macro could be additionally escaped to delay their evaluation to the subcommand execution time.
3. The result of the subcommands execution is piped to the command after `/if`.
4. The `/abort` command interrupts the script execution when encountered.

`/if` commands can be used as a ternary operator.
The following example will pass a "true" string to the next command the variable `a` equals 5, and a "false" string otherwise.

```stscript
/if left=a right=5 rule=eq else={: /pass false:} {: /pass true :} |
/echo
```

## Escape Sequences

### Macros

Escaping of macros works just like before. However, with closures, you will need to escape macros a lot less often than before. Either escape the two opening curly braces, or both the opening and closing pair.

```stscript
/echo \{\{char}} |
/echo \{\{char\}\}
```

### Pipes

Pipes don't need to be escaped in closures (when used as command separators). Everywhere where you want to use a literal pipe character instead of a command separator, you need to escape it.

```stscript
/echo title="a\|b" c\|d |
/echo title=a\|b c\|d |
```

With the parser flag `STRICT_ESCAPING` you don't need to escape pipes in quoted values.

```stscript
/parser-flag STRICT_ESCAPING |
/echo title="a|b" c\|d |
/echo title=a\|b c\|d |
```

### Quotes

To use a literal quote-character inside a quoted value, the character must be escaped.

```stscript
/echo title="a \"b\" c" d "e" f
```

### Spaces

To use space in the value of a named argument, you either have to surround the value in quote, or escape the space character.

```stscript
/echo title="a b" c d |
/echo title=a\ b c d
```

### Closure Delimiters

If you want to use the character combinations used to mark the beginning or end of a closure, you have to escape the sequence with a single backslash.

```stscript
/echo \{: |
/echo \:}
```

## Pipe Breakers

```stscript
||
```

To prevent the previous command's output from being automatically injected as the unnamed argument into the next command, put double pipes between the two commands.

```stscript
/echo we don't want to pass this on ||
/world
```

## Closures

```stscript
{: ... :}
```

Closures (block statements, lambdas, anonymous functions, whatever you want to call them) are a series of commands wrapped between `{:` and `:}`, that are only evaluated once that part of the code is executed.

### Sub-Commands

Closures make using sub-commands a lot easier and get rid of the need to escape pipes and macros.

```stscript
// if without closures |
/if left=1 rule=eq right=1
    else="
        /echo not equal \|
        /return 0
    "
    /echo equal \|
    /return \{\{pipe}}
```

```stscript
// if with closures |
/if left=1 rule=eq right=1
    else={:
        /echo not equal |
        /return 0
    :}
    {:
        /echo equal |
        /return {{pipe}}
    :}
```

### Scopes

Closures have their own scope and support scoped variables. Scoped variables are declared with `/let`, their values set and retrieved with `/var`. Another way to get a scoped variable is the `{{var::}}` macro.

```stscript
/let x |
/let y 2 |
/var x 1 |
/var y |
/echo x is {{var::x}} and y is {{pipe}}.
```

Within a closure, you have access to all variables declared within that same closure or in one of its ancestors. You don't have access to variables declared in a closure's descendants.  
If a variable is declared with the same name as a variable that was declared in one of the closure's ancestors, you don't have access to the ancestor variable in this closure and its descendants.

```stscript
/let x this is root x |
/let y this is root y |
/return {:
    /echo called from level-1: x is "{{var::x}}" and y is "{{var::y}}" |
    /delay 500 |
    /let x this is level-1 x |
    /echo called from level-1: x is "{{var::x}}" and y is "{{var::y}}" |
    /delay 500 |
    /return {:
        /echo called from level-2: x is "{{var::x}}" and y is "{{var::y}}" |
        /let x this is level-2 x |
        /echo called from level-2: x is "{{var::x}}" and y is "{{var::y}}" |
        /delay 500
    :}()
:}() |
/echo called from root: x is "{{var::x}}" and y is "{{var::y}}"
```

### Named Closures

```stscript
/let x {: ... :} | /:x
```

Closures can be assigned to variables (only scoped variables) to be called at a later point or to be used as sub-commands.

```stscript
/let myClosure {:
    /echo this is my closure
:} |
/:myClosure
```

```stscript
/let myClosure {:
    /echo this is my closure |
    /delay 500
:} |
/times 3 {{var::myClosure}}
```

`/:` can also be used to execute Quick Replies, as it is just a shorthand for `/run`.

```stscript
/:QrSetName.QrButtonLabel |
/run QrSetName.QrButtonLabel
```

### Closure Arguments

Named closures can take named arguments, just like slash commands. The arguments can have default values.

```stscript
/let myClosure {: a=1 b=
    /echo a is {{var::a}} and b is {{var::b}}
:} |
/:myClosure b=10
```

### Closures and Piped Arguments

The piped value from a parent closure will not be automatically injected into the first command of a child closure.  
You can still explicitly reference the parent's piped value with `{{pipe}}`, but if you leave the unnamed argument of the first command inside a closure blank, the value will *not* be automatically injected.

```stscript
/* This used to attempt to change the model to "foo"
   because the value "foo" from the /echo outside of
   the loop was injected into the /model command
   inside of the loop.
   Now it will simply echo the current model without 
   attempting to change it.
*|
/echo foo |
/times 2 {:
	/model |
	/echo |
:} |
```
```stscript
/* You can still recreate the old behavior by
   explicitly using the {{pipe}} macro.
*|
/echo foo |
/times 2 {:
	/model {{pipe}} |
	/echo |
:} |
```

### Immediately Executed Closures

```stscript
{: ... :}()
```

Closures can be immediately executed, meaning they will be replaced with their return value. This is helpful in places where no explicit support for closures exists, and to shorten some commands that would otherwise require a lot of intermediate variables.

```stscript
// a simple length comparison of two strings without closures |
/len foo |
/var lenOfFoo {{pipe}} |
/len bar |
/var lenOfBar {{pipe}} |
/if left={{var::lenOfFoo}} rule=eq right={{var:lenOfBar}} /echo yay!
```

```stscript
// the same comparison with immediately executed closures |
/if left={:/len foo:}() rule=eq right={:/len bar:}() /echo yay!
```

In addition to running named closures saved inside scoped variables, the `/run` command can also be used to execute closures immediately.

```stscript
/run {:
	/add 1 2 3 4 |
:} |
/echo |
```

## Comments

```stscript
// ... | /# ...
```

A comment is a human-readable explanation or annotation in the script code. Comments don't break pipes.

```stscript
// this is a comment |
/echo foo |
/# this is also a comment
```

### Block Comments

Block comments can be used to quickly comment out multiple commands at once. They will not terminate on a pipe.

```stscript
/echo foo |
/*
/echo bar |
/echo foobar |
*|
/echo foo again |
```

## Flow Control

### Loops: `/while` and `/times`

If you need to run some command in a loop until a certain condition is met, use the `/while` command.

```stscript
/while left=valueA right=valueB rule=operation guard=on "commands"
```

On each step of the loop it compares the value of variable A with the value of variable B, and if the condition yields true, then executes any valid slash command enclosed in quotes, otherwise exists the loop. This command doesn't write anything to the output pipe.

#### Arguments for `/while`

**The set of available boolean comparisons, handing of variables, literal values, and subcommands is the same as for the `/if` command.**

The optional `guard` named argument (`on` by default) is used to protect against endless loops, limiting the number of iterations to 100.
To disable and allow endless loops, set `guard=off`.

This example adds 1 to the value of `i` until it reaches 10, then outputs the resulting value (10 in this case).

```stscript
/setvar key=i 0 |
/while left=i right=10 rule=lt "/addvar key=i 1" |
/echo {{getvar::i}} |
/flushvar i
```

#### Arguments for `/times`

Runs a subcommand a specified number of times.

`/times (repeats) "(command)"` – any valid slash command enclosed in quotes repeats a number of times, e.g. `/setvar key=i 1 | /times 5 "/addvar key=i 1"` adds 1 to the value of "i" 5 times.
- {{timesIndex}} is replaced with the iteration number (zero-based), e.g. `/times 4 {:/echo {{timesIndex}}:}` echoes the numbers 0 through 4.
- Loops are limited to 100 iterations by default, pass `guard=off` to disable.

### Breaking out of Loops and Closures

```stscript
/break |
```

The `/break` command can be used to break out of a loop (`/while` or `/times`) or a closure early. The unnamed argument of `/break` can be used to pass a value different from the current pipe along.  
`/break` is currently implemented in the following commands:
- `/while` - exits the loop early
- `/times` - exits the loop early
- `/run` (with a closure or closure via variable) - exits the closure early
- `/:` (with a closure) - exits the closure early

```stscript
/times 10 {:
	/echo {{timesIndex}}
	/delay 500 |
	/if left={{timesIndex}} rule=gt right=3 {:
		/break
	:} |
:} |
```

```stscript
/let x {: iterations=2
	/if left={{var::iterations}} rule=gt right=10 {:
		/break too many iterations! |
	:} |
	/times {{var::iterations}} {:
		/delay 500 |
		/echo {{timesIndex}} |
	:} |
:} |
/:x iterations=30 |
/echo the final result is: {{pipe}}
```

```stscript
/run {:
	/break 1 |
	/pass 2 |
:} |
/echo pipe will be one: {{pipe}} |
```

```stscript
/let x {:
	/break 1 |
	/pass 2 |
:} |
/:x |
/echo pipe will be one: {{pipe}} |
```

## Math operations

- All of the following operations accept a series of numbers or variable names and output the result to the pipe.
- Invalid operations (such as division by zero), and operations that result in a NaN value or infinity return zero.
- Multiplication, addition, minimum and maximum accept an unlimited number of arguments separated by spaces.
- Subtraction, division, exponentiation, and modulo accept two arguments separated by spaces.
- Sine, cosine, natural logarithm, square root, absolute value, and rounding accept one argument.

**List of operations:**

1. `/add (a b c d)` – performs an addition of the set of values, e.g. `/add 10 i 30 j`
2. `/mul (a b c d)` – performs a multiplication of the set of values, e.g. `/mul 10 i 30 j`
3. `/max (a b c d)` – returns a maximum from the set of values, e.g. `/max 1 0 4 k`
4. `/min (a b c d)` – return a minimum from the set of values, e.g. `/min 5 4 i 2`
5. `/sub (a b)` – performs a subtraction of two values, e.g. `/sub i 5`
6. `/div (a b)` – performs a division of two values, e.g. `/div 10 i`
7. `/mod (a b)` – performs a modulo operation of two values, e.g. `/mod i 2`
8. `/pow (a b)` – performs a power operation of two values, e.g. `/pow i 2`
9. `/sin (a)` – performs a sine operation of a value, e.g. `/sin i`
10. `/cos (a)` – performs a cosine operation of a value, e.g. `/cos i`
11. `/log (a)` – performs a natural logarithm operation of a value, e.g. `/log i`
12. `/abs (a)` – performs an absolute value operation of a value, e.g. `/abs -10`
13. `/sqrt (a)` – performs a square root operation of a value, e.g. `/sqrt 9`
14. `/round (a)` – performs a rounding to the nearest integer operation of a value, e.g. `/round 3.14`
15. `/rand (round=round|ceil|floor from=number=0 to=number=1)` – returns a random number between from and to, e.g. `/rand` or `/rand 10` or `/rand from=5 to=10`. Ranges are inclusive. The returned value will contain a fractional part. Use `round` named argument to get an integral value, e.g. `/rand round=ceil` to round up, `round=floor` to round down, and `round=round` to round to nearest.

### Example 1: get an area of a circle with a radius of 50.

```stscript
/setglobalvar key=PI 3.1415 |
/setvar key=r 50 |
/mul r r PI |
/round |
/echo Circle area: {{pipe}}
```

### Example 2: calculate a factorial of 5.

```stscript
/setvar key=input 5 |
/setvar key=i 1 |
/setvar key=product 1 |
/while left=i right=input rule=lte "/mul product i \| /setvar key=product \| /addvar key=i 1" |
/getvar product |
/echo Factorial of {{getvar::input}}: {{pipe}} |
/flushvar input |
/flushvar i |
/flushvar product
```

## Using the LLM

Scripts can make requests to your currently connected LLM API using the following commands:

- `/gen (prompt)` — generates text using the provided prompt for the selected character and including chat messages.
- `/genraw (prompt)` — generates text using just the provided prompt, ignoring the current character and chat.
- `/trigger` — triggers a normal generation (equivalent to clicking a "Send" button). If in group chat, you can optionally provide a 1-based group member index or a character name to have them reply, otherwise triggers a group round according to the group settings.

### Arguments for `/gen` and `/genraw`

```stscript
/genraw lock=on/off stop=[] instruct=on/off (prompt)
```

- `lock` — can be `on` or `off`. Specifies whether a user input should be blocked while the generation is in progress. Default: `off`.
- `stop` — JSON-serialized array of strings. Adds a custom stop string (if the API supports it) just for this generation. Default: none.
- `instruct` (only `/genraw`) — can be `on` or `off`. Allows to use instruct formatting on the input prompt (if instruct mode is enabled and the API supports it). Set to `off` to force pure prompts. Default: `on`.
- `as` (for Text Completion APIs) — can be `system` (default) or `char`. Defines how the last prompt line will be formatted. `char` will use a character name, `system` will use no or neutral name.

The generated text is then passed through the pipe to the next command and can be saved to a variable or displayed using the I/O capabilities:

```stscript
/genraw Write a funny message from Cthulhu about taking over the world. Use emojis. |
/popup <h3>Cthulhu says:</h3><div>{{pipe}}</div>
```

|---------------------------------------------------|

or to insert the generated message as a response from your character:

```stscript
/genraw You have been memory wiped, your name is now Lisa and you're tearing me apart. You're tearing me apart Lisa! |
/sendas name={{char}} {{pipe}}
```

## Temporal character

If you are not in a group chat, scripts may temporarily make a request to the currently connected LLM as a different character.

- `/ask (prompt)` — generates text using the provided prompt for a specified character and including chat messages. Please note that swipes of the response from this character will revert back to the current character.

```stscript
/ask name=... (prompt)
```
### Arguments for `/ask`

- `name` — **Required**. The name of the character to ask (or a unique character identifier, such as an avatar key). This must be provided as a named argument.
- `return` — Specifies how the return value should be provided. Defaults to `pipe` (output via the command pipe). Other options can be specified if supported by the API.

```stscript
/ask name=Alice What is your favorite color?
```

## Prompt injections

Scripts can add custom LLM prompt injections, making it essentially an equivalent of unlimited Author's Notes.

- `/inject (text)` — inserts any text into the normal LLM prompt for the current chat, and requires a unique identifier. Saved to chat metadata.
- `/listinjects` — shows a list of all prompt injections added by scripts for the current chat in a system message.
- `/flushinjects` — deletes all prompt injections added by scripts for the current chat.
- `/note (text)` — sets the Author's Note value for the current chat. Saved to chat metadata.
- `/interval` — sets the Author's Note insertion interval for the current chat.
- `/depth` — sets the Author's Note insertion depth for the in-chat position.
- `/position`  — sets the Author's Note position for the current chat.

### Arguments for `/inject`

```stscript
/inject id=IdGoesHere position=chat depth=4 My prompt injection
```

- `id` — an identifier string or a reference to a variable. Consequent calls of `/inject` with the same ID will overwrite the previous text injection. **Required argument.**
- `position` — sets a position for the injection. Default: `after`. Possible values:
  - `after`: after the main prompt.
  - `before`: before main prompt.
  - `chat`: in-chat.
- `depth` — sets an injection depth for the in-chat position. 0 means insertion after the last message, 1 - before the last message, etc. Default: 4.
- Unnamed argument is a text to be injected. An empty string will unset the previous value for the provided identifier.

## Access chat messages

### Read messages

You can access messages in the currently selected chat using the `/messages` command.

```stscript
/messages names=on/off start-finish
```

- The `names` argument is used to specify whether you want to include character names or not, default: `on`.
- In an unnamed argument, it accepts a message index or range in the `start-finish` format. Ranges are inclusive!
- If the range is unsatisfiable, i.e. an invalid index or more messages than exist are requested, then an empty string is returned.
- Messages that are hidden from the prompt (denoted by the ghost icon) are excluded from the output.
- If you want to know the index of the latest message, use the `{{lastMessageId}}` macro, and `{{lastMessage}}` will get you the message itself.

To calculate the start index for a range, for example, when you need to get the last N messages, use variable subtraction.
This example will get you 3 last messages in the chat:

```stscript
/setvar key=start {{lastMessageId}} |
/addvar key=start -2 |
/messages names=off {{getvar::start}}-{{lastMessageId}} |
/setinput
```

### Send messages

A script can send messages as either a user, character, persona, neutral narrator, or add comments.

1. `/send (text)` — adds a message as the currently selected persona.
2. `/sendas name=charname (text)` — adds a message as any character, matching by their name. `name` argument is required. Use the `{{char}}` macro to send as the current character.
3. `/sys (text)` — adds a message from the neutral narrator that doesn't belong to the user or character. The displayed name is purely cosmetic and can be customized with the `/sysname` command.
4. `/comment (text)` — adds a hidden comment that is displayed in the chat but is not visible to the prompt.
5. `/addswipe (text)` — adds a swipe to the last character message. Can't add a swipe to the user or hidden messages.
6. `/hide (message id or range)` — hides one or several messages from the prompt based on the provided message index or inclusive range in the `start-finish` format.
7. `/unhide (message id or range)` — returns one or several messages to the prompt based on the provided message index or inclusive range in the `start-finish` format.

`/send`, `/sendas`, `/sys`, and `/comment` commands optionally accept a named argument `at` with a zero-based numeric value (or a variable name that contains such a value) that specifies an exact position of message insertion. By default new messages are inserted at the end of the chat log.

This will insert a user message at the beginning of the conversation history:

```stscript
/send at=0 Hi, I use Linux.
```

### Delete messages

**These commands are potentially destructive and have no "undo" function. Check the /backups/ folder if you accidentally deleted something important.**

1. `/cut (message id or range)` — cuts one or several messages from the chat based on the provided message index or inclusive range in the `start-finish` format.
2. `/del (number)` — deletes last N messages from the chat.
3. `/delswipe (1-based swipe id)` — deletes a swipe from the last character message based on the provided 1-based swipe ID.
4. `/delname (character name)` — deletes all messages in the current chat that belong to a character with the specified name.
5. `/delchat` — deletes the current chat.

## World Info commands

World Info (also known as Lorebook) is a highly utilitarian tool for dynamically inserting data into the prompt. See the dedicated page for more detailed explanation: World Info.

1. `/getchatbook` – gets a name of the chat-bound World Info file or create a new one if it was unbound, and pass it down the pipe.
2. `/findentry file=bookName field=fieldName [text]` – finds a UID of the record from the specified file (or a variable pointing to a file name) using fuzzy matching of a field value with the provided text (default field: `key`) and passes the UID down the pipe, e.g. `/findentry file=chatLore field=key Shadowfang`.
3. `/getentryfield file=bookName field=field [UID]` – gets a field value (default field: `content`) of the record with the UID from the specified World Info file (or a variable pointing to a file name) and passes the value down the pipe, e.g. `/getentryfield file=chatLore field=content 123`.
4. `/setentryfield file=bookName uid=UID field=field [text]` – sets a field value (default field: `content`) of the record with the UID (or a variable pointing to UID) from the specified World Info file (or a variable pointing to a file name). To set multiple values for key fields, use a comma-delimited list as a text value, e.g. `/setentryfield file=chatLore uid=123 field=key Shadowfang,sword,weapon`.
5. `/createentry file=bookName key=keyValue [content text]` – creates a new record in the specified file  (or a variable pointing to a file name) with the key and content (both of these arguments are *optional*) and passes the UID down the pipe, e.g. `/createentry file=chatLore key=Shadowfang The sword of the king`.

### Valid entry fields

| Field              | UI element        | Value type      |
|:-------------------|:------------------|:----------------|
| `content`          | Content           | String          |
| `comment`          | Title / Memo      | String          |
| `key`              | Primary Keywords  | List of strings |
| `keysecondary`     | Optional Filter   | List of strings |
| `constant`         | Constant Status   | Boolean (1/0)   |
| `disable`          | Disabled Status   | Boolean (1/0)   |
| `order`            | Order             | Number          |
| `selectiveLogic`   | Logic             | (see below)     |
| `excludeRecursion` | Non-recursable    | Boolean (1/0)   |
| `probability`      | Trigger%          | Number (0-100)  |
| `depth`            | Depth             | Number (0-999)  |
| `position`         | Position          | (see below)     |
| `role`             | Depth Role        | (see below)     |
| `scanDepth`        | Scan Depth        | Number (0-100)  |
| `caseSensitive`    | Case-Sensitive    | Boolean (1/0)   |
| `matchWholeWords`  | Match Whole Words | Boolean (1/0)   |
| `vectorized`       | Vectorized Status | Boolean (1/0)   |
| `automationId`     | Automation ID     | String          |
| `group`            | Inclusion Group   | String          |
| `groupOverride`    | Inclusion Group Prioritize | Boolean (1/0) |
| `groupWeight`      | Inclusion Group Weight | Number (0-100) |
| `useGroupScoring`  | Group Scoring     | Boolean (1/0)   |
| `characterFilterExclude` | Character Filter Exclude Mode | List of strings |
| `characterFilterNames` | Character Filter Names | List of strings |
| `characterFilterTags` | Character Filter Tags | List of strings |
| `matchCharacterDepthPrompt` | Match Character Depth Prompt | Boolean (1/0) |
| `matchCharacterDescription` | Match Character Description | Boolean (1/0) |
| `matchCharacterPersonality` | Match Character Personality | Boolean (1/0) |
| `matchCreatorNotes` | Match Creator Notes | Boolean (1/0) |
| `matchPersonaDescription` | Match Persona Description | Boolean (1/0) |
| `matchScenario` | Match Scenario | Boolean (1/0) |

**Logic values**

- 0 = AND ANY
- 1 = NOT ALL
- 2 = NOT ANY
- 3 = AND ALL

**Position values**

- 0 = before main prompt
- 1 = after main prompt
- 2 = top of Author's Note
- 3 = bottom of Author's Note
- 4 = in-chat at depth
- 5 = top of example messages
- 6 = bottom of example messages

**Role values** (Position = 4 only)
- 0 = System
- 1 = User
- 2 = Assistant

### Example 1: Read a content from the chat lorebook by key

```stscript
/getchatbook | /setvar key=chatLore |
/findentry file={{getvar::chatLore}} field=key Shadowfang |
/getentryfield file={{getvar::chatLore}} field=key |
/echo
```

### Example 2: Create a chat lorebook entry with key and content

```stscript
/getchatbook | /setvar key=chatLore |
/createentry file={{getvar::chatLore}} key="Milla" Milla Basset is a friend of Lilac and Carol. She is a hush basset puppy who possesses the power of alchemy. |
/echo
```

### Example 3: Expand an existing lorebook entry with new information from the chat

```stscript
/getchatbook | /setvar key=chatLore |
/findentry file={{getvar::chatLore}} field=key Milla |
/setvar key=millaUid |
/getentryfield file={{getvar::chatLore}} field=content |
/setvar key=millaContent |
/gen lock=on Tell me more about Milla Basset based on the provided conversation history. Incorporate existing information into your reply: {{getvar::millaContent}} |
/setvar key=millaContent |
/echo New content: {{pipe}} |
/setentryfield file={{getvar::chatLore}} uid=millaUid field=content {{getvar::millaContent}}
```

## Text manipulation

There's a variety of useful text manipulation utility commands to be used in various script scenarios.

1. `/trimtokens` — trims the input to the specified number of text tokens from the start or from the end and outputs the result to the pipe.
2. `/trimstart` — trims the input to the start of the first complete sentence and outputs the result to the pipe.
3. `/trimend` — trims the input to the end of the last complete sentence and outputs the result to the pipe.
4. `/fuzzy` — performs fuzzy matching of the input text to the list of strings, outputting the best string match to the pipe.
5. `/regex name=scriptName [text]` — executes a regex script from the Regex extension for the specified text. The script must be enabled.

### Arguments for `/trimtokens`

```stscript
/trimtokens limit=number direction=start/end (input)
```

1. `direction` sets the direction for trimming, which can be either `start` or `end`. Default: `end`.
2. `limit` sets the amount of tokens to leave in the output. Can also specify a variable name containing the number. **Required argument.**
3. Unnamed argument is the input text to be trimmed.

### Arguments for `/fuzzy`

```stscript
/fuzzy list=["candidate1","candidate2"] (input)
```

1. `list` is a JSON-serialized array of strings containing the candidates. Can also specify a variable name containing the list. **Required argument.**
2. Unnamed argument is the input text to be matched. Output is one of the candidates matching the input most closely.

## Autocomplete

- Autocomplete is enabled both on the chat input, and the large Quick Reply editor.
- Autocomplete works anywhere in your input. Even with multiple piped commands and nested closures.
- Autocomplete supports three ways of looking up matching commands (*User Settings* -> *STscript Matching*).

1. **Starts with** The "old" way. Only commands that begin exactly with the typed value will show up.
2. **Includes**  All commands that *include* the type value will show up. Example: When entering `/delete`, the commands `/qr-delete` and `/qr-set-delete` will show up in the autocomplete list (/qr-**delete**, /qr-set-**delete**).
3. **Fuzzy**  All commands that can be fuzzy-matched against the typed value will show up. Example: When entering `/seas`, the command `/sendas` will show up in the autocomplete list (/**se**nd**as**).

- Command arguments are supported by autocomplete as well. The list will show up for required arguments automatically. For optional arguments, press *Ctrl*+*Space* to open the list of available options.
- When entering `/:` to execute a closure or QR, autocomplete will show a list of scoped variables and QRs.
- Autocomplete has limited support for macros (in slash commands). Type `{{` to get a list of available macros.
- Use the *up* and *down* *arrow keys* to select an option from the list of autocomplete options.
- Press *Enter* or *Tab* or *click* on an option to place the option at the cursor.
- Press *Escape* to close the autocomplete list.
- Press *Ctrl*+*Space* to open the autocomplete list or toggle the selected option's details.

## Parser Flags

```stscript
/parser-flag
```

The parser accepts flags to modify its behavior. These flags can be toggled on and off at any point in a script and all following input will be evaluated accordingly.  
You can set your default flags in user settings.

### Strict Escaping

```stscript
/parser-flag STRICT_ESCAPING on |
```

Changes with `STRICT_ESCAPING` enabled are as follows.

#### Pipes

Pipes don't need to be escaped in quoted values.

```stscript
/echo title="a|b" c\|d
```

#### Backslashes

A backslash in front of a symbol can be escaped to provide the literal backslash followed by the functional symbol.

```stscript
// this will echo "foo \", then echo "bar" |
/echo foo \\|
/echo bar
```

```stscript
/echo \\|
/echo \\\|
```

### Replace Variable Macros

```stscript
/parser-flag REPLACE_GETVAR on |
```

This flag helps to avoid double-substitutions when the variable values contain text that could be interpreted as macros. The `{{var::}}` macros get substituted last and no further substitutions happen on the resulting text / variable value.

Replaces all `{{getvar::}}` and `{{getglobalvar::}}` macros with `{{var::}}`.
Behind the scenes, the parser will insert a series of command executors before the command with the replaced macros:

- call `/let` to save the current `{{pipe}}` to a scoped variable
- call `/getvar` or `/getglobalvar` to get the variable used in the macro
- call `/let` to save the retrieved variable to a scoped variable
- call `/return` with the saved `{{pipe}}` value to restore the correct piped value for the next command

```stscript
// the following will echo the last message's id / number |
/setvar key=x \{\{lastMessageId}} |
/echo {{getvar::x}}
```

```stscript
// this will echo the literal text {{lastMessageId}} |
/parser-flag REPLACE_GETVAR |
/setvar key=x \{\{lastMessageId}} |
/echo {{getvar::x}}
```

## Quick Replies: script library and auto-execution

Quick Replies is a built-in SillyTavern extension that provides an easy way to store and execute your scripts.

### Configuring Quick Replies

In order to get started, enable open the extensions panel (stacked blocks icon), and expand the Quick Replies menu.

<div style="display:flex;justify-content:center">

</div>

**Quick Replies are disabled by default, you need to enable them first.** Then you will see a bar appearing above your chat input bar.

You can set the displayed button text label (we recommend using emojis for brevity) and the script that will be executed when you click the button.

The number of buttons is controlled by the **Number of slots** settings (max = 100), adjust it according to your needs and click "Apply" when done.

**Inject user input automatically** recommended to be disabled when using STscript, otherwise it may interfere with your inputs, use the `{{input}}` macro to get the current value of the input bar in scripts instead.

**Quick Reply presets** allow to have multiple sets of predefined Quick Replies and switch between manually or by using the `/qrset (name of set)` command.
Don't forget to click "Update" before switching to a different set to write your changes to the currently used preset!

### Manual execution

Now you can add your first script to the library. Pick any free slot (or create one), type "Click me" into the left box to set the label, then paste this into the right box:

```stscript
/addvar key=clicks 1 |
/if left=clicks right=5 rule=eq else="/echo Keep going..." "/echo You did it!  \| /flushvar clicks"
```

Then click 5 times on the button that appeared above the chat bar.
Every click increments the variable `clicks` by one and displays a different message when the value equals 5 and resets the variable.

### Automatic execution

Open the modal menu by clicking the `⋮` button for the created command.

|---------------------------------------------------------|

In this menu you can do the following:

- Edit the script in a convenient full-screen editor
- Hide the button from the chat bar, making it accessible only for auto-execution.
- Enable automatic execution on one or more of the following conditions:
  * App startup
  * Sending a user message to the chat
  * Receiving an AI message in the chat
  * Opening a character or group chat
  * Triggering a reply from a group member
  * Activating a World Info entry using the same Automation ID
- Provide a custom tool tip for the quick reply (text displayed when hovering over the quick reply in your UI)
- Execute the script for test purposes

Commands are executed automatically only if the Quick Replies extension is enabled.

For example, you can display a message after sending five user messages by adding the following script and setting it to auto-execute on the user message.

```stscript
/addvar key=usercounter 1 |
/echo You've sent {{pipe}} messages. |
/if left=usercounter right=5 rule=gte "/echo Game over! \| /flushvar usercounter"
```

### Debugger

A basic debugger exists inside the expanded Quick Reply editor. Set breakpoints with `/breakpoint |` anywhere in your script. When executing the script from the QR editor, the execution will be interrupted at that point, allowing you to examine the currently available variables, pipe, command arguments, and more, and to step through the rest of the code one by one.

```stscript
/let x {: n=1
	/echo n is {{var::n}} |
	/mul n n |
:} |
/breakpoint |
/:x n=3 |
/echo result is {{pipe}} |
```

|--------------------------------------------------------|

### Calling procedures

A `/run` command can call scripts defined in the Quick Replies by their label, basically providing the ability to define procedures and return results from them. This allows to have reusable script blocks that other scripts could reference. The last result from the procedure's pipe is passed to the next command after it.

```stscript
/run ScriptLabel
```

Let's create two Quick Replies:

***
**Label:**

`GetRandom`

**Command:**

```stscript
/pass {{roll:d100}}
```
***
**Label:**

`GetMessage`

**Command:**
```stscript
/run GetRandom | /echo Your lucky number is: {{pipe}}
```
***

Clicking on the `GetMessage` button will call the `GetRandom` procedure which will resolve the `{{roll}}` macro and pass the number to the caller, displaying it to the user.

- Procedures do not accept named or unnamed arguments, but can reference the same variables as the caller.
- Avoid recursion when calling procedures as it may produce the "call stack exceeded" error if handled unadvisedly.

#### Calling procedures from a different Quick Reply preset

You can call a procedure from a different quick reply preset using the `a.b` syntax, where a = QR preset name and b = QR label name

```stscript
/run QRpreset1.QRlabel1
```

By default, the system will first look for a quick reply label `a.b`, so if one of your labels is literally "QRpreset1.QRlabel1" it will try to run that. If no such label is found, it will search for a QR preset name "QRpreset1" with a QR labeled "QRlabel1".

### Quick Replies management commands

#### Create Quick Reply

* `/qr-create (arguments, [message])` – creates a new Quick Reply, example: `/qr-create set=MyPreset label=MyButton /echo 123`

Arguments:
- `label`    - string - text on the button, e.g., `label=MyButton`
- `set`      - string - name of the QR set, e.g., `set=PresetName1`
- `hidden`   - bool   - whether the button should be hidden, e.g., `hidden=true`
- `startup`  - bool   - auto execute on app startup, e.g., `startup=true`
- `user`     - bool   - auto execute on user message, e.g., `user=true`
- `bot`      - bool   - auto execute on AI message, e.g., `bot=true`
- `load`     - bool   - auto execute on chat load, e.g., `load=true`
- `title`    - bool   - title / tooltip to be shown on button, e.g., `title="My Fancy Button"`

#### Delete Quick Reply

* `/qr-delete (set=string [label])` – deletes Quick Reply

#### Update Quick Reply

* `/qr-update (arguments, [message])` – updates Quick Reply, example: `/qr-update set=MyPreset label=MyButton newlabel=MyRenamedButton /echo 123`

Arguments:
- `newlabel` - string - new text for the button, e.g. `newlabel=MyRenamedButton`
- `label`    - string - text on the button, e.g., `label=MyButton`
- `set`      - string - name of the QR set, e.g., `set=PresetName1`
- `hidden`   - bool   - whether the button should be hidden, e.g., `hidden=true`
- `startup`  - bool   - auto execute on app startup, e.g., `startup=true`
- `user`     - bool   - auto execute on user message, e.g., `user=true`
- `bot`      - bool   - auto execute on AI message, e.g., `bot=true`
- `load`     - bool   - auto execute on chat load, e.g., `load=true`
- `title`    - bool   - title / tooltip to be shown on button, e.g., `title="My Fancy Button"`

####

* `qr-get` - retrieves all of a Quick Reply's properties, example: `/qr-get set=myQrSet id=42`

#### Create or update QR preset

* `/qr-presetupdate (arguments [label])` or `/qr-presetadd (arguments [label])`

Arguments:
- `enabled` - bool - enable or disable the preset
- `nosend`  - bool - disable send / insert in user input (invalid for slash commands)
- `before`  - bool - place QR before user input
- `slots`   - int  - number of slots
- `inject`  - bool - inject user input automatically (if disabled use `{{input}}`)

Create a new preset (overrides existing ones), example: `/qr-presetadd slots=3 MyNewPreset`

#### Add QR context menu

* `/qr-contextadd (set=string label=string chain=bool [preset name])` – add context menu preset to a QR, example: `/qr-contextadd set=MyPreset label=MyButton chain=true MyOtherPreset`

#### Remove all context menus

* `/qr-contextclear (set=string [label])` – remove all context menu presets from a QR, example: `/qr-contextclear set=MyPreset MyButton`

#### Remove one context menu

* `/qr-contextdel (set=string label=string [preset name])` – remove context menu preset from a QR, example: `/qr-contextdel set=MyPreset label=MyButton MyOtherPreset`

### Quick Reply value escaping

`|{}` can be escaped with backslash in the QR message / command.

For example, use `/qr-create label=MyButton /getvar myvar \| /echo \{\{pipe\}\}` to create a QR that calls `/getvar myvar | /echo {{pipe}}`.

## Extension commands

SillyTavern extensions (both built-in, downloadable and third-party) can add their own slash command. Below is just an example of the capabilities in the official extensions. The list may be incomplete, make sure to check `/help slash` for the most complete list of available commands.

1. `/websearch (query)` — searches snippets of the web pages online for the specified query and returns the result into the pipe. Provided by the Web Search extension.
2. `/imagine (prompt)` — generates an image using the provided prompt. Provided by the Image Generation extension.
3. `/emote (sprite)` — sets a sprite for the active character by fuzzy matching its name. Provided by the Character Expressions extension.
4. `/costume (subfolder)` — sets a sprite set override for the active character. Provided by the Character Expressions extension.
5. `/music (name)` — force changes a played background music file by its name. Provided by the Dynamic Audio extension.
6. `/ambient (name)` — force changes a played ambient sound file by its name. Provided by the Dynamic Audio extension.
7. `/roll (dice formula)` — adds a hidden message to the chat with the result of a dice roll. Provided by the D&D Dice extension.

## UI interaction

Scripts can also interact with SillyTavern's UI: navigate through the chats or change styling parameters.

### Character navigation

1. `/random` — opens a chat with the random character.
2. `/go (name)` — opens a chat with the character of the specified name. First, searches for the exact name match, then by a prefix, then by a substring.

### UI styling

1. `/bubble` — sets the message style to the "bubble chat" style.
2. `/flat` — sets the message style to the "flat chat" style.
3. `/single` — sets the message style to the "single document" style.
4. `/movingui (name)` — activates a MovingUI preset by name.
5. `/resetui` — resets the MovingUI panels state to their original positions.
6. `/panels` — toggles the UI panels visibility: top bar, left and right drawers.
7. `/bg (name)` — finds and sets a background using fuzzy names matching. Respect the chat background lock state.
8. `/lockbg` — locks the background image for the current chat.
9. `/unlockbg` — unlocks the background image for the current chat.

## More examples

### Generate chat summary (by @IkariDevGIT)

```stscript
/setglobalvar key=summaryPrompt Summarize the most important facts and events that have happened in the chat given to you in the Input header. Limit the summary to 100 words or less. Your response should include nothing but the summary. |
/setvar key=tmp |
/messages 0-{{lastMessageId}} |
/trimtokens limit=3000 direction=end |
/setvar key=s1 |
/echo Generating, please wait... |
/genraw lock=on instruct=off {{instructInput}}{{newline}}{{getglobalvar::summaryPrompt}}{{newline}}{{newline}}{{instructInput}}{{newline}}{{getvar::s1}}{{newline}}{{newline}}{{instructOutput}}{{newline}}The chat summary:{{newline}} |
/setvar key=tmp |
/echo Done! |
/setinput {{getvar::tmp}} |
/flushvar tmp |
/flushvar s1
```

### Buttons popup usage

```stscript
/setglobalvar key=genders ["boy", "girl", "other"] |
/buttons labels=genders Who are you? |
/echo You picked: {{pipe}}
```

### Get Nth Fibonacci's number (using Binet's formula)

**Hint**: Set value of `fib_no` to the desired number

```stscript

/setvar key=fib_no 5 |
/pow 5 0.5 | /setglobalvar key=SQRT5 |
/setglobalvar key=PHI 1.618033 |
/pow PHI fib_no | /div {{pipe}} SQRT5 |
/round |
/echo {{getvar::fib_no}}th Fibonacci's number is: {{pipe}}
```

### Recursive Factorial (using closures)

```stscript
/let fact {: n=
    /if left={{var::n}} rule=gt right=1
        else={:
            /return 1
        :}
        {:
            /sub {{var::n}} 1 |
            /:fact n={{pipe}} |
            /mul {{var::n}} {{pipe}}
        :}
:} |

/input Calculate factorial of: |
/let n {{pipe}} |
/:fact n={{var::n}} |
/echo factorial of {{var::n}} is {{pipe}}
```

# SECTION: SillyTavern_LicenseCredits

# License and credits

**This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.**

**See the GNU Affero General Public License for more details.**

Original TavernAI (https://github.com/TavernAI/TavernAI) 1.2.8 by Humi: MIT License

## Pre-v1.9.0 Contributors
The git commit history was squashed to the state of release 1.9.0.

Unfortunately, losing commit history also means losing the code contribution history. If you contributed to the SillyTavern development and want to see yourself credited in the README file and Docs website, please get in touch with us!

## Documentation Contributors

Click the image below to see the full list of SillyTavern documentation contributors.

[](https://github.com/SillyTavern/SillyTavern-Docs/graphs/contributors)

