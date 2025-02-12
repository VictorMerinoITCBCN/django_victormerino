from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.last_name}"