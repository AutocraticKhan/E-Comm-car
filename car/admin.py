from django.contrib import admin
from .models import  Car
# Register your models here.


@admin.register(Car)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price','available', 'bags', 'passengers']
    list_filter = ['available', 'transmission', 'group', 'passengers']
    list_editable = ['price', 'available']
    # prepopulated_fields = {'slug': ('name',)}