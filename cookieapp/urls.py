from django.urls import path
from rest_framework import routers

from students.views import StudentViewSet
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
]