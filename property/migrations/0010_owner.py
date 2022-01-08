# Generated by Django 2.2.24 on 2022-01-05 09:47

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_fillPurePhoneNumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, db_index=True, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, db_index=True, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца')),
                ('flat', models.ManyToManyField(related_name='flat_owners', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
