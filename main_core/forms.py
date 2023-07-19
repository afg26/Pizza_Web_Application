from django import forms
from .models import Pizza

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['sauce', 'cheese', 'toppings']
        widgets = {
            'toppings': forms.CheckboxSelectMultiple
        }
