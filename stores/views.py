from django.shortcuts import render
from django.http import HttpResponse
from .models.products import Products

from .models.category import Categories

from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models.User_Detail import User_Detail

from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.conf import settings 

import random

from django.core.mail import send_mail

from datetime import date




def first(request):
    return render(request,'home.html')



def home(request):
    return render(request, 'home.html')
    

def product(request):
    products = None
    
    cate=Categories.getcategory()

    catid=request.GET.get('category')
    if catid:
        products=Products.getproducts_category(catid)
    else:
        products=Products.getproducts

    context = {
        'items': products,
        
        'category':cate,
    }
    return render(request, 'product.html', context)

def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')
