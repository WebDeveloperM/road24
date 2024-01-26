from django.db import models
from users.models import User
from road.utils.fields import expires_default

# Create your models here.

class Car(models.Model):
    number = models.CharField(max_length=200)
    teck_number = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.number


class Fine(models.Model):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True)
    decision_number = models.CharField(max_length=150)
    violation_date = models.DateTimeField(default = expires_default())
    decision_date = models.DateTimeField(auto_now_add=True)
    violation_clause = models.CharField(max_length=250)
    violation_description = models.TextField()
    violation_address = models.TextField()
    fine_amount = models.IntegerField()
    fine_fast = models.IntegerField()
    fine_image= models.ImageField(null=True,blank=True)
    is_payment = models.BooleanField(default=False)

    
 
 

class Card(models.Model):
    card_number = models.CharField(max_length=200)
    card_date = models.CharField(max_length=200)
    card_holder = models.CharField(max_length=200)
    card_cvc = models.CharField(max_length=200)
    price = models.IntegerField()

    user = models.ForeignKey(User , on_delete = models.CASCADE , null =True , blank=True)

    def __str__(self):
        return self.card_holder