from django.urls import path
from .views import *

urlpatterns = [
    path('', DashboardViews.as_view(), name='dashboard'),
    path('add-question/', AdminAddQuestionView.as_view(), name='admin_add_question'),
    # path('quiz/', UserQuizView.as_view(), name='quiz'),
    # path('quiz/submit/', SubmitQuizView.as_view(), name='submit_quiz'),
    
    path('quiz/', UserQuizView.as_view(), name='quiz'),
    path('quiz/submit/', SubmitQuizView.as_view(), name='submit_quiz'),

]
