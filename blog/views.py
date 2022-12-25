from django.shortcuts import render, get_object_or_404
from .models import Blog #Import blog entry model into views

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date') #instantiate project data into variable projects
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})


    
     
    