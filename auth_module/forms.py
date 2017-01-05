from django import forms
from django.contrib.auth.models import User
from auth_module.models import *

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']
        
        
class UserInfoForm(forms.ModelForm):
    
    
    class Meta:
        model = Profile
        exclude = ['birth_date','user']
#         fields = ['location','bio']
        
        
        

        