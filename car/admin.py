from django.contrib import admin

from .models import Category, Sub_category, Vehicle, Return_datetime,Return_location,Pickup_datetime,Pickup_location


@admin.register(Pickup_location)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'pickup_location')

@admin.register(Return_location)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'return_location')

@admin.register(Pickup_datetime)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'pickup_datetime')

@admin.register(Return_datetime)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'return_datetime')

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