# This Python file uses the following encoding: utf-8
import sys
import os
import ctypes
import stt

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


myappid = 'sttttts.sttttts.sttttts.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class sttttts(QWidget):
	def __init__(self):
		super(sttttts,self).__init__()
		self.load_ui()

	def load_ui(self):
		loader = QUiLoader()
		path = os.path.join(os.path.dirname(__file__), "form.ui")
		ui_file = QFile(path)
		ui_file.open(QFile.ReadOnly)
		loader.load(ui_file, self)
		ui_file.close()


if __name__ == "__main__":
	app = QApplication([])
	widget = sttttts()
	widget.show()
	sys.exit(app.exec_())
