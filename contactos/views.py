from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.contrib.auth.models import User
from .models import Contacto
from .serializers import ContactoSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all().order_by('-fecha_creacion')
    serializer_class = ContactoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]