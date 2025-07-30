from django.contrib import admin
from django.urls import path, include

from posts.urls import urlpatterns as posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts', include(posts), name='posts'),
]
