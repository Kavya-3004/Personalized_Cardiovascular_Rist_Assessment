# Model Card: Personalized Cardiovascular Risk Assessment Champion Model

## 📌 Model Overview

* **Model Name**: Random Forest Classifier (Champion)
* **Model Version**: `1.0.0`
* **Release Date**: September 2026
* **Model Type**: Supervised Ensemble Classification (`sklearn.ensemble.RandomForestClassifier`)
* **Primary Task**: Binary Cardiovascular Disease Detection (`0`: No Heart Disease, `1`: Heart Disease Detected)
* **Post-Processing**: Continuous risk probability output mapped to educational presentation bands (`LOW`, `MEDIUM`, `HIGH`) and local patient-level feature attributions via TreeSHAP.

---

## 🎯 Intended Use

* **Intended Users**: Healthcare researchers, medical informatics students, data scientists, and clinical decision support engineers.
* **Intended Use Case**: Educational exploration and research demonstration of clinical risk stratification from tabular health metrics with local interpretability.
* **Out-of-Scope Use Cases**: Real-world unassisted clinical diagnosis, prescription of treatment/medication, or acute cardiac triage decisions.

---

## 🔬 Benchmark Comparison & Model Selection

During the benchmarking phase, three candidate architectures were trained and evaluated on stratified splits (`random_state=42`):
1. **Logistic Regression (L2 Regularized)**
2. **Random Forest Classifier (Ensemble of 100 Estimators)**
3. **XGBoost Classifier (Gradient Boosted Trees)**

### Validation Set Performance (45 Patients)

| Metric | Random Forest (Champion) | Logistic Regression | XGBoost |
|---|---|---|---|
| **Accuracy** | **84.44%** | 80.00% | 77.78% |
| **Precision** | **85.00%** | 83.33% | 78.95% |
| **Recall (Sensitivity)** | **80.95%** | 71.43% | 71.43% |
| **F1-Score** | **82.93%** | 76.92% | 75.00% |
| **ROC-AUC** | **0.9256** | 0.8889 | 0.8948 |

### Selection Rationale:
In clinical risk assessment, **False Negatives (missed heart disease)** are far costlier than False Positives. Random Forest was selected as the **Champion Model** due to its superior recall (80.95% on validation, 90.48% on final holdout test) and highest ROC-AUC (0.9256).

---

## 📊 Final Holdout Test Set Performance (46 Patients)

* **Accuracy**: **86.96%** (40 / 46 correct classifications)
* **Recall (Sensitivity)**: **90.48%** (19 of 21 cardiac disease cases detected; **only 2 false negatives**)
* **Precision**: **82.61%**
* **F1-Score**: **86.36%**
* **ROC-AUC**: **0.9362**

---

## 🔍 Explainability Engine (TreeSHAP)

Every individual prediction generates local feature contributions $\phi_j$ satisfying the additive efficiency property:

$$f(x) = \mathbb{E}[f(x)] + \sum_{j=1}^{13} \phi_j$$

* **Positive SHAP Value ($\phi_j > 0$)**: Pushes the model prediction towards disease presence (`increases risk`).
* **Negative SHAP Value ($\phi_j < 0$)**: Pushes the model prediction towards healthy status (`decreases risk`).
* Top influential features globally: Chest Pain Type (`cp`), Thalassemia Defect (`thal`), Major Vessels (`ca`), Maximum Heart Rate (`thalach`), and ST Depression (`oldpeak`).

---

## ⚠️ Risk Bands & Clinical Caution Thresholds

The model outputs calibrated probabilities $P(\text{disease})$ mapped into three user-facing bands:
* **LOW Risk ($P < 40\%$)**: General preventive cardiovascular wellness recommendations.
* **MEDIUM Risk ($40\% \le P \le 70\%$)**: Targeted lifestyle optimization, regular vitals monitoring, and primary physician check-up.
* **HIGH Risk ($P > 70\%$)**: Urgent clinical follow-up, cardiology consultation, and comprehensive diagnostic evaluation.

---

## 🛡️ Limitations & Ethical Considerations

1. **Dataset Demographics**: The Cleveland dataset comprises 303 historical records predominantly from a specific regional adult cohort. Cross-demographic generalization must be validated.
2. **Tabular vs. Multi-Modal**: While ECG waveforms provide vital acute diagnostic indicators, the active classification model uses 13 clinical tabular parameters.
3. **Statistical vs. Causal Interpretation**: SHAP values explain model associations, **not biological causation**.
