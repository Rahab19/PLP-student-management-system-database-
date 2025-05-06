# PLP-student-management-system-database-

A MySQL-based database system  for managing student data, course enrollments, and academic performance using **FastAPI** and **MySQL**.

---

## 📌 Features

- Store student details: name, gender, date of birth, email
- Manage available courses by department
- Record course enrollments per student
- Track student grades for each course
- RESTful API built with FastAPI
- MySQL as the backend relational database
- Full CRUD support (Create, Read, Update, Delete)

---

## 🗂️ Database Structure

The system consists of four core tables:

1. `students`
2. `courses`
3. `enrollments`
4. `grades`

## 📬 API Endpoints Overview

| Method | Endpoint             | Description             |
|--------|----------------------|-------------------------|
| POST   | /students/           | Add a new student       |
| GET    | /students/           | Get all students        |
| PUT    | /students/{id}       | Update student info     |
| DELETE | /students/{id}       | Delete a student        |
| POST   | /courses/            | Add a new course        |
| GET    | /courses/            | Get all courses         |
| POST   | /enrollments/        | Enroll a student        |
| PUT    | /enrollments/{id}    | Update enrollment       |
| DELETE | /enrollments/{id}    | Delete enrollment       |
| POST   | /grades/             | Record a grade          |
| PUT    | /grades/{id}         | Update grade            |
| DELETE | /grades/{id}         | Delete grade            |


## 🚀 Getting Started

### 1. Clone the Repository

```bash
https://github.com/Rahab19/PLP-student-management-system-database-.git
cd student-api
```
### 2. Import the database

```bash
mysql -u root  -p < student_records.sql
```

### 3. Python packages installation

```bash
pip install -r requirements.txt
```
