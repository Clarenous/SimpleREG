from django.db import models


class Holiday(models.Model):
    HolidayName = models.CharField(max_length=50, default="blank")
    HolidayStartDate = models.DateField(auto_now=False, auto_now_add=False, default=0)
    HolidayEndDate = models.DateField(auto_now=False, auto_now_add=False, default=0)

    def __str__(self):
        return str(self.id) + ' : ' + self.HolidayName + ' ' + str(self.HolidayStartDate) + ' ' + str(self.HolidayEndDate)


class LeaveInfo(models.Model):
    holiday = models.ForeignKey(Holiday, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    # Information we need as followed:
    StuClass_int = models.IntegerField(default=0)
    StuNumber_int = models.IntegerField(default=0)
    StuName_text = models.CharField(max_length=50, default="blank")
    LeaveTime_date = models.DateField(auto_now=False, auto_now_add=False)
    Destination_text = models.CharField(max_length=50, default="留校")
    BackTime_date = models.DateField(auto_now=False, auto_now_add=False)
    StuPhone_bigint = models.BigIntegerField(default=0)
    Contact_text = models.CharField(max_length=50, default="blank")
    ContactPhone_bigint = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.id) + ' : ' + self.StuName_text + ' ' + str(self.StuNumber_int)