from users.models import User
import csv
import time

csvFile = open("UserInfo.csv", "r")
r = csv.reader(csvFile)

print("Start Importing: ", time.asctime( time.localtime(time.time()) ))

i = 0

for row in r:
    i = i + 1
    print("["+str(i)+"]", "Importing...", time.asctime( time.localtime(time.time()) ) )
    user = User.objects.create_user(str(row[1]), password=str(row[1]))
    user.StuNumber = row[1]
    user.StuName = row[2]
    user.StuClass = row[0]
    user.save()

print("End Importing: ", time.asctime( time.localtime(time.time()) ))