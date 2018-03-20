from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    LoginFirstTime = models.BooleanField(default=True)
    StuNumber = models.IntegerField(blank=True)
    StuName = models.CharField(max_length=50, blank=True)
    StuClass = models.IntegerField(blank=True)
    StuQQ = models.IntegerField(blank=True)

    class Meta(AbstractUser.Meta):
        pass

