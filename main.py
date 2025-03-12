import speech_recognition as sr
import pyttsx3
import ollama
import os
import subprocess

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
    else:
        speak("Sorry, I don't know how to open that application.")

# Main assistant loop
while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            os.system('cls') 
            print("Listening...")
            audio = recognizer.listen(mic)

            # Recognize speech using Google API (set for Indian English)
            user_input = recognizer.recognize_google(audio, language="en-IN")
            user_input = user_input.lower()

            # print(f"You said: {user_input}")
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
                else:
                    ai_response = get_ai_response(user_input)
                    # print(f"Assistant: {ai_response}")
                    print("^_^")
                    speak(ai_response)

            else:
                print("Waiting for the assistant's name to be mentioned...")

    except sr.UnknownValueError:
        continue
        # print("Sorry, I didn't catch that.")

    except sr.RequestError:
        continue
        # print("Could not connect to Google Speech Recognition service.")

