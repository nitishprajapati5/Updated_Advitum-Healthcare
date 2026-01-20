from django.contrib import admin
from .models.products import Products
from .models.category import Categories
from .models.User_Detail import User_Detail


class admintable(admin.ModelAdmin):
    list_display=['id','name','description','category','price']

class userdetail(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'gmail', 'password', 'confirm_password']
       

admin.site.register(Products,admintable)
admin.site.register(Categories)
admin.site.register(User_Detail,userdetail)