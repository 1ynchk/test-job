from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView 

from .models import Posts
from .serializers import PostsSerializers

class PostsAPIView(APIView):

    def get(self, request):
        '''Возвращает список публикаций'''

        queryset = Posts.objects.all()
        serializer_queryset = PostsSerializers(queryset, many=True).data

        return Response({'data': serializer_queryset})

    def post(self, request):
        '''Добавляет новую публикацию'''

        title = request.data.get('title')
        content = request.data.get('content')

        try:
            post = Posts(title=title, content=content)
            post.save()
        except Exception:
            return Response({'status': 'Ошибка', 'comment': 'Длина поля названия или контента не должна быть равна нулю'}, status=400) 

        serialized_post = PostsSerializers(post).data

        return Response({'data': serialized_post})
