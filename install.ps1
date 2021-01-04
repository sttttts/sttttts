Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe" -OutFile "python-3.9.1-amd64.exe"
.\python-3.9.1-amd64.exe /passive Include_pip=1 Include_launcher=1 Include_exe=1
python -m pip install pip PySide2 pipwin SpeechRecognition
pipwin install PyAudio