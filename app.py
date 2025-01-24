from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Local in-memory storage for students
students = []

@app.route("/")
def home():
    return render_template("home.html", students=students)

@app.route("/enroll", methods=["POST"])
def enroll():
    name = request.form.get("name")
    email = request.form.get("email")
    age = request.form.get("age")

    # Input validation
    if not name or not email or not age:
        flash("All fields are required!")
        return redirect("/")

    # Check if email already exists
    if any(student["email"] == email for student in students):
        flash("A student with this email already exists!")
        return redirect("/")

    try:
        age = int(age)
    except ValueError:
        flash("Age must be a valid number!")
        return redirect("/")

    # Add student to the in-memory list
    students.append({"name": name, "email": email, "age": age})
    flash(f"Student {name} enrolled successfully!")
    return redirect("/")

@app.route("/delete/<email>", methods=["POST"])
def delete(email):
    global students
    students = [student for student in students if student["email"] != email]
    flash(f"Student with email {email} has been removed!")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
