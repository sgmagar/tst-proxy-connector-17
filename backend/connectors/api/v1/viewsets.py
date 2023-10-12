
import requests
import base64
import urllib.parse
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class BaseConnectorViewSet(viewsets.GenericViewSet):
    BASE_URL = None
    AUTH_TYPE = None
    USERNAME = None
    PASSWORD = None
    TOKEN = None
    SECRET = None
    QUERY_NAME = None
    
    def _generate_basic_token(self):
        return base64.b64encode(f"{self.USERNAME}:{self.PASSWORD}".encode("utf-8")).decode("utf-8")

    def _get_authorization_value(self):
        if self.AUTH_TYPE == "basic":
            return f"Basic {self._generate_basic_token()}"
        if self.AUTH_TYPE == "bearer":
            return f"Bearer {self.TOKEN}"
        return ""

    def _get_headers(self):
        return {"Authorization": self._get_authorization_value()}

    def _get_params(self):
        if not self.QUERY_NAME:
            return {}
        return {self.QUERY_NAME: self.SECRET}

    def _api_call(self, url, request_type="get", payload=None, headers=None, params=None):
        payload = payload or {}
        headers = headers or {}
        params = params or {}
        base_url = self.BASE_URL.endswith("/") and self.BASE_URL or f"{self.BASE_URL}/"
        url = urllib.parse.urljoin(base_url, url.lstrip("/"))
        response = requests.request(request_type, url, data=payload, params={**self._get_params(), **params}, headers={**self._get_headers(), **headers})
        try:
            return response.json()
        except Exception:
            return {}

class NewConnector2ViewSet(BaseConnectorViewSet):
    PASSWORD = settings.NEW_CONNECTOR2_PASSWORD
    USERNAME = settings.NEW_CONNECTOR2_USERNAME
    BASE_URL = "https://dsd.sdds/dsddklllggssdffklk/"
    AUTH_TYPE = "basic"
    IDENTIFIER = "NEW_CONNECTOR2"
    
    @action(detail=False, methods=["get"], url_path="ddsddff")
    def ddsddff(self, request, *args, **kwargs):
        params = request.query_params
        payload = request.data
        data = self._api_call("/ddsddff", request_type="get", payload=payload, params=params)
        return Response(data)
    
    @action(detail=False, methods=["get"], url_path="helloman")
    def helloman(self, request, *args, **kwargs):
        params = request.query_params
        payload = request.data
        data = self._api_call("/helloman/", request_type="get", payload=payload, params=params)
        return Response(data)

class NewConnector3ViewSet(BaseConnectorViewSet):
    TOKEN = settings.NEW_CONNECTOR3_TOKEN
    BASE_URL = "https://dsd.sddsds/sddsdgghjkk/"
    AUTH_TYPE = "bearer"
    IDENTIFIER = "NEW_CONNECTOR3"
    
    @action(detail=False, methods=["get"], url_path="dsdssdasssd")
    def dsdssdasssd(self, request, *args, **kwargs):
        params = request.query_params
        payload = request.data
        data = self._api_call("/dsdssdasssd", request_type="get", payload=payload, params=params)
        return Response(data)

class NewConnector4ViewSet(BaseConnectorViewSet):
    SECRET = settings.NEW_CONNECTOR4_SECRET
    QUERY_NAME = "private_key"
    BASE_URL = "https://sdds.sdds/sddsdlf/"
    AUTH_TYPE = "apiKey"
    IDENTIFIER = "NEW_CONNECTOR4"
    
    @action(detail=False, methods=["get"], url_path="ddsdsd")
    def ddsdsd(self, request, *args, **kwargs):
        params = request.query_params
        payload = request.data
        data = self._api_call("/ddsdsd", request_type="get", payload=payload, params=params)
        return Response(data)
 
