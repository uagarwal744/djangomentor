from django.db import models

class MyProfile(models.Model):
    user = models.OneToOneField("auth.User")
    date_of_birth = models.DateField()
    bio = models.TextField()

