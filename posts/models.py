from django.db import models
from pyuploadcare.dj.models import ImageField


class Post(models.Model):
    image = ImageField(blank=True, manual_crop='')
    title= models.CharField(max_length=30)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Category(models.Model):
     name= models.CharField(max_length=30)
     subscribers = models.IntegerField()



class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment = models.TextField() 
    created = models.DateTimeField(auto_now_add=True)


