import wave

import pyaudio
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer() # adding object for the recognizer
engine = pyttsx3.init()

def get_io_devices():
	p = pyaudio.PyAudio()
	info = p.get_host_api_info_by_index(0)
	numdevices = info.get('deviceCount')
	inp = []
	out = []
	for i in range(0, numdevices):
		if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
			inp.append(p.get_device_info_by_host_api_device_index(0, i).get('name'))
	for i in range(0, numdevices):
		if (p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels')) > 0:
			out.append(p.get_device_info_by_host_api_device_index(0, i).get('name'))
	return inp,out

def stt(inp):

	# speech to text
	if inp: pass
	with sr.Microphone(device_index=inp) as source: # making the system default mic as the input source
		print("Say Anything:")
		audio = r.listen(source=source) # listening to the input
		print(f"Stopped Listenning")
		try:
			text = r.recognize_google(audio) # understanding the input
			print(f'you said "{text}"')
		except:
			print("lol i didnt know what you said")
			return
		del(source)
		return text

def make_stt_file(text):
	# text to speech
	
	engine.save_to_file(text, 'tts.wav')
	engine.runAndWait()

def tts(out):
	# playing to VB-Audio Cable Input

	wf = wave.open("tts.wav", 'rb')
	p = pyaudio.PyAudio()
	CHUNK = 182
	discord = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True,
		output_device_index=out)

	speakers = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True)

	data = wf.readframes(CHUNK)

	while data != b'':
		discord.write(data)
		speakers.write(data)
		data = wf.readframes(CHUNK)

def main(inp,out):
	make_stt_file(stt(inp))
	tts(out)

if __name__ == "__main__":
	main(0,0)