from django.shortcuts import render

# Importing from models.py
from projects.models import Project

# Created views under here

# ORM query that selects all objects within the project table
def project_index(request):
    
    # Initiates query
    projects = Project.objects.all()
    
    # Defines dictionary context
    context = {
        'projects': projects
    }

    # Context dictionary added as argument to render()
    return render(request, 'project_index.html', context)

# Another ORM query that retrieves project with primary key equal to that in the function argument
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    
    # Defines context dictionary 
    context = {
        'project': project
    }

    # After assigning project to context dictionary above, pass to render()
    return render(request, 'project_detail.html', context)