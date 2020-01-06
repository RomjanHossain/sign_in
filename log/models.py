from django.db import models

# Create your models here.


class Form(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    bio = models.CharField(max_length=500)
    passion = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
