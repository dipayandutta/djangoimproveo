from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio  = models.TextField()
    profile_picture = models.ImageField(blank=True)
    website = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # String method to return the object 
    def __str__(self):
        return "{0} - {1}".format(self.user.first_name,self.user.last_name)