from django.db import models


class ToDo(models.Model):
    task = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

