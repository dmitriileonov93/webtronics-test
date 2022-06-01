from django.db import models

from users.models import User


class Post(models.Model):
    '''
    Класс для представления обьектов "Пост".
        Содержит заголовок, ключ пользователя, текст поста и дату публикации.
    '''
    title = models.CharField('Заголовок поста', max_length=250)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        '''Строковое представление объекта.'''
        return self.title


class PostInLiked(models.Model):
    '''
    Класс для представления обьектов Понравившихся постов.
        Содержит ключ пользователя и ключ поста.
    '''
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='liked',
        verbose_name='Пользователь'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='liked',
        verbose_name='Статья'
    )

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        unique_together = ['post', 'user']

    def __str__(self):
        '''Строковое представление объекта.'''
        return f'Понравилось {self.user} - {self.post}'
