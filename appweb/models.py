from django.db import models

# Create your models here.
class Repos(models.Model):
    username = models.CharField(max_length=60)
    repo = models.CharField(max_length=100)
    stars = models.IntegerField()
    colabs = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.repo
