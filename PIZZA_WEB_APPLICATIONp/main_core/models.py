from django.contrib.auth.models import User
from django.db import models

class Pizza(models.Model):
    PIZZA_CHOICES = [
        ('pepperoni', 'Pepperoni'),
        ('sausage', 'Sausage'),
        ('cheese', 'Cheese'),
        ('veggie', 'Veggie'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=PIZZA_CHOICES, default='pepperoni')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=10.99)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField('Pizza', related_name='carts')

    def __str__(self):
        return f"Cart for {self.user}"



