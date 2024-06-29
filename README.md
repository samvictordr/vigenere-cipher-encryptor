# Vigenère Cipher Encryptor

This Django project implements a Vigenère cipher application, allowing users to encrypt and decrypt text using a keyword. It includes a web interface built with Django, HTML, CSS, and Bootstrap for a responsive and user-friendly experience.

## Features

- **Encryption**: Encrypts plain text using the Vigenère cipher technique.
- **Decryption**: Decrypts cipher text back to the original plain text using the provided keyword.
- **Responsive UI**: Designed using HTML, CSS, and Bootstrap for a visually appealing and adaptive interface.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/vigenere-cipher-django.git
   cd vigenere-cipher-django
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Apply migrations** to set up the database (SQLite by default):

   ```bash
   python manage.py migrate
   ```

4. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

5. **Access the application**:

   Open a web browser and go to `http://127.0.0.1:8000/` to view the Vigenère cipher application.

## Usage

- **Encrypting Text**:
  1. Enter the text you want to encrypt.
  2. Provide a keyword for encryption.
  3. Select the "Encrypt" option and submit the form.
  4. The encrypted text will be displayed on the screen.

- **Decrypting Text**:
  1. Enter the cipher text you want to decrypt.
  2. Use the same keyword that was used for encryption.
  3. Select the "Decrypt" option and submit the form.
  4. The decrypted text will be displayed on the screen.

## Project Structure

- **`vigenere_cipher_app`**: Django application directory.
  - `cipher.py`: Contains encryption and decryption logic.
  - `forms.py`: Defines Django forms for user input.
  - `urls.py`: Routes URLs to views.
  - `views.py`: Handles HTTP requests and renders templates.

- **`vigenere_cipher_project`**: Django project settings and configuration.

- **`templates`**: HTML templates for rendering user interface.

- **`static`**: Contains CSS and other static files.

## License

This project is licensed under Creative Commons Zero, so feel free to clone and edit to your heart's will! - see the [LICENSE](LICENSE) file for details.
