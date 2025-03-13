import speech_recognition as sr
import pyttsx3
import ollama
import os
import subprocess
import webbrowser

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define assistant's name
assistant_name = "tom" 

# Function to speak output
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to interact with Ollama (AI Model)
def get_ai_response(prompt):
    print(">_-")
    response = ollama.chat(model="short-mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

# Function to open an application
def open_application(app_name):
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

# Function to search Google
def search_google(query):
    speak(f"Searching for {query}")
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)

# Main assistant loop
while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.3)
            os.system('cls') 
            print("Listening...")
            audio = recognizer.listen(mic)

            # Recognize speech using Google API (set for Indian English)
            user_input = recognizer.recognize_google(audio, language="en-IN")
            user_input = user_input.lower()

            print("-_-")

            # Check if the assistant's name is mentioned (to trigger assistant)
            if assistant_name.lower() in user_input:
                # Remove the assistant's name from the input for further processing
                user_input = user_input.replace(assistant_name.lower(), "").strip()

                if "exit" in user_input or "quit" in user_input:
                    print("Exiting assistant...")
                    speak("Goodbye!")
                    break

                if "open" in user_input:
                    open_application(user_input)
                elif "search in google for" in user_input:
                    query = user_input.replace("search in google for", "").strip()
                    search_google(query)
                else:
                    ai_response = get_ai_response(user_input)
                    print("^_^")
                    speak(ai_response)

            else:
                print(" (-_-) Waiting for the assistant's name to be mentioned.")

    except sr.UnknownValueError:
        continue
    except sr.RequestError:
        continue


