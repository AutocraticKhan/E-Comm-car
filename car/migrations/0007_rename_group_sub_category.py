# Generated by Django 4.2.5 on 2023-09-12 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_category_alter_group_options_remove_group_slug_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='Sub_category',
        ),
    ]
