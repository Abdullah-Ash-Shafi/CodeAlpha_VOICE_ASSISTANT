# Voice Assistant

A simple voice assistant that listens to user commands, interacts with an AI model using Ollama, and opens applications based on voice input.

## Features
- Speech recognition using `speech_recognition`.
- Text-to-speech output using `pyttsx3`.
- AI-powered responses using `ollama`.
- Ability to open common applications like Chrome, Notepad, and Calculator.

## Requirements
Ensure you have the following dependencies installed:

```sh
pip install speechrecognition pyttsx3 ollama
```

### Additional Requirements:
- `subprocess` (built-in Python module)
- `os` (built-in Python module)

## Usage
1. **Run the script**
   ```sh
   python voice_assistant.py
   ```
2. **Speak a command** when prompted:
   - To ask a general question: *"What is the capital of France?"*
   - To open an application: *"Open Chrome"*, *"Open Notepad"*
   - To exit: *"Exit"* or *"Quit"*

## How It Works
- The assistant continuously listens for voice input.
- If the command includes "open", it attempts to launch the specified application.
- Otherwise, it forwards the input to the AI model (Ollama) for a response.
- The response is then spoken back to the user.

## Supported Applications
- **Google Chrome**
- **Notepad**
- **Calculator**

## Notes
- The speech recognition uses Google’s API (`recognize_google`). Ensure you have an active internet connection.
- The AI model used is `short-mistral` from Ollama.
- This project is designed for Windows-based systems; modify `subprocess.Popen` paths for other OS compatibility.

## Future Enhancements
- Add support for more applications.
- Improve AI model response handling.
- Implement a GUI interface for better usability.

---
**Author:** SHAFI

