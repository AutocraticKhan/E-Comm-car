from django.contrib import admin

from .models import Category, Sub_category, Vehicle, Number_day,Return_location,Pickup_location


@admin.register(Pickup_location)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'pickup_location')

@admin.register(Return_location)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'return_location')



class NumberDayAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'display_rental_duration')

    def display_rental_duration(self, obj):
        return obj.calculate_rental_duration()

    display_rental_duration.short_description = 'Rental Duration (days)'

admin.site.register(Number_day, NumberDayAdmin)


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
        'period',
        'price_perday',
        'available',
        'bags',
        'passengers',
    )
    list_filter = ('sub_category', 'available','period')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}