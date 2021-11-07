from rest_framework import authentication
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api.models import Users,Clients

class Customauth(BaseAuthentication):
    def authenticate(self, request):
        username=request.GET.get('username')
        password=request.GET.get('password')
        try:
            user=Users.objects.get(user_fname = username) and Users.objects.get(user_password = password)
        except Users.DoesNotExist:
            raise AuthenticationFailed('No Such User')
        return (user,None)

class Customauthclient(BaseAuthentication):
    def authenticate(self, request):
        username=request.GET.get('username')
        password=request.GET.get('password')
        try:
            client=Clients.objects.get(client_fname = username) and Clients.objects.get(client_password = password)
        except Clients.DoesNotExist:
            raise AuthenticationFailed('No Such User')
        return (client,None)