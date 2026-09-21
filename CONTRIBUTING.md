# Contributing to Personalized Cardiovascular Risk Assessment

Thank you for your interest in contributing to this project! We welcome contributions from data scientists, machine learning engineers, healthcare researchers, and open-source enthusiasts.

## 📋 Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Branching Strategy & Workflow](#branching-strategy--workflow)
- [Running Tests](#running-tests)
- [Coding Standards](#coding-standards)
- [Submitting a Pull Request](#submitting-a-pull-request)

---

## Code of Conduct
This project adheres to the [Contributor Covenant](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

---

## How Can I Contribute?
- **Bug Fixes**: Report or resolve edge cases in model inference, preprocessing, or the Streamlit UI.
- **Model Enhancements**: Experiment with alternative architectures (e.g., LightGBM, TabNet) while maintaining strict recall safeguards.
- **Explainability**: Integrate supplementary interpretability views (e.g., LIME, partial dependence plots).
- **Documentation**: Clarify clinical feature descriptions or improve deployment tutorials.

---

## Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Personalized_Cardiovascular_Risk_Assessment.git
   cd Personalized_Cardiovascular_Risk_Assessment
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Launch the Streamlit app locally**:
   ```bash
   streamlit run app.py
   ```

---

## Running Tests

All unit and integration tests must pass before submitting code:
```bash
python -m unittest discover tests
```

---

## Coding Standards
- Follow **PEP 8** style guidelines.
- Use explicit type annotations where possible.
- Include docstrings formatted in Google or NumPy style for all functions and classes.
- Ensure any clinical metrics or thresholds are thoroughly referenced and tested.

---

## Submitting a Pull Request
1. Fork the repo and create a feature branch (`git checkout -b feat/your-feature-name`).
2. Commit your changes with conventional commit messages (`feat:`, `fix:`, `docs:`, `test:`).
3. Ensure all automated tests pass.
4. Open a Pull Request referencing any related issues.
