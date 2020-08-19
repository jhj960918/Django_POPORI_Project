from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm
from poporimember.forms import LoginForm
from poporimember.views import signin


def index(request):
    blogs = Blog.objects.order_by('-id')
    login_form = LoginForm()
    return render(request,'poporimember/signin.html',{'form':login_form})

def create(request):
    return render(request,'poporiapp/create.html')

def portfolioPage(request):
    blogs = Blog.objects.order_by('-id')
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'poporiapp/portfolioPage.html', {'blogs':blogs,'posts':posts} )

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'poporiapp/detail.html', {'blog': blog_detail})

def postcreate(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.images = request.FILES['images']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/' + str(blog.id))

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('/detail/' + str(blog.id))
    else:
        form = BlogForm(instance = blog)
 
        return render(request,'poporiapp/update.html', {'form':form})

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')

def search(request):
    q= request.GET['q']
    if q:
        blogs = Blog.objects.filter(title__icontains=q).order_by('-id')
    else:
        return redirect('portfolioPage')
    paginator = Paginator(blogs,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'poporiapp/portfolioPage.html', {'blogs':blogs,'posts':posts,'q':q } )
