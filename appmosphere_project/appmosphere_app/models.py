from django.db import models

class Profilepage (models.Model):
    username = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    bio = models.CharField(max_length=500)

    def __str__(self):
        return self.username
    

class Comment(models.Model):
    comment = models.CharField(max_length=500)
    like = models.BooleanField(True)
    dislike = models.BooleanField(False)

    def __str__(self):
        return self.comment
    
class Feed(models.Model):
    img = models.CharField(max_length=300)
    comment = models.CharField(max_length=500)
    user = models.CharField(max_length=300)