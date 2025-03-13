import tkinter as tk
from threading import Thread
from gui import create_gui
from assistant import voice_assistant

def run_assistant():
    voice_assistant()

if __name__ == "__main__":
    # Start the assistant in a separate thread
    Thread(target=run_assistant, daemon=True).start()

    # Create and run the GUI
    create_gui()

