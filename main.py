import speech_recognition as sr
import pyttsx3
import ollama
import os
import subprocess
import webbrowser
import tkinter as tk
from threading import Thread
import time
import psutil

recognizer = sr.Recognizer()
engine = pyttsx3.init()

assistant_name = "tom" 

root = tk.Tk()
root.title("Tom - Voice Assistant")
root.geometry("400x300")
root.configure(bg="black")

status_label = tk.Label(root, text="Waiting...", font=("Arial", 23), fg="white", bg="black")
status_label.pack(pady=20)

def update_status(text, color):
    status_label.config(text=text, fg=color)
    root.update()

# Function to speak output
def speak(text):
    update_status("Speaking...", "blue")
    engine.say(text)
    engine.runAndWait()
    update_status("Waiting...", "white")

# Function to interact with Ollama
def get_ai_response(prompt):
    update_status("Processing...", "yellow")
    try:
        response = ollama.chat(model="short-mistral", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except ollama._types.ResponseError as e:
        print(f"Error with Ollama: {e}")
        return "Sorry, there was an issue with the AI model. Please try again later."
    except Exception as e:
        print(f"General error: {e}")
        return "Sorry, I couldn't process your request at the moment."

# Function to open an application
def open_application(app_name):
    update_status("Opening application...", "green")
    if "chrome" in app_name:
        speak("Opening Google Chrome")
        subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])
    elif "notepad" in app_name:
        speak("Opening Notepad")
        subprocess.Popen(["notepad.exe"])
    elif "calculator" in app_name:
        speak("Opening Calculator")
        subprocess.Popen(["calc.exe"])
    elif "linkedin" in app_name:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "vs code" in app_name or "visual studio code" in app_name:
        speak("Opening Visual Studio Code")
        subprocess.Popen(["C:\\Program Files\\Microsoft VS Code\\Code.exe"])
    else:
        speak("Sorry, I don't know how to open that application.")
    update_status("Waiting...", "white")

# Function to close an application
def close_application(app_name):
    update_status("Closing application...", "red")
    for proc in psutil.process_iter(['pid', 'name']):
        if app_name.lower() in proc.info['name'].lower():
            proc.terminate()
            speak(f"Closing")
            break
    else:
        speak(f"Could not find {app_name} running.")
    update_status("Waiting...", "white")

# Function to search Google
def search_google(query):
    speak(f"Searching for {query}")
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    update_status("Waiting...", "white")

# Function to handle voice commands
def voice_assistant():
    while True:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                os.system('cls') 
                update_status("Listening...", "red")
                print("Listening...")
                audio = recognizer.listen(mic)

                user_input = recognizer.recognize_google(audio).lower()

                update_status("Processing...", "yellow")
                print("Processing...")

                if assistant_name.lower() in user_input:
                    user_input = user_input.replace(assistant_name.lower(), "").strip()

                    if "exit" in user_input or "quit" in user_input:
                        print("Exiting assistant...")
                        speak("Goodbye!")
                        root.destroy()
                        break

                    if "open" in user_input:
                        open_application(user_input)
                    elif "close" in user_input:
                        app_name = user_input.replace("close", "").strip()
                        close_application(app_name)
                    elif "search in google for" in user_input:
                        query = user_input.replace("search in google for", "").strip()
                        search_google(query)
                    else:
                        ai_response = get_ai_response(user_input)
                        print("Speaking...")
                        speak(ai_response)
                
                update_status("Waiting...", "white")
                print("Waiting...")

                time.sleep(1)  # Prevents the CPU from being overwhelmed

        except sr.UnknownValueError:
            print("-_-_-_-_-_-_-_-_-_-")
            continue
        except sr.RequestError:
            print("===========")
            continue

# Run voice assistant in a separate thread
Thread(target=voice_assistant, daemon=True).start()
root.mainloop()




