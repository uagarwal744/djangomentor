from __future__ import unicode_literals

from django.db import models

from django.db import models

class MyProfile(models.Model):
    user = models.OneToOneField("auth.User")
    date_of_birth = models.DateField()
    bio = models.TextField()

