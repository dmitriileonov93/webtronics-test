from djoser.serializers import UserCreateSerializer


class UserRegistrationSerializer(UserCreateSerializer):
    '''
    Сериализатор для создания пользователя.
    '''
    class Meta(UserCreateSerializer.Meta):
        fields = ('username', 'password', 'email')
