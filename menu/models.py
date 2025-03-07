from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.URLField(blank=True, null=True) 
    chef = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name