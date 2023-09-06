from django.contrib import admin
from .models import  Vehicle, Group
# Register your models here.


@admin.register(Vehicle)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price','available', 'bags', 'passengers']
    list_filter = ['available', 'transmission', 'group', 'passengers']
    list_editable = ['price', 'available']
    # prepopulated_fields = {'slug': ('name',)}

@admin.register(Group)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['group', 'slug']
    list_filter = ['group']
 