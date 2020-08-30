from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts = [
    {
        'author': 'Shaunak Pal',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '29 August, 2020',
    },
    {
        'author': 'Abhinav',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '29 August, 2020',
    }
]



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})