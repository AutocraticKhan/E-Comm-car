# Generated by Django 4.2.5 on 2023-09-06 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car_group_car_transmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['group'],
            },
        ),
        migrations.RemoveField(
            model_name='car',
            name='category',
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('A', 'Automatic'), ('M', 'Manual')], default='M', max_length=1),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='car',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_type', to='car.group'),
        ),
    ]
