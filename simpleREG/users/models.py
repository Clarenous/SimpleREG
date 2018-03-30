from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    LoginFirstTime = models.BooleanField(default=True)
    StuNumber = models.IntegerField(blank=True, null=True)
    StuName = models.CharField(max_length=50, blank=True, null=True)
    StuClass = models.IntegerField(blank=True, null=True)
    StuQQ = models.IntegerField(blank=True, null=True)

    class Meta(AbstractUser.Meta):
        pass

