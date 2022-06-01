from django.contrib.auth.models import AbstractUser
from django.db import models

from .utils import get_more_info, verify_email


class User(AbstractUser):
    '''Класс для представления пользователя.'''
    is_email_verified = models.BooleanField(
        'Проверенная ли почта', default=False
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        '''Строковое представление объекта.'''
        return self.username

    def save(self, *args, **kwargs):
        '''
        При сохранении добавляется доп информация.
        '''
        if self.email:
            data = get_more_info(self.email)
            if data is not None:
                self.first_name = data['name']['givenName']
                self.last_name = data['name']['familyName']
            # email_verify_data = verify_email(self.email)
            # if email_verify_data['status'] == 'valid':
            #     self.is_email_verified = True
        super().save(*args, **kwargs)
