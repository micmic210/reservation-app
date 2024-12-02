from django.shortcuts import render
from .models import Menu

def home_view(request):
    return render(request, 'home.html')  

def philosophy_view(request):
    return render(request, 'philosophy.html')

def contact_view(request):
    return render(request, 'contact.html')

def thank_you_view(request):
    return render(request, 'thank_you.html')

def menu_view(request): 
    menu_items = Menu.objects.all()  # Obtain all menu items from menu model 
    return render(request, 'menu/menu.html', {'menu_items': menu_items})
