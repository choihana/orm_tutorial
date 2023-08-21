from django.db import models

# Create your models here.

class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.phone

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null = True, blank=True)

    def __str__(self):
        return self.name

