from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(null=False, blank=False)
    featured = models.BooleanField(default=True)
