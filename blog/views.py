from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog 
import datetime
from django.utils import timezone
def home(request) :
    blogs = Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blogs_detail = get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blogs':blogs_detail})

def new(request):
    return render(request,'new.html')

def create(request) :
    blog = Blog()
    blog.title = request.GET['title']
    blog.writer = request.GET['body']
    blog.date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

