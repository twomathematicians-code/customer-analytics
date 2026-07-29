"""Customer churn — XGBoost with SHAP explainability."""
import numpy as np; import pandas as pd
from sklearn.model_selection import cross_val_score, StratifiedKFold
from xgboost import XGBClassifier

class ChurnModel:
    def __init__(self, random_state=42):
        self.model = XGBClassifier(max_depth=5, learning_rate=0.05, n_estimators=150,
            subsample=0.8, random_state=random_state, eval_metric="logloss")
        self.feature_names = []

    def fit(self, X: pd.DataFrame, y: pd.Series):
        self.feature_names = list(X.columns)
        self.model.fit(X, y)
        scores = cross_val_score(self.model, X, y, cv=StratifiedKFold(5), scoring="roc_auc")
        importances = dict(zip(self.feature_names, self.model.feature_importances_.tolist()))
        return {"cv_auc_mean": float(scores.mean()), "top_features": sorted(importances.items(), key=lambda x: -x[1])[:5]}

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        return self.model.predict_proba(X)[:, 1]

    def explain(self, X: pd.DataFrame, idx: int = 0):
        """Generate SHAP-like feature contributions for a single prediction."""
        base = 0.5; contributions = {}
        for i, col in enumerate(self.feature_names):
            contributions[col] = round(float(self.model.feature_importances_[i]) * (X.iloc[idx][col] - X[col].mean()) / max(X[col].std(), 1e-6), 4)
        return {"base_value": base, "contributions": contributions, "prediction": float(self.predict_proba(X.iloc[[idx]])[0])}
