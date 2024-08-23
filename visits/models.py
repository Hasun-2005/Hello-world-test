from django.db import models
class PageVisit(models.Model):
      #db

      path = models.TextField(blank = True,null = True) #col
      timestap = models.DateTimeField(auto_now_add = True) #col



# Create your models here.
