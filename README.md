# Voice Assistant

A modular voice assistant that listens to user commands, interacts with an AI model using Ollama, opens and closes applications, and searches Google.

## Features
- **Speech Recognition** using `speech_recognition`
- **Text-to-Speech Output** using `pyttsx3`
- **AI-powered responses** using `ollama`
- **Application Management**: Open and close common applications like Chrome, Notepad, Calculator, VS Code, etc.
- **Web Search**: Search queries on Google
- **Modular Code Structure** for better organization and maintainability
- **GUI Interface** for status updates

## Requirements
Ensure you have the following dependencies installed:

```sh
pip install speechrecognition pyttsx3 ollama psutil
```

### Built-in Python Modules (No Installation Needed)
- `subprocess`
- `os`
- `time`
- `threading`
- `tkinter`

## Project Structure
```
voice_assistant/
│── main.py   # Main script that runs the voice assistant
│── voice_assistant.py   # Handles voice recognition and AI interaction
│── application_manager.py  # Handles opening and closing applications
│── gui.py   # Manages GUI updates and speaking function
│── README.md   # Documentation
```

## Usage
1. **Run the script**
   ```sh
   python main.py
   ```
2. **Speak a command** when prompted:
   - Open an application: *"Open Chrome"*, *"Open Notepad"*, *"Open VS Code"*
   - Close an application: *"Close Chrome"*, *"Close Notepad"*
   - Search Google: *"Search in Google for Python tutorials"*
   - Ask AI: *"What is the capital of France?"*
   - Exit: *"Exit"* or *"Quit"*

## Supported Applications
- **Google Chrome**
- **Notepad**
- **Calculator**
- **Visual Studio Code**
- **LinkedIn (Opens in browser)**

## How It Works
1. The assistant continuously listens for voice input.
2. It processes the command and determines the appropriate action:
   - Opens/closes an application.
   - Performs a Google search.
   - Sends the input to the AI model (`short-mistral` from Ollama) for a response.
3. The assistant speaks the response and updates the GUI accordingly.

## Notes
- The speech recognition uses Google’s API (`recognize_google`). Ensure you have an active internet connection.
- This project is designed for Windows-based systems; modify paths for other OS compatibility.
- `psutil` is used to manage process termination when closing applications.

## Future Enhancements
- Improve AI response handling.
- Add support for more applications.
- Expand functionality to support task automation.
- Implement a settings module for user customization.

---
**Author:** SHAFI

