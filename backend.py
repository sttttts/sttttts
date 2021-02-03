import wave

import pyaudio
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer() # adding object for the recognizer
engine = pyttsx3.init()
p = pyaudio.PyAudio()

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

class sttttts:
	"""
	The class that does speech to text, to text to speech.
	"""
	def __init__(self,input_index,output_index,output_index2):
		self.mic = sr.Microphone(device_index=input_index)
		self.output_index = output_index
		self.output_index2 = output_index2
	def stt(self):

		# speech to text
		with self.mic as source: # making the system default mic as the input source
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

	def make_stt_file(self,text):
		# text to speech

		engine.save_to_file(text, 'tts.wav')
		engine.runAndWait()

	def tts(self):
		# playing to VB-Audio Cable Input

		wf = wave.open("tts.wav", 'rb')
		CHUNK = 182
		output1 = p.open(
			format=p.get_format_from_width(wf.getsampwidth()),
			channels=wf.getnchannels(),
			rate=wf.getframerate(),
			output=True,
			output_device_index=self.output_index
		)
		data = wf.readframes(CHUNK)
		if(self.output_index2 != None):
			output2 = p.open(
				format=p.get_format_from_width(wf.getsampwidth()),
				channels=wf.getnchannels(),
				rate=wf.getframerate(),
				output=True,
				output_device_index=self.output_index2
			)

			while data != b'':
				output1.write(data)
				output2.write(data)
				data = wf.readframes(CHUNK)
		else:
			while data != b'':
				output1.write(data)
				data = wf.readframes(CHUNK)

def main(inp,out,inp2 = None):
	io = sttttts(inp,out,inp2)
	text = io.stt()
	if text is None:
		return
	io.make_stt_file(text)
	io.tts()

if __name__ == "__main__":
	main(0,4)