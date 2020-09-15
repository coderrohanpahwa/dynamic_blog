from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    contact_number=models.CharField(max_length=10)
    query=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
class Post(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    # author=models.CharField(max_length=50,default="Rohan")
    # id=models.IntegerField(primary_key=True)
    def __str__(self):
        return self.title