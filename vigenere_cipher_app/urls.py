# vigenere_cipher_project/urls.py

from django.urls import path
from .views import vigenere_cipher_view

urlpatterns = [
    path('', vigenere_cipher_view, name='vigenere_cipher'),
]
