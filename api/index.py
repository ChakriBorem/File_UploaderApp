from flask import Flask, render_template, request, jsonify
from azure.storage.blob import BlobServiceClient
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, template_folder="../templates", static_folder="../static")

AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("CONTAINER_NAME", "uploads")

blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

ALLOWED_EXT = {"png", "jpg", "jpeg", "pdf", "txt"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file found'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    ext = file.filename.rsplit('.', 1)[-1].lower()
    if ext not in ALLOWED_EXT:
        return jsonify({'error': 'Invalid file type'}), 400

    filename = secure_filename(file.filename)
    blob_client = container_client.get_blob_client(filename)
    blob_client.upload_blob(file, overwrite=True)

    blob_url = blob_client.url
    return jsonify({'message': 'Upload successful', 'file_url': blob_url})

if __name__ == "__main__":
    app.run()
