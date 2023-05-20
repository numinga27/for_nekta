from rest_framework import serializers


from .models import (Request, RequestMessage,
                      RequestMembership, MessageMembership, User)

class UserSerializer(serializers.ModelSerializer):
    '''Сериализатор для юзера'''
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class RequestSerializer(serializers.ModelSerializer):
    '''Сериазатор для заявок '''
    author = UserSerializer(read_only=True)
    class Meta:
        model = Request
        fields = ['id', 'title', 'description', 'date', 'author', 'status']

class RequestMessageSerializer(serializers.ModelSerializer):
    '''Сериализатор для сообщений'''
    user = UserSerializer(read_only=True)
    class Meta:
        model = RequestMessage
        fields = ['id', 'comment', 'date', 'user', 'request']

class RequestMembershipSerializer(serializers.ModelSerializer):
    '''Сериализатор для тех кто может видеть и создавать заявки'''
    user = UserSerializer(read_only=True)
    request = RequestSerializer(read_only=True)
    class Meta:
        model = RequestMembership
        fields = ['id', 'user', 'request', 'date_joined']

class MessageMembershipSerializer(serializers.ModelSerializer):
    '''Сериализатор для тех кто может видеть и создавать сообщения '''
    user = UserSerializer(read_only=True)
    message = RequestMessageSerializer(read_only=True)
    class Meta:
        model = MessageMembership
        fields = ['id', 'user', 'message', 'date_joined']


