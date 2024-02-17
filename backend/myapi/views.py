# En views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapi.models import User
from rest_framework import status
from django.contrib.auth import authenticate
from django.db import transaction
from .serializers import UserSerializer
import os
import pandas as pd
import traceback
from .data_utils import getPlotData
from .predict_model import fit_model

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

@api_view(['POST'])
def upload_csv(request, username):
    try:
        user = User.objects.get(username=username)  # Obtén al usuario actual desde la solicitud
        print(user)

        # Verifica si el usuario tiene una carpeta de carga especificada
        # if not user.upload_folder:
        #     print("no existia la carpeta")
        #     # Si no tiene una carpeta de carga, crea una basada en su nombre de usuario
        #     user.upload_folder = user.upload_folder
        #     user.save()

        # Directorio de carga completo
        upload_directory = os.path.join('../users/', user.username)
        print(upload_directory)
        
        # Verifica si el directorio de carga existe, si no, créalo
        if not os.path.exists(upload_directory):
            print('creamos el directorio')
            os.makedirs(upload_directory)
        
        csv_file = request.FILES.get('csv_file')
        print(csv_file)
        if csv_file:
            # Ruta completa del archivo a guardar
            file_path = os.path.join(upload_directory, 'data.csv')

            # Guarda el archivo en la carpeta específica para el usuario
            with open(file_path, 'wb') as destination:
                for chunk in csv_file.chunks():
                    destination.write(chunk)

            fit_model(user.username)

            return Response({'message': 'Archivo CSV procesado exitosamente'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No se proporcionó un archivo CSV'}, status=status.HTTP_400_BAD_REQUEST)

    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        traceback.print_exc()
        return Response({'error': f'Error al procesar el archivo CSV: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def column_chart(request):
    return Response(getPlotData("../data/user_abel/data_house_0.csv"))