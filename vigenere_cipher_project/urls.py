# vigenere_cipher_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vigenere_cipher_app.urls')),
]
