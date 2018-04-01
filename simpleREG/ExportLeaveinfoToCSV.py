import csv
import time
from exeats.models import Holiday, LeaveInfo

csvFile = open("LeaveInfo_20180405.csv", "w", newline='')
writer = csv.writer(csvFile)

holiday_list = Holiday.objects.order_by('-id')
holiday = holiday_list[len(holiday_list)-1]

leaveinfo_list = holiday.leaveinfo_set.order_by('-StuNumber_int')
leaveinfo_list = leaveinfo_list[::-1]

fileHeaders = ["班级", "学号", "姓名","离校时间","假期去向","预计返校时间","联系电话","紧急联系人及其联系方式"]
info = [0, 0, "", "", "", "", 0, ""]

# 写入的内容以列表的形式传入函数
writer.writerow(fileHeaders)

t = 0
print("Start Exporting: ", time.asctime( time.localtime(time.time()) ))

for leaveinfo in leaveinfo_list:
    t = t + 1
    print("[" + str(t) + "]", "Exporting...", time.asctime(time.localtime(time.time())))
    info[0] = leaveinfo.StuClass_int
    info[1] = leaveinfo.StuNumber_int
    info[2] = leaveinfo.StuName_text
    if leaveinfo.isLeaving_bool:
        info[3] = leaveinfo.LeaveTime_date
        info[5] = leaveinfo.BackTime_date
    else:
        info[3] = ""
        info[5] = ""
    info[4] = leaveinfo.Destination_text
    info[6] = leaveinfo.StuPhone_bigint
    info[7] = leaveinfo.Contact_text + " " + str(leaveinfo.ContactPhone_bigint)
    writer.writerow(info)

print("End Exporting: ", time.asctime( time.localtime(time.time()) ))
csvFile.close()