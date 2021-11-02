from django.db import models

# Create your models here.


class Demo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField()
    date = models.DateField()
    category = models.CharField(max_length=50)
    rating = models.PositiveIntegerField()
    author = models.CharField(max_length=50)
