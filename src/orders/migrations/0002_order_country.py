# Generated by Django 3.1.5 on 2021-01-06 04:04

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(default='India', max_length=2),
            preserve_default=False,
        ),
    ]
