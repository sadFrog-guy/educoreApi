from django.db import models

from utils.models import BaseModel
from teachers.models import Teacher
from groups.models import Group


class GroupTeacher(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='group_conductings')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_teachers')

    class Meta:
        unique_together = ('teacher', 'group')

    def __str__(self):
        return str(f'{self.teacher}')