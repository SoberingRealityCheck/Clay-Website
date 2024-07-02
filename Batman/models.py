from django.db import models

# Create your models here.
class Comment(models.Model):
    firstname = models.CharField(max_length=25,null=False)
    lastname = models.CharField(max_length=25,null=False)
    text = models.TextField(max_length=255,null=False)

