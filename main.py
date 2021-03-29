# This Python file uses the following encoding: utf-8
import ctypes
from system_hotkey import SystemHotkey
import PySimpleGUI as sg
import backend as b

myappid = 'sttttts.sttttts.sttttts.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


# Define the window's contents
layout = [
	# [sg.Text("Volume %")],
	# [sg.Slider(range = (0, 100),orientation="h",default_value=70,key="-VOLUME-")],
	# [sg.Text("Sensitivity %")],
	# [sg.Slider(range = (0, 100),orientation="h",default_value=80,key="-SENSITIVTY-")],
	[sg.Text("Input")],
	[sg.Combo(b.get_io_devices()[0],readonly=True,default_value=b.get_io_devices()[0][0],key="-INPUT-")],
	[sg.Text("Output")],
	[sg.Combo(b.get_io_devices()[1],readonly=True,default_value=b.get_io_devices()[1][0],key="-OUTPUT-")],
	[sg.Text("Output 2")],
	[sg.Combo(["Disabled"] + b.get_io_devices()[1],readonly=True,default_value="Disabled",key="-OUTPUT2-")],
	[sg.Text("Say manually")],
	[sg.Input(key="-MANUAL-"),sg.Button("Say")],
	[sg.Button('Ok'), sg.Button('Quit')]
]
# Create the window
window = sg.Window('sttttts', layout,icon="logos\\icon.ico")
hk = SystemHotkey()
hk.register(('control', 'q'), callback=lambda x:b.main(None,None,None))
hk.register(('alt', 'q'), callback=lambda x:b.repeat(None,None))

# Display and interact with the Window using an Event Loop
while True:
	event, values = window.read()
	# See if user wants to quit or window was closed
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		break
	devices = b.get_io_devices()
	wanted_input = devices[0].index(values["-INPUT-"])
	wanted_output = devices[1].index(values["-OUTPUT-"]) + len(devices[0])
	if values["-OUTPUT2-"] == "Disabled":
		wanted_output2 = None
	else:
		wanted_output2 = devices[1].index(values["-OUTPUT2-"]) + len(devices[0])
	if event == 'Say':
		b.say(wanted_output,wanted_output2,values["-MANUAL-"])
	hk.unregister(('control', 'q'))
	hk.unregister(('alt', 'q'))
	hk.register(('control', 'q'), callback=lambda x:b.main(wanted_input,wanted_output,wanted_output2))
	hk.register(('alt', 'q'), callback=lambda x:b.repeat(wanted_output,wanted_output2))
# Finish up by removing from the screen
window.close()