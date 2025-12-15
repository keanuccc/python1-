from sklearn.decomposition import PCA
import pandas as pd

def run_pca(df: pd.DataFrame, n_components: int = 3):
    pca = PCA(n_components=n_components)
    scores = pca.fit_transform(df.iloc[:, 2:])

    return {
        "scores": pd.DataFrame(
            scores,
            columns=[f"PC{i+1}" for i in range(n_components)]
        ),
        "loadings": pd.DataFrame(
            pca.components_.T,
            index=df.columns[2:],
            columns=[f"PC{i+1}" for i in range(n_components)]
        ),
        "explained_variance_ratio": pca.explained_variance_ratio_
    }

