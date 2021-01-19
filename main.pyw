# This Python file uses the following encoding: utf-8
import sys
import os
import ctypes
import backend
import PySimpleGUI as sg
from system_hotkey import SystemHotkey

myappid = 'sttttts.sttttts.sttttts.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


# Define the window's contents
layout = [
	[sg.Text("Volume %")],
	[sg.Slider(range = (0, 100),orientation="h",default_value=70,key="-VOLUME-")],
	[sg.Text("Sensitivity %")],
	[sg.Slider(range = (0, 100),orientation="h",default_value=80,key="-SENSITIVTY-")],
	[sg.Text("Input")],
	[sg.Combo(backend.get_io_devices()[0],readonly=True,default_value=backend.get_io_devices()[0][0],key="-INPUT-")],
	[sg.Text("Output")],
	[sg.Combo(backend.get_io_devices()[1],readonly=True,default_value=backend.get_io_devices()[1][0],key="-OUTPUT-")], [sg.Button('Ok'), sg.Button('Quit')]
]
# Create the window
window = sg.Window('sttttts', layout,icon="logos\\icon.ico")
hk = SystemHotkey()
hk.register(('control', 'q'), callback=lambda x:backend.main(0,0))

# Display and interact with the Window using an Event Loop
while True:
	event, values = window.read()
	# See if user wants to quit or window was closed
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		break
	devices = backend.get_io_devices()
	wanted_input = devices[0].index(values["-INPUT-"])
	wanted_output = devices[1].index(values["-OUTPUT-"])
	hk.unregister(('control', 'q'))
	hk.register(('control', 'q'), callback=lambda x:backend.main(wanted_input,wanted_output))
# Finish up by removing from the screen
window.close()