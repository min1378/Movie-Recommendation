from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


# 유저는 커스텀 유저를 사용(default 유저를 사용하더라도 장고에서는 커스텀 유저를 사용하라고 권장.)
# 디폴트를 사용하더라도 커스텀 유저를 사용하는 번거로움이 있음.
class User(AbstractUser):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=False)
    