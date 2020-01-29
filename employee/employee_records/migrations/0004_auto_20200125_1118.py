# Generated by Django 2.2.9 on 2020-01-25 11:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_records', '0003_auto_20200124_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=40, validators=[django.core.validators.RegexValidator('^\\w+([\\.-]?\\w+)*@\\w+([\\.-]?\\w+)*(\\.\\w{2,3})+$')]),
        ),
    ]
