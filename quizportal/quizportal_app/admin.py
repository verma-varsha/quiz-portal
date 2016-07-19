from django.contrib import admin
from models import Quiz, UserProfile, QuestionMC, Choice, QuestionSA, User_QuizMarks
# Register your models here.
admin.site.register(Quiz)
admin.site.register(UserProfile)
admin.site.register(QuestionMC)
admin.site.register(Choice)
admin.site.register(QuestionSA)
admin.site.register(User_QuizMarks)