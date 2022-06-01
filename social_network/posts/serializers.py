from rest_framework import serializers

from .models import Post, PostInLiked


class PostSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для постов.
    '''
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'title',
            'text',
            'author',
        )
