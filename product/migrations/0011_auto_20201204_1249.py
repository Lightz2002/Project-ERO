# Generated by Django 3.1.2 on 2020-12-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20201204_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default='logo.png', null=True, upload_to=''),
        ),
    ]
