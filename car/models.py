from django.db import models

# Create your models here.
class Category(models.Model):

    class Group(models.TextChoices):
        CAR = 'CR', 'Car/Sedan'
        VAN = 'VN', 'Van'
        SUV = 'SV', 'SUV'
        SPECIAL = 'SP', 'Special'
        SVAGON = 'Sw', 'Station Wagon'

    class Transmission(models.TextChoices):
        AUTOMATIC = 'A', 'Automatic'
        MANUAL = 'M', 'Manual'
       

    group = models.CharField(max_length=2,
                              choices=Group.choices,
                              default=Group.CAR)
    transmission = models.CharField(max_length=1,
                              choices=Transmission.choices,
                              default=Transmission.MANUAL)

    

    class Meta:
        ordering = ['group']
        indexes = [
        models.Index(fields=['group']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

    class Product(models.Model):
        category = models.ForeignKey(Category,related_name='car_type',on_delete=models.CASCADE)
        name = models.CharField(max_length=200)
        slug = models.SlugField(max_length=200,unique=True)
        image = models.ImageField(upload_to='vehicles/%Y/%m/%d',blank=True)
        description = models.TextField(blank=True)
        price = models.DecimalField(max_digits=5,decimal_places=2)
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
