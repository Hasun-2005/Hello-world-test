from django.db import models
from django.db import models

class PageVisit(models.Model):
    path = models.TextField(blank=True, null=True)  # Path of the visited page
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically adds the current timestamp on creation

    def __str__(self):
        return f"Visited {self.path} at {self.timestamp}"




# Create your models here.
