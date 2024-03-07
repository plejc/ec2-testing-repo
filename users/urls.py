from django.urls import path
from .views import CustomUserRegistrationView, CustomUserLoginView, CustomUserLogoutView,HomeView

urlpatterns = [
    path('register/', CustomUserRegistrationView.as_view(), name='register'),
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('logout/', CustomUserLogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
]
