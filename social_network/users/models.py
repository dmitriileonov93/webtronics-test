from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    '''Класс для представления пользователя.'''

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        '''Строковое представление объекта.'''
        return self.username
