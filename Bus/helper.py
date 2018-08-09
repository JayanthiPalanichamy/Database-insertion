import datetime
def doesItArrivesNextDay(sql):
    busList = sql.split(',')
    departure_time = datetime.datetime.strptime(busList[2][2:-1], '%H:%M:%S').time()
    arrival_time = datetime.datetime.strptime(busList[3][2:-1], '%H:%M:%S').time()
    return arrival_time < departure_time 
