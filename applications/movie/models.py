from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Avg

from applications.likes.models import Like
from applications.ratings.models import Rating


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = GenericRelation(Like)
    ratings = GenericRelation(Rating)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_rating(self):
        return Rating.objects.aggregate(Avg('star'))
