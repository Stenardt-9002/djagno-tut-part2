# Generated by Django 2.0.7 on 2019-05-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190502_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='feature',
            field=models.BooleanField(default=True),
        ),
    ]
