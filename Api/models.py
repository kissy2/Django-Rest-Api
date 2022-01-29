from django.db import models

# Create your models here.

class Note(models.Model):
  title = models.CharField(max_length=50,default="Test")
  detail = models.CharField(max_length=300, blank=True)
  status = models.BooleanField(default=False, blank=True)
  date = models.DateTimeField(auto_now_add=True, blank=True)