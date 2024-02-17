# En views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapi.models import User
from rest_framework import status
from django.contrib.auth import authenticate
from django.db import transaction
from .serializers import UserSerializer

@api_view(['POST'])
def register_user(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        print("Valido")
        with transaction.atomic():
            serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)    

@api_view(['POST'])
def login_user(request):
    print(request.data)
    username = request.data.get('username', '')
    password = request.data.get('password', '')

    try:
        user = User.objects.get(username=username)
        print(f'El usuario con el nombre de usuario {username} existe.')
        print(user)
    except User.DoesNotExist:
        # El usuario no existemodels
        print(f'El usuario con el nombre de usuario {username} no existe.')
        
    if user.password == password:
        # Iniciar sesión para el usuario autenticado
        # login(request, user)
        return Response({'message': 'Inicio de sesión exitoso.'}, status=status.HTTP_200_OK)
    else:
        # Credenciales inválidas
        return Response({'error': 'Nombre de usuario o contraseña incorrectos.'}, status=status.HTTP_401_UNAUTHORIZED)

    