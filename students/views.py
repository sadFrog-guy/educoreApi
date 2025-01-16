from django.http import HttpResponse
from rest_framework import viewsets

from students.models import Student
from students.serializers import StudentSerializer


def index(request):
    return HttpResponse("STUDENTS")

class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer