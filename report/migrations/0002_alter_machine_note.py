# Generated by Django 3.2.25 on 2025-02-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='note',
            field=models.TextField(),
        ),
    ]
