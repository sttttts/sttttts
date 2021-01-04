import speech_recognition as sr
from system_hotkey import SystemHotkey
import tts

# VVVVVV stt part; the heavy lifter of this file VVVVVV

r = sr.Recognizer() # adding object for the recognizer

def listen():
    with sr.Microphone() as source: # making the system default mic as the input source
        print("Say Anything:")
        audio = r.listen(source=source) # listening to the input

        try:
            text = r.recognize_google(audio) # understanding the input
            print(f'you said "{text}"')
            tts.speak(words=text)
        except:
            print("lol i didnt know what you said")




# VVVVVV the part that activates the stt VVVVVV

hk = SystemHotkey()
hk.register(('control', 'q'), callback=lambda x:listen())