from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Updated to ForeignKey
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} | {self.author}"
    
    def get_absolute_url(self):
        return reverse('home')
