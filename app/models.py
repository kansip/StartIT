from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    dt = models.DateField(auto_now_add=True)


class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()
    check=models.BooleanField(default=False)
