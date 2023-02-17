from django.db import models

# Create your models here.

class numbers(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=40)
    phno=models.IntegerField()