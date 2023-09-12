# HockeyVision
My Summer 2023 work with computer vision and deep learning using video from my local street hockey league. My working project contains a Python player tracking component, which identifies distinct players from input video, along with a Django backend along with a React.js frontend.

!["https://github.com/carterw16/yourrepo/raw/main/path/to/your/image.pngScreen Shot 2023-09-12 at 1.21.02 AM.png"](https://github.com/carterw16/HockeyVision/blob/main/Screen%20Shot%202023-09-12%20at%201.21.02%20AM.png)

## Player Tracking
The player tracking component of this project uses the YOLO and DeepSort algorithms to track players in an input game video. Image features for each concescutively tracked object are stored in my own Tracker object. Those track features are then fit with Sklearn's K-means cluster algorithm to group tracks with similar features (i.e tracks that are likely to be the same person). In this way, players can be reidentified after leaving the frame and returning later in the video. 

## Backend
The backend runs a Django API endoint. A PostgreSQL database stores data for games, videos, tracks, and clusters (groups of tracks predicted to correspond with one person). This data all comes from the player tracking component. 

## Frontend
The frontend is a React.js frontend which displays processed videos along with their associated clusters with example still frames indicating each person.

## Run Backend
`cd backend`
`python manage.py runserver`

## Run Frontend
`cd frontend`
`npm install`
`npm start`
