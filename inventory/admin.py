from django.contrib import admin
from .models import Product
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50"/>', obj.image)
        return "No Image"

    image_preview.short_description = 'Image'


admin.site.register(Product, ProductAdmin)