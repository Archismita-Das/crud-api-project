from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow React frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

students = []


# Home Route
@app.get("/")
def home():
    return {"message": "Student CRUD API"}


# CREATE Student
@app.post("/students")
def add_student(student: dict):

    students.append(student)

    return {
        "message": "Student added successfully",
        "students": students
    }


# READ All Students
@app.get("/students")
def get_students():

    return students


# UPDATE Student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: dict):

    if student_id < len(students):

        students[student_id] = updated_student

        return {
            "message": "Student updated successfully",
            "students": students
        }

    return {"error": "Student not found"}


# DELETE Student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id < len(students):

        deleted_student = students.pop(student_id)

        return {
            "message": "Student deleted successfully",
            "deleted_student": deleted_student
        }

    return {"error": "Student not found"}