# Generated by Django 2.2.19 on 2021-05-27 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_calendar', '0002_regulator_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regulator',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
