from django.urls import path
from .views import home,first,product,contact,about

urlpatterns = [
    path('', first, name='first'),
    path('home', home, name='home'),
  path('product', product, name='products'),
  path('about', about, name='about'),
  path('contact', contact, name='contact'),
]
