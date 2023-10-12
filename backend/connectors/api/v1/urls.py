
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import NewConnector2ViewSet,NewConnector3ViewSet,NewConnector4ViewSet
router = DefaultRouter()
router.register('newconnector2', NewConnector2ViewSet, basename='newconnector2')
router.register('newconnector3', NewConnector3ViewSet, basename='newconnector3')
router.register('newconnector4', NewConnector4ViewSet, basename='newconnector4')

urlpatterns = [
    path("connectors/", include(router.urls)),
]
