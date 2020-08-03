from django.shortcuts import render, redirect
from .forms import PostForm


def index(request):
    context = {}
    if request.method == 'GET':
        context = {
            'form': PostForm
        }
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
