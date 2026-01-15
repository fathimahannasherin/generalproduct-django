from django.contrib import admin
from .models import Product,Variation

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # This line tells Django to "auto-fill" the slug based on the product_name
    prepopulated_fields = {'slug': ('product_name',)} 
    
    # Other helpful admin settings
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')

# Make sure you register the model with the Admin class
admin.site.register(Product, ProductAdmin)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

admin.site.register(Variation, VariationAdmin)