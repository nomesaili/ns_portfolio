from django.shortcuts import render
from .models import Project #Import project model into views

def home(request):

    projects = Project.objects.all() #instantiate project data into variable projects

    return render(request,'portfolio/home.html', {'projects':projects})


