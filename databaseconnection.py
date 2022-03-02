import pymysql as pm
print('Imported Successfully')

con =pm.connect(host='localhost',user='root',password='',database='studentss')
if con !=None:
    print('Connected Successfully!!!!!!!!')

cursor = con.cursor()

SQLQuery = 'select * from sdetails'
cursor.execute(SQLQuery)
data=cursor.fetchall()
for row in data:
    print(row)

con.close()
print('Connection closed')