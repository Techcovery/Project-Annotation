from django.db import models

class Article(models.Model):
    las_moux = models.IntegerField(default=100)
    las_mouy = models.IntegerField(default=180)
    title = models.CharField(max_length=255, default="some string")

    def __str__(self):
        return self.las_moux, self.las_mouy,self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name
