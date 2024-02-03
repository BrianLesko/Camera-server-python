# Brian Joseph Lesko 
# 2/1/24
# Create a LAN server that hosts a live data feed generated from the host machine 
# Run the app with streamlit run app.py --server.address 0.0.0.0 --server.port 8501
# access the app from another device through the host machine's IP address and the port 8501 ip:port

import streamlit as st
import numpy as np
import time
import cv2 # pip install opencv-python-headless

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_BRIGHTNESS, 1)

@st.cache_data(max_entries=10, ttl=60)
def get_frame_1(time):
    data = np.random.rand(300, 300)
    return data

@st.cache_data(max_entries=10, ttl=60)
def get_frame(time):
    global camera
    try: 
        _, frame = camera.read()
        frame = cv2.convertScaleAbs(frame, alpha=1, beta=50)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
    except:
        return np.zeros((300, 300, 3))

def main():
    st.title("Live Camera Feed")
    image_spot = st.image([])

    while True:
        data = get_frame(time.time())
        image_spot.image(data, use_column_width=True)

main() 