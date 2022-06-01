from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для постов.
    '''
    author = serializers.StringRelatedField(read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'title',
            'text',
            'author',
            'is_liked',
        )

    def get_is_liked(self, obj):
        '''
        Метод для отображения в избранном или нет.
        '''
        user = self.context['request'].user
        if user.is_authenticated:
            if obj.liked.filter(user=user).exists():
                return True
            return False
        return None
