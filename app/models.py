from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        ordering = ['date_joined']

    def __str__(self):
        return [
            self.username,
            self.first_name,
            self.last_name,
            self.date_joined,
        ]

class File(models.Model):
    csv_file = models.FileField(upload_to='')
    xml_file = models.FileField(upload_to='')
