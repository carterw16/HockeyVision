from deep_sort.deep_sort.tracker import Tracker as DeepSortTracker
from deep_sort.tools import generate_detections as gdet
from deep_sort.deep_sort import nn_matching
from deep_sort.deep_sort.detection import Detection
import numpy as np
import os


class Tracker:
    tracker = None
    encoder = None
    tracks = None
    scene = None

    def __init__(self):
        max_cosine_distance = 0.4
        nn_budget = None

        # encoder_model_filename = 'model_data/mars-small128.pb'
        encoder_model_filename = os.path.join(os.path.dirname(__file__), 'model_data', 'mars-small128.pb')

        metric = nn_matching.NearestNeighborDistanceMetric("cosine", max_cosine_distance, nn_budget)
        self.tracker = DeepSortTracker(metric)
        self.encoder = gdet.create_box_encoder(encoder_model_filename, batch_size=1)
        self.scene = 0

    def update(self, frame, detections):

        bboxes = np.asarray([d[:-1] for d in detections])
        if len(bboxes) > 0:
            bboxes[:, 2:] = bboxes[:, 2:] - bboxes[:, 0:2]
        scores = [d[-1] for d in detections]

        features = self.encoder(frame, bboxes)

        dets = []
        for bbox_id, bbox in enumerate(bboxes):
            dets.append(Detection(bbox, scores[bbox_id], features[bbox_id]))

        self.tracker.predict()
        self.tracker.update(dets, frame)
        self.update_tracks()

    def update_tracks(self):
        self.scene += 1
        tracks = []
        for track in self.tracker.tracks:
            if not track.is_confirmed() or track.time_since_update > 1:
                continue

            bbox = track.to_tlbr()

            id = track.track_id
            features = np.array(track.features_history).mean(axis=0)
            frames = track.frames_history
            bboxes = track.bbox_history
            age = track.age
            tracks.append(Track(id, bbox, features, self.scene, age, frames, bboxes))

        self.tracks = tracks


class Track:
    track_id = None
    bbox = None
    features = None
    last_scene = None
    age = None
    saved_frames = None
    saved_bboxes = None

    def __init__(self, id, bbox, features, last_scene, age, frames, bboxes):
        self.track_id = id
        self.bbox = bbox
        self.features = features
        self.last_scene = last_scene
        self.age = age
        self.saved_frames = frames
        self.saved_bboxes = bboxes