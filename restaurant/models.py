from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Menu(models.Model):
    item=models.CharField(max_length=100)
    price=models.IntegerField()
    
    def __str__(self):
        return self.item

class Booking(models.Model):
    tableno=models.IntegerField()
    people=models.IntegerField()    