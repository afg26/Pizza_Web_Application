from django.shortcuts import render, redirect
from .forms import PizzaForm
from .models import Cart, Pizza
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def Home(request):
    return render(request, 'Home_Page.html')

def MenuPage(request):
    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas
    }
    return render(request, 'Menu_Page.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza_type = form.cleaned_data['pizza_type']
            pizza = Pizza.objects.create(name=f"{pizza_type.title()} Pizza", type=pizza_type)

            user_cart, _ = Cart.objects.get_or_create(user=request.user)
            user_cart.pizzas.add(pizza)

            return redirect('Menu Page')
    else:
        form = PizzaForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

@login_required
def view_cart(request):
    user_cart, _ = Cart.objects.get_or_create(user=request.user)
    pizzas_in_cart = user_cart.pizzas.all()

    cart_details = []
    for pizza in pizzas_in_cart:
        cart_details.append({
            'pizza': pizza,
        })

    context = {
        'cart_details': cart_details,
    }
    return render(request, 'view_cart.html', context)

@login_required
def remove_from_cart(request):
    if request.method == 'POST':
        pizza_id = request.POST.get('pizza_id')
        try:
            pizza = Pizza.objects.get(pk=pizza_id)
            user_cart, _ = Cart.objects.get_or_create(user=request.user)
            user_cart.pizzas.remove(pizza)
        except Pizza.DoesNotExist:
            pass  # Handle the case when the pizza does not exist

    return redirect('View Cart')