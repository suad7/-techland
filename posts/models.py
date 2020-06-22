from django.db import models
from pyuploadcare.dj.models import ImageField
from authentication.models import User


class Post(models.Model):
    image = ImageField(blank=True, manual_crop='')
    title= models.CharField(max_length=30)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author=models.ForeignKey('authentication.User', on_delete=models.CASCADE)


class Category(models.Model):
     name= models.CharField(max_length=30)



class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField() 
    created = models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True,on_delete=models.CASCADE)


    def  __str__(self):
        return str(self.content)

    
    def children(self):
        return Comment.objects.filter(parent=self)

    

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True