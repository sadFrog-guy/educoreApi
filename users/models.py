from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.models import BaseModel

class CustomUser(AbstractUser):
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE, blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ROLE_CHOICES = [
        ('superadmin', 'Super admin'),
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True,)

    def mark_inactive(self):
        self.is_active = False
        self.save()

    def mark_active(self):
        self.is_active = True
        self.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"