"""Bootstrap confidence interval for a metric."""
import numpy as np

def bootstrap_mean(values, n_boot=2000, seed=42, confidence=0.95):
    rng = np.random.default_rng(seed)
    values = np.asarray(values)
    samples = rng.choice(values, size=(n_boot, len(values)), replace=True).mean(axis=1)
    alpha = (1 - confidence) / 2
    return {
        "estimate": float(values.mean()),
        "lower": float(np.quantile(samples, alpha)),
        "upper": float(np.quantile(samples, 1 - alpha)),
    }
