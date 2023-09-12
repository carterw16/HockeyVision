import os, random, datetime
import numpy as np
from kmeans import kMeans, cluster
import psycopg2
import cv2
from ultralytics import YOLO
from tracker import Tracker
from matplotlib import pyplot as plt
from dotenv import load_dotenv
import boto3
from storage import send_data

def track_video(input_file='2persontrack.mov', output_file='out.mp4'):
    video_path = os.path.join(os.path.dirname(__file__), 'data', input_file)
    video_out_path = os.path.join(os.path.dirname(__file__), output_file)

    cap = cv2.VideoCapture(video_path)
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    frames_left = frames
    fps = cap.get(cv2.CAP_PROP_FPS)

    ret, frame = cap.read()
    shape = frame.shape

    cap_out = cv2.VideoWriter(
        video_out_path,
        cv2.VideoWriter_fourcc(*'avc1'),
        cap.get(cv2.CAP_PROP_FPS),
        (frame.shape[1], frame.shape[0]))

    model = YOLO("yolov8n.pt")

    tracker = Tracker()

    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for j in range(10)]
    track_history = {}
    # frame_history = {}
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

                # frame_history.setdefault(track_id, []).append(frame[int(y1):int(y2),int(x1):int(x2)])

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

    return track_history, fps, shape


def main():
    input_file = 'd5vid_short.mov'
    output_file_name = os.path.splitext(input_file)[0]+'out'
    track_hist, fps, shape = track_video(input_file, output_file_name+'.mp4')
    grouped_tracks = cluster(track_hist)
    frame_width = shape[1]
    frame_height = shape[0]
    send_data(
        vid_name=output_file_name,
        game_name='d5_shortgame',
        cluster_dict=grouped_tracks,
        fps=fps,
        frame_width=frame_width,
        frame_height=frame_height
        )
    print(grouped_tracks)

if __name__ == "__main__":
    main()
