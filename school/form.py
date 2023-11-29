#from school .models import CustomUser
#from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#class CustomUserCreationForm(UserCreationForm):

   # class Meta(UserCreationForm.Meta):
    #    model = CustomUser
     #   fields = ['f_name', 'm_name', 'dep', 'hcounty', 'hscounty', 'id_no', 'regno', 'phone', 'username', 'email', 'password1', 'password2']


#class CustomUserChangeForm(UserChangeForm):

 #   class Meta:
  #      model = CustomUser
   #     fields = UserChangeForm.Meta.fields


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
