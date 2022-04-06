from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('detail/<str:pk>/', views.project, name='project'),
    path('add-project/', views.createProject, name='add-project'),
    path('edit/<str:pk>/', views.editProject, name='edit'),
    path('delete/<str:pk>/', views.deleteProject, name='delete'),
]
