from rest_framework import viewsets, permissions
from rest_framework.authtoken.views import ObtainAuthToken


from .permessions import IsRequestAuthorOrAdmin
from .models import User, Request, RequestMessage, RequestMembership, MessageMembership
from .serializers import (UserSerializer, RequestSerializer, RequestMessageSerializer, 
                          RequestMembershipSerializer, MessageMembershipSerializer,TokenSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsRequestAuthorOrAdmin]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RequestMessageViewSet(viewsets.ModelViewSet):
    queryset = RequestMessage.objects.all()
    serializer_class = RequestMessageSerializer
    permission_classes = [IsRequestAuthorOrAdmin]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RequestMembershipViewSet(viewsets.ModelViewSet):
    queryset = RequestMembership.objects.all()
    serializer_class = RequestMembershipSerializer
    permission_classes = [IsRequestAuthorOrAdmin]


class MessageMembershipViewSet(viewsets.ModelViewSet):
    queryset = MessageMembership.objects.all()
    serializer_class = MessageMembershipSerializer
    permission_classes = [IsRequestAuthorOrAdmin]


class AuthToken(ObtainAuthToken):
    """Авторизация пользователя."""

    serializer_class = TokenSerializer
    permission_classes = [permissions.AllowAny]

