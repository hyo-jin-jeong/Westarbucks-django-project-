# Generated by Django 3.2.3 on 2021-05-24 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_product_id_image_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nutrition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.nutrition'),
        ),
    ]
