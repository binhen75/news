from django.conf import settings
from django.db import models
from django.urls import reverse



# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )   

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})
