# from django.db.models import Sum
from rest_framework import viewsets
# from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    '''
    Вьюсэт для обработки запросов для "./posts/...".
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        '''
        При создании поста полю author присваивается текущий пользователь.
        '''
        serializer.save(author=self.request.user)





