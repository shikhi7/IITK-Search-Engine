import sqlite3
import sys
sys.path.insert(0, 'Student_Search')
import st_search as ss

conn = sqlite3.connect('student.db')
c = conn.cursor()
# Create table
table_heads = """CREATE TABLE iitk_students(rollno int primary key, name text, program varchar(100), department varchar(100),hostel varchar(100), email varchar(100), gender varchar(100), bloodGroup varchar(100), country varchar(100),imageUrl varchar(100))"""
#c.execute(table_heads)
roll = 150001
lim = 160000
should_keys = ['Roll No: ','Name: ','Program: ','Department: ','Hostel Info: ',' E-Mail: ',' Gender:',' Blood Group:',' CountryOfOrigin:','image']

def updateTable():
    while roll<lim:
        si = ss.getStudentData(roll)
        print(si['Name: '])
        if 'Program: ' not in si.keys():
            break
        lk={}
        for k in should_keys:
            if k not in si.keys():
                lk[k]=''
            else:
                lk[k]=si[k]
        c.execute("SELECT rollno FROM iitk_students WHERE rollno = ?", (roll,))
        data = c.fetchall()
        if len(data)==0:
            c.execute("INSERT INTO iitk_students VALUES(?,?,?,?,?,?,?,?,?,?)", (int(lk['Roll No: ']),lk['Name: '], lk['Program: '], lk['Department: '], lk['Hostel Info: '], lk[' E-Mail: '], lk[' Gender:'], lk[' Blood Group:'], lk[' CountryOfOrigin:'], lk['image']))
            conn.commit()
        roll+=1


def queryforEmails():
    c.execute("SELECT rollno, name FROM iitk_students WHERE program=='BTech'")
    data = c.fetchall()
    print(data)


queryforEmails()
conn.close()
