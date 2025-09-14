import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Load known face images
path = 'known_faces'
images = []
names = []
for file in os.listdir(path):
    img = cv2.imread(f'{path}/{file}')
    images.append(img)
    names.append(os.path.splitext(file)[0])

# Encode faces
def find_encodings(images):
    encoded_list = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if encodings:
            encoded_list.append(encodings[0])
    return encoded_list

known_encodings = find_encodings(images)

# Mark attendance
def mark_attendance(name):
    with open('attendance.csv', 'r+') as f:
        lines = f.readlines()
        name_list = [line.split(',')[0] for line in lines]
        if name not in name_list:
            now = datetime.now()
            time_str = now.strftime('%H:%M:%S')
            f.write(f'{name},{time_str}\n')

# Initialize webcam
cap = cv2.VideoCapture(0)

print("🔍 Scanning for faces...")

while True:
    success, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    faces_cur_frame = face_recognition.face_locations(rgb_small_frame)
    encodes_cur_frame = face_recognition.face_encodings(rgb_small_frame, faces_cur_frame)

    for encode_face, face_loc in zip(encodes_cur_frame, faces_cur_frame):
        matches = face_recognition.compare_faces(known_encodings, encode_face)
        face_dist = face_recognition.face_distance(known_encodings, encode_face)

        if len(face_dist) > 0:
            match_index = np.argmin(face_dist)
            if matches[match_index]:
                name = names[match_index].upper()
                y1, x2, y2, x1 = face_loc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

                # Draw box and name
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1+6, y2-6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                mark_attendance(name)

    cv2.imshow('Face Recognition Attendance', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
