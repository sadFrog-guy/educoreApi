from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Group
from groups.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    permission_classes = [AllowAny]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer