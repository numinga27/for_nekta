from rest_framework import viewsets, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


from .permessions import IsRequestAuthorOrAdmin
from .models import User, Request, RequestMessage, RequestMembership, MessageMembership
from .serializers import (UserSerializer, RequestSerializer, RequestMessageSerializer, 
                          RequestMembershipSerializer, MessageMembershipSerializer)


class UserViewSet(viewsets.ModelViewSet):
    '''Метод создания пользователей'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class RequestViewSet(viewsets.ModelViewSet):
    '''Метод для заявок'''
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsRequestAuthorOrAdmin]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, pk=None):
        queryset = Request.objects.all()
        request_obj = get_object_or_404(queryset, pk=pk)
        serializer = RequestSerializer(request_obj)
        return Response(serializer.data)
    
    def list(self, request):
        queryset = Request.objects.filter(author=request.user)
        serializer = RequestSerializer(queryset, many=True)
        return Response(serializer.data)
    


class RequestMessageViewSet(viewsets.ModelViewSet):
    '''Метод для сообщений заявок'''
    queryset = RequestMessage.objects.all()
    serializer_class = RequestMessageSerializer
    permission_classes = [IsRequestAuthorOrAdmin]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    
    def list(self, request):
        queryset = RequestMessage.objects.filter(message_request__author=request.user)
        serializer = RequestMessageSerializer(queryset, many=True)
        return Response(serializer.data)

   


class RequestMembershipViewSet(viewsets.ModelViewSet):
    '''Модель для тех кто может видеть заявки '''
    queryset = RequestMembership.objects.all()
    serializer_class = RequestMembershipSerializer
    permission_classes = [IsRequestAuthorOrAdmin]


class MessageMembershipViewSet(viewsets.ModelViewSet):
    '''Метод для тех кто может видеть и оставлять сообщения'''
    queryset = MessageMembership.objects.all()
    serializer_class = MessageMembershipSerializer
    permission_classes = [IsRequestAuthorOrAdmin]



