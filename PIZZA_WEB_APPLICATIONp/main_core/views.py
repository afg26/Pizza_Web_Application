from django.shortcuts import render



def Home(request):
    return render(request, 'Home_Page.html')

def MenuPage(request):
    return render(request, 'Menu_Page.html')

def About_Page(request):
    return render(request, 'about.html')




