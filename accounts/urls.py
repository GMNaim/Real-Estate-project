from django.urls import path
from .views import register, login, dashboard


urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('dashboard', dashboard, name='dashboard'),

]
