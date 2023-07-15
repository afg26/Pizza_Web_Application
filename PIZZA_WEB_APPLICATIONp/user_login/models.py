from django.db import models

# Create your models here.
class Add_data(models.Model):
    email = models.CharField(max_length=400)
    password1 = models.CharField(max_length=100)
    username = models.CharField(max_length=200)
    password2 = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    