import speech_recognition as sr
import pyttsx3
import pyaudio
import wave

r = sr.Recognizer() # adding object for the recognizer
engine = pyttsx3.init()

def stt():

	# speech to text

	with sr.Microphone() as source: # making the system default mic as the input source
		print("Say Anything:")
		audio = r.listen(source=source) # listening to the input
		print(f"Stopped Listenning")
		try:
			text = r.recognize_google(audio) # understanding the input
			print(f'you said "{text}"')
		except:
			print("lol i didnt know what you said")
			return
		return text

def make_stt_file(text):
	# text to speech
	
	engine.save_to_file(text, 'tts.wav')
	engine.runAndWait()

def tts():
	# playing to VB-Audio Cable Input

	wf = wave.open("tts.wav", 'rb')
	p = pyaudio.PyAudio()
	CHUNK = 182

	discord = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True,
		output_device_index=6)

	speakers = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True)

	data = wf.readframes(CHUNK)

	while data != '':
		discord.write(data)
		speakers.write(data)
		data = wf.readframes(CHUNK)

def main():
	make_stt_file(stt())
	tts()

if __name__ == "__main__":
	main()