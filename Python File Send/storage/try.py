import os
import zipfile
import tempfile
import base64
from datetime import datetime
from flask import Flask, request, render_template_string, jsonify, send_file
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Flask app initialization
app = Flask(__name__)

# Load Supabase config from environment variables
SUPABASE_URL = os.getenv("")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET", "default-bucket")

# Flag to check if Supabase is configured
USE_SUPABASE = SUPABASE_URL and SUPABASE_KEY

# ---------------- Encryption Functions ---------------- #

def generate_key_from_password(password: str, salt: bytes = None) -> tuple:
    """Generates a cryptographic key from a password and salt."""
    if salt is None:
        salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt

def encrypt_file(file_path: str, password: str) -> tuple:
    """Encrypts a file's contents using a password."""
    key, salt = generate_key_from_password(password)
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    return encrypted_data, salt

def decrypt_file(encrypted_data: bytes, password: str, salt: bytes) -> bytes:
    """Decrypts data using a password and salt."""
    key, _ = generate_key_from_password(password, salt)
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data)


# ---------------- Storage Functions ---------------- #

def upload_file(file_data: bytes, filename: str) -> str:
    """Uploads a file to Supabase or local storage."""
    unique_filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{filename}"

    if USE_SUPABASE:
        import requests
        headers = {
            'Authorization': f'Bearer {SUPABASE_KEY}',
            'Content-Type': 'application/octet-stream'
        }
        url = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{unique_filename}"
        response = requests.post(url, headers=headers, data=file_data)
        if response.status_code in (200, 201):
            return unique_filename
        raise Exception(f"Supabase upload failed: {response.text}")
    else:
        os.makedirs("storage", exist_ok=True)
        path = os.path.join("storage", unique_filename)
        with open(path, "wb") as f:
            f.write(file_data)
        return unique_filename

def download_file(filename: str) -> bytes:
    """Downloads a file from Supabase or local storage."""
    if USE_SUPABASE:
        import requests
        headers = {'Authorization': f'Bearer {SUPABASE_KEY}'}
        url = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{filename}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
        raise Exception(f"Supabase download failed: {response.text}")
    else:
        path = os.path.join("storage", filename)
        if not os.path.exists(path):
            raise FileNotFoundError("File not found in local storage")
        with open(path, "rb") as f:
            return f.read()


# ---------------- Helper Functions ---------------- #

def create_zip_file(file_path: str, original_filename: str) -> str:
    """Zips a single file."""
    zip_path = tempfile.mktemp(suffix='.zip')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, original_filename)
    return zip_path

def generate_encrypted_code(filename: str, salt: bytes) -> str:
    """Generates a base64-encoded string for file retrieval."""
    combined = f"{filename}:{base64.b64encode(salt).decode()}"
    encoded = base64.urlsafe_b64encode(combined.encode()).decode()
    return encoded

def decode_encrypted_code(code: str) -> tuple:
    """Decodes the retrieval string to get filename and salt."""
    decoded = base64.urlsafe_b64decode(code.encode()).decode()
    filename, salt_b64 = decoded.split(':', 1)
    salt = base64.b64decode(salt_b64.encode())
    return filename, salt


# ---------------- HTML Template ---------------- #
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>File Encryption App</title>
</head>
<body style="font-family: Arial; text-align:center; padding:50px;">
    <h1>🔐 File Encryption App</h1>
    <h3>Mode: {{ 'Supabase' if use_supabase else 'Local Storage' }}</h3>

    <form id="encrypt-form" enctype="multipart/form-data" method="POST" action="/encrypt">
        <h2>Encrypt & Upload</h2>
        <input type="file" name="file" required><br><br>
        <input type="password" name="password" placeholder="Password" required><br><br>
        <button type="submit">Encrypt & Upload</button>
    </form>

    <hr>

    <form id="decrypt-form" method="POST" action="/decrypt">
        <h2>Decrypt & Download</h2>
        <input type="text" name="code" placeholder="Encrypted Code" required><br><br>
        <input type="password" name="password" placeholder="Password" required><br><br>
        <button type="submit">Decrypt & Download</button>
    </form>
</body>
</html>
"""


# ---------------- Routes ---------------- #

@app.route('/')
def index():
    """Serves the main application page."""
    return render_template_string(HTML_TEMPLATE, use_supabase=USE_SUPABASE)


@app.route('/encrypt', methods=['POST'])
def handle_encrypt_file():
    """Endpoint to handle file encryption and upload."""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']
        password = request.form.get('password')

        if not password or file.filename == '':
            return jsonify({'error': 'File and password required'}), 400

        temp_file_path = tempfile.mktemp()
        file.save(temp_file_path)

        try:
            # Zip → Encrypt
            zip_path = create_zip_file(temp_file_path, file.filename)
            encrypted_data, salt = encrypt_file(zip_path, password)

            # Upload (Supabase or Local)
            uploaded_filename = upload_file(encrypted_data, f"encrypted_{file.filename}.zip")

            # Generate retrieval code
            code = generate_encrypted_code(uploaded_filename, salt)
            return jsonify({'code': code, 'message': 'File encrypted & uploaded successfully'})
        finally:
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
            if 'zip_path' in locals() and os.path.exists(zip_path):
                os.unlink(zip_path)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/decrypt', methods=['POST'])
def handle_decrypt_file():
    """Endpoint to handle file decryption and download."""
    try:
        code = request.form.get('code')
        password = request.form.get('password')
        if not code or not password:
            return jsonify({'error': 'Code and password required'}), 400

        filename, salt = decode_encrypted_code(code)

        # Download (Supabase or Local)
        encrypted_data = download_file(filename)

        # Decrypt
        decrypted_data = decrypt_file(encrypted_data, password, salt)

        temp_file_path = tempfile.mktemp(suffix='.zip')
        with open(temp_file_path, 'wb') as f:
            f.write(decrypted_data)

        # Send the decrypted zip file as a download
        return send_file(temp_file_path, as_attachment=True, download_name='decrypted_file.zip')

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ---------------- Run ---------------- #
if __name__ == '__main__':
    print("🚀 File Encryption App Starting...")
    if USE_SUPABASE:
        print("✅ Using Supabase Storage")
    else:
        print("📦 Using Local Storage (storage/ folder)")
    app.run(debug=True, host='0.0.0.0', port=5000)
