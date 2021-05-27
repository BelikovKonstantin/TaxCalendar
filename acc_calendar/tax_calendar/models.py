from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


class Regulator(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    TYPE_CHOICES = [('report', 'report'), ('payment', 'payment')]
    name = models.CharField(max_length=20)
    description = models.TextField()
    repeatability = models.CharField(max_length=500)
    subject = models.CharField(max_length=500)
    regulator = models.ForeignKey(Regulator, on_delete=models.CASCADE, related_name='events')
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name