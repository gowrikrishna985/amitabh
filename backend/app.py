from flask import Flask, render_template, request, redirect, url_for
import os
import math
from werkzeug.utils import secure_filename
from tree_analyzer import estimate_tree_height_from_image

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# Get the absolute path to the uploads folder
# Since the static folder is ../frontend/static, uploads should be in ../frontend/static/uploads
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Allowed file extensions (optional check)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home route (serves index.html)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return render_template('index.html', message='No file part')

    file = request.files['image']
    if file.filename == '':
        return render_template('index.html', message='No file selected')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            file.save(filepath)
            # Use automatic tree height estimation
            estimated_height = estimate_tree_height_from_image(filepath)
            
            if estimated_height and estimated_height > 0:
                real_height = estimated_height+10
            else:
                # Fallback to a reasonable default if automatic detection fails
                real_height = 12.5  # Default fallback height
            
            os.remove(filepath)
            amitabh_height = 1.88  # meters
            num_amitabhs = real_height / amitabh_height
            num_amitabhs_rounded = int(num_amitabhs + 0.5)
            return render_template('index.html', message=f'your tree is about {num_amitabhs:.1f} Amitabh Bachchans tall', num_amitabhs=num_amitabhs_rounded)
        except Exception as e:
            if os.path.exists(filepath):
                os.remove(filepath)
            return render_template('index.html', message=f'Error: {str(e)}')

    return render_template('index.html', message='File type not allowed')

if __name__ == '__main__':
    app.run(debug=True)
