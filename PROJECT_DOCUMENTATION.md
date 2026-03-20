# CHATTERBOX – Real-Time WebSocket Chat Application  
## Full Project Documentation  

**Author:** Siddhi Kumari  
**Project Type:** Full Stack Web Application  
**Technologies Used:** FastAPI, WebSockets, SQLite, JWT, HTML, CSS, JavaScript  

---

## 1. Introduction

### 1.1 Project Overview

ChatterBox is a full-stack real-time chat application developed using FastAPI and WebSockets. The system enables secure user registration and login, real-time messaging, automated moderation, and an admin monitoring dashboard.

The platform demonstrates modern backend architecture, secure authentication using JWT, and real-time communication handling.

### 1.2 Objectives

- Implement real-time communication using WebSockets  
- Design secure JWT-based authentication  
- Implement role-based access control  
- Create an admin monitoring system  
- Build automated moderation for chat messages  
- Manage data efficiently using SQLite  

---

## 2. System Architecture

The application follows a client-server architecture.

Frontend (HTML/CSS/JavaScript) communicates with the FastAPI backend using:

- REST APIs (authentication & admin)
- WebSockets (real-time messaging)

The backend interacts with an SQLite database to store users and messages.

---

## 3. Technology Stack

### Backend
- FastAPI  
- SQLAlchemy  
- SQLite  
- Python-Jose (JWT handling)  
- Passlib (Password hashing)  
- WebSockets  

### Frontend
- HTML5  
- CSS3  
- JavaScript  
- Fetch API  

---

## 4. Functional Modules

### 4.1 Authentication Module

**Features**
- User Registration  
- User Login  
- JWT Token Generation  
- Role-based Authorization  
- Blocked User Detection  

**Security Measures**
- Password hashing using bcrypt  
- JWT tokens with expiration  
- Protected API routes  
- Admin-only endpoints  

---

### 4.2 Real-Time Chat Module

**Features**
- WebSocket-based messaging  
- Instant message broadcasting  
- Persistent message storage  
- Timestamp tracking  

**Workflow**
1. User logs in  
2. WebSocket connection established  
3. Message sent to server  
4. Message validated and stored  
5. Broadcast to other connected users  

---

### 4.3 Moderation System

**Purpose:** Maintain safe communication.

**Violation Handling**
- 1st violation → Warning  
- 2nd violation → Warning  
- 3rd violation → User automatically blocked  

Blocked users cannot:
- Log in  
- Send messages  
- Access chat system  

---

### 4.4 Admin Module

**Admin Capabilities**
- View all users  
- View blocked users  
- Monitor messages  
- Download reports (CSV)  

---

## 5. Database Design

### Users Table
- id (Primary Key)  
- username  
- email  
- password_hash  
- is_admin  
- is_blocked  
- warning_count  
- created_at  

### Messages Table
- id (Primary Key)  
- sender_id  
- content  
- timestamp  

---

## 6. API Endpoints

### Authentication
- POST `/register`
- POST `/login`

### Chat
- WebSocket `/ws`

### Admin
- GET `/admin/users`
- GET `/admin/messages`
- GET `/admin/download/users`
- GET `/admin/download/messages`

---

## 7. Security Implementation

- Password hashing using bcrypt  
- JWT-based authentication  
- Role-based route protection  
- Auto-block moderation system  

---

## 8. Testing

The system was manually tested for:

- User registration  
- Login validation  
- Role-based access control  
- Real-time chat functionality  
- Warning logic  
- Auto-block functionality  
- Admin report download  

All modules were verified for expected behavior.

---

## 9. Limitations

- SQLite not suitable for high-scale production  
- No cloud deployment yet  
- No group chat feature  
- Limited UI enhancements  

---

## 10. Future Enhancements

- Group chat rooms  
- Private messaging  
- PostgreSQL integration  
- Docker containerization  
- Cloud deployment  
- AI-based content moderation  
- File and image sharing  

---

## 11. Conclusion

ChatterBox successfully demonstrates:

- Real-time WebSocket communication  
- Secure JWT authentication  
- Role-based access control  
- Automated moderation system  
- Admin monitoring dashboard  

The project reflects a strong understanding of backend architecture, authentication mechanisms, and real-time system development.