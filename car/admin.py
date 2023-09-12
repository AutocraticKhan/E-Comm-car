from django.contrib import admin

from .models import Category, Sub_category, Vehicle


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


@admin.register(Sub_category)
class Sub_categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_category', 'category')
    list_filter = ('category',)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sub_category',
        'transmission',
        'name',
        'slug',
        'image',
        'description',
        'price_perday',
        'available',
        'bags',
        'passengers',
    )
    list_filter = ('sub_category', 'available')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}