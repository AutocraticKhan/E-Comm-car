# Generated by Django 4.2.5 on 2023-09-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0011_pickup_datetime_pickup_location_return_datetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number_day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_datetime', models.DateTimeField()),
                ('return_datetime', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Pickup_datetime',
        ),
        migrations.DeleteModel(
            name='Return_datetime',
        ),
    ]
