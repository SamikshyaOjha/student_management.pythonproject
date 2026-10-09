from flask import Flask, render_template, request

app = Flask(__name__)

students = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        address = request.form["address"]
        phone = request.form["phone"]
        email = request.form["email"]
        course = request.form["course"]

        student = {
            "name": name,
            "age": age,
            "address": address,
            "phone": phone,
            "email": email,
            "course": course
        }

        students.append(student)

        return "Student added successfully!"

    return render_template("add_student.html")


if __name__ == "__main__":
    app.run(debug=True)