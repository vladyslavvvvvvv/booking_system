from django.db import models

#
class Apartment(models.Model):
    price = models.IntegerField()
    capacity = models.IntegerField()
    location = models.CharField(max_length=490)
    rooms = models.IntegerField()
    available = models.BooleanField()
    owner = models.ForeignKey("LandLord", on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE,null=True)
class LandLord(models.Model):
    name = models.CharField(max_length=494)
    class Meta:
        verbose_name = "owner"
class Customer(models.Model):
    name = models.CharField(max_length=494)