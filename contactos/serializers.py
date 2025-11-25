from rest_framework import serializers
from .models import Contacto
#formato JSON

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Contacto

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)#5
        return user

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:#.
        model = Contacto#s
        fields = '__all__'
class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'#todos los campos del modelo