from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class chategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class video(models.Model):
    title = models.CharField(max_length=100)
    chategory = models.ForeignKey(chategory,null=True, on_delete= models.CASCADE)
    description = models.TextField()
    url = models.URLField(max_length=500)
    image = models.ImageField(upload_to='static/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):  
        return self.title

class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(video, on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return self.content
