from django.db import models
import datetime as dt
# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    tags = models.ManyToManyField(tags)
    category = models.ForeignKey(Category,on_delete = models.DO_NOTHING)
    location = models.ForeignKey(Location,on_delete = models.DO_NOTHING)
    upload_date = models.DateTimeField(auto_now_add=True,blank =True)
    image = models.ImageField(upload_to= 'gallery/',default="image")

class Category(models.Model):
    name =  models.CharField(max_length =60)


class Location(models.Model):
    name =  models.CharField(max_length =60)