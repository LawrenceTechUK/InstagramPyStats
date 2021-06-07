import json
import count.py
print ("Lawrence Tech's Instagram User Stats Logger")
print ("Please enter your username you want to log: ")
userToLog = input()
print ("Please enter the hostname of your MySQL Server: ")
hostname = input()
print ("Please enter the username for your MySQL Server: ")
username = input()
print ("Please enter the password for that MySQL Server user: ")
password = input()
print ("Please enter the database of your MySQL Server: ")
database = input()
print ("Please enter the table of your MySQL Server: ")
table = input()
print ("Are your sure you want to overwrite the current config: Y/N")
sure = input()
data = '{"username":"' + userToLog + '", "sql":{"servername":"' + hostname + '", "user":"' + username + '", "pass":"' + password + '", "database":"' + database + '", "table":"' + table + '"}}'
if sure == "Y":
    f = open("settings.json", "w")
    f.write(data)
    f.close()
    excfile('count.py')
