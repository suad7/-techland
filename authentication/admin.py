from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .email import send_welcome_email

from .models import User



class AddUserForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ('email', 'username')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UpdateUserForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()


    class Meta:
        model= User
        fields= (
            'email', 'password', 'username','is_active', 'is_staff','is_student'
        )

    def clean_password(self):
        return self.initial['password']



class UserAdmin(BaseUserAdmin):
    add_form = AddUserForm
    form = UpdateUserForm

    model = User

    list_display = ('email', 'username','is_staff', 'is_active','is_student',)
    list_filter = ('email', 'is_staff', 'is_active','is_student',)
    fieldsets = (
        (None, {'fields': ('email', 'username','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_student')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_student')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User,UserAdmin)