from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('projects/', views.projects_index, name='projects_index'),
  path('projects/<int:project_id>/', views.projects_detail, name='projects_detail'),
]