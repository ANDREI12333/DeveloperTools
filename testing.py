import os
import time
import speech_recognition as sr

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

text = get_audio()

if "hello" in text:
    speak("hello, how are you?")
elif "what is your name" in text:
    speak("My name is Tim")