# ⚡ QUICK START GUIDE - Your PyTorch Tree Trimming App

## 5 Minute Setup

### 1️⃣ **Create Project Folder**
```bash
mkdir tree-trimming-app
cd tree-trimming-app
```

### 2️⃣ **Copy Your Files**

Put these in `tree-trimming-app/`:
- ✅ `app_pytorch.py` (rename to `app.py`)
- ✅ `requirements_pytorch.txt` (rename to `requirements.txt`)
- ✅ `rain_tree_trim_model_best.pth` (your model)
- ✅ Create folder `templates/` inside
- ✅ Put `index.html` inside `templates/`

**Result:**
```
tree-trimming-app/
├── app.py
├── requirements.txt
├── rain_tree_trim_model_best.pth
└── templates/
    └── index.html
```

### 3️⃣ **Install Dependencies**

In Anaconda Prompt (in the project folder):

```bash
conda install pytorch::pytorch torchvision -c pytorch
conda install Flask Flask-CORS Pillow
```

Or simply:
```bash
pip install -r requirements.txt
```

### 4️⃣ **Check Model Path**

Open `app.py` and find line 12. Make sure it points to your model:

```python
MODEL_PATH = r"C:\Users\user\Desktop\labelled data\Dataset pokok\train.py\rain_tree_trim_model_best.pth"
```

**If your model is in the project folder, change to:**
```python
MODEL_PATH = "rain_tree_trim_model_best.pth"
```

### 5️⃣ **Run!**

```bash
python app.py
```

### 6️⃣ **Open Browser**

Go to: **http://localhost:5000**

---

## ✨ That's It!

Your app is ready to use! 

- Click the upload area or drag & drop
- See instant predictions
- Shows "Needs Trimming" or "Does Not Need Trimming"

---

## 🆘 If You Get Errors

| Error | Solution |
|-------|----------|
| `FileNotFoundError: rain_tree_trim_model_best.pth` | Check model path in `app.py` line 12 |
| `No module named 'torch'` | Run: `conda install pytorch::pytorch torchvision -c pytorch` |
| `Port 5000 already in use` | Change port 5000 to 5001 in app.py (last line) |
| `Model loaded: False` | Check if `.pth` file exists at the path |

---

## 📸 What to Expect

When you upload a tree image:
1. Model processes it (2-5 seconds on CPU, faster on GPU)
2. Shows prediction: **"Needs Trimming"** (red) or **"Does Not Need Trimming"** (green)
3. Shows confidence percentage

---

**Questions?** Check `PYTORCH_SETUP.md` for detailed troubleshooting.

Good luck! 🌳
