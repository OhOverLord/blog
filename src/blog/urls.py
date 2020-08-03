from django.urls import path
from .views import index, add_post

urlpatterns = [
    path('', index, name='index'),
    path('add_post/', add_post, name='add_post')
]