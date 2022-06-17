from django.db import models
from pessoa.models import Person

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    available = models.BooleanField(default=False)
    responsible = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name