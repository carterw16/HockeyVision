from sklearn.cluster import KMeans
import numpy as np

def kMeans(data):
  model = KMeans(n_init='auto', n_clusters=5, random_state=0)
  fitted = model.fit(data)
  return fitted

def cluster(track_hist):
    data = [track_hist[track].features for track in track_hist]
    kmeans = kMeans(data)
    grouped_tracks = {}

    for i, track in enumerate(track_hist):
        # track_hist[track].saved_frames = frame_hist[track]
        grouped_tracks.setdefault(kmeans.labels_[i], []).append(track_hist[track])

    return grouped_tracks