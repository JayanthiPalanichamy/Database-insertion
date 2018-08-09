import sys
sys.path.append('../Connection')
from Connect import connect

connection = connect()
cursor = connection.cursor()
cursor.execute('select * from dropping_point')
index= len(cursor.fetchall())
with open('droppingPoint.txt', 'r') as f:
    dropping_point = [line for line in f]
for sql in dropping_point[1:]:
    index +=1
    stringSql = "insert into dropping_point (id ,"+dropping_point[0][1:-1]+" values( "+str(index)+","+sql[1:-1]
    cursor.execute(stringSql)
connection.commit()
