import sys
import socket
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QApplication, QLabel, QWidget, QPushButton, QLineEdit
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Student' s Information"
        self.left = 10
        self.top = 60
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.nameLabel = QLabel("Name:")
        self.nameBox = QLineEdit(self)
        self.rollLabel = QLabel("Roll:")
        self.rollBox = QLineEdit(self)
        self.sectionLabel = QLabel("Section:")
        self.sectionBox = QLineEdit(self)
        self.sectionBox.resize(20, 20)

        h_box1 = QHBoxLayout()
        h_box1.addWidget(self.nameLabel)
        h_box1.addSpacing(30)
        h_box1.addWidget(self.nameBox)

        h_box2 = QHBoxLayout()
        h_box2.addWidget(self.rollLabel)
        h_box2.addSpacing(40)
        h_box2.addWidget(self.rollBox)

        h_box3 = QHBoxLayout()
        h_box3.addWidget(self.sectionLabel)
        h_box3.addSpacing(20)
        h_box3.addWidget(self.sectionBox)

        self.submit = QPushButton('Submit')
        self.exit = QPushButton('Exit')

        v_box = QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addWidget(self.submit)
        v_box.addWidget(self.exit)
        self.setLayout(v_box)

        self.submit.clicked.connect(self.action)
        self.exit.clicked.connect(self.action2)

        self.show()

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def action(self):
        a = self.nameBox.text()
        b = self.rollBox.text()
        c = self.sectionBox.text()
        ip = self.get_ip()

        self.send_data(a,b,c,ip)

        print(a, b, c, ip)

    def action2(self):
        self.close()

    def send_data(self, a, b, c, ip):
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate('./laas-3f922-firebase-adminsdk-22bpq-a23ab6f2ad.json')

        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://laas-3f922.firebaseio.com/'
        })

        # As an admin, the app has access to read and write all data, regradless of Security Rules
        ref = db.reference('all_students/online')

        stu_name = a
        stu_roll = b
        stu_sec = c
        address = ip + ":8000"

        stu_id = 'student_' + stu_roll

        ref.update({
            stu_id: {
                'student_name': stu_name,
                'student_roll': stu_roll,
                'student_sect': stu_sec,
                'student_node_ip': address
            }
        })

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
