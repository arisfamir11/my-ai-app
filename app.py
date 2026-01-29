from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import torch
from torchvision import transforms, models
from PIL import Image
import os
import numpy as np

app = Flask(__name__)
CORS(app)

# ===== SETTINGS (From your model) =====
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MODEL_PATH = "rain_tree_trim_model_best.pth"
IMG_SIZE = 224
CLASSES = ['no_trim', 'trim']

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# ===== TRANSFORMS (Same as your model) =====
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

# ===== LOAD MODEL =====
print("Loading model...")
try:
    model = models.resnet18(pretrained=False)
    model.fc = torch.nn.Sequential(
        torch.nn.Dropout(0.5),
        torch.nn.Linear(model.fc.in_features, len(CLASSES))
    )
    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    model = model.to(DEVICE)
    model.eval()
    print(f"✓ Model loaded successfully on {DEVICE}")
except Exception as e:
    print(f"✗ Error loading model: {e}")
    model = None


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def predict_tree_status(image_path):
    """Predict if tree needs trimming using PyTorch model"""
    
    if model is None:
        return {
            'error': 'Model not loaded',
            'status': 'unknown',
            'needs_trimming': None,
            'confidence': 0
        }
    
    try:
        # Load and preprocess image
        img = Image.open(image_path).convert("RGB")
        img_tensor = transform(img).unsqueeze(0).to(DEVICE)
        
        # Make prediction
        with torch.no_grad():
            output = model(img_tensor)
            # Get probabilities
            probabilities = torch.softmax(output, dim=1)
            confidence, pred = torch.max(probabilities, 1)
            pred_class = CLASSES[pred.item()]
            confidence_score = float(confidence.item())
        
        # Determine if tree needs trimming
        needs_trimming = pred_class == 'trim'
        
        return {
            'needs_trimming': needs_trimming,
            'confidence': round(confidence_score, 3),
            'prediction': pred_class,
            'status': 'Needs Trimming' if needs_trimming else 'Does Not Need Trimming',
            'error': None
        }
    
    except Exception as e:
        print(f"Error during prediction: {e}")
        return {
            'error': str(e),
            'status': 'error',
            'needs_trimming': None,
            'confidence': 0
        }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle image upload and prediction"""
    
    # Check if file is in request
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed. Use PNG, JPG, JPEG, or GIF'}), 400
    
    try:
        # Save file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Make prediction
        result = predict_tree_status(filepath)
        
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'model_loaded': model is not None,
        'device': DEVICE,
        'classes': CLASSES
    }), 200


if __name__ == '__main__':
    print(f"\n{'='*50}")
    print("🌳 Tree Trimming Classifier Web App")
    print(f"{'='*50}")
    print(f"Device: {DEVICE}")
    print(f"Model loaded: {model is not None}")
    print(f"Classes: {CLASSES}")
    print(f"{'='*50}")
    print("\nStarting Flask server...")
    print("Open browser at: http://localhost:5000\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
