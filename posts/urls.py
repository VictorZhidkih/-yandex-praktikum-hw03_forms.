from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path(
        'group/<slug:slug>/', 
        views.group_posts, 
        name='group_list'
    ),
    path('', views.index, name='index'),
    path(
        'profile/<str:username>/',
        views.profile,
        name='profile'
    ),
    # Просмотр записи
    path(
        'posts/<int:post_id>/',
        views.post_detail,
        name='post_detail'
    ),
    path(
        'create_post/',
        views.post_create,
        name='post_create'
    ),
]
