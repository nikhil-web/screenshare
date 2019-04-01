import sys
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QApplication, QLabel, QWidget, QPushButton, QLineEdit

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Admin"
        self.left = 10
        self.top = 60
        self.width = 400
        self.height = 140
        self.initUI()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())