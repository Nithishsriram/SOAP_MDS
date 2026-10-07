from sklearn.manifold import MDS

mds = MDS(
    n_components=2,
    metric=True,
    dissimilarity='precomputed',
    n_init=10,
    max_iter=3000,
    random_state=42
)

embedding = mds.fit_transform(distance_matrix)

print(embedding)