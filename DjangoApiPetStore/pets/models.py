from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('name', max_length=255)

    class Meta:
        db_table = 'pets_category'

class Tag(models.Model):
    name = models.CharField('name', max_length=255)

    class Meta:
        db_table = 'pets_tag'

class Pet(models.Model):
    name = models.CharField('name', max_length=255)
    status = models.CharField('status', max_length=255)
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, verbose_name='tag', on_delete=models.CASCADE)

    class Meta:
        db_table = 'pets_pet'
