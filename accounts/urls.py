from django.urls import path
from .views import register, login, dashboard, logout


urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='register'),
    path('dashboard', dashboard, name='dashboard'),

]
