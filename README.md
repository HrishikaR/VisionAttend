# 🎓 VisionAttend – AI-Powered Smart Attendance System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?style=for-the-badge&logo=streamlit)
![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-green?style=for-the-badge&logo=supabase)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-orange?style=for-the-badge&logo=opencv)
![dlib](https://img.shields.io/badge/dlib-Face%20Recognition-purple?style=for-the-badge)
![Resemblyzer](https://img.shields.io/badge/Resemblyzer-Voice%20Recognition-yellow?style=for-the-badge)

**An AI-powered attendance management system that automates classroom attendance using Face Recognition, Voice Recognition, QR-based Enrollment, and Real-time Attendance Analytics.**

</div>

---

# 📖 Overview

VisionAttend is a smart attendance system designed to eliminate manual attendance processes by leveraging Artificial Intelligence and Computer Vision.

The application enables teachers to create subjects, enroll students using secure QR codes, register biometric data, and automatically mark attendance using classroom images and voice recordings.

The system combines facial recognition and speaker recognition to improve reliability while maintaining a simple and intuitive interface built with Streamlit.
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge)](https://visionattend-uq3y9wqypivnmzrujgv9nl.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)](https://github.com/HrishikaR/VisionAttend)
---

# ✨ Features

## 👨‍🏫 Teacher Features

- Secure Teacher Authentication
- Subject Management
- Create & Manage Classes
- QR Code Student Enrollment
- Automatic Attendance using Face Recognition
- Bulk Attendance using Voice Recognition
- Attendance History
- Student Attendance Reports
- Dashboard with Class Statistics

---

## 👨‍🎓 Student Features

- Student Registration
- Face Enrollment
- Voice Enrollment
- Join Subjects using QR Code
- View Registered Subjects
- View Attendance History

---

# 🧠 AI Modules

## 👤 Face Recognition

The system uses deep learning-based face recognition powered by **dlib**.

Pipeline:

```
Classroom Image
      ↓
Face Detection
      ↓
Face Alignment
      ↓
128-D Face Embedding
      ↓
SVM Classification
      ↓
Euclidean Distance Verification
      ↓
Attendance Marked
```

### Technologies

- dlib
- Face Landmark Detection
- Face Embeddings
- Support Vector Machine (SVM)
- Euclidean Distance Matching

---

## 🎤 Voice Recognition

The application also supports speaker identification using **Resemblyzer**.

Pipeline:

```
Voice Recording
      ↓
Audio Preprocessing
      ↓
Speaker Embedding
      ↓
Cosine Similarity
      ↓
Speaker Identification
```

### Technologies

- Resemblyzer
- Librosa
- Speaker Embeddings
- Cosine Similarity

---

# 🗂️ System Architecture

```
                Teacher / Student
                       │
                Streamlit Frontend
                       │
          ┌────────────┴────────────┐
          │                         │
   Face Recognition          Voice Recognition
          │                         │
      AI Models               AI Models
          │                         │
          └────────────┬────────────┘
                       │
                  Attendance Engine
                       │
                  Supabase Database
                       │
             Attendance Reports
```

---

# ⚙️ Tech Stack

## Frontend

- Streamlit

## Backend

- Python

## Database

- Supabase
- PostgreSQL

## AI / Machine Learning

- dlib
- Resemblyzer
- NumPy
- scikit-learn
- OpenCV
- Librosa

---

# 📁 Project Structure

```
VisionAttend/
│
├── app.py
├── db.py
├── face_pipeline.py
├── voice_pipeline.py
├── teacher.py
├── student.py
├── home.py
├── utils.py
├── assets/
├── models/
├── requirements.txt
└── README.md
```

---

# 🔐 Authentication

- Teacher Login
- Student Registration
- Password Hashing using bcrypt
- Session Management
- Secure QR-based Subject Enrollment

---

# 📸 Face Recognition Workflow

1. Student registers face.
2. Face embeddings are generated.
3. Embeddings are stored securely.
4. Teacher uploads classroom image.
5. Faces are detected.
6. Embeddings are extracted.
7. SVM predicts student identities.
8. Euclidean distance verifies predictions.
9. Attendance is recorded.

---

# 🎙️ Voice Recognition Workflow

1. Student registers voice.
2. Speaker embeddings are generated.
3. Voice embeddings are stored.
4. Teacher uploads classroom recording.
5. Audio is segmented.
6. Speaker embeddings are generated.
7. Cosine similarity identifies speakers.
8. Attendance is updated.

---

# 🗄️ Database Design

The application stores:

- Teachers
- Students
- Subjects
- Student Enrollments
- Face Embeddings
- Voice Embeddings
- Attendance Logs

Database relationships are managed using PostgreSQL through Supabase.

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/VisionAttend.git
```

```bash
cd VisionAttend
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
SUPABASE_URL=YOUR_URL
SUPABASE_KEY=YOUR_KEY
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 📊 Future Enhancements

- Real-time Camera Attendance
- Multi-Face Live Tracking
- Anti-Spoof Detection
- Attendance Notifications
- Cloud Deployment
- Face Mask Detection
- Multi-Classroom Support
- Attendance Analytics Dashboard

---

# 📚 Libraries Used

- Streamlit
- dlib
- OpenCV
- NumPy
- Librosa
- Resemblyzer
- scikit-learn
- bcrypt
- Supabase
- PostgreSQL

---

# 👥 Contributors

This project was developed as a collaborative academic project. Contributions include AI model integration, biometric attendance pipelines, database management, and application development.

---

# 📄 License

This project is intended for educational and research purposes.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star!

</div>
