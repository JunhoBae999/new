from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog 
import datetime
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import BlogPost

def home(request) :
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'home.html',{'blogs':blogs,'posts':posts})

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

def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -> POST
    #2. 빈 페이지를 띄워주는 기능 -> GET
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')

    else :
        form = BlogPost()
        return render(request,'new.html',{'form':form})    

