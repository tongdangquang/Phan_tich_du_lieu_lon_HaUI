import pandas as pd
from sklearn.decomposition import PCA
from sklearn.datasets import load_breast_cancer

def extract_pca_features(n_col):
    df = load_breast_cancer()
    model = PCA(n_components=n_col)
    pca_result = model.fit_transform(df.data)
    return pca_result

pca_features = extract_pca_features(2)
pca_df = pd.DataFrame(pca_features)
pca_df.to_csv('pca_results.csv')