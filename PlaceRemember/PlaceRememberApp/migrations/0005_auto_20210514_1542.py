# Generated by Django 3.2 on 2021-05-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlaceRememberApp', '0004_auto_20210513_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=25, max_digits=30, null=True, verbose_name='долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=25, max_digits=30, null=True, verbose_name='широта'),
        ),
    ]
