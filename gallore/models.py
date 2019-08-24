from django.db import models
import datetime as dt
# Create your models here.

class Category(models.Model):
    name =  models.CharField(max_length =60)
    def __str__(self):
        return self.name

class Location(models.Model):
    name =  models.CharField(max_length =60)
    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location,on_delete = models.DO_NOTHING)
    upload_date = models.DateTimeField(auto_now_add=True,blank =True)
    image = models.ImageField(upload_to= 'gallery/',default="image")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
    
    # def delete_image(self):
    #     self.save()
    
    # def update_image(self):
    #     self.save()
    
    # def get_image_by_id(id):
    #     self.save()
    
    @classmethod
    def search_image(cls,category):
        searchedImage=cls.objects.filter(name__icontains=category)
        return searchedImage
    
    @classmethod
    def filter_by_location(cls,location):
        location = cls.objects.filter(location=name)
        return location


