import face_recognition
import cv2
import numpy as np
import pandas as pd
import pyttsx3
import os
import tkinter as tk
from tkinter import ttk
from datetime import datetime


engine = pyttsx3.init()
engine.setProperty("rate", 150)  


subjects = ["Mathematics II", "PPS", "BEEE", "TE", "BME"]


def select_subject():
    def on_submit():
        global selected_subject
        selected_subject = subject_var.get()
        root.destroy()

    root = tk.Tk()
    root.title("Select Subject")
    tk.Label(root, text="Choose a subject:", font=("Arial", 12)).pack(pady=10)
    
    subject_var = tk.StringVar()
    dropdown = ttk.Combobox(root, textvariable=subject_var, values=subjects, state="readonly")
    dropdown.pack(pady=5)
    dropdown.current(0)  

    submit_btn = tk.Button(root, text="Submit", command=on_submit)
    submit_btn.pack(pady=10)
    
    root.mainloop()


selected_subject = ""
select_subject()


known_face_encodings = []
known_face_names = []

def encode_face(image_path, name):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    if encodings:
        known_face_encodings.append(encodings[0])
        known_face_names.append(name)


encode_face(r"path_to_image\image_name.jpg", "person_name")
encode_face(r"path_to_image\image_name.jpg", "person_name")
encode_face(r"path_to_image\image_name.jpg", "person_name")



video_capture = cv2.VideoCapture(0)


today_date = datetime.now().strftime("%Y-%m-%d")
file_path = f"attendance_{today_date}.xlsx"


if not os.path.exists(file_path):
    df = pd.DataFrame(columns=["Name", "Subject", "Time"])
    df.to_excel(file_path, index=False)


def mark_attendance(name):
    df = pd.read_excel(file_path)
    

    if not ((df["Name"] == name) & (df["Subject"] == selected_subject)).any():
        now = datetime.now()
        time_string = now.strftime("%Y-%m-%d %H:%M:%S")
        
        
        new_entry = pd.DataFrame({"Name": [name], "Subject": [selected_subject], "Time": [time_string]})
        df = pd.concat([df, new_entry], ignore_index=True)
        
        
        df.to_excel(file_path, index=False)
        
        
        print(f"Attendance marked for {name} in {selected_subject} at {time_string}")
        engine.say(f"{name}, Present for {selected_subject}")
        engine.runAndWait()

while True:
    ret, frame = video_capture.read()

    
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    
    face_locations = [(top * 4, right * 4, bottom * 4, left * 4) for (top, right, bottom, left) in face_locations]

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if matches:
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)


        if name != "Unknown":
            mark_attendance(name)

    
    cv2.imshow('Video', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()