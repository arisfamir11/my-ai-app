# 📦 Installation Guide - PyTorch Tree Trimming App

## The EASIEST Way (Using Conda)

### Step 1: Open Anaconda Prompt
- Windows: Search "Anaconda Prompt" in Start Menu
- Mac/Linux: Open Terminal

### Step 2: Create Project Folder
```bash
mkdir tree-trimming-app
cd tree-trimming-app
```

### Step 3: Install PyTorch (Better with Conda)
```bash
conda install pytorch::pytorch torchvision torchaudio -c pytorch
```

This installs:
- PyTorch (the main library)
- TorchVision (for image processing)
- TorchAudio (not needed but good to have)

### Step 4: Install Flask and Other Packages
```bash
conda install Flask Flask-CORS Pillow
```

### Step 5: Download Your Files
From the outputs folder, download:
1. `app_pytorch.py` → Rename to **`app.py`**
2. `requirements_pytorch.txt` → (optional, not needed if installing via conda)
3. `templates/index.html` → Create a `templates` folder first, then put this inside
4. Copy your model file: **`rain_tree_trim_model_best.pth`**

### Step 6: Check Your Folder Structure
```
tree-trimming-app/
├── app.py
├── rain_tree_trim_model_best.pth
├── templates/
│   └── index.html
```

### Step 7: Verify Model Path in app.py
Open `app.py` and find line 12:
```python
MODEL_PATH = r"C:\Users\user\Desktop\labelled data\Dataset pokok\train.py\rain_tree_trim_model_best.pth"
```

Make sure this path is correct! If your model is in the project folder, change to:
```python
MODEL_PATH = "rain_tree_trim_model_best.pth"
```

### Step 8: Run the App!
```bash
python app.py
```

You should see:
```
==================================================
🌳 Tree Trimming Classifier Web App
==================================================
Device: cuda
Model loaded: True
Classes: ['no_trim', 'trim']
==================================================

Starting Flask server...
Open browser at: http://localhost:5000
```

### Step 9: Open Browser
Go to: **http://localhost:5000**

---

## If You Don't Have Anaconda Installed

### Option A: Install Anaconda First (Recommended)
1. Download from: https://www.anaconda.com/download
2. Install it
3. Follow the steps above

### Option B: Use pip (May Have Issues)
If you only have Python installed (no Anaconda):

```bash
pip install torch torchvision torchaudio
pip install Flask Flask-CORS Pillow
```

But conda is more reliable for PyTorch!

---

## Common Installation Issues

### Issue 1: "conda: command not found"
**Solution:** 
- Restart Anaconda Prompt
- Or add Anaconda to PATH and restart computer

### Issue 2: "torch installation failed"
**Solution:** Try installing just torch first:
```bash
conda install pytorch::pytorch -c pytorch
conda install torchvision -c pytorch
```

### Issue 3: Slow installation
**Note:** This is normal! PyTorch is large (~1-2 GB). Wait 5-10 minutes.

### Issue 4: "No module named 'torch'"
**Solution:** Make sure you're in the correct Anaconda Prompt (base environment)
```bash
# You should see (base) at the start of the prompt
(base) C:\Users\user>
```

---

## Verify Installation

After installation, test it:

```bash
python test_setup.py
```

This will check:
✓ Python version
✓ All packages installed
✓ Model file location
✓ PyTorch working correctly

---

## GPU vs CPU

If you have an NVIDIA GPU, PyTorch will use it automatically (faster).

Check in startup message:
- `Device: cuda` = GPU (fast! ⚡)
- `Device: cpu` = CPU (slower, but still works)

To force CPU (if GPU causing issues):
Edit `app.py` line 10:
```python
DEVICE = "cpu"  # Force CPU
```

---

## Memory Issues?

If you get out of memory errors:
1. Reduce image size in `app.py` (line 12):
   ```python
   IMG_SIZE = 224  # Try 128 or 160 instead
   ```

2. Or disable debug mode in `app.py` (last line):
   ```python
   app.run(debug=False, host='0.0.0.0', port=5000)
   ```

---

## Ready to Go! 🚀

Once installed:
1. Run: `python app.py`
2. Open: `http://localhost:5000`
3. Upload tree image
4. Get prediction!

For detailed troubleshooting, see: **PYTORCH_SETUP.md**
