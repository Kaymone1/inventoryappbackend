# Generated by Django 4.2.7 on 2023-12-13 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nicuinventory', '0002_alter_inventoryitem_criticality_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='updated_by',
            field=models.CharField(default='', max_length=40),
        ),
    ]
