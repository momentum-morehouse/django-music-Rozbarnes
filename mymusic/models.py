from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length = 255, null=True,blank=True) 
    title = models.CharField(max_length = 255, null=True,blank=True)
    released = models.DateField(null=True,blank=True)
    image_url = models.TextField(null= True, blank=True)

class Detail(models.Model):
  detail = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="detail")
  text = models.TextField(null=True, blank=True)
  date_added = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.title} by {self.artist}"

class Users(models.Model):
   # music_user = models.CharField(max_length=255)(null=True,blank=False)

   # def __str__(self):
        #return f"{self.user}"
    pass