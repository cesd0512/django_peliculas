from django.db import models
from django.contrib.auth.models import User
    

class Movie(models.Model):
    name = models.TextField()
    duration = models.FloatField(help_text="in hours")
    type = models.TextField(choices=[
        ('action', 'Action'),
        ('science_fiction', 'Science Fiction'),
        ('comedy', 'Comedy'),
        ('terror', 'Terror'),
        ('drama', 'Drama'),
        ('suspense', 'Suspense'),
        ('romantic', 'Romantic'),
        ])
    producers = models.TextField()
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
