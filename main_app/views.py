from django.shortcuts import render
from .models import Project


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def projects_index(request):
  projects = Project.objects.all()
  return render(request, 'projects/index.html', { 'projects': projects })

def projects_detail(request, project_id):
  project = Project.objects.get(id=project_id)
  return render(request, 'projects/detail.html', { 'project': project })