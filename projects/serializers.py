from rest_framework import serializers
from .models import Project, ProjectMember
from accounts.models import CustomUser


class ProjectMemberSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_full_name = serializers.CharField(source='user.full_name', read_only=True)

    class Meta:
        model = ProjectMember
        fields = ['id', 'user', 'user_email', 'user_full_name', 'role']


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    members = ProjectMemberSerializer(many=True, read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'name', 'description', 'owner', 'members',
            'start_date', 'end_date', 'datetime_created', 
            'datetime_modified', 'is_active'
        ]
        read_only_fields = ['owner', 'created_by']