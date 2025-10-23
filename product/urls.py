
from django.contrib import admin
from django.urls import path , register_converter
from .views import *

class UnicodeSlugconverter:
    regex = r'[-\w\u0600-\u06FF]+'

    def to_python(self,value):
        return value
    def to_url(self,value):
        return value
    
register_converter(UnicodeSlugconverter,'uslug')


urlpatterns = [
    path('product',products),
    path('product/category/<uslug:slug>',products ,name="product_cat"),
    path('product/<int:pk>/<uslug:slug>', porduct_detale),
]



