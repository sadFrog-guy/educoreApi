from django.http import HttpResponse
from rest_framework import viewsets

from students.models import Student
from students.serializers import StudentSerializer
from users.models import CustomUser
from users.serializers import CustomUserSerializer


class UsersViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer