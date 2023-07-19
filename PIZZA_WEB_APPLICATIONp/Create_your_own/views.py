# customize.py
# Facilitates customization of a pizza for transferring to cart


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

import locale

# Available toppings for the pizza with their respective prices
toppings = [
    {"name": "Pepperoni", "price": 1.50},
    {"name": "Mushrooms", "price": 1.00},
    {"name": "Onions", "price": 0.75},
    {"name": "Sausage", "price": 1.25},
    {"name": "Bacon", "price": 1.75},
    {"name": "Extra cheese", "price": 1.50},
    {"name": "Black olives", "price": 1.00},
    {"name": "Green peppers", "price": 0.75}
]

# Available sauce types with their respective prices
sauces = [
    {"name": "Marinara", "price": 1.00},
    {"name": "Barbecue", "price": 1.50},
    {"name": "Alfredo", "price": 2.00}
]

# Available cheese types with their respective prices
cheeses = [
    {"name": "Mozzarella", "price": 1.00},
    {"name": "Cheddar", "price": 1.25},
    {"name": "Parmesan", "price": 1.50}
]

locale.setlocale(locale.LC_ALL, '')  # Set the locale for proper currency formatting


def main_page(request):
    return HttpResponse(loader.get_template('main.html').render())


def customize_pizza(request):
    if request.method == 'POST':
        if 'cheese_pizza' in request.POST:
            # Create a plain cheese pizza with default options
            pizza = {
                'toppings': [],
                'sauce': 'Marinara',
                'cheese': 'Mozzarella'
            }

            # Retrieve the current cart from the session or create an empty cart
            cart = request.session.get('cart', [])

            # Add the plain cheese pizza to the cart
            cart.append(pizza)

            # Save the updated cart in the session
            request.session['cart'] = cart

            return redirect('customize_pizza')

        # Retrieve the selected toppings, sauce type, and cheese type from the form
        selected_toppings = request.POST.getlist('toppings')
        selected_sauce = request.POST.get('sauce')
        selected_cheese = request.POST.get('cheese')

        # Create a pizza dictionary with the selected options
        pizza = {
            'toppings': selected_toppings,
            'sauce': selected_sauce,
            'cheese': selected_cheese
        }

        # Retrieve the current cart from the session or create an empty cart
        cart = request.session.get('cart', [])

        # Add the current pizza to the cart
        cart.append(pizza)

        # Save the updated cart in the session
        request.session['cart'] = cart

        return redirect('customize_pizza')

    # Render the customize page with available toppings, sauce types, and cheese types
    context = {
        'toppings': toppings,
        'sauces': sauces,
        'cheeses': cheeses
    }
    return HttpResponse(loader.get_template('Create_your_own.html').render(context, request))


def view_cart(request):
    # Retrieve the current cart from the session
    cart = request.session.get('cart', [])

    # Calculate the total price of all pizzas in the cart
    total_price = sum(calculate_pizza_price(pizza) for pizza in cart)

    # Render the cart page with cart details and total price
    context = {
        'cart': cart,
        'total_price': format_currency(total_price)
    }
    return HttpResponse(loader.get_template('cart.html').render(context, request))


def place_order(request):
    if request.method == 'POST':
        # Retrieve the current cart from the session
        cart = request.session.get('cart', [])

        if not cart:
            return redirect('view_cart')

        # Clear the cart
        request.session['cart'] = []

        # Process the order (e.g., save to database, send confirmation email, etc.)

        # Render the order confirmation page
        return HttpResponse(loader.get_template('order.html').render())

    # Redirect to the view_cart page for GET requests
    return redirect('view_cart')


def remove_pizza(request, index):
    # Retrieve the current cart from the session
    cart = request.session.get('cart', [])

    # Remove the pizza at the specified index from the cart
    if 0 <= index < len(cart):
        del cart[index]

    # Update the cart in the session
    request.session['cart'] = cart

    return redirect('view_cart')


def calculate_pizza_price(pizza):
    # Calculate the price of a pizza based on selected toppings, sauce type, and cheese type
    price = 0

    if pizza['toppings']:
        price += sum(next(item['price'] for item in toppings if item['name'] == topping)
                     for topping in pizza['toppings'])

    if pizza['sauce']:
        price += next(item['price'] for item in sauces if item['name'] == pizza['sauce'])

    if pizza['cheese']:
        price += next(item['price'] for item in cheeses if item['name'] == pizza['cheese'])

    return price


def format_currency(amount):
    return locale.currency(amount, grouping=True)
