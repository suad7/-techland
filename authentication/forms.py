from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email','username','password1', 'password2')
        

    
