from django.db import models


class Consumer(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)