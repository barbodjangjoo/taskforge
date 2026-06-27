from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.db import models

from .models import Project


from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db import models

from .models import Project, Board, Column, Task


class ProjectListView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'projects/project_list.html', {'projects': []})

        projects = Project.objects.filter(
            models.Q(owner=request.user) | 
            models.Q(members=request.user)
        ).distinct().order_by('-datetime_created')

        return render(request, 'projects/project_list.html', {'projects': projects})


class ProjectBoardView(View):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return render(request, 'projects/project_list.html', {'projects': []})

        project = get_object_or_404(Project, pk=pk)

        if not (project.owner == request.user or project.members.filter(id=request.user.id).exists()):
            return render(request, 'projects/project_list.html', {'projects': []})

        boards = Board.objects.filter(project=project)
        columns = Column.objects.filter(board__project=project).order_by('position')

        return render(request, 'projects/kanban_board.html', {
            'project': project,
            'boards': boards,
            'columns': columns,
        })
    
class CreateColumnView(View):
    def post(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        name = request.POST.get('name', 'ستون جدید')
        
        
        last_column = Column.objects.filter(board__project=project).order_by('-position').first()
        position = (last_column.position + 1) if last_column else 0

        Column.objects.create(
            board=project.boards.first(),
            name=name,
            position=position
        )
        
        return redirect('projects_htmx:project_board', pk=project_id)