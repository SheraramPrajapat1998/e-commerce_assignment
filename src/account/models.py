from django.db import models
from django.conf import settings
from django_adminstats.registry import register_model

class Profile(models.Model):
  user          = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  date_of_birth = models.DateField(blank=True, null=True)
  photo         = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, default='default.jpeg')
  date          = models.DateTimeField(auto_now_add=True) 

  def __str__(self):
    return f"Profile for user {self.user.username}"

register_model(Profile)