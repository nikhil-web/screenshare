import pymysql
import warnings

#database connection

connection = pymysql.connect(host="localhost",user="root",passwd="",database="Lab")

cursor = connection.cursor()

Attendance = """CREATE TABLE IF NOT EXISTS Attendance(ID INT(20) PRIMARY KEY AUTO_INCREMENT, NAME CHAR(20) NOT NULL, ROLL CHAR(15))"""
warnings.filterwarnings('ignore')

cursor.execute(Attendance)

connection.close()