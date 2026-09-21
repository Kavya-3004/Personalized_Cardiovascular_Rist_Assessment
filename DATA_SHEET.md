# Data Sheet: Personalized Cardiovascular Risk Assessment Datasets

Following the recommendations of *Datasheets for Datasets* (Gebru et al., 2021).

---

## 1. Motivation

* **Purpose**: This dataset collection supports reproducible research and evaluation of machine learning algorithms for personal cardiovascular risk prediction.
* **Funding / Creators**: Original Cleveland Clinic Foundation investigators (Robert Detrano, M.D., Ph.D.) and Mendeley Data ECG imaging contributors (DOI: 10.17632/gwbz3fsgp8.2).

---

## 2. Composition

### A. Primary Tabular Dataset (UCI Cleveland Heart Disease)
* **Total Records**: 303 original patient entries.
* **Post-Deduplication**: 302 unique verified records (1 exact duplicate identified and removed).
* **Missing Value Handling**: Mode imputation on sparse clinical columns (`ca`: 0.0, `thal`: 3.0).
* **Features (13 Diagnostic Predictors)**:
  1. `age`: Patient age in years.
  2. `sex`: Biological sex (1 = male, 0 = female).
  3. `cp`: Chest pain type (1: typical angina, 2: atypical angina, 3: non-anginal, 4: asymptomatic).
  4. `trestbps`: Resting blood pressure (mm Hg on admission).
  5. `chol`: Serum cholesterol in mg/dl.
  6. `fbs`: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false).
  7. `restecg`: Resting ECG results (0: normal, 1: ST-T wave abnormality, 2: LV hypertrophy).
  8. `thalach`: Maximum heart rate achieved during stress testing.
  9. `exang`: Exercise-induced angina (1 = yes, 0 = no).
  10. `oldpeak`: ST depression induced by exercise relative to rest.
  11. `slope`: Slope of peak exercise ST segment (1: upsloping, 2: flat, 3: downsloping).
  12. `ca`: Number of major vessels (0–3) colored by fluoroscopy.
  13. `thal`: Thalassemia category (3 = normal, 6 = fixed defect, 7 = reversible defect).
* **Target**: Binary classification `target_binary` (0: absence of heart disease, 1: presence of heart disease [stages 1–4 combined]).

### B. Raw Multi-Modal ECG Image Dataset
* **Sub-directories**:
  - `data/raw/ECG/`: Myocardial Infarction 12-lead ECG sample recordings.
  - `data/raw/abnormal_heatbeat/`: Arrhythmia and abnormal rhythm traces.
  - `data/raw/his_MI/`: Previous myocardial infarction clinical ECGs.
  - `data/raw/normal/`: Baseline healthy ECG waveforms.
  - `data/raw/uci - normal/` & `uci - sick/`: Patient profile visual cards.

---

## 3. Data Segregation & Splitting Strategy

To ensure zero data leakage and reliable clinical evaluation:
* **Stratified Splitting**: Stratified by binary disease prevalence across all partitions.
* **Train Set**: 70% (211 patients) — used for model training and StandardScaler parameter fitting.
* **Validation Set**: 15% (45 patients) — used strictly for hyperparameter selection and candidate model benchmarking.
* **Hold-Out Test Set**: 15% (46 patients) — locked until final champion evaluation.

---

## 4. Collection & Preprocessing Pipeline

```text
Raw UCI Cleveland Ingestion
       │
       ▼
Automated Deduplication (Exact hash & feature matching)
       │
       ▼
Mode Imputation for Clinical Categoricals
       │
       ▼
Stratified Train/Val/Test Partitioning (70 / 15 / 15)
       │
       ▼
StandardScaler Fitting (fitted ONLY on Train, applied to Val & Test)
```

---

## 5. Uses & Distribution

* **License**: Publicly available for academic research. UCI Heart Disease Dataset license: Creative Commons Attribution 4.0 International (CC BY 4.0).
* **Distribution Formats**: CSV (`data/processed/train.csv`, `val.csv`, `test.csv`) and JSON summary manifests (`split_summary.json`).
