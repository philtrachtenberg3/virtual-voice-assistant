import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text to speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(f"Recognized: {command}")
            return command.lower()
    except Exception as e:
        print(f"Error: {e}")
        return ""

def run_assistant():
    command = listen()
    if 'reminder' in command:
        speak("What would you like to be reminded about?")
    elif 'to do' in command:
        speak("Adding to your to-do list.")
    elif 'search' in command:
        speak("What do you need to find on the web?")
    else:
        speak("I did not understand your command.")

if __name__ == "__main__":
    speak("Hello, I am your assistant. How can I help you today?")
    run_assistant()