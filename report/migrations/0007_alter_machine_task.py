# Generated by Django 3.2.25 on 2025-03-06 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0006_fixvar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='task',
            field=models.CharField(choices=[('T', 'Threading'), ('W', 'Welding')], max_length=100),
        ),
    ]
