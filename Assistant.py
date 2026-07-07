import speech_recognition as sr
import win32com.client
import time

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Volume = 100
speaker.Rate = 0

def speak(text):
    speaker.Speak(text)

speak("The Assistant is online. Hello Sir, how can I help you today?")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1

        audio = r.listen(source)

    try:
        print("Recognizing...")

        query = r.recognize_google(audio, language='en-in')

        print(f"User said: {query}\n")

        speak(f"You said {query}")

        time.sleep(1)

        return query

    except Exception:
        print("I am sorry, I did not understand that.")
        return ""

while True:
    query = takeCommand()

    if query:
        query = query.lower()

        if 'bye-bye' in query:
            speak("Goodbye Sir")
            break