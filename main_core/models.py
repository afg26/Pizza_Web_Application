from django.contrib.auth.models import User
from django.db import models

class Topping(models.Model):
    PEPPERONI = 'pepperoni'
    SAUSAGE = 'sausage'
    CHICKEN = 'chicken'
    PEPPERS = 'peppers'
    TOPPING_CHOICES = [
        (PEPPERONI, 'Pepperoni'),
        (SAUSAGE, 'Sausage'),
        (CHICKEN, 'Chicken'),
        (PEPPERS, 'Peppers'),
    ]
    name = models.CharField(max_length=50, choices=TOPPING_CHOICES)

    def __str__(self):
        return self.name

class Sauce(models.Model):
    MARINARA = 'marinara'
    ALFREDO = 'alfredo'
    RANCH = 'ranch'
    BUFFALO = 'buffalo'
    SAUCE_CHOICES = [
        (MARINARA, 'Marinara'),
        (ALFREDO, 'Alfredo'),
        (RANCH, 'Ranch'),
        (BUFFALO, 'Buffalo'),
    ]
    name = models.CharField(max_length=50, choices=SAUCE_CHOICES)

    def __str__(self):
        return self.name

class Cheese(models.Model):
    MOZZARELLA = 'mozzarella'
    PARMESAN = 'parmesan'
    PROVOLONE = 'provolone'
    CHEESE_CHOICES = [
        (MOZZARELLA, 'Mozzarella'),
        (PARMESAN, 'Parmesan'),
        (PROVOLONE, 'Provolone'),
    ]
    name = models.CharField(max_length=50, choices=CHEESE_CHOICES)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    toppings = models.ManyToManyField(Topping)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField('Pizza', related_name='carts')

    def __str__(self):
        return f"Cart for {self.user}"
