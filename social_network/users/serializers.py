from djoser.serializers import UserCreateSerializer


class UserSerializer(UserCreateSerializer):
    '''
    Сериализатор для создания пользователя.
    '''
    class Meta(UserCreateSerializer.Meta):
        fields = ('username', 'password', 'email',
                  'first_name', 'last_name', 'email_verify_status')
        extra_kwargs = {
            'email': {'required': True},
            'email_verify_status': {'read_only': True}
        }
