from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50, null=False)
    bsecode = models.CharField(max_length=10, null=False)

def __str__(self):
    return self.name