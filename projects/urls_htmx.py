from django.urls import path
from . import htmx_views

app_name = 'projects_htmx'

urlpatterns = [
    path('', htmx_views.ProjectListView.as_view(), name='home'),
    path('projects/<int:pk>/board/', htmx_views.ProjectBoardView.as_view(), name='project_board'),
]