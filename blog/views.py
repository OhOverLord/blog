from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post


def index(request):
    context = {}
    if request.method == 'GET':
        try:
            latest_post = Post.objects.latest('date_pub')
            posts = Post.objects.all()[1:10]
            context['latest_post'] = latest_post
            context['posts'] = posts
        except ObjectDoesNotExist:
            return redirect('add_post/')
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


def post_detail(request, slug):
    if request.method == 'GET':
        obj = get_object_or_404(Post, slug__iexact=slug)
        context = {
            'post': obj,
        }
        return render(request, 'post_detail.html', context)
