# Generated by Django 4.2.4 on 2023-12-29 10:37

from django.db import migrations, models
import road.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('road', '0004_alter_fine_violation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fine',
            name='violation_date',
            field=models.DateTimeField(verbose_name=road.utils.fields.expires_default),
        ),
    ]