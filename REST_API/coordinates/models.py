from django.db import models


class Coordinates(models.Model):
  cur_moux = models.IntegerField(default=1)
  cur_mouy = models.IntegerField(default=1)
  las_moux = models.IntegerField(default=100)
  las_mouy = models.IntegerField(default=180)


  # def __str__(self):
  #   return self.las_moux, self.las_mouy, self.cur_moux, self.cur_mouy
