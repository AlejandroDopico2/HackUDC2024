# En serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Extrae el nombre de usuario del campo validado
        username = validated_data.get('username')

        # Asigna el valor de upload_folder al nombre de usuario
        validated_data['upload_folder'] = f'user_{username}'

        # Crea y retorna el nuevo usuario
        return super().create(validated_data)