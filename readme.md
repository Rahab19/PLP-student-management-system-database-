# 🎓 Student Records Management System

A MySQL-based database system for managing student records, course enrollments, and academic performance.

## 📌 Features

- Store student information (name, gender, date of birth, email, enrollment date)
- Manage available courses
- Record course enrollments for each student
- Track student grades for each course

## 🗂️ Database Structure

The system consists of four core tables:

1. **students**
2. **courses**
3. **enrollments**
4. **grades**

### 📋 Schema Overview

```plaintext
students ─┬─< enrollments >─┬─ courses
          └─< grades (via enrollments)
