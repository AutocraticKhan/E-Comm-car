from django.db import models

class Group(models.Model):
    group = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,blank=True ,unique=True)

    class Meta:
        ordering = ['group']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.group

class Vehicle(models.Model):
    class Transmission(models.TextChoices):
        AUTOMATIC = 'A', 'Automatic'
        MANUAL = 'M', 'Manual'

    group = models.ForeignKey(Group, related_name='car_type', on_delete=models.CASCADE)
    transmission = models.CharField(max_length=1, choices=Transmission.choices, default=Transmission.MANUAL)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='vehicles/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)
    bags = models.IntegerField()
    passengers = models.IntegerField()

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name
