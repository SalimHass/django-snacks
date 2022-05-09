from pydoc import describe
from django.db import models

# Create your models here.
class Thing(models.Model):
    name= models.CharField(max_length=255)
    description =models.TimeField()

    def __str__(self):
        return self.name

