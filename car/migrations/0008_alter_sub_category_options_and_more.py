# Generated by Django 4.2.5 on 2023-09-12 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_rename_group_sub_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sub_category',
            options={'ordering': ['sub_category'], 'verbose_name': 'sub_category', 'verbose_name_plural': 'sub_category'},
        ),
        migrations.RenameField(
            model_name='sub_category',
            old_name='group',
            new_name='sub_category',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='group',
            new_name='sub_category',
        ),
    ]
