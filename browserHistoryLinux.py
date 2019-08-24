import getpass
import sqlite3
import csv

username = getpass.getuser()
con = sqlite3.connect('/home/' + username + '/.config/google-chrome/Default/History')
c = con.cursor()

c.execute('select * from urls');
results = c.fetchall()

names = [description[0] for description in c.description]
with open('browserHistoryLinux.csv', 'w+', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(names)
    for result in results:
        writer.writerow(result)
        print("File Written")
