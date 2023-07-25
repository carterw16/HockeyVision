from sklearn.cluster import KMeans
import numpy as np

def kMeans(data):
  model = KMeans(n_init='auto', n_clusters=2, random_state=0)
  fitted = model.fit(data)
  return fitted