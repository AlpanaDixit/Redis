from django.db import models

class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    review = models.TextField()
    ratings = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name