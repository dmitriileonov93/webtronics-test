from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''Класс для представления пользователя.'''

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        '''Строковое представление объекта.'''
        return self.username
