from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country,on_delete=models.CASCADE, blank=True, null=True,default=None)
    def __str__(self) -> str:
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    star = models.SmallIntegerField()
    image = models.ImageField(upload_to='hotel')
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True,default=None)
    def __str__(self) -> str:
        return self.name

class PartnerShipBrands(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='PartnerBrand')

    def __str__(self) -> str:
        return self.name