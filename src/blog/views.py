from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def index(request):
    context = {}
    if request.method == 'GET':
        try:
            latest_post = Post.objects.latest('date_pub')
            posts = Post.objects.all()[:10]
            context['latest_post'] = latest_post
            context['posts'] = posts
        except ValueError:
            print("lol")
    return render(request, 'index.html', context)


def add_post(request):
    context = {}
    if request.method == 'GET':
        context = {
            'form': PostForm
        }
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'add_post.html', context)
