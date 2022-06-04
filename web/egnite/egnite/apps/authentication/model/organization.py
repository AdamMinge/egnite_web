from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
