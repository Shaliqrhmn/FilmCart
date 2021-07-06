from django.db import models


# Create your models here.
class FilmDetail(models.Model):
    film_name = models.CharField(max_length=250)
    film_desc = models.TextField()
    film_year = models.IntegerField()
    film_icon = models.ImageField()

    def __str__(self):
        return self.film_name
