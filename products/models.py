from django.db import models
from django.db.models.deletion import CASCADE


class Menu(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'menu'


class Category(models.Model):
    name = models.CharField(max_length = 45)
    menu = models.ForeignKey('Menu', on_delete = models.CASCADE)

    class Meta:
        db_table = 'categories'


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    #nutrition cascade?? protect??
    nutrition = models.OneToOneField('Nutrition', on_delete=CASCADE)  

    class Meta:
        db_table = 'products'


class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    size_ml = models.CharField(max_length=45, blank=True)
    size_full_ounce = models.CharField(max_length=45, blank=True)

    class Meta:
        db_table = 'nutritions'

    
class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    product_id = models.ForeignKey('Product', on_delete = models.CASCADE)
        
    class Meta:
        db_table = 'images'


class Allergy(models.Model):
    name = models.CharField(max_length=45)
    product = models.ManyToManyField(Product)

    class Meta:
        db_table = 'allergy'



