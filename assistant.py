import speech_recognition as sr
import pyttsx3
import ollama
import time
from application_manager import open_application, close_application, search_google
from gui import update_status, speak, exit_from_gui
import sys


# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define assistant's name
assistant_name = "tom"


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


def voice_assistant():
    while True:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                update_status("Listening...", "red")
                audio = recognizer.listen(mic)

                user_input = recognizer.recognize_google(audio, language="en-IN").lower()

                update_status("Processing...", "yellow")
                print(f"User Input: {user_input}")

                if assistant_name.lower() in user_input:
                    user_input = user_input.replace(assistant_name.lower(), "").strip()

                    if "exit" in user_input or "quit" in user_input:
                        print("Exiting assistant...")
                        speak("Goodbye!")
                        
                        # Destroy GUI and exit program
                        exit_from_gui()
                        sys.exit()      # Ensure full termination

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
                        speak(ai_response)

                update_status("Waiting...", "white")
                time.sleep(1)

        except sr.UnknownValueError:
            continue
        except sr.RequestError:
            print("Error with speech recognition.")
            continue
