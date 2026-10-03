# Student REST API using Flask

from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Harsh",
        "course": "MCA",
        "marks": 82
    },
    {
        "id": 2,
        "name": "Rahul",
        "course": "MCA",
        "marks": 76
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Student API is running",
        "version": "1.0"
    })


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    student = next(
        (student for student in students if student["id"] == student_id),
        None
    )

    if student is None:
        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify(student)


@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    if not data or "name" not in data or "course" not in data or "marks" not in data:
        return jsonify({
            "error": "Name, course and marks are required"
        }), 400

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "course": data["course"],
        "marks": data["marks"]
    }

    students.append(new_student)

    return jsonify({
        "message": "Student added successfully",
        "student": new_student
    }), 201


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    student = next(
        (student for student in students if student["id"] == student_id),
        None
    )

    if student is None:
        return jsonify({
            "error": "Student not found"
        }), 404

    students.remove(student)

    return jsonify({
        "message": "Student deleted successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)
