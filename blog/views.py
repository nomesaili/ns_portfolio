from django.shortcuts import render
from .models import Blog #Import blog entry model into views

# Create your views here.
def all_blogs(request):

    blogs = Blog.objects.all() #instantiate project data into variable projects

    return render(request, 'blog/all_blogs.html', {'blog':blogs})

    
     
    