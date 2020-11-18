from PyQt5 import QtWidgets, uic
import sys, pynput, time
from pynput.keyboard import Key
keyboard = pynput.keyboard.Controller()
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt
import clipboard, win32gui

def press(keys, inbtw = 0.1, wait = 0.1):
    for i in range(len(keys)):
        keys[i] = key2pynputkey(keys[i])

    for i in keys:
        keyboard.press(i)
        time.sleep(inbtw)

    for i in keys:
        keyboard.release(i)
        time.sleep(inbtw)
    time.sleep(wait)

def key2pynputkey(key):
    dic = {
        'alt'   : Key.alt,
        'tab'   : Key.tab,
        'enter' : Key.enter,
        'down'   : Key.down,
        'right' : Key.right,
        'ctrl' : Key.ctrl,
        'f4' : Key.f4,
    }
    try:
        return dic[key]
    except:
        return key

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('basic.ui', self)
        self.setWindowTitle("Sheng's misery")
        self.name_lineedit = self.findChild(QLineEdit, 'name_lineEdit')
        self.name_lineedit.textChanged.connect(self.update_out)
        self.ph_spinbox = self.findChild(QSpinBox, 'pH_spinBox')
        self.autoinc_checkbox = self.findChild(QCheckBox, 'autoinc_checkBox')
        self.anneal_lineedit_2 = self.findChild(QLineEdit, 'anneal_lineEdit_2')
        self.anneal_lineedit_2.textChanged.connect(self.update_out)
        self.anneal_checkbox_2 = self.findChild(QCheckBox, 'anneal_checkBox_2')
        self.anneal_checkbox_2.stateChanged.connect(self.update_out)
        self.out_lineedit_3 = self.findChild(QLineEdit, 'out_lineEdit_3')
        self.out_lineedit_3.setAlignment(Qt.AlignCenter)
        self.starto_pushbutton = self.findChild(QPushButton, 'starto_pushButton')
        self.starto_pushbutton.clicked.connect(self.starto_pushbuttonP)
        
        self.show()

    def starto_pushbuttonP(self):
        try:
            win32gui.SetForegroundWindow(win32gui.FindWindow(None, 'Spectra Analysis'))
        except:
            QMessageBox.about(self, "bug", "oh shit")
            return
        press(['alt', 'p'])
        press(['right'])
        press(['down'])
        press(['enter'])
        press(['enter'], wait = 0.5)

        press(['alt', 'f'])        
        press(['e'])

        clipboard.copy(self.update_out(''))
        if self.autoinc_checkbox.checkState() == Qt.Checked:
            self.ph_spinbox.setValue(self.ph_spinbox.value() + 1)

        press(['ctrl', 'v'])
        press(['tab'])
        press(['down'])
        press(['down'])
        press(['tab'])
        press(['enter'])
        press(['enter'], wait = 0.5)

        press(['alt', 'f4'])
        press(['n'])
        press(['n'])

        #print("starto_pushbutton")

    def update_out(self, *args):
        string = self.name_lineedit.text() + ' pH ' + str(self.ph_spinbox.value())
        if self.anneal_checkbox_2.checkState() == Qt.Checked:
            string += " " + self.anneal_lineedit_2.text()
        self.out_lineedit_3.setText(string)
        return string

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()