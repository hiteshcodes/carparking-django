from django.http import request,JsonResponse
from django.shortcuts import render
from rest_framework import serializers
# from rest_framework import serializers
# from rest_framework import authentication 
from .serializers import UserSerializer,ClientSerializer
from .models import Users,Clients
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.customauth import Customauth,Customauthclient
from api import serializers

# Create your views here.

class UserAPI(APIView):
    def get(self ,request,pk=None,format=None):
        user_id = pk
        if user_id is not None:
            user = Users.objects.get(pk=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        user = Users.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data) 

    def post(self ,request,format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg:Data Created'} ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_201_CREATED)

    def  put(self ,request,pk=None,format=None):
        user_id = pk
        user = Users.objects.get(pk=user_id)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Upload'})
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def patch(self ,request,pk,format=None):
        user_id = pk
        user = Users.objects.get(pk=user_id)
        serializer = UserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def delete(self ,request,pk,format=None):
        user_id=pk
        user = Users.objects.get(pk=user_id)
        user.delete()
        return Response({'msg':'Data delete'}) 
        



class ClientAPI(APIView):
    def get(self ,request,pk=None,format=None):
        client_id = pk
        if client_id is not None:
            client = Clients.objects.get(pk=client_id)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        client = Clients.objects.all()
        serializer = ClientSerializer(client,many=True)
        return Response(serializer.data) 

    def post(self ,request,format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg:Data Created'} ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_201_CREATED)

    def  put(self ,request,pk=None,format=None):
        client_id = pk
        client = Clients.objects.get(pk=client_id)
        serializer = ClientSerializer(client,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Upload'})
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def patch(self ,request,pk,format=None):
        client_id = pk
        client = Clients.objects.get(pk=client_id)
        serializer = ClientSerializer(client,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def delete(self ,request,pk,format=None):
        client_id=pk
        client = Clients.objects.get(pk=client_id)
        client.delete()
        return Response({'msg':'Data delete'}) 
