# vigenere_cipher_app/cipher.py

def generate_vigenere_table(word):
    word = word.upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table = {}

    for i, letter in enumerate(word):
        shifted_alphabet = alphabet[i:] + alphabet[:i]
        table[letter] = shifted_alphabet

    return table

def encrypt(plaintext, word):
    plaintext = plaintext.upper()
    word = (word.upper() * ((len(plaintext) // len(word)) + 1))[:len(plaintext)]
    table = generate_vigenere_table(word)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted = []

    for p_char, k_char in zip(plaintext, word):
        if p_char in alphabet:
            row = table[k_char]
            index = alphabet.index(p_char)
            encrypted_char = row[index]
            encrypted.append(encrypted_char)
        else:
            encrypted.append(p_char)

    return ''.join(encrypted)

def decrypt(ciphertext, word):
    ciphertext = ciphertext.upper()
    word = (word.upper() * ((len(ciphertext) // len(word)) + 1))[:len(ciphertext)]
    table = generate_vigenere_table(word)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypted = []

    for c_char, k_char in zip(ciphertext, word):
        if c_char in alphabet:
            row = table[k_char]
            index = row.index(c_char)
            decrypted_char = alphabet[index]
            decrypted.append(decrypted_char)
        else:
            decrypted.append(c_char)

    return ''.join(decrypted)
