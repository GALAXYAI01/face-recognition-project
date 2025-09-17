ATTENDX is a smart AI-powered attendance system that uses face recognition to automatically mark attendance. Built with Python, OpenCV, and Pandas, it eliminates manual roll calls, prevents proxy attendance, and ensures a fast, secure, and efficient attendance process.

✨ Features

🎥 Real-time Face Recognition – Detects and recognizes faces using a webcam

📝 Automated Attendance – Marks attendance directly in Excel (.xlsx)

🔊 Text-to-Speech (TTS) – Announces "Present" with the student’s name

📚 Subject-Wise Tracking – Dropdown menu to select subjects

🔄 Daily Reset – Fresh attendance sheet generated each day

🖥️ User-Friendly Interface – Simple and intuitive design

🛠️ Tech Stack

Programming Language: Python

Libraries:

OpenCV (video capture & image processing)

face_recognition (face detection & recognition)

Pandas (attendance management in Excel)

pyttsx3 (text-to-speech announcements)

openpyxl (Excel file support)

📂 Project Structure
ATTENDX/
│-- attendx.py        # Main project script
│-- requirements.txt  # Dependencies
│-- attendance/       # Stores daily attendance Excel files
│-- images/           # Known faces dataset (e.g., student photos)
│-- README.md         # Project documentation

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/ATTENDX.git
cd ATTENDX

2. Create a Virtual Environment
conda create --name attendx python=3.9 -y
conda activate attendx

3. Install Dependencies
pip install -r requirements.txt

4. Run the Project
python attendx.py

📊 Output Example

✅ Attendance marked in Excel file with name, subject, date & time

🔊 Audio output: “Present [Name]”

🎥 Live webcam feed with bounding box and name label

📌 Applications

🏫 Schools & Colleges – Seamless student attendance

🏢 Offices – Employee attendance tracking

🔒 Secure Areas – Access control & monitoring

🚀 Future Scope

Cloud-based attendance storage

Mobile app integration for remote monitoring

Multi-camera classroom support

Enhanced deep learning models for higher accuracy

🏷️ Keywords

AI · Face Recognition · Python · OpenCV · Attendance System · Pandas
