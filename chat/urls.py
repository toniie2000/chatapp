from django.urls import path
from .views import loginPage, chatPage

urlpatterns = [
    path('login/', loginPage, name='login-user'),
    path('chat/', chatPage, name='chatPage'),  # Ensure this name matches
]
