from django.contrib import admin
from django.urls import include, path
from Inicio.views import Inicio
from django.contrib.auth import views as auth_views

urlpatterns= [
    path('',Inicio.as_view(),name='Inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'),name='logout')
]
