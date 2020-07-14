from django.db import models

# Create your models here.
class Album(models.Model):
    artist_name = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    birthday = models.DateField(null=True,blank=True)

    def __str__(self):
      return f"{self.name}"

class User(models.Model):
    music_lover = models.CharField 
    (max_length = 255)(null=True, blank=False)

    def__str__(self):
        return f"{self.user}"
    