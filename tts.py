import pyttsx3

engine = pyttsx3.init()

def speak(words):
	engine.say(words)
	engine.save_to_file(words, 'tts.ogg')
	engine.runAndWait()
