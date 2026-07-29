#!/usr/bin/env python3
"""Customer churn model training pipeline."""
import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent.parent))

import logging, yaml, numpy as np
from src.models.train import ChurnModel

logging.basicConfig(level=logging.INFO)

def main():
    with open("configs/model_config.yaml") as f:
        cfg = yaml.safe_load(f)
    
    model = ChurnModel(random_state=cfg["model"]["random_state"])
    
    # Synthetic training data
    import pandas as pd
    n = 2000
    data = pd.DataFrame({
        "tenure_months": np.random.randint(1, 72, n),
        "monthly_charges": np.random.uniform(20, 120, n),
        "contract_type": np.random.choice([0, 1, 2], n, p=[0.5, 0.3, 0.2]),
        "num_tickets": np.random.randint(0, 10, n),
        "total_charges": np.random.uniform(100, 5000, n),
    })
    labels = ((data["num_tickets"] > 3) & (data["tenure_months"] < 12)).astype(int)
    
    metrics = model.fit(data, labels)
    logging.info("Churn model trained: CV AUC=%.3f", metrics["cv_auc_mean"])
    logging.info("Top features: %s", metrics["top_features"])

if __name__ == "__main__":
    main()
