from django.urls import path
from .views import home, first, product, contact, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', first, name='first'),
    path('home', home, name='home'),
    path('product', product, name='products'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)