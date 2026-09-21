# Deployment Guide: Personalized Cardiovascular Risk Assessment

This guide outlines deployment options for running the interactive Streamlit application in production or cloud environments.

---

## 🌟 Option 1: Streamlit Community Cloud (Recommended Free Cloud Deployment)

1. **Push your repository to GitHub**:
   Ensure your code is pushed to your personal GitHub account (e.g. `https://github.com/<username>/Personalized_Cardiovascular_Risk_Assessment`).
2. **Log into Streamlit Community Cloud**:
   Visit [share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account.
3. **Deploy New App**:
   - Repository: `<your-username>/Personalized_Cardiovascular_Risk_Assessment`
   - Branch: `main`
   - Main file path: `app.py`
4. **Deploy**:
   Click **Deploy**. Streamlit Cloud automatically reads `requirements.txt` and `.streamlit/config.toml` and provides a public live URL!

---

## 🐳 Option 2: Docker Container (Local or Cloud Server)

### Prerequisites:
- Docker Desktop or Docker Engine installed.

### Build and Run with Docker:
```bash
# Build the Docker image
docker build -t cardio-risk-app .

# Run the container
docker run -d -p 8501:8501 --name cardio-risk-container cardio-risk-app
```
Access the application at `http://localhost:8501`.

### Run with Docker Compose:
```bash
docker compose up -d
```
To stop the container:
```bash
docker compose down
```

---

## 🤗 Option 3: Hugging Face Spaces (Gradio / Streamlit)

1. Create a new Space on [huggingface.co/spaces](https://huggingface.co/spaces).
2. Choose **Streamlit** as the Space SDK.
3. Set visibility to **Public**.
4. Clone the space repository and push your project files (`app.py`, `src/`, `models/`, `requirements.txt`).
5. Hugging Face Spaces will build and deploy the container automatically.

---

## 💻 Option 4: Local Development

```bash
# 1. Clone repository
git clone https://github.com/<your-username>/Personalized_Cardiovascular_Risk_Assessment.git
cd Personalized_Cardiovascular_Risk_Assessment

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # Or on Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch app
streamlit run app.py
```
