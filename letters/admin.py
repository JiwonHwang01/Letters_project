from django.contrib import admin
from letters.models import LetterCase, User, Letter

admin.site.register(LetterCase)
admin.site.register(User)
admin.site.register(Letter)