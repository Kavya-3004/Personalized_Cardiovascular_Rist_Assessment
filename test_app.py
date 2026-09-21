"""
Application and Integration Verification Suite
Personalized Cardiovascular Risk Assessment

Tests app import, end-to-end inference flow, and explicit verification criteria:
1. Valid patient prediction
2. Invalid/missing features handling
3. Probability output bounds and formatting
4. Risk-level classification thresholds
5. SHAP explanation generation
6. Full Streamlit app integration scenarios (Test Cases 1, 2, and 3)
"""

import os
import sys
import unittest
from pathlib import Path
import pandas as pd

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.predict import (
    predict_cardiovascular_risk,
    get_patient_summary,
    FEATURE_NAMES,
    DEFAULT_MODEL_PATH
)
from src.explain import (
    explain_prediction,
    plot_patient_shap,
    DISPLAY_NAMES
)


class TestStreamlitAppIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        test_csv_path = PROJECT_ROOT / "data" / "processed" / "test.csv"
        cls.test_df = pd.read_csv(test_csv_path)
        cls.valid_patient = {k: float(cls.test_df.iloc[0][k]) for k in FEATURE_NAMES}

    def test_app_file_syntax_and_imports(self):
        """Verifies app.py compiles, imports successfully, and contains main()."""
        import app
        self.assertTrue(hasattr(app, "main"), "app.py is missing main() function!")

    def test_valid_patient_prediction(self):
        """Verifies valid patient inputs produce structured prediction output."""
        res = predict_cardiovascular_risk(self.valid_patient)
        self.assertIsInstance(res, dict)
        self.assertIn("predicted_class", res)
        self.assertIn(res["predicted_class"], [0, 1])
        self.assertIn("prediction_label", res)
        self.assertIn(res["prediction_label"], ["No Heart Disease", "Heart Disease Detected"])
        self.assertIn("disease_probability", res)
        self.assertIn("disease_probability_percent", res)
        self.assertIn("risk_level", res)

    def test_invalid_missing_features(self):
        """Verifies that missing or incomplete feature inputs raise a clean ValueError."""
        incomplete_patient = {"age": 55.0, "sex": 1.0}
        with self.assertRaises(ValueError) as ctx:
            predict_cardiovascular_risk(incomplete_patient)
        self.assertIn("missing required features", str(ctx.exception).lower())

    def test_probability_output(self):
        """Verifies probability is strictly within [0.0, 1.0] and percent formatting is exact."""
        res = predict_cardiovascular_risk(self.valid_patient)
        prob = res["disease_probability"]
        self.assertGreaterEqual(prob, 0.0)
        self.assertLessEqual(prob, 1.0)
        self.assertAlmostEqual(res["disease_probability_percent"], round(prob * 100.0, 2), places=2)

    def test_risk_level_classification(self):
        """Verifies risk-level mapping follows presentation bands (<0.30 LOW, 0.30-0.60 MEDIUM, >0.60 HIGH)."""
        res = predict_cardiovascular_risk(self.valid_patient)
        prob = res["disease_probability"]
        risk = res["risk_level"]

        if prob < 0.30:
            self.assertEqual(risk, "LOW")
        elif prob <= 0.60:
            self.assertEqual(risk, "MEDIUM")
        else:
            self.assertEqual(risk, "HIGH")

    def test_shap_explanation_generation(self):
        """Verifies SHAP explanation returns top 5 valid features with correct directions and numeric values."""
        shap_factors = explain_prediction(self.valid_patient, top_n=5)
        self.assertIsInstance(shap_factors, list)
        self.assertEqual(len(shap_factors), 5)

        for factor in shap_factors:
            self.assertIn("feature", factor)
            self.assertIn(factor["feature"], FEATURE_NAMES)
            self.assertIn("display_name", factor)
            self.assertEqual(factor["display_name"], DISPLAY_NAMES[factor["feature"]])
            self.assertIsInstance(factor["shap_value"], float)
            self.assertIsInstance(factor["importance"], float)
            self.assertAlmostEqual(factor["importance"], abs(factor["shap_value"]), places=4)

            if factor["shap_value"] > 0:
                self.assertEqual(factor["direction"], "increases risk")
            else:
                self.assertEqual(factor["direction"], "decreases risk")

    def test_case_1_real_patient_from_test_csv(self):
        """Test Case 1: Real patient row from data/processed/test.csv."""
        res = predict_cardiovascular_risk(self.valid_patient)
        summary = get_patient_summary(self.valid_patient)
        shap_factors = explain_prediction(self.valid_patient, top_n=5)

        chart_path = PROJECT_ROOT / "outputs" / "shap_test_case_1.png"
        plot_patient_shap(self.valid_patient, output_path=str(chart_path), top_n=5)
        self.assertTrue(chart_path.exists())

        print("\n=== TEST CASE 1 (Real Test Patient Row 0) ===")
        print(f"Prediction: {res['prediction_label']} ({res['disease_probability_percent']:.1f}%)")
        print(f"Risk Level: {res['risk_level']}")
        print(f"Top SHAP Factor: {shap_factors[0]['display_name']} ({shap_factors[0]['direction']})")

    def test_case_2_manually_entered_patient(self):
        """Test Case 2: Manually entered patient with elevated clinical markers."""
        high_risk_patient = {
            "age": 63.0,
            "sex": 1.0,         # Male
            "cp": 4.0,          # Asymptomatic
            "trestbps": 160.0,   # High BP
            "chol": 286.0,      # Elevated Cholesterol
            "fbs": 1.0,         # Elevated FBS
            "restecg": 2.0,     # LVH
            "thalach": 108.0,   # Low Max HR
            "exang": 1.0,       # Angina present
            "oldpeak": 3.4,     # Significant ST depression
            "slope": 2.0,       # Flat slope
            "ca": 2.0,          # 2 vessels
            "thal": 7.0         # Reversible defect
        }

        res = predict_cardiovascular_risk(high_risk_patient)
        summary = get_patient_summary(high_risk_patient)
        shap_factors = explain_prediction(high_risk_patient, top_n=5)

        self.assertEqual(res["predicted_class"], 1)
        self.assertEqual(res["risk_level"], "HIGH")
        self.assertGreater(res["disease_probability"], 0.60)

        print("\n=== TEST CASE 2 (Manually Entered High-Risk Patient) ===")
        print(f"Prediction: {res['prediction_label']} ({res['disease_probability_percent']:.1f}%)")
        print(f"Risk Level: {res['risk_level']}")
        print(f"Top 3 SHAP Factors:")
        for i, f in enumerate(shap_factors[:3], 1):
            print(f"  {i}. {f['display_name']} ({f['shap_value']:+.4f}) -> {f['direction']}")

    def test_case_3_invalid_input_scenario(self):
        """Test Case 3: Invalid input scenario (missing features error handling)."""
        invalid_patient = {"age": 50.0, "sex": 1.0}
        with self.assertRaises(ValueError) as ctx:
            predict_cardiovascular_risk(invalid_patient)

        self.assertIn("missing required features", str(ctx.exception))
        print("\n=== TEST CASE 3 (Invalid Input Handled Gracefully) ===")
        print(f"Successfully caught expected validation error: {ctx.exception}")


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStreamlitAppIntegration)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)
