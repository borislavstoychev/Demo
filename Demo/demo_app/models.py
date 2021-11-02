from django.db import models

# Create your models here.


class Demo(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    image = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
