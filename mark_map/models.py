from django.db import models


class Coordinates(models.Model):
    coordinate = models.CharField(max_length=50)

    def __str__(self):
        return self.coordinate
