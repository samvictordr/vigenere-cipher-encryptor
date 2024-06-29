# vigenere_cipher_app/views.py

from django.shortcuts import render
from .forms import VigenereCipherForm
from .cipher import encrypt, decrypt

def vigenere_cipher_view(request):
    res = None
    form = VigenereCipherForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        word = form.cleaned_data['word']
        action = form.cleaned_data['action']

        if action == 'encrypt':
            res = encrypt(text, word)
        elif action == 'decrypt':
            res = decrypt(text, word)

    context = {
        'form': form,
        'result': res,
    }

    return render(request, 'vigenere_cipher_app/vigenere_cipher.html', context)
