from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    
    def create_user(self,email,username,password,commit=True):

        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('User must have a username'))
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save()
        return user

    
    def create_superuser(self, email, username,password):

        user = self.create_user(
            email,
            password=password,
            username=username,
            commit=False,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_student = False
        user.save(using=self._db)
        return user


        