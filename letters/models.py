from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    password = models.CharField(max_length=100)
    lettercase_url = models.CharField(max_length=200, default = None, null=True)
    


class LetterCase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    letter_url = models.CharField(max_length=200)
    letter_count = models.IntegerField(default=0)

    def __str__(self):
        return self.letter_url

class Letter(models.Model):
    visitor_id = models.CharField(max_length=50)
    visitor_pw = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    letter_text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.visitor_id