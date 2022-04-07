import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

# speak("Good day, sir. Im Jarvis your personal assistant!")

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

# speak("Sup")
text = get_audio()
print(text)

if "hello" in text:
    speak("Whats up there!")
elif "what is your name" in text:
    speak("My name is Jarvis")