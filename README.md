# Face Attendance System

## Overview

The Face Attendance System is a Python-based application that automatically marks attendance using face recognition technology. Instead of taking attendance manually, the system detects a person's face through a webcam, recognizes the registered user, and records their attendance.

This project is simple to use and helps reduce the time required for attendance while avoiding manual errors.

---

## Features

* Register new users by capturing their face.
* Detect faces using a webcam.
* Recognize registered users.
* Mark attendance automatically.
* Save attendance records in an Excel file.
* View the list of registered users.
* Delete registered users when required.
* Easy-to-use interface.
* Fast and accurate face detection.

---

## Technologies Used

This project is developed using the following technologies:

* Python
* OpenCV
* Face Recognition
* NumPy
* Pickle
* OpenPyXL (for Excel files)
* Haar Cascade Classifier

---

## Project Structure

```
face-attendance-system/
│
├── models/
│   └── haarcascade_frontalface_default.xml
│
├── app.py
├── attendance_excel.py
├── camera_test.py
├── delete_registered.py
├── enroll_face.py
├── face_detection.py
├── view_registered.py
├── .gitignore
└── README.md
```

---

## File Description

### app.py

This is the main file of the project. It provides the main menu and connects all other modules together.

---

### enroll_face.py

This file is used to register a new person. It captures images from the webcam and stores the face information so that the person can be recognized later.

---

### face_detection.py

This file detects and recognizes faces using the trained face data. Once a registered face is recognized, attendance is marked automatically.

---

### attendance_excel.py

This file creates and updates the attendance sheet in Excel format.

---

### view_registered.py

This file displays all registered users.

---

### delete_registered.py

This file removes a registered user from the database.

---

### camera_test.py

This file checks whether the webcam is working correctly before using the application.

---

### models/

This folder contains the Haar Cascade XML file used for detecting human faces.

---

## How It Works

1. Open the application.
2. Register a new user by capturing their face.
3. The face data is saved.
4. Start face recognition.
5. The webcam detects faces.
6. If a registered face is found, the person's attendance is marked automatically.
7. Attendance is stored in an Excel file.

---

## Installation

### Step 1

Clone this repository.

```bash
git clone https://github.com/sathwik2157H/face-attendance-system.git
```

### Step 2

Move into the project folder.

```bash
cd face-attendance-system
```

### Step 3

Install the required Python packages.

```bash
pip install -r requirements.txt
```

### Step 4

Run the application.

```bash
python app.py
```

---

## Requirements

* Python 3.x
* Webcam
* Windows Operating System
* Required Python libraries

---

## Future Improvements

Some improvements that can be added in the future are:

* Database integration using MySQL or SQLite.
* User login and authentication.
* Better graphical user interface.
* Cloud storage for attendance records.
* Real-time dashboard.
* Email notifications.
* Face mask detection.
* Mobile application support.

---

## Learning Outcomes

By developing this project, I learned:

* Python programming
* OpenCV basics
* Face detection and recognition
* Working with Excel files
* File handling
* Object-oriented programming
* Git and GitHub
* Building a complete real-world application

---

## Author

**Malluvalasa Sathwik**

GitHub: https://github.com/sathwik2157H

---

## License

This project is created for learning and educational purposes.
