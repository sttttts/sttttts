import pyttsx3
engine = pyttsx3.init()

def speak(words):
    engine.say(words)
    engine.runAndWait()
