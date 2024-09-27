from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    skills = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics', default='default-avatar.png')

    def __str__(self):
        return self.user.username
