from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=120)
    alias = models.CharField(max_length=70)
    topMovie = models.CharField(max_length=170)

    def __str__(self):
        return self.name
