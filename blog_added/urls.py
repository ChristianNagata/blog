"""URLs de 'blog_added'"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_posts/', views.edit_posts, name='edit_posts'),
    path('edit_post/<int:blogpost_id>/', views.edit_post, name='edit_post'),
    path('read_more/<int:blogpost_id>/', views.read_more, name='read_more'),
]
