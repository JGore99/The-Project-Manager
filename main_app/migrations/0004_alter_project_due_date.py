# Generated by Django 4.0 on 2021-12-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_date_project_due_date_remove_tasks_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateField(verbose_name='Due date'),
        ),
    ]