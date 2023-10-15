from django.contrib import admin
from .models import Product, Order
# Register your models here.

admin.site.site_header = "E-commerce site"
admin.site.site_title = "E-commerce title"

admin.site.register(Product)
admin.site.register(Order)
