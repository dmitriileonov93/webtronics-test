from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from posts.models import Post, PostInLiked

from users.utils import verify_email


class PostLikedMixin:
    '''
    Дополнительный эндпоинты для понравившихся постов.
    '''
    @action(
        methods=['POST', 'DELETE'],
        detail=True,
        permission_classes=[permissions.IsAuthenticated, ]
    )
    def like(self, request, pk=None):
        '''
        Эндпоинт ".../<pk>/like/" для создания/удаления Лайка.
        '''
        post = get_object_or_404(Post, pk=pk)
        serializer = self.get_serializer(
            post, context={'request': request}
        )
        if request.method == 'POST':
            if post.liked.filter(
                    user=request.user
            ).exists():
                return Response(
                    {'errors': ['Статья уже в избранном.']},
                    status=status.HTTP_400_BAD_REQUEST)
            PostInLiked.objects.create(
                user=request.user, post=post
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if request.method == 'DELETE':
            if not post.liked.filter(
                    user=request.user
            ).exists():
                return Response(
                    {'errors': ['Вы не добавляли статью с избранное.']},
                    status=status.HTTP_400_BAD_REQUEST)
            post.liked.get(user=request.user).delete()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False,
        permission_classes=[permissions.IsAuthenticated, ],
    )
    def liked(self, request):
        '''
        Эндпоинт ".../liked/" выводит понравившиеся посты.
        '''
        liked_posts = self.get_queryset().filter(
            liked__user=request.user
        )
        serializer = self.get_serializer(liked_posts, many=True)
        return Response(serializer.data)
