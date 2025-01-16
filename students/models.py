from django.contrib.auth.models import AbstractUser
from django.db import models

from users.models import CustomUser
from utils.models import BaseModel

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile', blank=True, null=True)
    notes = models.TextField(blank=True, null=True, verbose_name="Примечания")

    def groups_count(self):
        return self.group_memberships.count()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
