from django.urls import include, path

from questions.views import (QuizListView, StudentInterestsView, TakenQuizListView,
 take_quiz, TeacherQuizListView, home, QuizUpdateView, QuizDeleteView, QuizResultsView,
 question_add, question_change, QuestionDeleteView, QuizCreateView)

urlpatterns = [
    path('', home, name='home'),

    path('students/', include(([
        path('', QuizListView.as_view(), name='quiz_list'),
        path('interests/', StudentInterestsView.as_view(), name='student_interests'),
        path('taken/', TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/',take_quiz, name='take_quiz'),
    ], 'questions'), namespace='students')),

    path('teachers/', include(([
        path('', TeacherQuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', QuestionDeleteView.as_view(), name='question_delete'),
    ], 'questions'), namespace='teachers')),
]
