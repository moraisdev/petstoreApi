from django.db import models
from django.contrib.auth import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    phone = models.CharField('phone', max_length=255)
    userStatus = models.CharField('userStatus', max_length=255)

    class Meta:
        db_table = 'users_user'

