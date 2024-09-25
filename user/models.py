from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

