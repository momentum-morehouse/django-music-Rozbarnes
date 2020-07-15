from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length = 255, null=True,blank=True) 
    title = models.CharField(max_length = 255, null=True,blank=True)
    released = models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Users(models.Model):
   # music_user = models.CharField(max_length=255)(null=True,blank=False)

   # def __str__(self):
        #return f"{self.user}"
    pass