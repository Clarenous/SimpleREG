from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    LoginFirstTime = models.BooleanField(default=True)
    StuNumber = models.IntegerField()
    StuName = models.CharField(max_length=50)
    StuClass = models.IntegerField()
    StuQQ = models.IntegerField()

    class Meta(AbstractUser.Meta):
        pass

