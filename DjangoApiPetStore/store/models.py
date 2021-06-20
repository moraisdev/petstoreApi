from django.db import models
from pets.models import Pet

# Create your models here.
class Order(models.Model):
    quantity = models.IntegerField('quantity')
    status = models.CharField('status', max_length=255)
    complete = models.BooleanField('complete', default=False)
    shipDate = models.DateTimeField('shipDate')
    petId = models.ForeignKey(Pet, verbose_name='pet', on_delete=models.CASCADE)

    class Meta:
        db_table = 'store_order'