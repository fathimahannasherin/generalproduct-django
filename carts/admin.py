from django.contrib import admin
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

class CartItemAdmin(admin.ModelAdmin):
    # Ensure there are no leading spaces in 'get_variations'
    list_display = ('product', 'get_variations', 'cart', 'quantity', 'is_active')

    # IMPORTANT: This function MUST be indented 4 spaces (inside the class)
    def get_variations(self, obj):
        # This reaches into the ManyToMany variations field defined in your models.py
        return ", ".join([str(v.variation_value) for v in obj.variations.all()])
    
    get_variations.short_description = 'Variations'

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)