# Generated by Django 3.2.25 on 2025-03-06 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0008_auto_20250306_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixvar',
            name='param_1',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='fixvar',
            name='param_2',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='fixvar',
            name='param_3',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='fixvar',
            name='param_4',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='fixvar',
            name='param_5',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
