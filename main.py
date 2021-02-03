# This Python file uses the following encoding: utf-8
import sys
import os
import ctypes
from system_hotkey import SystemHotkey
import PySimpleGUI as sg
import backend

myappid = 'sttttts.sttttts.sttttts.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


# Define the window's contents
layout = [
	# [sg.Text("Volume %")],
	# [sg.Slider(range = (0, 100),orientation="h",default_value=70,key="-VOLUME-")],
	# [sg.Text("Sensitivity %")],
	# [sg.Slider(range = (0, 100),orientation="h",default_value=80,key="-SENSITIVTY-")],
	[sg.Text("Input")],
	[sg.Combo(backend.get_io_devices()[0],readonly=True,default_value=backend.get_io_devices()[0][0],key="-INPUT-")],
	[sg.Text("Output")],
	[sg.Combo(backend.get_io_devices()[1],readonly=True,default_value=backend.get_io_devices()[1][0],key="-OUTPUT-")],
	[sg.Text("Output 2")],
	[sg.Combo(["Disabled"] + backend.get_io_devices()[1],readonly=True,default_value="Disabled",key="-OUTPUT2-")],
	[sg.Button('Ok'), sg.Button('Quit')]
]
# Create the window
window = sg.Window('sttttts', layout,icon="logos\\icon.ico")
hk = SystemHotkey()
hk.register(('control', 'q'), callback=lambda x:backend.main(0,4))

# Display and interact with the Window using an Event Loop
while True:
	event, values = window.read()
	# See if user wants to quit or window was closed
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		break
	devices = backend.get_io_devices()
	wanted_input = devices[0].index(values["-INPUT-"])
	wanted_output = devices[1].index(values["-OUTPUT-"]) + len(devices[0])
	if values["-OUTPUT2-"] == "Disabled":
		wanted_output2 = None
	else:
		wanted_output2 = devices[1].index(values["-OUTPUT2-"]) + len(devices[0])
	hk.unregister(('control', 'q'))
	if wanted_output2 == "Disabled":
		wanted_output2 = None
	hk.register(('control', 'q'), callback=lambda x:backend.main(wanted_input,wanted_output,wanted_output2))
# Finish up by removing from the screen
window.close()