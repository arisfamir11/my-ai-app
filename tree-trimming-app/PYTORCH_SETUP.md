# Tree Trimming Classifier - PyTorch Web App Setup

## Your Model Info
- **Model Type**: ResNet18 (PyTorch)
- **Classes**: `no_trim`, `trim`
- **Input Size**: 224x224
- **Model Location**: `C:\Users\user\Desktop\labelled data\Dataset pokok\train.py\rain_tree_trim_model_best.pth`

---

## 📋 **Quick Setup Steps**

### **Step 1: Copy Files to Your Project**

Download and copy these files to your `tree-trimming-app` folder:
- `app_pytorch.py` → rename to `app.py`
- `requirements_pytorch.txt` → rename to `requirements.txt`
- `templates/index.html` → put in `templates/` subfolder
- Your model file: `rain_tree_trim_model_best.pth`

Your folder structure should look like:
```
tree-trimming-app/
├── app.py                           (app_pytorch.py renamed)
├── requirements.txt                 (requirements_pytorch.txt renamed)
├── rain_tree_trim_model_best.pth   (your model file)
├── templates/
│   └── index.html
└── uploads/                         (created automatically)
```

---

### **Step 2: Update Model Path in `app.py`**

In Anaconda Prompt, open the file with a text editor:

Find this line (around line 12):
```python
MODEL_PATH = r"C:\Users\user\Desktop\labelled data\Dataset pokok\train.py\rain_tree_trim_model_best.pth"
```

**Change it to the actual path where your model file is.**

Two options:

**Option A: Put model file in project folder (Easiest)**
1. Copy `rain_tree_trim_model_best.pth` to your `tree-trimming-app` folder
2. Change the line to:
   ```python
   MODEL_PATH = "rain_tree_trim_model_best.pth"
   ```

**Option B: Keep model file where it is**
Just make sure the path in `app.py` is correct and the file exists there.

---

### **Step 3: Install Dependencies**

**Using Conda (Recommended for PyTorch):**
```bash
conda install pytorch::pytorch torchvision torchaudio -c pytorch
conda install Flask Flask-CORS Pillow
```

**Or using pip:**
```bash
pip install -r requirements.txt
```

⚠️ If pip has issues with torch, use conda instead!

---

### **Step 4: Run the App**

In Anaconda Prompt (in `tree-trimming-app` folder):

```bash
python app.py
```

You should see:
```
==================================================
🌳 Tree Trimming Classifier Web App
==================================================
Device: cuda  (or cpu)
Model loaded: True
Classes: ['no_trim', 'trim']
==================================================

Starting Flask server...
Open browser at: http://localhost:5000
```

---

### **Step 5: Open in Browser**

Go to:
```
http://localhost:5000
```

Done! 🎉

---

## 🔧 **Troubleshooting**

### **Error: "FileNotFoundError: [Errno 2] No such file or directory: 'rain_tree_trim_model_best.pth'"**

The model file path is wrong. Fix:
1. Check the exact location of your `.pth` file
2. Copy the full path from File Explorer
3. Update `MODEL_PATH` in `app.py`

**Example:**
```python
MODEL_PATH = r"C:\Users\user\Desktop\labelled data\Dataset pokok\train.py\rain_tree_trim_model_best.pth"
```

(Use the `r` before the string to avoid backslash issues)

---

### **Error: "No module named 'torch'"**

Install PyTorch using conda (better for PyTorch):
```bash
conda install pytorch::pytorch torchvision -c pytorch
```

Or if using pip and getting errors, try:
```bash
pip install torch==2.0.1 torchvision==0.15.2
```

---

### **Model says "loaded: False"**

1. Check the model file exists at the path
2. Verify the file is not corrupted
3. Check file permissions
4. Try with full path instead of relative path

Test your model first in Python:
```python
import torch
model_state = torch.load(r"C:\your\path\rain_tree_trim_model_best.pth", map_location='cpu')
print("Model loaded successfully!")
```

---

### **"Address already in use" error**

Port 5000 is busy. Change in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use 5001
```

Then open: `http://localhost:5001`

---

### **Slow predictions (model taking long time)**

- If on CPU: This is normal, wait 5-10 seconds
- If on GPU: Check `Device: cuda` in the startup message
- To force CPU: Change line 10 in `app.py`:
  ```python
  DEVICE = "cpu"  # Force CPU mode
  ```

---

## 📊 **How It Works**

1. **User uploads image** via web interface
2. **Flask backend** receives the image
3. **PyTorch model** processes the image:
   - Resize to 224x224
   - Normalize with ImageNet stats
   - Run through ResNet18
   - Get prediction: `trim` or `no_trim`
4. **Results displayed** with confidence score

---

## 🎨 **Customizing the Web Interface**

Edit `templates/index.html` to change:
- Colors: Look for `#667eea` and `#764ba2`
- Text: Look for `<h1>`, `<p>` tags
- Messages: Look for "Needs Trimming", "Does Not Need Trimming"

---

## 📱 **Accessing from Other Computers**

If you want to access the app from another computer on your network:

1. Get your computer's IP address:
   ```bash
   ipconfig
   ```
   Look for "IPv4 Address" (e.g., `192.168.1.100`)

2. On the other computer, go to:
   ```
   http://192.168.1.100:5000
   ```

---

## 🚀 **Next Steps**

Once working, you can:
- **Deploy to cloud** (Heroku, AWS, Google Cloud)
- **Make a mobile app** that connects to this server
- **Add more features** (history, batch processing, etc.)
- **Optimize model** (pruning, quantization for faster predictions)

---

## ✅ **Checklist Before Running**

- [ ] Model file (`rain_tree_trim_model_best.pth`) exists
- [ ] Model path in `app.py` is correct
- [ ] `templates/index.html` is in `templates/` folder
- [ ] Requirements installed (`pip install -r requirements.txt` or conda)
- [ ] No other app using port 5000
- [ ] Python 3.8 or higher (`python --version`)

---

Happy classifying! 🌳

For more help, check the Flask documentation: https://flask.palletsprojects.com/
