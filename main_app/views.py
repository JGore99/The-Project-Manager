from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project, Task
from .forms import TaskForm


class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def projects_index(request):
  projects = Project.objects.filter(user=request.user)
  return render(request, 'projects/index.html', { 'projects': projects })

@login_required
def projects_detail(request, project_id):
  project = Project.objects.get(id=project_id)
  task_form = TaskForm()
  return render(request, 'projects/detail.html', { 'project': project, 'task_form': task_form })

@login_required
def add_task(request, project_id):
  form = TaskForm(request.POST)
  if form.is_valid():
    new_task = form.save(commit=False)
    new_task.project_id = project_id
    new_task.save()
  return redirect('projects_detail', project_id=project_id)

# I know this is wrong. THis is me trying to fumble through it.
# def update_task(request, task_id):
#   model = Task(request.POST)
#   fields = ['details', 'priority']

class ProjectCreate(LoginRequiredMixin, CreateView):
  model = Project
  fields = ['name', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ProjectUpdate(LoginRequiredMixin, UpdateView):
  model = Project
  fields = ['name', 'description']

class ProjectDelete(LoginRequiredMixin, DeleteView):
  model = Project
  success_url = '/projects/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('projects_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)