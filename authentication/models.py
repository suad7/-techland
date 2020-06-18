from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager
from pyuploadcare.dj.models import ImageField
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=True)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()


    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    bio = models.TextField()
    picture = ImageField(blank=True, manual_crop='')
