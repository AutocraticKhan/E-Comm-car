from django.db import models

# Create your models here.

class BookingManagement(models.Model):
    VAT_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=19.00)
    pay_on_arrival_discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)
    pay_online_discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=15.00)
    super_collision_damage_waiver_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    twu_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    baby_seat_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    booster_seat_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    roof_rack_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return "Booking Management Configuration"
