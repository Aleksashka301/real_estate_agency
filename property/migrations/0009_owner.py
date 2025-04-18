# Generated by Django 5.2 on 2025-04-04 12:06

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20250404_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('normalized_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='RU', verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(related_name='owners', to='property.flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
