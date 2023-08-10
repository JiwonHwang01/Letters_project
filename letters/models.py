from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    password = models.CharField(max_length=50)
    lettercase_id = models.CharField(max_length=200, default="")

class LetterCase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    letter_url = models.CharField(max_length=200)
    letter_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username + ": " + self.letter_url

class Letter(models.Model):
    visitor_id = models.CharField(max_length=50)
    visitor_pw = models.CharField(max_length=50)
    letter_text = models.CharField(max_length=255)
    lettercase = models.ForeignKey(LetterCase, on_delete=models.CASCADE)

    def __str__(self):
        return self.visitor_id