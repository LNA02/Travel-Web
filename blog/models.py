from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

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

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default='Author Name')
    choice = models.CharField(
        max_length = 20,
        choices = MONTH_CHOICES,
        default = '1'
    )
    image = models.TextField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/-Insert_image_here-.svg/480px--Insert_image_here-.svg.png')
    imageBody = models.ImageField(null=True)
    audio = models.FileField(upload_to='media/music', null=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # def __str__(self) :
    #     return  f'Title: {self.title} \nAuthor: {self.author} \nMonth: {self.choice} \nBody: {self.body} '
    
    def get_absolute_url(self):
        return reverse('blog')
    
class Comment(models.Model):
    author = models.CharField(max_length=100, default='Author Name')
    comment = models.TextField(max_length=200)