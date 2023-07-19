from django.shortcuts import render, redirect
from .forms import Add_user


# Create your views here.
def sign_up(response):
    if response.method=="POST":
        form = Add_user(response.POST)
        if form.is_valid():
            form.save()
            return redirect('..')
        
    else:
        form = Add_user()
    return render(response, 'sign_up.html', {"form":form})

