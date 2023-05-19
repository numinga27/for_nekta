from rest_framework import serializers


from .models import (Request, RequestMessage,
                      RequestMembership, MessageMembership, User)

class UserSerializer(serializers.ModelSerializer):
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
    author = UserSerializer(read_only=True)
    class Meta:
        model = Request
        fields = ['id', 'title', 'description', 'date', 'author', 'status']

class RequestMessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = RequestMessage
        fields = ['id', 'comment', 'date', 'user', 'request']

class RequestMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    request = RequestSerializer(read_only=True)
    class Meta:
        model = RequestMembership
        fields = ['id', 'user', 'request', 'date_joined']

class MessageMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    message = RequestMessageSerializer(read_only=True)
    class Meta:
        model = MessageMembership
        fields = ['id', 'user', 'message', 'date_joined']


class TokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label='Email',
        write_only=True)
    password = serializers.CharField(
        label='Пароль',
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label='Токен',
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                email=email,
                password=password)
            if not user:
                raise serializers.ValidationError(
                    code='authorization'
                )
        else:
            msg = 'Необходимо указать "адрес электронной почты" и "пароль".'
            raise serializers.ValidationError(
                msg,
                code='authorization'
            )
        attrs['user'] = user
        return attrs
    