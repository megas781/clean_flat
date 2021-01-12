from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#нужно еще создать и импортировать форму
from django.urls import reverse_lazy, reverse
#from django.contrib import messages

#для наследования классам
from django.contrib.auth.views import LoginView, LogoutView
# нужно для создания пользователя (при реги страции)
from django.contrib.auth.forms import User
from .forms import CustomAuthUserForm, CustomRegisterUserForm


#Мутим страницу авторизации через классы
class CustomLoginView (LoginView):
    template_name = 'login/login.html'
    form_class = CustomAuthUserForm
    success_url = reverse_lazy('')
    # template_name = 'login/register.html'
    # form_class = CustomRegisterUserForm
    # success_url = reverse_lazy('edit-page')
    # success_msg = 'Регистрация прошла успешно'

class CustomRegisterView(CreateView):
    template_name = 'login/register.html'
    form_class = CustomRegisterUserForm
    success_url = '/'
    success_msg = 'Регистрация прошла успешно'