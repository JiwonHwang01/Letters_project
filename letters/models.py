from django.db import models

class LetterCase(models.Model):
    user_id = models.CharField(max_length=50)
    letter_url = models.CharField(max_length=200)
    letter_count = models.IntegerField()

    def __str__(self):
        return self.user_id + "'s letter_case"

class User(models.Model):
    user_id = models.CharField(max_length=50)
    user_pw = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    create_date = models.DateTimeField('data published')
    lettercase_id = models.ForeignKey(LetterCase, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id
    
class Letter(models.Model):
    visitor_id = models.CharField(max_length=50)
    visitor_pw = models.CharField(max_length=50)
    letter_text = models.CharField(max_length=255)
    lettercase = models.ForeignKey(LetterCase, on_delete=models.CASCADE)

    def __str__(self):
        return self.visitor_id