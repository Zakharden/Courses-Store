# Generated by Django 4.0.8 on 2023-03-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='titel',
            field=models.CharField(max_length=255),
        ),
    ]
