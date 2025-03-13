import tkinter as tk
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

root = tk.Tk()
status_label = tk.Label(root, text="Waiting...", font=("Arial", 23), fg="white", bg="black")
status_label.pack(pady=20)

def update_status(text, color):
    status_label.config(text=text, fg=color)
    root.update()

def speak(text):
    update_status("Speaking...", "blue")
    engine.say(text)
    engine.runAndWait()
    update_status("Waiting...", "white")

def create_gui():
    root.title("Tom - Voice Assistant")
    root.geometry("400x300")
    root.configure(bg="black")
    root.mainloop()

def exit_from_gui():
    root.destroy()  # Close GUI
