import sys
sys.path.append('../Connection')
from Connect import connect

connection = connect()
cursor = connection.cursor()

with open('busAmenities.txt', 'r') as f:
    bus_amenities = [line for line in f]
for sql in bus_amenities[1:]:
    cursor.execute("insert into bus_amenities "+bus_amenities[0][0:-1]+" values"+sql[0:-1])
connection.commit()
