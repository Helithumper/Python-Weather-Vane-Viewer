from prettytable import PrettyTable
import MySQLdb
import sys


db = MySQLdb.connect(host='45.55.180.111',user='peyton',passwd='password',db='weather');

cur = db.cursor();
limits = 10;
choice = 1;
if len(sys.argv) > 1:
    try:
        if int(sys.argv[1]):
            limits = sys.argv[1];
    except ValueError:
        pass

    choice = 2 if sys.argv[1].lower()=="barometer" else 1;
if len(sys.argv) > 2:
    limits = int(sys.argv[2]);

#WEATHER STATION
if choice == 1:
    cur.execute("select * from weatherdata order by id desc limit " + str(limits));
    print("-----------WEATHER STATION DATA!-----------")
    weatherstationtable = PrettyTable(["ID","Date","Time","Temperature","Windspeed","Sunlight"]);
    #weatherstationtable.set_padding_width(1);
    for row in cur.fetchall():
        weatherstationtable.add_row(row);

    print weatherstationtable;

########################################

#BAROMETER
else:
    cur.execute("select * from barometer order by id desc limit " + str(limits));
    print("\n\n\n")
    print("--------------BAROMETER DATA!--------------")
    barometertable = PrettyTable(["ID","Date","Time","Barometric Pressure"]);
    for row in cur.fetchall():
        barometertable.add_row(row);
    print barometertable;
