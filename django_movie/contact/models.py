from django.db import models
from datetime import date

# Create your models here.
class Contact(models.Model):
    """Email Sign UP"""
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email