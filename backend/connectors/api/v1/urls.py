
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import NewConnector2ViewSet,NewConnector3ViewSet
router = DefaultRouter()
router.register('newconnector2', NewConnector2ViewSet, basename='newconnector2')
router.register('newconnector3', NewConnector3ViewSet, basename='newconnector3')

urlpatterns = [
    path("connectors/", include(router.urls)),
]
