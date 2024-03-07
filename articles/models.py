from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    title= models.CharField(max_length=100)
    subtitle= models.CharField(max_length=120,default="")
    slug= models.SlugField()
    body= models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(blank=True)
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    objects = models.Manager()
    def __str__(self):
         return str(self.title)

    def getSnippet(self):
        return self.body[:100]+'...'