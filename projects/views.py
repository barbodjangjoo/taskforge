from django.shortcuts import render
from django.db import models
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(
            models.Q(owner=self.request.user) | 
            models.Q(members__user=self.request.user)
        ).distinct()

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user,
            created_by=self.request.user
        )

    @action(detail=True, methods=['post'])
    def add_member(self, request, pk=None):
        project = self.get_object()
        return Response({"message": "عضو اضافه شد"}, status=status.HTTP_200_OK)