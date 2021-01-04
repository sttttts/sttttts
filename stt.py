import speech_recognition as sr

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Say Anything:")
        audio = r.listen(source=source)

        try:
            text = r.recognize_google(audio)
            print(f'you said "{text}"')
        except:
            print("lol i didnt know what you said")