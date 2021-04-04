"""Credicxo_Assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt import views as jwtv

from College import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Jwt Token Athentication
    path('api/jwt_token/', jwtv.TokenObtainPairView.as_view()),
    path('api/jwt_token/refresh/', jwtv.TokenRefreshView.as_view()),

    path('api/signup/', views.RegisterView.as_view(), name='auth_register'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    #to set the password go to http://127.0.0.1:8000/api/password_reset/confirm/

    path('api/add_student/', views.AddStudents.as_view()),
    path('api/list_student/', views.ListStudents.as_view()),
    path('api/add_teacher/', views.AddTeachers.as_view()),
    path('api/list_teacher/', views.ListTeachers.as_view()),
]
