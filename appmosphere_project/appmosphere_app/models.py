from django.db import models

class Profilepage (models.Model):
    username = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    bio = models.CharField(max_length=500)

    def __str__(self):
        return self.username