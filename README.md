# Jasco1500ruinedMyLife
this thing clicks smoothing and export to txt for you in jasco's spectra manager.

to use:
use pip to install: pyqt5, pynput, clipboard, and maybe win32gui if it doesnt exist already
for jasco computers that dont have internet access (like the one in my department) you can use pyinstaller like 
pyinstaller --onefile pythonScriptName.py
but since I cant program and have to use qtdesigner, make sure to copy the basic.ui file with the generated exe to make the whole thign work.

program looks like:
![Chungus](https://github.com/syw784/Jasco1500ruinedMyLife/raw/main/kkk.PNG)

to use:
put names in text fields until its your desired name format;
click "starto";
this will first try to find a window called spectramanager, which is the window jasco opens when a spectrum is collected.
then it tries to smooth it by using keyboard commands.
then it tries to export it to txt using keyboard commands.
then it closes spectramanager.

ideally you can make this a loop so it does the whole thing automatically while you collect spectra, but since im leaving the program,
![Chungus](https://i.imgflip.com/2wd65n.jpg)
