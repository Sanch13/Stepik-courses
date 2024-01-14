from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    birth_data = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
