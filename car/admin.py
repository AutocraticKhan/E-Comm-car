from django.contrib import admin

from .models import Category, Group, Vehicle


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'category')
    list_filter = ('category',)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'group',
        'transmission',
        'name',
        'slug',
        'image',
        'description',
        'price',
        'available',
        'bags',
        'passengers',
    )
    list_filter = ('group', 'available')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}