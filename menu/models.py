from django.db import models

# Create your models here.


class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField()
    description = models.TextField()

    

