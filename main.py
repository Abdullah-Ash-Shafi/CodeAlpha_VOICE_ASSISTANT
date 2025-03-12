import speech_recognition as sr
import pyttsx3
import ollama
import os
import subprocess

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak output
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to interact with Ollama (AI Model)
def get_ai_response(prompt):
    print("... ... ... ... ...")
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
    else:
        speak("Sorry, I don't know how to open that application.")


while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Listening...")
            audio = recognizer.listen(mic)

            # Recognize speech using Google API (set for Indian English)
            user_input = recognizer.recognize_google(audio, language="en-IN")
            user_input = user_input.lower()

            # print(f"You said: {user_input}")

            # Exit condition
            if "exit" in user_input or "quit" in user_input:
                # print("Exiting assistant")
                speak("Goodbye!")
                break

            # Check if the user wants to open an app
            if "open" in user_input:
                open_application(user_input)
            else:
                ai_response = get_ai_response(user_input)
                # print(f"Assistant: {ai_response}")

                speak(ai_response)

    except sr.UnknownValueError:
        continue
        #print("Sorry, I didn't catch that.")
    except sr.RequestError:
        continue
        #print("Could not connect to Google Speech Recognition service.")
