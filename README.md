
# STTTTTS

Converts your lovely human voice to an ugly robot voice, for the purpose of anonymity. Amazing!

## FAQ

### WHAT

a lot of people don't like sharing their Real Voice™ on the internet, which is fair. This project aims to rectify that by
1. Reading their voice and converting it to text (speech to text)
2. Generating an audio file of a robot saying it (to text to speech)
3. Spitting it back out as microphone input.

### HOW

microphone reading library -> Google Speech Recognition -> tts generating library -> virtual microphone

### IS THIS NOT A VOICE CHANGER?

well yes, but actually no.

its a voice change in the sense that its basically taking what you say and then saying it in a different voice but its not a voice changer in the sense that it applies filters to your voice

### HOW DO I USE IT

1. install the dependencies using `pip install -r requirements.txt`
2. double click main.py
3. mess with the inputs and outputs
3. ctrl+q to activate!

### DO YOU HAVE A DISCORD

yes! join [here](https://discord.gg/4Ru6SRasJB)!

## INSTALL GUIDE
step one is to clone the repo, using

```git clone https://github.com/sttttts/sttttts/```

if you use ssh cloning you definitely already know what to do

now you need to get the dependencies and their dependencies:
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyAudio](https://pypi.org/project/PyAudio/)
- [system_hotkey](https://pypi.org/project/system_hotkey/)
- [PySimpleGUI](https://pypi.org/project/PySimpleGUI/)
- [pywin32](https://pypi.org/project/pywin32/)

or you can run the install.s1 file using powershell **(but if you have python already then use the install.bat)

once everything is done installing, double click the file to run the program!
