from prettytable import PrettyTable
import MySQLdb


db = MySQLdb.connect(host='45.55.180.111',user='peyton',passwd='password',db='weather');

cur = db.cursor();


#WEATHER STATION
cur.execute("select * from weatherdata order by id desc limit 10");
print("-----------WEATHER STATION DATA!-----------")
weatherstationtable = PrettyTable(["ID","Date","Time","Temperature","Windspeed","Sunlight"]);
#weatherstationtable.set_padding_width(1);
for row in cur.fetchall():
    weatherstationtable.add_row(row);

print weatherstationtable;

########################################

#BAROMETER
cur.execute("select * from barometer order by id desc limit 10");
print("\n\n\n")
print("--------------BAROMETER DATA!--------------")
barometertable = PrettyTable(["ID","Date","Time","Barometric Pressure"]);
for row in cur.fetchall():
    barometertable.add_row(row);
print barometertable;
