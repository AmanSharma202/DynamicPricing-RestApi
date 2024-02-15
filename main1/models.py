
from django.db import models

class Organization(models.Model):
    id = models.CharField(primary_key=True ,max_length=3)
    name = models.CharField(max_length=255)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    typeof = models.CharField(max_length=255)
    description = models.TextField()

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=255)
    base_distance_in_km = models.IntegerField(default=5)
    km_price = models.DecimalField(max_digits=5, decimal_places=2)
    fix_price = models.DecimalField(max_digits=5, decimal_places=2)
