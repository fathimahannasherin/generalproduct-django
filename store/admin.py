from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # This line tells Django to "auto-fill" the slug based on the product_name
    prepopulated_fields = {'slug': ('product_name',)} 
    
    # Other helpful admin settings
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')

# Make sure you register the model with the Admin class
admin.site.register(Product, ProductAdmin)