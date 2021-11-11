from django.contrib import admin

# Register your models here.
from .models import Product, ProductCategory, Contact

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Contact)
