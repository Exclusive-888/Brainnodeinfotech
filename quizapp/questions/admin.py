from django.contrib import admin
from questions.models import User, Subject, Quiz, Question, Answer, Student, TakenQuiz, StudentAnswer
# Register your models here.
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)
admin.site.register(TakenQuiz)
admin.site.register(StudentAnswer)