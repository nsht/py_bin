# Generated by Django 2.2 on 2019-04-07 20:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190406_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin',
            name='protected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bin',
            name='status',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='bin',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
