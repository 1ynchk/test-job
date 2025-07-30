from rest_framework import serializers

from .models import Posts

class PostsSerializers(serializers.ModelSerializer):
    '''Модель для сериализатора'''

    class Meta:
        model = Posts
        fields = '__all__'