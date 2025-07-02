# 🧠 Project Overview: Chest X-Ray Diagnosis with AI

## 🩺 Title

**AI-Powered Chest X-Ray Disease Detection: Pneumonia & Tuberculosis**

---

## ✅ Objective

Build a machine learning system to classify chest X-ray images into **Normal**, **Pneumonia**, and **Tuberculosis (TB)** classes, with model explainability and a user-friendly web app.

---

## 🔍 Problem Statement

Chest-related diseases like Pneumonia and TB are leading causes of illness and death globally, especially in areas with a shortage of radiologists. An AI-powered tool that can **automatically detect signs of lung disease** from chest X-rays can assist healthcare workers in early screening and triage.

---

## 🎯 Project Goals

| Goal                    | Description                                                          |
| ----------------------- | -------------------------------------------------------------------- |
| 💻 Build a CNN model    | Classify X-rays into: Normal, Pneumonia, TB                          |
| 🖼️ Explain Predictions | Use Grad-CAM to show which part of the X-ray influenced the decision |
| 🧪 Evaluate Robustness  | Use multiple datasets from different hospitals/countries             |
| 🌐 Web Deployment       | Allow users to upload X-rays and view predictions via a web app      |

---

## 📊 Dataset Sources

### 1. **Chest X-ray Pneumonia Dataset (Kermany et al.)**
- **Classes:** Normal, Pneumonia (bacterial & viral)
- **Source:** Guangzhou Women and Children's Medical Center, China
- **Link:** [Kaggle Dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

### 2. **Tuberculosis X-ray Datasets (NIH - Montgomery & Shenzhen)**
- **Classes:** TB, Normal
- **Sources:** Shenzhen No.3 Hospital (China), Montgomery County (USA)
- **Link:** [NIH Dataset Page](https://lhncbc.nlm.nih.gov/publication/pub9931)

---

## 🔧 Tools & Technologies

| Area            | Tools                                          |
| --------------- | ---------------------------------------------- |
| Programming     | Python                                         |
| ML/DL Framework | PyTorch                                        |
| Data Handling   | NumPy, Pandas, OpenCV                          |
| Visualization   | Matplotlib, Seaborn                            |
| Model           | DenseNet121 (default), ResNet50                |
| Explainability  | Grad-CAM (`pytorch-grad-cam`)                  |
| Web App         | Streamlit                                      |
| Notebooks       | Jupyter Notebook                               |

---

## 🧠 Skills You'll Learn

- End-to-end machine learning workflow
- Computer vision using CNNs
- Data preprocessing and augmentation
- Model evaluation (accuracy, precision, confusion matrix)
- Explainability with Grad-CAM
- Basic frontend deployment (image input + prediction output)

---

## 📁 Folder Structure

```
chest-xray-diagnosis/
│
├── app/
│   └── app.py                  # Streamlit web app
│
├── data/
│   ├── raw/
│   │   ├── normal/             # Raw Normal X-rays
│   │   ├── pneumonia/          # Raw Pneumonia X-rays
│   │   └── tb/                 # Raw TB X-rays
│   └── split/
│       ├── train/
│       │   ├── normal/
│       │   ├── pneumonia/
│       │   └── tb/
│       ├── val/
│       │   ├── normal/
│       │   ├── pneumonia/
│       │   └── tb/
│       └── test/
│           ├── normal/
│           ├── pneumonia/
│           └── tb/
│
├── models/
│   └── .gitkeep                # Placeholder for trained models
│
├── notebooks/
│   ├── 01_eda.ipynb            # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb  # Data Preprocessing
│   ├── 03_model_training.ipynb # Model Training & Evaluation
│   └── 04_gradcam_explain.ipynb# Grad-CAM Explainability
│
├── utils/
│   ├── data_utils.py           # Data splitting and utilities
│   └── grad_cam_utils.py       # Grad-CAM utility functions
│
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
```

---

## 🚀 How to Run

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Prepare data:**
   - Place all raw images in `data/raw/normal/`, `data/raw/pneumonia/`, and `data/raw/tb/`.
   - Run the data splitting script:
     ```
     python utils/data_utils.py
     ```

3. **Explore and train:**
   - Use the Jupyter notebooks in `notebooks/` for EDA, preprocessing, training, and explainability.

4. **Run the web app:**
   ```
   streamlit run app/app.py
   ```

---

## ⚠️ Notes

- The `data/` and `models/` folders are excluded from git tracking via `.gitignore`.
- Place your trained model files in `models/` for the web app to use.
- The project is modular—feel free to extend or swap out models, preprocessing, or explainability methods. 

## 👨‍💻 Developed by

**Yash Nayan**  
