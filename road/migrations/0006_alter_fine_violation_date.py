# Generated by Django 4.2.4 on 2023-12-29 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('road', '0005_alter_fine_violation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fine',
            name='violation_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 12, 27, 10, 37, 23, 771512, tzinfo=datetime.timezone.utc)),
        ),
    ]
