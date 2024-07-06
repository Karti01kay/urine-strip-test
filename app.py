from flask import Flask, request, jsonify, send_from_directory
import cv2
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def analyze_strip(image_path):
    # Load the image
    image = cv2.imread(image_path)
    # Convert the image to RGB (OpenCV loads images in BGR format by default)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Assuming the image has 10 color patches, we can divide the width by 10 to get each patch
    height, width, _ = image.shape
    patch_width = width // 10

    colors = []
    for i in range(10):
        # Crop the patch
        patch = image_rgb[:, i*patch_width:(i+1)*patch_width]
        # Calculate the mean color of the patch
        mean_color = cv2.mean(patch)[:3]
        # Convert to integer
        mean_color = tuple(map(int, mean_color))
        colors.append(mean_color)

    return colors

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        colors = analyze_strip(file_path)
        return jsonify({'colors': colors})

if __name__ == '__main__':
    app.run(debug=True)
