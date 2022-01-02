from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project
from .forms import TaskForm


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def projects_index(request):
  projects = Project.objects.all()
  return render(request, 'projects/index.html', { 'projects': projects })

def projects_detail(request, project_id):
  project = Project.objects.get(id=project_id)
  task_form = TaskForm()
  return render(request, 'projects/detail.html', { 'project': project, 'task_form': task_form })

def add_task(request, project_id):
  form = TaskForm(request.POST)
  if form.is_valid():
    new_task = form.save(commit=False)
    new_task.project_id = project_id
    new_task.save()
  return redirect('projects_detail', project_id=project_id)

class ProjectCreate(CreateView):
  model = Project
  fields = '__all__'
  success_url = '/projects/'

class ProjectUpdate(UpdateView):
  model = Project
  fields = '__all__'

class ProjectDelete(DeleteView):
  model = Project
  success_url = '/projects/'