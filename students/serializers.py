from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['user.first_name', 'user.last_name', 'user.id', 'groups_count']