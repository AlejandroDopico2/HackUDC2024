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
from .predict_model import fit_model, predict
import threading
from .csv_utils import *
from .pdf_utils import *

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
    print("hola")
    try:
        user = User.objects.get(username=username)  # Obtén al usuario actual desde la solicitud
        print(user)

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
            temporal_file_path = os.path.join(upload_directory, 'temporal_data.csv') 

            # Guarda el archivo en la carpeta específica para el usuario
            with open(temporal_file_path, 'wb') as destination:
                
                for chunk in csv_file.chunks():
                    destination.write(chunk)

            if os.path.exists(file_path):
                # if is_duplicate(file_path, csv_file):
                #     print('Pedritoooo')

                #     os.remove(temporal_file_path)
                #     return Response({'error': 'Este CSV está repetido'}, status=status.HTTP_400_BAD_REQUEST)
                
                concatenate_csv(file_path, temporal_file_path)
            else:
                os.rename(temporal_file_path, file_path)

            # fit_model(user.username)

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

@api_view(['POST'])
def predict_month(request, username):
    try:
        user = User.objects.get(username=username)  # Obtén al usuario actual desde la solicitud
        predict(username)
        return Response({'message': 'Archivo CSV predicho exitosamente'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        traceback.print_exc()
        return Response({'error': f'Error al procesar el archivo CSV: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def upload_pdf(request, username):
    try:
        user = User.objects.get(username=username)  # Obtén al usuario actual desde la solicitud


        upload_directory = os.path.join('../users/', user.username, 'facturas')
        print(upload_directory)
        
        # Verifica si el directorio de carga existe, si no, créalo
        if not os.path.exists(upload_directory):
            print('creamos el directorio')
            os.makedirs(upload_directory)
        
        pdf_file = request.FILES.get('pdf_file')
        print(pdf_file)
        if pdf_file:


            file_name = pdf_file.name  # o genera un nombre único usando uuid
            file_path = os.path.join(upload_directory, file_name)

            with open(file_path, 'wb') as destination:
                for chunk in pdf_file.chunks():
                    destination.write(chunk)


            res = read_pdf(file_path)
            print(res)
            return Response({'message': 'Archivo PDF procesado exitosamente'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No se proporcionó un archivo PDF'}, status=status.HTTP_400_BAD_REQUEST)

    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        traceback.print_exc()
        return Response({'error': f'Error al procesar el archivo PDF: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)