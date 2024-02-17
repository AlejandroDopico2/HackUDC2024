from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('upload/<str:username>/', views.upload_csv, name='upload_csv'),
    path('columnChart/', views.column_chart, name='column_chart'),


]