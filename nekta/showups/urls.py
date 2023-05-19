from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserViewSet, RequestViewSet, RequestMessageViewSet, 
                    RequestMembershipViewSet, MessageMembershipViewSet)


app_name = 'showups'


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'requests', RequestViewSet)
router.register(r'messages', RequestMessageViewSet)
router.register(r'request-memberships', RequestMembershipViewSet)
router.register(r'message-memberships', MessageMembershipViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),]