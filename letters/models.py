from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import generate_letter_hash_id

class User(AbstractUser):
    lettercase_url = models.CharField(max_length=200, default = None, null=True, blank = True)
    
class LetterCase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    letter_url = models.CharField(max_length=200)
    letter_count = models.IntegerField(default=0)

    def __str__(self):
        return self.letter_url

class Letter(models.Model):
    visitor_id = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    letter_text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.visitor_id
    
    @property
    def hash_id(self):
        """편지 ID를 해시화한 값 반환"""
        return generate_letter_hash_id(self.id)
    
    @classmethod
    def get_by_hash_id(cls, hash_id):
        """해시 ID로 편지 객체 찾기"""
        # 모든 편지를 순회하며 해시 ID가 일치하는 것 찾기
        # 효율성을 위해 캐싱을 추가할 수 있음
        for letter in cls.objects.all():
            if letter.hash_id == hash_id:
                return letter
        return None