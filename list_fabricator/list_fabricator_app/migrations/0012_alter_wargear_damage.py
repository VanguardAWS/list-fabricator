# Generated by Django 4.1.3 on 2022-12-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_fabricator_app', '0011_unitdatasheet_wargear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wargear',
            name='damage',
            field=models.CharField(max_length=200),
        ),
    ]
