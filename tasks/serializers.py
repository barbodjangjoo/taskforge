from rest_framework import serializers
from .models import Board, Column, Task
from accounts.models import CustomUser


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['id', 'name', 'position', 'datetime_created']


class BoardSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'name', 'is_default', 'columns', 'datetime_created']


class TaskSerializer(serializers.ModelSerializer):
    assignee_name = serializers.CharField(source='assignee.full_name', read_only=True)
    column_name = serializers.CharField(source='column.name', read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'column', 'column_name',
            'project', 'assignee', 'assignee_name', 'priority',
            'due_date', 'labels', 'datetime_created', 'datetime_modified'
        ]
        read_only_fields = ['project']   # پروژه رو نمی‌ذاریم کاربر مستقیم تغییر بده