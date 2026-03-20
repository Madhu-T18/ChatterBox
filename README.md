# 🚀 ChatterBox – Real-Time WebSocket Chat Application  

## 📌 Overview  

**ChatterBox** is a full-stack real-time chat application built using FastAPI and WebSockets.  
It supports secure authentication, instant messaging, automated moderation, and an admin monitoring dashboard.

This project demonstrates modern backend architecture, JWT-based authentication, and real-time communication handling.

---

## ✨ Features  

- 🔐 User Registration & Login  
- 🎫 JWT-based Authentication  
- 👤 Role-based Access (Admin & User)  
- 💬 Real-Time Chat using WebSockets  
- 🛡️ Automated Bad Word Detection  
- ⚠️ Warning & Auto-Block System  
- 📊 Admin Dashboard  
- 📥 CSV Report Download  
- 🗄️ SQLite Database Integration  

---

## 🛠️ Tech Stack  

### 🔹 Backend  
- FastAPI  
- SQLAlchemy  
- SQLite  
- Python-Jose (JWT)  
- Passlib (bcrypt)  
- WebSockets  

### 🔹 Frontend  
- HTML5  
- CSS3  
- JavaScript  
- Fetch API  

---

## 📂 Project Structure  

```
CHATTERBOX/
│
├── backend/
│   ├── app/
│   │   ├── admin/
│   │   │   ├── __init__.py
│   │   │   └── admin_routes.py
│   │   │
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   └── jwt.py
│   │   │
│   │   ├── chat/
│   │   │   ├── __init__.py
│   │   │   ├── chat_history.py
│   │   │   ├── messages.py
│   │   │   └── websocket.py
│   │   │
│   │   ├── ml/
│   │   │   ├── __init__.py
│   │   │   └── bad_word_model.py
│   │   │
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── security.py
│   │   │   └── time.py
│   │   │
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   ├── requirements.txt
│   └── run.py
│
├── frontend/
│   ├── admin/
│   ├── assets/
│   ├── css/
│   ├── js/
│   ├── chat.html
│   ├── index.html
│   └── register.html
│
├── LICENSE
├── PROJECT_DOCUMENTATION.md
└── README.md
```

---

## ⚙️ Installation Guide  

### 🔹 1️⃣ Clone the Repository  

```bash
git clone https://github.com/siddhi240900/ChatterBox-RealTime-Chat.git
cd ChatterBox-RealTime-Chat
```

---

### 🔹 2️⃣ Backend Setup  

```bash
cd backend
python -m venv venv
pip install -r requirements.txt
python run.py
```

Backend will run at:  

```
http://127.0.0.1:8000
```

---

### 🔹 3️⃣ Frontend Setup  

```bash
cd frontend
npm install
npm run dev
```

---

## 🔐 Admin Features  

Admin users can:  

- View all registered users  
- Monitor chat messages  
- View blocked users  
- Download reports in CSV format  

---

## 🛡️ Security Implementation  

- Password hashing using bcrypt  
- JWT token authentication  
- Role-based route protection  
- Auto-block moderation system  

---

## 📈 Future Improvements  

- Group chat functionality  
- Private messaging  
- PostgreSQL integration  
- Docker containerization  
- Cloud deployment  
- AI-powered moderation  

---

## 📜 License  

This project is licensed under the MIT License.
