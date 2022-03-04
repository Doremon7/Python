import pymysql

con = pymysql.connect(host = 'localhost', user = 'root', password = '', database = 'studentss')

def insert(sname,scourse,ssalary,semail,smobile):
    cursor = con.cursor()        #cursor should be created always in every query.
    SQLQuery = 'insert into sdetails(sname,scourse,ssalary,semail,smobile) values(%s,%s,%s,%s,%s)'   # here %s is a palceholder where user give input
    i = cursor.execute(SQLQuery,(sname,scourse,ssalary,semail,smobile))
    con.commit()    # to make changes in database permanent we use this command
    return i

def update(sid,sname,scourse,ssalary,semail,smobile):
    cursor = con.cursor()       
    SQLQuery = 'update sdetails set sid=%s,sname=%s,scourse=%s,ssalary=%s,semail=%s,smobile=%s'   
    i = cursor.execute(SQLQuery,(sid,sname,scourse,ssalary,semail,smobile))
    con.commit()
    return i

def delete(sid):
    cursor = con.cursor()
    SQLQuery = 'delete from sdetails where sid=%s'
    i = cursor.execute(SQLQuery,(sid))
    con.commit()
    return i

def all():
    cursor = con.cursor()
    SQLQuery = 'select * from sdetails'
    i = cursor.execute(SQLQuery)
    rows = cursor.fetchall()
    return rows

def get_single_student(sid):
    cursor = con.cursor()
    SQLQuery = 'select * from sdetails where sid=%s'
    cursor.execute(SQLQuery,(sid))
    row = cursor.fetchone()
    return row

#to fetch the all data we use fetchall() method of cursor
#to fetch the single data we use fetchone() method of cursor
