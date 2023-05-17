from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .models import Request, RequestMessage
from .permessions import IsOwnerOrReadOnly
from .serializers import RequestSerializer, RequestMessageSerializer

# Create your views here.
class RequestViewSet(viewsets.ModelViewSet):
    '''Метод заявки'''
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class RequestMessageViewSet(viewsets.ModelViewSet):
    ''' Метод для сообщений '''
    serializer_class = RequestMessageSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        request_id = self.kwargs.get('request_id')
        request = get_object_or_404(Request, id=request_id)
        serializer.save(author=self.request.user, requests=request)

    def get_queryset(self):
        request_id = self.kwargs.get("request_id")
        request_i= get_object_or_404(Request, id=request_id)

        return request_i.messages.all()