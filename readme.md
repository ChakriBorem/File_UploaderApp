# 🌩️ Challenge 1: Cloud Platform Usage

---

## 🎯 Objective
A simple web app built with **Flask (Python)** that allows users to upload files to **Azure Blob Storage** through a clean web interface.  
The backend runs on Flask, while the app is deployed on **Vercel (serverless)** for free hosting.

---

## 🚀 Features
- Upload files directly to **Azure Blob Storage**
- Simple and responsive **HTML + CSS** frontend
- Flask backend API for file uploads
- Deployed on **Vercel** (Python serverless runtime)
- Supports file type validation and secure uploads

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Flask (Python) |
| Cloud Storage | Azure Blob Storage |
| Deployment | Vercel |

---

## ⚙️ Setup (Local Development)

```bash
# 1️⃣ Clone the repository
git clone https://github.com/ChakriBorem/File_UploaderApp.git
cd File_UploaderApp

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Create a .env file in the root directory
AZURE_STORAGE_CONNECTION_STRING=your_connection_string_here
CONTAINER_NAME=uploads

# 4️⃣ Run locally
python app.py

