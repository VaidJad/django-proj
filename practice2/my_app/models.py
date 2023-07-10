from django.db import models
from django.contrib.auth.models import User

class UserprofileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional fields

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(blank=True,upload_to='profile_pic_folder')

    def __str__(self):
        return self.user.username