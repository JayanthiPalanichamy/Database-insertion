import sys
sys.path.append('../Connection')
from Connect import connect

connection = connect()
cursor = connection.cursor()
cursor.execute('select * from city')
index= len(cursor.fetchall())
with open('cities.txt', 'r') as f:
    cities = [line for line in f]
for sql in cities:
    index +=1
    stringSql = "insert into city values( "+str(index)+","+sql[0:-1] + " )"
    cursor.execute(stringSql)
connection.commit()
