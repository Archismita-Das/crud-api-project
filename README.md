# CRUD API Project using FastAPI and React

## Overview

This project is a full-stack CRUD (Create, Read, Update, Delete) application developed as part of the Associate Developer Internship task.

The project consists of:
- FastAPI Backend
- React Frontend
- CRUD Operations
- API Integration

---

# Technologies Used

## Backend
- Python
- FastAPI
- Uvicorn

## Frontend
- React
- Vite
- JavaScript

---

# Features

## CREATE
Add new student records dynamically.

## READ
Fetch and display all students from backend API.

## UPDATE
Update existing student records.

## DELETE
Delete student records dynamically.

---

# Project Structure

```text
crud-api-project/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── package.json
│
├── README.md
```

---

# Backend Setup

## Go to backend folder

```bash
cd backend
```

## Install dependencies

```bash
pip install fastapi uvicorn
```

## Run backend server

```bash
python -m uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Frontend Setup

## Go to frontend folder

```bash
cd frontend
```

## Install dependencies

```bash
npm install
```

## Run frontend

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /students | Fetch all students |
| POST | /students | Add new student |
| PUT | /students/{id} | Update student |
| DELETE | /students/{id} | Delete student |

---

# React Concepts Used

- useState
- useEffect
- Fetch API
- Component Rendering
- State Management

---

# FastAPI Concepts Used

- REST APIs
- CRUD Operations
- Routing
- JSON Handling
- CORS Middleware

---

# Learning Outcome

This project helped in understanding:
- Full-stack development workflow
- Backend API development
- Frontend-backend integration
- CRUD operations
- React state management
- API testing and handling

---

# Developed By

Archismita Das
Associate Developer Intern
