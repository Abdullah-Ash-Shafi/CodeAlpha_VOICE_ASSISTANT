import subprocess
import psutil
import webbrowser
from gui import speak, update_status

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

def close_application(app_name):
    update_status("Closing application...", "red")
    for proc in psutil.process_iter(['pid', 'name']):
        if app_name.lower() in proc.info['name'].lower():
            proc.terminate()
            speak(f"Closing {proc.info['name']}")
            break
    else:
        speak(f"Could not find {app_name} running.")
    update_status("Waiting...", "white")

def search_google(query):
    speak(f"Searching for {query}")
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    update_status("Waiting...", "white")
