from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


CUSTOMER = 'customer'
GAI = 'gai'

TYPES = (
   (CUSTOMER, 'Foydalanuchi'),
   (GAI, 'Gai')
)


class User(AbstractUser):
    phone = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=100, choices =TYPES , null=True,blank=True)
    dispatch_id = models.TextField(null=True, blank=True)

    class Meta(AbstractUser.Meta):
        db_table = 'users_user'
        app_label = 'users'



class SmsCode(models.Model):
    dispatch_id = models.CharField(max_length=8)
    code = models.CharField(max_length=4, null=True, blank=True)

    def str(self):
        return self.code

    class Meta:
        db_table = 'main_sms_code'


        