import psycopg2
from datetime import date
from dotenv import load_dotenv
import os
from s3_upload import upload_file
import cv2

def send_data(vid_name=None, game_name=None, cluster_dict=None, fps=None, frame_width=None, frame_height=None):
    upload_file(vid_name+'.mp4', 'hockeyvision-videos', vid_name)

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
    if game_name is not None:
        cur.execute(
            'INSERT INTO public.myapp_game (date, title) VALUES (%s, %s) RETURNING id;',
            (date.today(), game_name))
    if vid_name is not None:
        game_id = cur.fetchone()[0]
        cur.execute(
            '''INSERT INTO public.myapp_video (name, game_id, fps, width, height)
                VALUES (%s, %s, %s, %s, %s) RETURNING id''',
            (vid_name, game_id, fps, frame_width, frame_height))
    if cluster_dict is not None:
        video_id = cur.fetchone()[0]
        for i, cluster in enumerate(cluster_dict.values()):
            cur.execute(
                'INSERT INTO public.myapp_cluster (predicted, junk, video_id) VALUES (%s, %s, %s) RETURNING id',
                (True, False, video_id))
            cluster_id = cur.fetchone()[0]
            for j, track in enumerate(cluster):
                bboxes = track.saved_bboxes
                lifetime = [track.last_scene - track.age, track.last_scene]
                cur.execute(
                'INSERT INTO public.myapp_track (pred_cluster_id, bboxes, lifetime, video_id) VALUES (%s, %s, %s, %s)',
                (cluster_id, bboxes, lifetime, video_id))
    conn.commit()
    conn.close()
