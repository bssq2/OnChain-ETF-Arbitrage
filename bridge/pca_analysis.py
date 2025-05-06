"""
pca_analysis.py

Performs a basic PCA on mock ETF basket data to derive principal components
and suggests a rebalance ratio.

Requirements:
    pip install numpy pandas scikit-learn
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def main():
    # Mock data: 5 tickers, 30 days of returns
    data = {
        'AAPL': np.random.normal(0.001, 0.01, 30),
        'GOOG': np.random.normal(0.0012, 0.009, 30),
        'TSLA': np.random.normal(0.002, 0.015, 30),
        'AMZN': np.random.normal(0.0008, 0.01, 30),
        'MSFT': np.random.normal(0.0011, 0.008, 30),
    }
    df = pd.DataFrame(data)

    # PCA
    pca = PCA(n_components=2)
    pca.fit(df)

    # Principal Components
    components = pca.components_
    explained_variance = pca.explained_variance_ratio_

    print("Principal Components:")
    print(components)
    print("Explained Variance Ratio:", explained_variance)

    # A naive approach might be to use the first principal component weights
    # to define target weighting for these tickers
    pc1 = components[0]
    normalized = pc1 / np.sum(np.abs(pc1))

    print("\nSuggested weighting based on PC1:")
    for idx, ticker in enumerate(df.columns):
        print(f"{ticker}: {normalized[idx]:.4f}")

if __name__ == "__main__":
    main()