# Face Recognition Attendance System

This is a simple real-time **Face Recognition Attendance System** built using Python, OpenCV, and the face recognition library.

## 📌 Features
- Detects and recognizes known faces from webcam
- Automatically logs attendance to a CSV file
- Lightweight and easy to use
- Uses face embeddings for high accuracy

## 🗂️ Folder Structure

```
FaceRecognitionAttendance/
├── attendance.py         # Main script
├── attendance.csv        # CSV file that logs attendance
└── known_faces/          # Folder for known face images (e.g., sridhar.jpg)
```

## 🚀 How to Run

### 1. Install Dependencies

pip install opencv-python face-recognition numpy
```

> **Note:** You may also need to install `dlib` which is required by `face_recognition`. Use:

pip install dlib
```

### 2. Add Known Faces

Place clear front-facing images of people you want to recognize inside the `known_faces/` folder. Name the files as the person's name, e.g.:

```
known_faces/
├── sridhar.jpg
├── john_doe.jpg
```

### 3. Run the Program

python attendance.py
```

- The webcam will open and start detecting faces.
- If a known face is detected, it will be marked in `attendance.csv` with the current time.

## 📁 Sample Output

```
Name,Time
SRIDHAR,13:05:22
JOHN_DOE,13:06:01
```

## 💡 Future Improvements

- Add GUI using Tkinter
- Use SQLite or Firebase for persistent attendance storage
- Add login/authentication system for admin
- Display real-time analytics

---

Built for educational purposes.
