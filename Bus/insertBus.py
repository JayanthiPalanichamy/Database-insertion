import sys
sys.path.append('../Connection')
from Connect import connect
import datetime
from helper import doesItArrivesNextDay
connection = connect()
cursor = connection.cursor()
cursor.execute('select * from Bus')
index= len(cursor.fetchall())

with open('numberOfDaysRepeat.txt', 'r') as f:
    noOfDays = [line for line in f]
noOfDays = int(noOfDays[0][:-1])

with open('bus.txt', 'r') as f:
    bus = [line for line in f]
for sql in bus[1:]:
    departureDate = datetime.datetime.now()
    for i in range(noOfDays):
        departureDate += datetime.timedelta(days=1)
        if(doesItArrivesNextDay(sql)):
            arrivalDate = departureDate +datetime.timedelta(days=1)
        else :
            arrivalDate = departureDate
        doesItArrivesNextDay(sql)
        index +=1
        sqlString = "Insert into bus"+bus[0][:-2]+" , journey_date, arrival_date, bus_identifier) values "+sql[:-2]+",\'"+str(departureDate)+"\',\'"+str(arrivalDate)+"\',"+str(index)+")"
        cursor.execute(sqlString)
connection.commit()
