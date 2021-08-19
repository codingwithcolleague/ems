from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password = forms.CharField()
    
    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'email' , 'username' , 'password']
        label = {
            'password' : 'Password'
        }
        
        #exclude 
        
        label = {
             'password':'Password'
        }
        
    # def clean_email(self):
    #     if self.cleaned_data["email"].endWith("@techwave.net"):
    #         return self.clean_data["email"]
    #     else:
    #         raise ValidationError("error")
        
    def save(self):
        password = self.cleaned_data.pop("password")
        u = super().save()
        u.set_password(password)
        u.save()
        return u