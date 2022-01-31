from django.urls import path
from main.views import (
    IndexView,
)

urlpatterns = [
    path('', IndexView, name='index'),
]