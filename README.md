# GT Voice Assistant

A beginner-friendly Python voice assistant prototype for the GT Voice Assistant project listed on the resume.

## Features
- Speech-to-text using `SpeechRecognition`
- Text-to-speech using `pyttsx3`
- Opens a Google search in your browser
- Tells the current date and time
- Opens common websites such as YouTube and Google
- Text-input fallback if you cannot use a microphone

## Requirements
- Python 3.10 or newer
- Microphone for voice input (optional if using text mode)
- Internet connection for speech recognition and web searches

## Run on Windows (VS Code / Command Prompt)

1. Extract the ZIP and open the `gt_voice_assistant` folder in VS Code.
2. Open Terminal in that folder.
3. Create and activate a virtual environment:

```bash
py -m venv .venv
.venv\Scripts\activate
```

4. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

5. Start the assistant:

```bash
python main.py
```

Choose voice mode or text mode when prompted.

## Example commands
- "search Python tutorials"
- "open YouTube"
- "open Google"
- "what time is it"
- "what is today's date"
- "help"
- "exit"

## Troubleshooting
- If microphone access fails, check Windows microphone permissions and select text mode.
- If `py` is not recognized, try `python` instead.
- Speech recognition requires internet access in this prototype.
- `pyttsx3` voice availability depends on voices installed on your operating system.

## Limitations
This is a learning prototype, not a fully conversational AI assistant. Search requests open browser results rather than independently verifying or summarizing websites. Do not describe it as using a trained machine-learning model unless you add and evaluate one.
