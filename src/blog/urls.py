from django.urls import path
from .views import index, add_post, post_detail


urlpatterns = [
    path('', index, name='index'),
    path('add_post/', add_post, name='add_post'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
]