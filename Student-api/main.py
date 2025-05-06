from fastapi import FastAPI, HTTPException
from database import cursor, connection
from models import Student, Course, Enrollment, Grade

app = FastAPI()

# -------- Students --------
@app.post("/students/")
def create_student(student: Student):
    sql = "INSERT INTO students (full_name, date_of_birth, email) VALUES (%s, %s, %s)"
    values = (student.full_name, student.date_of_birth, student.email)
    cursor.execute(sql, values)
    connection.commit()
    return {"message": "Student created successfully"}

@app.get("/students/")
def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    sql = "UPDATE students SET full_name=%s, date_of_birth=%s, email=%s WHERE student_id=%s"
    values = (student.full_name, student.date_of_birth, student.email, student_id)
    cursor.execute(sql, values)
    connection.commit()
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    connection.commit()
    return {"message": "Student deleted successfully"}

# -------- Courses --------
@app.post("/courses/")
def create_course(course: Course):
    sql = "INSERT INTO courses (course_name, department) VALUES (%s, %s)"
    cursor.execute(sql, (course.course_name, course.department))
    connection.commit()
    return {"message": "Course added"}

@app.get("/courses/")
def get_courses():
    cursor.execute("SELECT * FROM courses")
    return cursor.fetchall()

@app.put("/courses/{course_id}")
def update_course(course_id: int, course: Course):
    sql = "UPDATE courses SET course_name=%s, department=%s WHERE course_id=%s"
    cursor.execute(sql, (course.course_name, course.department, course_id))
    connection.commit()
    return {"message": "Course updated"}

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    cursor.execute("DELETE FROM courses WHERE course_id=%s", (course_id,))
    connection.commit()
    return {"message": "Course deleted"}

# -------- Enrollments --------
@app.post("/enrollments/")
def create_enrollment(enroll: Enrollment):
    sql = "INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)"
    cursor.execute(sql, (enroll.student_id, enroll.course_id, enroll.enrollment_date))
    connection.commit()
    return {"message": "Enrollment added"}

@app.get("/enrollments/")
def get_enrollments():
    cursor.execute("SELECT * FROM enrollments")
    return cursor.fetchall()

@app.put("/enrollments/{enrollment_id}")
def update_enrollment(enrollment_id: int, enroll: Enrollment):
    sql = """
        UPDATE enrollments 
        SET student_id = %s, course_id = %s, enrollment_date = %s 
        WHERE enrollment_id = %s
    """
    values = (enroll.student_id, enroll.course_id, enroll.enrollment_date, enrollment_id)
    cursor.execute(sql, values)
    connection.commit()
    return {"message": "Enrollment updated successfully"}

@app.delete("/enrollments/{enrollment_id}")
def delete_enrollment(enrollment_id: int):
    cursor.execute("DELETE FROM enrollments WHERE enrollment_id = %s", (enrollment_id,))
    connection.commit()
    return {"message": "Enrollment deleted successfully"}


# -------- Grades --------
@app.post("/grades/")
def add_grade(grade: Grade):
    sql = "INSERT INTO grades (enrollment_id, grade) VALUES (%s, %s)"
    cursor.execute(sql, (grade.enrollment_id, grade.grade))
    connection.commit()
    return {"message": "Grade added"}

@app.get("/grades/")
def get_grades():
    cursor.execute("SELECT * FROM grades")
    return cursor.fetchall()

@app.put("/grades/{grade_id}")
def update_grade(grade_id: int, grade: Grade):
    sql = "UPDATE grades SET enrollment_id = %s, grade = %s WHERE grade_id = %s"
    values = (grade.enrollment_id, grade.grade, grade_id)
    cursor.execute(sql, values)
    connection.commit()
    return {"message": "Grade updated successfully"}

@app.delete("/grades/{grade_id}")
def delete_grade(grade_id: int):
    cursor.execute("DELETE FROM grades WHERE grade_id = %s", (grade_id,))
    connection.commit()
    return {"message": "Grade deleted successfully"}


