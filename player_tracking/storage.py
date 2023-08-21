import psycopg2
from datetime import date
from dotenv import load_dotenv
import os
from s3_upload import upload_file
import cv2


def send_data(vid_name=None, game_name=None, cluster_dict=None):
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
            'INSERT INTO public.myapp_video (name, game_id) VALUES (%s, %s) RETURNING id',
            (vid_name, game_id))
    if cluster_dict is not None:
        video_id = cur.fetchone()[0]
        for i, cluster in enumerate(cluster_dict.values()):
            cur.execute(
                'INSERT INTO public.myapp_cluster (predicted, junk) VALUES (%s, %s) RETURNING id',
                (True, False))
            cluster_id = cur.fetchone()[0]
            for j, track in enumerate(cluster):
                track_frame = track.saved_frames[0]
                frame_name = 'cluster'+str(i)+'track'+str(j)
                filepath = 'track_frames/cluster'+str(i)+'track'+str(j)+'.jpg'
                if not os.path.exists('player_tracking/track_frames'):
                    os.mkdir('player_tracking/track_frames')
                cv2.imwrite('track_frames/'+frame_name+'.jpg',track_frame)
                upload_file(filepath, 'hockeyvision-videos', frame_name)
                cur.execute(
                'INSERT INTO public.myapp_track (pred_cluster, frame_name, video_id) VALUES (%s, %s, %s)',
                (cluster_id, frame_name, video_id))
    conn.commit()
    conn.close()
