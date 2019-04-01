import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import socket

def get_ip():
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


# Fetch the service account key JSON file contents
cred = credentials.Certificate('./laas-3f922-firebase-adminsdk-22bpq-a23ab6f2ad.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://laas-3f922.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('/')

stu_name = "Himanshu" 
stu_roll = "151500231"
address = get_ip()+":8000"

stu_id = 'student_'+ stu_roll

ref.update({
    stu_id : {
        'student_name': stu_name,
        'student_roll': stu_roll,
        'student_node_ip': address 
    }
})

print(ref.get())
