from os import stat
from django.urls import path

from main.views import (
    IndexView,
    QuizGameView,
)

urlpatterns = [
    path('', IndexView, name='index'),
    path('quiz', QuizGameView, name="quiz_game")
]