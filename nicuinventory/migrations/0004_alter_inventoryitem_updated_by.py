# Generated by Django 4.2.7 on 2023-12-13 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nicuinventory', '0003_inventoryitem_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='updated_by',
            field=models.CharField(max_length=40),
        ),
    ]
