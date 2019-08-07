import getpass
import sqlite3
import csv

username = getpass.getuser()
con = sqlite3.connect('C:\\Users\\' + username + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')
c = con.cursor()

c.execute('select * from urls');
results = c.fetchall()

with open('browserHistoryWindows.csv', 'w+', encoding='utf-8') as file:
    names = [description[0] for description in c.description]

    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(names)
    for result in results:
        writer.writerow(result)

    print("File Written")
