from PyQt5 import QtWidgets
from pyqt_chat_server.ui_server import Ui_ChatServer

class ServerWindow(QtWidgets.QMainWindow, Ui_ChatServer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.startBtn.clicked.connect(self.startOn)

    def startOn(self):
        self.startBtn.setEnabled(False)
        self.logView.append('')
