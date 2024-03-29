from django.db import models
from uuid import uuid4


class Good(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()


class Token(models.Model):
    rand_token = models.UUIDField(primary_key=True, default=uuid4, editable=False)
