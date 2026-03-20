# # # src/segmentation/cluster_customers.py
# # from sklearn.cluster import KMeans

# # def cluster_households(df, n_clusters=3):
# #     kmeans = KMeans(n_clusters=n_clusters, random_state=42)
# #     df['cluster'] = kmeans.fit_predict(df[['kWh']])
# #     return df

# # src/segmentation/cluster_customers.py
# from sklearn.cluster import KMeans

# def cluster_households(df, n_clusters=3):
#     kmeans = KMeans(n_clusters=n_clusters, random_state=42)
#     df['cluster'] = kmeans.fit_predict(df)
#     return df

from sklearn.cluster import KMeans

def cluster_households(df, n_clusters=3):
    """
    Cluster households based on aggregated statistics.
    Args:
        df (pd.DataFrame): Aggregated household stats with columns like mean, max, std, peak_ratio, variability.
        n_clusters (int): Number of clusters for KMeans.
    Returns:
        pd.DataFrame: Original df with a new 'cluster' column.
    """
    model = KMeans(n_clusters=n_clusters, random_state=42)
    df = df.copy()  # avoiding modifying original
    df["cluster"] = model.fit_predict(df)
    return df