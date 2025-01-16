from rest_framework import serializers


from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'start_date', 'end_date', 'id']