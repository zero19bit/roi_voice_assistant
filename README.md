# Roi Assistant — Version 0

A multilingual desktop voice assistant built with Python and Vosk speech recognition.

--------------------------------------------------

## Overview

Roi is a simple voice-controlled assistant capable of recognizing spoken commands in multiple languages and performing desktop or web-based actions.

Current supported languages:

- Persian (FA)
- Turkish (TR)
- English (US) — initial support

The assistant works completely offline using Vosk speech recognition models.

--------------------------------------------------

## Features

- Offline speech recognition
- Multilingual command processing
- Open applications and websites
- Media control support
- System volume control
- Screenshot shortcut
- Language switching
- Simple console-based interface

--------------------------------------------------

## Supported Actions

### Open Websites

- Google
- YouTube
- YouTube Music
- Telegram Web
- Instagram
- Spotify

### Open Applications

- PyCharm
- Notepad
- CMD / Terminal
- This PC (Explorer)

### Media Controls

- Volume Up
- Volume Down
- Mute
- Next Track
- Previous Track
- Play / Pause

### Other Functions

- Screenshot capture
- Exit confirmation
- Language switching

--------------------------------------------------

## Project Structure

```
project/
│
├── start.py
├── main.py
├── vosk_languages.py
├── config.json
│
├── talk_to_write_FA.py
├── talk_to_write_TR.py
└── talk_to_write_US.py
```

--------------------------------------------------

## File Descriptions

### start.py

Application entry point.

Runs:

import main
main.main()

--------------------------------------------------

### main.py

Core assistant logic.

Handles:

- Command processing
- Language loops
- Desktop automation
- Browser actions
- Media controls

--------------------------------------------------

### vosk_languages.py

Loads Vosk models for supported languages.

Creates:

- model_FA
- model_TR
- model_US

--------------------------------------------------

### config.json

Stores paths to Vosk models.

Example:

{
  "model_path_FA": "model/vosk-model-fa-0.42",
  "model_path_TR": "model/vosk-model-small-tr-0.3",
  "model_path_US": "model/vosk-model-small-en-us-0.15"
}

--------------------------------------------------

### talk_to_write_FA.py

Persian speech-to-text module.

--------------------------------------------------

### talk_to_write_TR.py

Turkish speech-to-text module.

--------------------------------------------------

### talk_to_write_US.py

English speech-to-text module.

--------------------------------------------------

## Installation

### Clone Project

git clone <repository-url>
cd roi-assistant

--------------------------------------------------

### Install Dependencies

pip install vosk pyautogui

Additional packages may be required depending on microphone and audio setup.

--------------------------------------------------

## Download Vosk Models

Download the required models from:

https://alphacephei.com/vosk/models

Place them inside:

model/

Example:

```
model/
├── vosk-model-fa-0.42
├── vosk-model-small-tr-0.3
└── vosk-model-small-en-us-0.15
```

--------------------------------------------------

## Run Project

python start.py

--------------------------------------------------

## Architecture

start.py
    ↓
main.py
    ↓
talk_to_write_*.py
    ↓
vosk_languages.py
    ↓
Vosk Speech Models

--------------------------------------------------

## Notes

- The assistant currently focuses on Windows systems.
- Most commands are based on keyword matching.
- Speech recognition is fully offline.

--------------------------------------------------

## Known Issue

vosk_languages.py references:

models.json

But the existing file is:

config.json

This should be unified before production use.

--------------------------------------------------

## Future Improvements

- Better NLP processing
- GUI version
- Wake-word activation
- Voice response system (TTS)
- More supported languages
- Linux support
- Smarter command handling

--------------------------------------------------

## Version

Current Release: Version 0

Experimental multilingual voice assistant project built with Python and Vosk.
