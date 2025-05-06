from pydantic import BaseModel
from datetime import date

class Student(BaseModel):
    full_name: str
    date_of_birth: date
    email: str

class Course(BaseModel):
    course_name: str
    department: str

class Enrollment(BaseModel):
    student_id: int
    course_id: int
    enrollment_date: date

class Grade(BaseModel):
    enrollment_id: int
    grade: str

