import os, random, datetime
import numpy as np
from kmeans import kMeans
import psycopg2
import cv2
from ultralytics import YOLO
from tracker import Tracker
from matplotlib import pyplot as plt
from dotenv import load_dotenv

def track_video(filename='2persontrack.mov'):
    video_path = os.path.join(os.path.dirname(__file__), 'data', filename)
    video_out_path = os.path.join(os.path.dirname(__file__), 'out.mp4')

    cap = cv2.VideoCapture(video_path)
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    frames_left = frames
    fps = cap.get(cv2.CAP_PROP_FPS)

    ret, frame = cap.read()

    cap_out = cv2.VideoWriter(video_out_path, cv2.VideoWriter_fourcc(*'MP4V'), cap.get(cv2.CAP_PROP_FPS),
                            (frame.shape[1], frame.shape[0]))

    model = YOLO("yolov8n.pt")

    tracker = Tracker()

    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for j in range(10)]
    track_history = {}
    frame_history = {}
    detection_threshold = 0.5
    while ret:
        results = model(frame, classes=[0])

        for result in results:
            detections = []
            for r in result.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = r
                x1 = int(x1)
                x2 = int(x2)
                y1 = int(y1)
                y2 = int(y2)
                class_id = int(class_id)
                if score > detection_threshold:
                    detections.append([x1, y1, x2, y2, score])
                

            tracker.update(frame, detections)

            for track in tracker.tracks:
                bbox = track.bbox
                x1, y1, x2, y2 = bbox
                track_id = track.track_id

                # if track_id not in track_history:
                #     track.saved_frames = frame[int(y1):int(y2),int(x1):int(x2)]
                # plt.imshow(track.saved_frame)
                frame_history.setdefault(track_id, []).append(frame[int(y1):int(y2),int(x1):int(x2)])
                # track_history.setdefault(track_id, [])
                track_history[track_id] = track
                color = (colors[track_id % len(colors)])
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 3)
                cv2.putText(frame, str(track_id), (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, color, 2, cv2.LINE_AA)

        frames_left -= 1
        seconds = round(frames_left / fps)
        video_time = datetime.timedelta(seconds=seconds)
        print(f"video time remaining: {video_time}")

        cap_out.write(frame)
        ret, frame = cap.read()

    cap.release()
    cap_out.release()
    cv2.destroyAllWindows()

    return track_history, frame_history

def cluster(track_hist, frame_hist):
    data = [track_hist[track].features for track in track_hist]
    kmeans = kMeans(data)
    grouped_tracks = {}

    for i, track in enumerate(track_hist):
        track_hist[track].saved_frames = frame_hist[track]
        grouped_tracks.setdefault(kmeans.labels_[i], []).append(track_hist[track])
    
    return grouped_tracks

def sendData():
    load_dotenv()
    DB_NAME = "hockeyvision"
    DB_USER = "postgres"
    DB_PASS = os.getenv("POSTGRES_PASSWORD")
    DB_HOST = "localhost"
    DB_PORT = "5432"
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                            host=DB_HOST, port=DB_PORT)
    print("Database connected successfully")

    cur = conn.cursor()
    cur.execute("""
        INSERT INTO public. (ID,NAME,EMAIL) VALUES
        (1,'Alan Walker','awalker@gmail.com'),
        (2,'Steve Jobs','sjobs@gmail.com')
    """)
    conn.commit()
    conn.close()


track_hist, frame_hist = track_video()
grouped_tracks = cluster(track_hist, frame_hist)

print(grouped_tracks)


