from setuptools import setup, find_packages

setup(
    name="personalized-cardiovascular-risk-assessment",
    version="1.0.0",
    description="Personalized Cardiovascular Risk Assessment using Clinical Health Metrics and Explainable AI (TreeSHAP)",
    author="Cardiovascular ML Research Team",
    packages=find_packages(include=["src", "src.*"]),
    python_requires=">=3.9",
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
        "xgboost>=2.0.0",
        "shap>=0.44.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "joblib>=1.3.0",
        "streamlit>=1.30.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "flake8>=6.1.0",
            "black>=23.9.0",
            "isort>=5.12.0",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
    ],
)
