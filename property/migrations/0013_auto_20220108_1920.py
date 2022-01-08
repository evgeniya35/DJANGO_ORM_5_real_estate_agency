# Generated by Django 2.2.24 on 2022-01-08 16:20

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_fillFlat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='owner',
            options={'verbose_name': 'Владелец', 'verbose_name_plural': 'Владельцы'},
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]
