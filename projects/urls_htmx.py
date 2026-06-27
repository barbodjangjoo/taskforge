from django.urls import path
from . import htmx_views

app_name = 'projects_htmx'

urlpatterns = [
    path('', htmx_views.ProjectListView.as_view(), name='home'),
    path('projects/<int:pk>/board/', htmx_views.ProjectBoardView.as_view(), name='project_board'),
    
    path('projects/<int:project_id>/add-column-form/', htmx_views.AddColumnFormView.as_view(), name='add_column_form'),
    path('projects/<int:project_id>/add-task-form/', htmx_views.AddTaskFormView.as_view(), name='add_task_form'),
    
    path('projects/<int:project_id>/add-column/', htmx_views.CreateColumnView.as_view(), name='add_column'),
]