from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Project


class ProjectListView(LoginRequiredMixin, View):
    def get(self, request):
        projects = Project.objects.filter(
            models.Q(owner=request.user) | 
            models.Q(members=request.user)
        ).distinct()
        
        return render(request, 'projects/project_list.html', {
            'projects': projects
        })


class ProjectBoardView(LoginRequiredMixin, View):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        if not (project.owner == request.user or project.members.filter(id=request.user.id).exists()):
            return render(request, '403.html', status=403)
        
        return render(request, 'projects/kanban_board.html', {
            'project': project
        })