from django import forms
import re
from django.contrib.auth.models import User
from blog.models import Post

class RegistrationForm(forms.Form) :
    username = forms.CharField(label='User Name')
    email = forms.CharField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat your password', widget=forms.PasswordInput())

    def clean_username(self) :
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Invalid username")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username 
        raise forms.ValidationError("Username already in use")
    
    def save(self) :
        User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
            )
        
MONTH_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author', 'choice', 'audio', 'body', 'image', 'imageBody')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Blog'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author Name'}),
            'choice': forms.Select(choices=MONTH_CHOICES),
            'audio': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Sound Track'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the Blog'}),
            'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image Link'}),
            'imageBody': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Inside Image'}),
        }
