from django.db import models


class User (models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.username
    
class Comment(models.Model):
    comment = models.CharField(max_length=500)
    like = models.BooleanField(True)
    dislike = models.BooleanField(False)

    def __str__(self):
        return self.comment


class Profilepage (models.Model):
    username = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    bio = models.CharField(max_length=500)

    comment = models.ManyToManyField(Comment)

    def __str__(self):
        return self.username
    
    
class Feed(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.CharField(max_length=300)
    comment = models.CharField(max_length=500)

    
    def __str__(self):
        return self.user