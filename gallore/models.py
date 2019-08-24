from django.db import models
import datetime as dt
# Create your models here.

class Category(models.Model):
    name =  models.CharField(max_length =60)
    def __str__(self):
        return self.name

class Location(models.Model):
    name =  models.CharField(max_length =60)

class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    # category = models.ForeignKey(Category,on_delete = models.DO_NOTHING)
    location = models.ForeignKey(Location,on_delete = models.DO_NOTHING)
    upload_date = models.DateTimeField(auto_now_add=True,blank =True)
    image = models.ImageField(upload_to= 'gallery/',default="image")


