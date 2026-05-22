from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key})
    
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

class LoginView(ObtainAuthToken):
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key})
    