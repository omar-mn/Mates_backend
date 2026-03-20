# 🚀 Mates Backend

Backend service for **Mates**, a real-time chat and community application where users can join rooms and communicate instantly.

> ⚡ This project is built as a backend learning journey using Django, REST APIs, and WebSockets.

---

## 📌 Overview

Mates is a chat-based platform that allows users to:
- Join public or private rooms
- Communicate in real-time
- Build small communities and interact together

This backend focuses on building scalable APIs and real-time communication.

---

## 🛠 Tech Stack

- **Language:** Python
- **Framework:** Django + Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (dj-rest-auth)
- **Realtime:** Django Channels (WebSockets)

---

## ✨ Features

### ✅ Implemented (MVP)
- User authentication (Register / Login)
- JWT-based authentication
- Create & join chat rooms (public / private)
- Real-time messaging using WebSockets
- Room-based chat system
- Retrieve messages per room

### 🚧 Coming Soon
- One-to-one chat
- User profile images
- Email verification
- Hidden/private rooms enhancements
- Online members indicator
- Emojis, reactions, and stickers
- File uploads
- Notifications system

---

## 🧱 Project Structure

```
backend/
│
├── Mates/         # Core project settings
├── Users/         # Custom user model & auth logic
├── Rooms/         # Rooms & memberships
├── Messages/      # Messaging + WebSocket consumers
├── media/         # Uploaded files
├── static/        # Static files
│
├── manage.py
├── requirements.txt
└── build.sh
```

### 🔹 Architecture

- **Models** → Database structure  
- **Serializers** → Data formatting  
- **Views (API Views)** → HTTP endpoints  
- **Consumers** → WebSocket handling  

---

## 🌐 API Endpoints

### 🔐 Auth
- `POST /api/auth/registration/`
- `POST /api/auth/login/`
- `GET /api/auth/user/`

### 💬 Rooms
- `GET /api/rooms/`

### 📨 Messages
- `GET /api/messages/<room_id>/`

### ⚡ WebSocket

```
ws://{base_url}/ws/message/<room_id>/?token=<JWT_TOKEN>
```

Example:
```
ws://localhost:8000/ws/message/3/?token=your_token_here
```

---

## 🗄 Database Models

- **Account** → Custom user model  
- **Room** → Chat rooms (public/private)  
- **Membership** → Join/leave system  
- **JoinRequest** → Room access requests  
- **Message** → Chat messages  

---

## ⚙️ Run Locally

```bash
git clone https://github.com/omar-mn/Mates_backend.git
cd Mates_backend

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

> ⚠️ Make sure PostgreSQL is running and configured correctly in your settings.

---

## 📡 API Docs

Postman Workspace:  
https://sudoers-3102.postman.co/workspace/5ea84f5f-1961-427e-8ca4-98dc629e550b

---

## 📊 Project Status

🚧 **Current Status:** MVP

### ✔️ Completed
- Authentication system
- Room system (public/private)
- Real-time messaging

### 🔜 Planned
- Profile system
- Email verification
- Reactions & emojis
- Online presence
- Performance improvements

---

## 🔗 Related Repositories

- Backend: https://github.com/omar-mn/Mates_backend  
- Frontend: https://github.com/omar-mn/Mates-Front  

---

## 💡 Author

Built by Omar Ali as part of a backend learning journey 🚀
