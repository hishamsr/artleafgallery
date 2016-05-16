
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from authentication.serializers import UserSerializer, GroupSerializer, SignUpSerializer
from authentication.permissions import IsAuthenticatedOrCreate


from rest_framework import permissions, routers, serializers, viewsets

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SignUp(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permissin_classes = [
        permissions.AllowAny # Or a non users can't register
    ]