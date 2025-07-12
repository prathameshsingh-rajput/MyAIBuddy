# Handles speaking the reply

import pyttsx3
import time

def speak(text):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)
    engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()
