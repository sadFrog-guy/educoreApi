from django.contrib.auth.models import AbstractUser
from django.db import models

from users.models import CustomUser
from utils.models import BaseModel


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile', blank=True, null=True)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"