# Generated by Django 4.1.3 on 2022-12-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_fabricator_app', '0006_delete_optionalwargear'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionalWargear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon', models.CharField(max_length=100)),
                ('unit', models.ManyToManyField(related_name='optional_wargear', to='list_fabricator_app.unitdatasheet')),
            ],
        ),
    ]
