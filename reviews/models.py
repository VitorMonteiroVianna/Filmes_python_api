from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators= [
            MinValueValidator(1, message= "A quantidade de estrelas deve ser entre 1 e 5"),
            MaxValueValidator(5, message= "A quantidade de estrelas deve ser entre 1 e 5"),
        ]
    )
    comment = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return str(self.movie)