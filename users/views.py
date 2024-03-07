from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'registration/home.html'
class CustomUserRegistrationView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page after registration
        return render(request, 'registration/register.html', {'form': form})

class CustomUserLoginView(View):
    def get(self, request):
        form = CustomUserLoginForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        return render(request, 'registration/login.html', {'form': form})

class CustomUserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')  # Redirect to home page after logout
