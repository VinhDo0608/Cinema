from django.db import models
from core.models import BaseModel
from django.utils import timezone
from admin_cinema.models import User

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
    actors = models.ManyToManyField(Actor)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Đảm bảo bạn có một model Movie
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title} - {self.created_at}'