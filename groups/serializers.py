from rest_framework import serializers
from .models import Group
from groupMemberships.models import GroupMembership

class GroupSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()
    
    class Meta:
        model = Group
        fields = ['name', 'start_date', 'end_date', 'status', 'status_display', 'id', 'members']

    def get_members(self, obj):
        memberships = GroupMembership.objects.filter(group=obj)
        members = [{
            'id': membership.student.id,
            'first_name': membership.student.user.first_name,
            'last_name': membership.student.user.last_name,
            'status': membership.status,
            'enrolled_date': membership.enrolled_date,
            'completion_date': membership.completion_date
        } for membership in memberships]
        return members
    
    def get_status_display(self, obj):
        status_dict = dict(Group.STATUS_CHOICES)
        return status_dict.get(obj.status)