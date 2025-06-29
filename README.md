# 🧠 Project Overview: Chest X-Ray Diagnosis with AI

## 🩺 Title

**AI-Powered Chest X-Ray Disease Detection: Pneumonia & Tuberculosis**

---

## ✅ Objective

To build a machine learning system that classifies chest X-ray images into **Normal**, **Pneumonia**, and **Tuberculosis (TB)** classes. The project includes:

* Training a deep learning model (e.g., DenseNet121, ResNet50)
* Using **Grad-CAM** to visualize decision regions (explainability)
* Creating an interactive web app to upload images and get predictions

---

## 🔍 Problem Statement

Chest-related diseases like Pneumonia and TB are leading causes of illness and death globally, especially in rural areas with a shortage of radiologists. An AI-powered tool that can **automatically detect signs of lung disease** from chest X-rays can assist healthcare workers in early screening and triage.

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

* 📦 Contains: **Normal** and **Pneumonia** (bacterial & viral)
* 👨‍⚕️ Hospital: Guangzhou Women and Children's Medical Center, China
* 📈 \~5,000 images
* ✅ Organized in `train`, `test`, `val` folders

🔗 [Kaggle Dataset Link](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

---

### 2. **Tuberculosis X-ray Datasets (NIH - Montgomery & Shenzhen)**

* 📦 Contains: **TB** and **Normal**
* 👨‍⚕️ Sources:

  * **Shenzhen** (China): Shenzhen No.3 Hospital
  * **Montgomery** (USA): Department of Health and Human Services, Maryland
* 📈 \~800 images
* Requires request via NIH

🔗 [NIH Dataset Page](https://lhncbc.nlm.nih.gov/publication/pub9931)

> ✅ You'll receive the ZIP files via email after submitting a request form.

---

## 🔧 Tools & Technologies

| Area            | Tools                                          |
| --------------- | ---------------------------------------------- |
| Programming     | Python                                         |
| ML/DL Framework | PyTorch                                        |
| Data Handling   | NumPy, Pandas, OpenCV                          |
| Visualization   | Matplotlib, Seaborn                            |
| Model           | ResNet50 / DenseNet121                         |
| Explainability  | Grad-CAM (`pytorch-grad-cam`)                  |
| Web App         | Streamlit or Flask                             |
| Deployment      | Streamlit Cloud / Render / Hugging Face Spaces |

---

## 🧠 Skills You'll Learn

* End-to-end machine learning workflow
* Computer vision using CNNs
* Data preprocessing and augmentation
* Model evaluation (accuracy, precision, confusion matrix)
* Explainability with Grad-CAM
* Basic frontend deployment (image input + prediction output)

---

## 📁 Folder Structure Summary

```
chest-xray-diagnosis/
├── data/
│   ├── raw/             # All merged raw data
│   └── split/           # train/val/test after processing
├── notebooks/           # Jupyter notebooks for each stage
├── models/              # Saved .pt model files
├── app/                 # Streamlit or Flask app
├── utils/               # Grad-CAM, data loader scripts
├── requirements.txt
|----.env
└── README.md
``` 