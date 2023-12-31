from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=10)
    class Meta:
        ordering = ['category']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category


class Sub_category(models.Model):
    sub_category = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category, related_name='car_category', on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        ordering = ['sub_category']
        verbose_name = 'sub_category'
        verbose_name_plural = 'sub_category'

    def __str__(self):
        return self.group

class Pickup_location(models.Model):
    pickup_location = models.CharField(max_length=200,blank=True)
    class Meta:
        ordering = ['pickup_location']
        verbose_name = 'pickup_location'
        verbose_name_plural = 'pickup_locations'

    def __str__(self):
        return self.pickup_location

class Number_day(models.Model):
    pickup_datetime = models.DateTimeField()
    return_datetime = models.DateTimeField()

    def __str__(self):
        return f"Reservation from {self.pickup_datetime} to {self.return_datetime}"

    def calculate_rental_duration(self):
        """
        Calculate the number of days between pickup and return.
        """
        days = (self.return_datetime - self.pickup_datetime).days
        if self.pickup_datetime and self.return_datetime:
            return days
        else:
            return 0



    def __str__(self):
        return f"Reservation at {self.pickup_datetime}"

class Return_location(models.Model):
    return_location = models.CharField(max_length=200,blank=True)
    class Meta:
        ordering = ['return_location']
        verbose_name = 'return_location'
        verbose_name_plural = 'return_locations'

    def __str__(self):
        return self.return_location


class Vehicle(models.Model):
    class Transmission(models.TextChoices):
        AUTOMATIC = 'A', 'Automatic'
        MANUAL = 'M', 'Manual'

    class Periods(models.TextChoices):
        WINTER = 'WR', 'Winter rates'
        SUMMER = 'SR', 'Summer rates'
        SUMMER_H = 'SHR', 'Summer High rates'

    sub_category = models.ForeignKey(Sub_category, related_name='car_type', on_delete=models.CASCADE, null=True, blank=True)
    transmission = models.CharField(max_length=1, choices=Transmission.choices, default=Transmission.MANUAL, blank=True)
    name = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='vehicles/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    period = models.CharField(max_length=3, choices=Periods.choices, blank=True)
    price_perday = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)
    bags = models.IntegerField(blank=True)
    passengers = models.IntegerField(blank=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name
        #lsdf