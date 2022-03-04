import database as db

menu= '''
 -----------------------------------
|  1. Add Student Details           |
|  2. Update Student Details        |
|  3. Delete Student Details        |
|  4. List of Students              |
|  5. Individual Student Details    |
 -----------------------------------
  Select Any 1 from Above
'''

choice = int(input(menu))
if choice==1:
    sname = input('Enter Student Name: ')
    scourse = input('Enter Course Enrolled : ')
    ssalary = float(input('Enter Internship salary  of Student : '))
    semail = input('Enter email Id: ')
    smobile = input('Enter Mobile Number :')
    row =db.insert(sname,scourse,ssalary,semail,smobile)
    print(f'{row} row inserted')

elif choice==2:
    sid = int(input('Enter Student Id to be update: '))
    supdate = db.get_single_student(sid)
    if supdate is not None:
        print('Old Students Details are :')
        print(supdate)
        sname = input('Enter Updated Student Name: ')
        scourse = input('Enter Course Enrolled : ')
        ssalary = float(input('Enter Internship Salary  of Student : '))
        semail = input('Enter email Id: ')
        smobile = input('Enter Mobile Number: ')
        row = db.update(sid,sname,scourse,ssalary,semail,smobile)
        print(f'{row} row Updated')
    else:
        print('Entered Student id is Not Found')

elif choice==3:
    sid = int(input('Enter Student Id to be Deleted: '))
    row = db.delete(sid)
    print(f'{row} row Deleted')
elif choice==4:
    row = db.all()
    print(f'{row} Table displayed')
elif choice==5:
    sid = int(input('Enter Stdent Id to Diplay a record: '))
    row = db.get_single_student(sid)
    print(f'{row} Single display')


