import sys
from PyQt5.QtWidgets import QApplication
from pyqt_chat_server.c_server import ServerWindow

app = QApplication(sys.argv)

server = ServerWindow()
sys.exit(app.exec_())