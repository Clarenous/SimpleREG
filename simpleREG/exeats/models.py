from django.db import models


class Holiday(models.Model):
    HolidayName = models.CharField(max_length=50, default="blank")
    HolidayStartDate = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    HolidayEndDate = models.DateField(auto_now=False, auto_now_add=False, default=0, blank=True)
    HolidayDisabled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' : ' + self.HolidayName + ' ' + str(self.HolidayStartDate) + ' ' + str(self.HolidayEndDate)


class LeaveInfo(models.Model):
    holiday = models.ForeignKey(Holiday, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    # Information we need as followed:
    StuClass_int = models.IntegerField(blank=True, null=True)
    StuNumber_int = models.IntegerField(blank=True, null=True)
    StuName_text = models.CharField(max_length=50, blank=True, null=True)
    isLeaving_bool = models.BooleanField(default=True)
    LeaveTime_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    Destination_text = models.CharField(max_length=50, null=True)
    BackTime_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    StuPhone_bigint = models.BigIntegerField(null=True)
    Contact_text = models.CharField(max_length=50, null=True)
    ContactPhone_bigint = models.BigIntegerField(null=True)

    def __str__(self):
        return str(self.id) + ' : ' + self.StuName_text + ' ' + str(self.StuNumber_int)