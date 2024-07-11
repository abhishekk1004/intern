from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price')
    search_fields = ('title',)

admin.site.register(Product, ProductAdmin)