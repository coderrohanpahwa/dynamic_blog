from django import forms
from .models import contact,Post
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.models import User

class Contact(forms.ModelForm):
    class Meta:
        model=contact
        fields=['name','email','contact_number','query']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'contact_number':forms.TextInput(attrs={'class':'form-control'}),
            'query':forms.Textarea(attrs={'class':'form-control'}),

        }
class SignUp(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Enter Password")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Enter Password (again)")
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','desc']
        labels={'title':'Enter Title','desc':'Enter description'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'})
        }