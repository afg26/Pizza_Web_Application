from django import forms
from .models import Pizza

class PizzaForm(forms.Form):
    pizza_choices = [
        ('pepperoni', 'Pepperoni'),
        ('sausage', 'Sausage'),
        ('cheese', 'Cheese'),
        ('veggie', 'Veggie'),
    ]
    pizza_type = forms.ChoiceField(choices=pizza_choices)