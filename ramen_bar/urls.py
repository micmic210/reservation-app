"""
URL configuration for ramen_bar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from menu import views as menu_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_views.home_view, name='home'),  # Home page
    path('philosophy/', menu_views.philosophy_view, name='philosophy'),  # Philosophy page
    path('contact/', menu_views.contact_view, name='contact'),  # Contact page
    path('thank-you/', menu_views.thank_you_view, name='thank_you'),  # Thank you page
    path('menu/', menu_views.menu_view, name='menu'),  # Menu page
]
