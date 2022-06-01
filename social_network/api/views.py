from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer
from .mixins import PostLikedMixin
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet, PostLikedMixin):
    '''
    Вьюсэт для обработки запросов для "./posts/...".
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        '''
        При создании поста полю author присваивается текущий пользователь.
        '''
        serializer.save(author=self.request.user)
