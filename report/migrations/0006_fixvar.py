# Generated by Django 3.2.25 on 2025-02-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_auto_20250225_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixvar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('param_2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('param_3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('param_4', models.DecimalField(decimal_places=2, max_digits=10)),
                ('param_5', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
