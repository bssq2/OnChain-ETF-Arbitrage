import numpy as np, pandas as pd
from sklearn.decomposition import PCA

def main():
    data = {
        'AAPL': np.random.normal(0.001, 0.01, 30),
        'GOOG': np.random.normal(0.0012, 0.009, 30),
        'TSLA': np.random.normal(0.002, 0.015, 30),
        'AMZN': np.random.normal(0.0008, 0.01, 30),
        'MSFT': np.random.normal(0.0011, 0.008, 30),
    }
    df = pd.DataFrame(data)
    pca = PCA(n_components=2).fit(df)
    pc1 = pca.components_[0]
    w = pc1 / np.sum(np.abs(pc1))
    print("PC1 weights:")
    for t, weight in zip(df.columns, w):
        print(f"{t}: {weight:.4f}")

if __name__ == "__main__":
    main()