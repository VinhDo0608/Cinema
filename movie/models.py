from django.db import models
from core.models import BaseModel

# Create your models here.
class Category(BaseModel):
     name = models.CharField(max_length = 100, null=False, blank=False)
     def __str__(self):
        return self.name

class Actor(BaseModel):
     name = models.CharField(max_length = 100, null=False, blank=False)
     def __str__(self):
        return self.name

class Director(BaseModel):
     name = models.CharField(max_length = 100, null=False, blank=False)
     def __str__(self):
        return self.name

class Movie(BaseModel):
    name = models.CharField(max_length = 100, null=False, blank=False)
    image = models.ImageField(max_length = 100, null=False, blank=False)
    duration_time = models.CharField(max_length=10,null=False, blank=False)
    release_day = models.DateField(null=False, blank=False)
    language = models.CharField(max_length=20, null=False, blank=False)
    trailer = models.FileField(verbose_name="Trailer", null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

class Comment():
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.FloatField()