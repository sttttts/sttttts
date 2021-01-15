# This Python file uses the following encoding: utf-8
import sys
import os
import ctypes
import backend
import PySimpleGUI as sg

myappid = 'sttttts.sttttts.sttttts.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# Define the window's contents
layout = [
	[sg.Text("Volume %")],
	[sg.Slider(range = (0, 100),orientation="h",default_value=70,key="-VOLUME-")],
	[sg.Text("Sensitivity %")],
	[sg.Slider(range = (0, 100),orientation="h",default_value=80,key="-SENSITIVTY-")],
	[sg.Button('Ok'), sg.Button('Quit')]
]

# Create the window
window = sg.Window('sttttts', layout,icon="logos\\icon.ico")

# Display and interact with the Window using an Event Loop
while True:
	event, values = window.read()
	print(values)
	# See if user wants to quit or window was closed
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		break

# Finish up by removing from the screen
window.close()