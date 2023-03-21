from django.db import models

# Create your models here.
class producttMainModel(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    unique_id = models.IntegerField()
    price = models.IntegerField()

class productImageModel(models.Model):
    product = models.ForeignKey(producttMainModel,on_delete=models.CASCADE)
    image = models.ImageField()