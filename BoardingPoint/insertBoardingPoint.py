import sys
sys.path.append('../Connection')
from Connect import connect

connection = connect()
cursor = connection.cursor()
cursor.execute('select * from boarding_point')
index= len(cursor.fetchall())
with open('boardingPoint.txt', 'r') as f:
    boarding_point = [line for line in f]
for sql in boarding_point[1:]:
    index +=1
    stringSql = "insert into boarding_point (id ,"+boarding_point[0][1:-1]+" values( "+str(index)+","+sql[1:-1]
    cursor.execute(stringSql)
connection.commit()
