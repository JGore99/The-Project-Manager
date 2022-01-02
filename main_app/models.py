from django.db import models
from django.urls import reverse
# from datetime import date
from django.contrib.auth.models import User

PRIORITIES = (
  ('L', 'Low'),
  ('M', 'Medium'),
  ('H', 'High'),
  ('I', 'Immediate')
)

class Project(models.Model):
  name = models.CharField(max_length=100)
  # due_date = models.DateField('Due date')
  description = models.TextField(max_length=300)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.name
    # return self.name, f"{self.get_date_display()} on {self.date}"

def get_absolute_url(self):
    return reverse('projects_detail', kwargs={'project_id': self.id})

class Task(models.Model):
  details = models.TextField(max_length=300)
  # date = models.DateField()
  priority = models.CharField(
    max_length=1,
    choices=PRIORITIES,
    default=PRIORITIES[0][0]
  )

  project = models.ForeignKey(Project, on_delete=models.CASCADE)

  def __str__(self):
    return self.details

  # class Meta:
  #   ordering = ['-date']