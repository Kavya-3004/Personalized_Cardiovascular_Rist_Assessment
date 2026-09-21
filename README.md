# Personalized Cardiovascular Risk Assessment

[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/UI-Streamlit%201.30+-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Model Champion](https://img.shields.io/badge/Champion-Random%20Forest%20(90.48%25%20Recall)-green)](docs/MODEL_CARD.md)
[![ROC-AUC](https://img.shields.io/badge/ROC--AUC-0.9362-brightgreen)](outputs/roc_curves.png)
[![CI/CD Pipeline](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue?logo=githubactions)](.github/workflows/ci.yml)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](Dockerfile)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## 📖 Project Overview

This repository hosts a production-grade machine learning framework for personalized cardiovascular risk assessment using clinical tabular health metrics and explainable artificial intelligence (XAI). The deployed system leverages an ensemble **Random Forest Classifier** and **TreeSHAP** to deliver accurate, interpretable, and actionable cardiac risk assessments.

During the benchmarking phase, three candidate algorithms were rigorously evaluated on stratified splits: **Logistic Regression**, **Random Forest**, and **XGBoost**. The **Random Forest** model was selected as champion based on superior clinical **Recall (90.48% on the hold-out test set)** and **ROC-AUC (0.9362)**, ensuring minimal false-negative risk. The complete inference pipeline is deployed via an interactive **Streamlit** clinical decision support interface.

---

## 📚 Technical Documentation Index

| Document | Description |
|---|---|
| 📄 [Model Card](docs/MODEL_CARD.md) | Formal model specification, evaluation metrics, fairness, and hyperparameters |
| 📊 [Data Sheet](docs/DATA_SHEET.md) | In-depth dataset provenance, deduplication audit, and stratified splitting |
| 🏛️ [System Architecture](docs/ARCHITECTURE.md) | High-level software architecture, data flow diagrams, and module specs |
| 🚀 [Deployment Guide](docs/DEPLOYMENT_GUIDE.md) | Step-by-step guides for Streamlit Community Cloud, Docker, and Hugging Face |
| ⚠️ [Clinical Disclaimer](docs/CLINICAL_DISCLAIMER.md) | Full academic, non-diagnostic, and ethical usage notices |
| 🤝 [Contributing Guidelines](CONTRIBUTING.md) | Contribution standards, development setup, and PR checklist |

---

## 🔗 Dataset Sources & External Links

### 1. UCI Heart Disease Dataset
* **Source**: [UCI Machine Learning Repository - Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease)
* **Mirror**: [Kaggle UCI Heart Disease Dataset](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)
* **Description**: Contains clinical patient records from the Cleveland database with 13 key diagnostic features and binary cardiovascular status.

### 2. Diagnostic ECG Repository (Multi-Modal Data)
* **Primary Source (Mendeley Data)**: [ECG Images Dataset of Cardiac Patients (DOI: 10.17632/gwbz3fsgp8.2)](https://data.mendeley.com/datasets/gwbz3fsgp8/2)
* **Description**: Collected for multi-modal exploratory research across diagnostic classes (Myocardial Infarction, Abnormal Heartbeat, Normal controls). *Note: The active deployed risk prediction pipeline utilizes the 13 verified clinical tabular metrics.*

---

## 📁 Repository Structure

```text
Personalized_Cardiovascular_Risk_Assessment/
├── .github/
│   ├── workflows/
│   │   └── ci.yml                 # Automated CI test suite
│   ├── ISSUE_TEMPLATE/            # Bug report & feature request templates
│   └── PULL_REQUEST_TEMPLATE.md   # Structured PR template
├── .streamlit/
│   └── config.toml                # Streamlit UI styling and server config
├── data/
│   ├── raw/                       # Raw UCI CSV and multi-modal ECG folders
│   ├── processed/                 # Deduplicated & stratified splits (train/val/test)
│   └── sample_patient_input.json  # Patient fixtures for testing
├── docs/
│   ├── MODEL_CARD.md              # Formal ML model card
│   ├── DATA_SHEET.md              # Comprehensive data documentation
│   ├── ARCHITECTURE.md            # System diagrams and data flow
│   ├── DEPLOYMENT_GUIDE.md        # Cloud & Docker deployment tutorials
│   └── CLINICAL_DISCLAIMER.md     # Medical and research notices
├── models/
│   ├── best_model.pkl             # Serialized Champion Random Forest
│   ├── scaler.pkl                 # Fitted StandardScaler
│   └── model_metadata.json        # Performance metrics and thresholds
├── notebooks/
│   ├── 00_Environment_Test.ipynb
│   ├── 01_UCI_Data_Inspection.ipynb
│   └── 02_Data_Preprocessing_and_Splits.ipynb
├── outputs/                       # ROC curves, confusion matrix, SHAP plots
├── scripts/
│   └── create_git_history.py      # Git history generator for realistic commits
├── src/
│   ├── __init__.py
│   ├── preprocessing.py           # Deduplication, imputation, segregation
│   ├── train_models.py            # Baseline training and evaluation
│   ├── predict.py                 # Core inference engine & risk classification
│   └── explain.py                 # TreeSHAP local feature attribution
├── tests/
│   ├── test_predict.py            # Unit tests for inference & probability bounds
│   ├── test_explain.py            # Unit tests for SHAP value computation
│   └── test_app.py                # End-to-end integration tests
├── .dockerignore                  # Docker build exclusions
├── .gitignore                     # Git tracking exclusions
├── Dockerfile                     # Production container specification
├── docker-compose.yml             # Container orchestration
├── LICENSE                        # MIT License
├── Makefile                       # Project shortcut commands
├── pyproject.toml                 # Modern Python packaging config
├── requirements.txt               # Pinned dependencies
├── requirements-dev.txt           # Development & testing tools
├── setup.py                       # Legacy packaging support
└── app.py                         # Streamlit interactive application
```

---

## 📊 Tabular Clinical Features Specification

The 13 clinical attributes used for model training and real-time inference:

| # | Feature | Description | Values / Units |
|---|---------|-------------|----------------|
| 1 | `age` | Patient age | Continuous (years) |
| 2 | `sex` | Biological sex | `1` = Male, `0` = Female |
| 3 | `cp` | Chest pain type | `1`: Typical angina, `2`: Atypical angina, `3`: Non-anginal pain, `4`: Asymptomatic |
| 4 | `trestbps` | Resting blood pressure | Continuous (mm Hg on admission) |
| 5 | `chol` | Serum cholesterol | Continuous (mg/dl) |
| 6 | `fbs` | Fasting blood sugar > 120 mg/dl | `1` = True, `0` = False |
| 7 | `restecg` | Resting electrocardiographic results | `0`: Normal, `1`: ST-T wave abnormality, `2`: Left ventricular hypertrophy |
| 8 | `thalach` | Maximum heart rate achieved | Continuous (bpm) |
| 9 | `exang` | Exercise-induced angina | `1` = Yes, `0` = No |
| 10 | `oldpeak` | ST depression induced by exercise relative to rest | Continuous (0.0 to 6.2) |
| 11 | `slope` | Slope of peak exercise ST segment | `1`: Upsloping, `2`: Flat, `3`: Downsloping |
| 12 | `ca` | Major vessels colored by fluoroscopy | `0` to `3` |
| 13 | `thal` | Thalassemia status | `3` = Normal, `6` = Fixed defect, `7` = Reversible defect |

**Target Variable**: `target_binary` (`0`: No heart disease, `1`: Heart disease present).

---

## 🚀 Machine Learning & Inference Pipeline

```text
Dataset Collection (UCI Cleveland Heart Disease Dataset)
      │
      ▼
Data Preprocessing, Deduplication & Mode Imputation (ca: 0.0, thal: 3.0)
      │
      ▼
Stratified Train / Validation / Test Splitting (70% / 15% / 15%)
      │
      ▼
Baseline Model Benchmarking (Logistic Regression, Random Forest, XGBoost)
      │
      ▼
Champion Selection: Random Forest (Top Validation Recall & ROC-AUC)
      │
      ▼
Hold-Out Test Evaluation (Accuracy: 86.96%, Recall: 90.48%, ROC-AUC: 0.9362)
      │
      ▼
Model Explainability (TreeSHAP Individual Patient Feature Attribution)
      │
      ▼
Interactive Streamlit Application (Presentation Bands: LOW / MEDIUM / HIGH)
```

---

## 📈 Model Performance & Evaluation Metrics

Evaluated on the stratified partitions (`random_state=42`):

### 1. Validation Set Benchmarking (45 Patients)
| Model | Accuracy | Precision | Recall (Sensitivity) | F1-Score | ROC-AUC |
|---|---|---|---|---|---|
| **Random Forest (Champion)** | **84.44%** | **85.00%** | **80.95%** | **82.93%** | **0.9256** |
| Logistic Regression | 80.00% | 83.33% | 71.43% | 76.92% | 0.8889 |
| XGBoost | 77.78% | 78.95% | 71.43% | 75.00% | 0.8948 |

### 2. Final Hold-Out Test Set Performance (46 Patients, Random Forest)
* **Accuracy**: **86.96%** (40 / 46 correct classifications)
* **Recall (Sensitivity)**: **90.48%** (19 of 21 cardiac disease cases detected; **only 2 false negatives**)
* **Precision**: **82.61%**
* **F1-Score**: **86.36%**
* **ROC-AUC**: **0.9362**

---

## 🔍 Explainability (TreeSHAP)

For every individual patient prediction, local feature attributions are computed via TreeSHAP:
$$f(x) = \mathbb{E}[f(x)] + \sum_{j=1}^{13} \phi_j$$
* **Positive Contribution ($\phi_j > 0$)**: Feature pushed model prediction toward higher disease probability (`increases risk`).
* **Negative Contribution ($\phi_j < 0$)**: Feature pushed model prediction toward lower disease probability (`decreases risk`).
* *Note: SHAP values describe statistical model contributions and do not represent biological or clinical causation.*

---

## 💻 Quickstart & Running Locally

### 1. Clone & Set Up Environment
```bash
git clone https://github.com/your-username/Personalized_Cardiovascular_Risk_Assessment.git
cd Personalized_Cardiovascular_Risk_Assessment

python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Launch the Streamlit App
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

### 3. Run Automated Tests
```bash
python -m unittest discover tests
```

---

## 🐳 Docker Deployment

Run with Docker in a single command:
```bash
docker compose up -d
```
Access the application at `http://localhost:8501`.

---

## ⚠️ Important Educational & Research Disclaimer

This application and codebase are developed for **educational, academic, and research demonstration purposes only**. The risk scores are generated by a machine learning model and do **not** constitute a clinical diagnosis, medical evaluation, treatment plan, or medication prescription. The **LOW / MEDIUM / HIGH** risk categories are project-defined presentation-layer bands and are **not** clinically validated diagnostic thresholds. Always consult a qualified medical professional for health evaluations. Read the full [Clinical Disclaimer](docs/CLINICAL_DISCLAIMER.md) for details.