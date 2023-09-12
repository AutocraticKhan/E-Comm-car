from django.contrib import admin
from .models import BookingManagement
# Register your models here.

@admin.register(BookingManagement)
class BMSAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'VAT_percentage',
        'pay_on_arrival_discount_percentage',
        'pay_online_discount_percentage',
        'super_collision_damage_waiver_price',
        'twu_price',
        'baby_seat_price',
        'booster_seat_price',
        'roof_rack_price',
    )
