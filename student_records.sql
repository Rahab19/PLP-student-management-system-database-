-- students table
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    gender ENUM('Male', 'Female') NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO students (full_name, gender, date_of_birth, email) VALUES
('Kevin Otieno', 'Male', '2001-03-14', 'kevin.otieno@uni.ac.ke'),
('Amina Yusuf', 'Female', '2000-11-22', 'amina.yusuf@uni.ac.ke'),
('Brian Mwangi', 'Male', '2002-06-01', 'brian.mwangi@uni.ac.ke'),
('Lucy Wanjiku', 'Female', '2001-09-18', 'lucy.wanjiku@uni.ac.ke'),
('Elvis Kiptoo', 'Male', '2000-01-30', 'elvis.kiptoo@uni.ac.ke');


-- courses table
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
);

INSERT INTO courses (course_name, department) VALUES
('Database Systems', 'Computer Science'),
('Discrete Mathematics', 'Mathematics'),
('English Composition', 'Humanities', ),
('Data Structures', 'Computer Science'),
('Accounting Principles', 'Business');
('Introduction to Computer Science', 'Computer Science'),
('Business Mathematics', 'Business'),
('English Literature', 'Arts'),
('Internet of Things', 'Computer Science'),
('Microeconomics', 'Economics');


-- enrollments table
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES
(1, 1, '2024-01-15'),
(1, 2, '2024-01-15'),
(2, 3, '2024-01-17'),
(3, 1, '2024-01-18'),
(3, 4, '2024-01-19'),
(4, 5, '2024-02-05'),
(5, 2, '2024-02-08');

-- grades table
CREATE TABLE grades (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT,
    grade CHAR(2),
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
);

INSERT INTO grades (enrollment_id, grade) VALUES
(1, 'A'),
(2, 'B+'),
(3, 'A-'),
(4, 'B'),
(5, 'A'),
(6, 'C+'),
(7, 'B-');


-- queries to retrieve data

SELECT * FROM students;

SELECT * FROM courses;

-- enrollments with student and course details

SELECT 
    e.enrollment_id,
    s.full_name AS student,
    c.course_name AS course,
    e.enrollment_date
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;


-- all grades with student and course names

SELECT 
    s.full_name,
    c.course_name,
    g.grade
FROM grades g
JOIN enrollments e ON g.enrollment_id = e.enrollment_id
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;

-- students who got an 'A' grade

SELECT 
    s.full_name,
    c.course_name,
    g.grade
FROM grades g
JOIN enrollments e ON g.enrollment_id = e.enrollment_id
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE g.grade = 'A';

-- Count how many students are enrolled in each course

SELECT 
    c.course_name,
    COUNT(e.student_id) AS total_students
FROM enrollments e
JOIN courses c ON e.course_id = c.course_id
GROUP BY c.course_name
ORDER BY total_students DESC;

-- Show enrollments made after January 1, 2024
SELECT 
    s.full_name,
    c.course_name,
    e.enrollment_date
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE e.enrollment_date > '2024-01-01'
ORDER BY e.enrollment_date;

