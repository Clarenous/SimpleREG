from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    LoginFirstTime = models.BooleanField(default=True)
    StuNumber = models.IntegerField(default=0)
    StuName = models.CharField(max_length=50, default="blank")
    StuClass = models.IntegerField(default=0)
    StuQQ = models.IntegerField(default=0)

    class Meta(AbstractUser.Meta):
        pass

