from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name