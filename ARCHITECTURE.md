# System Architecture & Technical Specifications

## 🏛️ High-Level System Architecture

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        User Interface Layer                            │
│                     (Streamlit Web Application)                        │
│   • Clinical Parameter Sliders & Input Selectors                       │
│   • Real-Time Risk Probability Metric & Dynamic Risk Badge             │
│   • SHAP Waterfall Feature Attribution Plot Rendering                  │
│   • Clinical Caution & Lifestyle Guidance Accordion                    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                       Inference & Logic Layer                          │
│                                                                        │
│   ┌─────────────────────┐                 ┌────────────────────────┐   │
│   │   Inference Engine  │                 │  Explainability Engine │   │
│   │   (src/predict.py)  │                 │    (src/explain.py)    │   │
│   │                     │                 │                        │   │
│   │ • Input Validation  │                 │ • TreeSHAP Explainer   │   │
│   │ • Feature Ordering  │                 │ • Base Value Baseline  │   │
│   │ • Model Loading     │                 │ • Patient Contributions│   │
│   │ • Calibrated Probs  │                 │ • Matplotlib Bar Chart │   │
│   └──────────┬──────────┘                 └───────────┬────────────┘   │
└──────────────┼────────────────────────────────────────┼────────────────┘
               │                                        │
               ▼                                        ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        Model Artifacts Store                           │
│   • models/best_model.pkl (Random Forest Champion)                     │
│   • models/scaler.pkl (StandardScaler fitted on train set)             │
│   • models/model_metadata.json (Metrics, threshold mappings)           │
└────────────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ Core Modules Breakdown

### 1. Preprocessing & Deduplication Pipeline (`src/preprocessing.py`)
- **Data Retrieval**: Ingests raw Cleveland data and sample multi-modal ECG directories.
- **Deduplication**: Hash-based and feature-level duplicate identification.
- **Missing Value Handling**: Conservative clinical mode imputation.
- **Stratified Segregation**: 70% Train, 15% Validation, 15% Hold-out Test partitions with zero leakage.

### 2. Model Training & Benchmarking (`src/train_models.py`)
- Standardizes feature distributions via `StandardScaler`.
- Trains and cross-benchmarks **Logistic Regression**, **Random Forest**, and **XGBoost**.
- Computes comprehensive classification metrics: Accuracy, Precision, Recall, F1-Score, and ROC-AUC.
- Generates ROC curves, confusion matrices, and feature importance bar graphs in `outputs/`.
- Selects the champion model prioritizing recall to mitigate false negatives.

### 3. Inference Engine (`src/predict.py`)
- Accepts raw patient dictionaries with 13 diagnostic parameters.
- Validates data types and ranges.
- Computes raw classification and calibrated probability $P(\text{disease})$.
- Assigns presentation-layer risk categories:
  - **LOW Risk**: $< 40\%$
  - **MEDIUM Risk**: $40\% - 70\%$
  - **HIGH Risk**: $> 70\%$

### 4. Explainable AI Engine (`src/explain.py`)
- Uses `shap.TreeExplainer` on the Random Forest ensemble.
- Extracts individual patient SHAP values $\phi_j$.
- Translates numerical attributions into intuitive human-readable explanations ("Chest pain increases risk", "Normal cholesterol decreases risk").
- Visualizes local attributions via colored horizontal bar charts.

### 5. Web Interface (`app.py`)
- Responsive multi-column layout built with Streamlit.
- Clinical parameter inputs grouped into **Demographics**, **Vitals & Labs**, and **Cardiac Stress Test** cards.
- Real-time prediction triggering, visual risk banners, SHAP plots, and tailored caution advisories.
