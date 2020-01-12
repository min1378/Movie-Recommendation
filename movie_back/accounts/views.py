from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.permissions import AllowAny 
from rest_framework import serializers

# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    # print(request.data)
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Sucess Create ID')


@api_view(['GET'])
def userprofile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(instance=user)
    return Response(serializer.data)


@api_view(['POST'])
def check_password(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if user.check_password(request.data['password']):
        return Response(True)
    else:
        return Response(False)


@api_view(['DELETE'])
def withdraw(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return Response(True)

@api_view(['PUT'])
def change(request, user_id):  
    user = get_object_or_404(User, pk=user_id)
    user.email = request.data['email']
    user.gender = request.data['gender']
    user.set_password(request.data['password'])
    user.save()
    serializer = UserSerializer(instance=user)
    return Response(True)
