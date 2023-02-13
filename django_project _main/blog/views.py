from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts= [
#     {
#         'author': 'Harish',
#         'title': 'Blog Post 1'
#         'content': 'First post'
#         'date_posted': 'Augut,27, 2018'
#     }
# ] 

def home(request):
    context = {
        'posts' : Post.objects.all()
    }

    return render(request, 'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':''})
# Create your views here.
