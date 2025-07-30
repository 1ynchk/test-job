from django.urls import path 

from .views import PostsAPIView

urlpatterns = [
    path('', PostsAPIView.as_view())
]