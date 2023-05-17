from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import include, path

from .views import RequestViewSet, RequestMessageViewSet

app_name = 'showups'

router_v1 = DefaultRouter()
router_v1.register(r'request', RequestViewSet)
router_v1.register(r'request/(?P<request_id>\d+)/messages', RequestMessageViewSet,
                   basename='messages'
                   )


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
