# python_flask_student_enrollement_example

Create a simple Flask application with the following features:

Form-based input for enrolling students.
In-memory data storage using a Python list (no database needed).
Flash messages to give feedback to the user (e.g., success, errors).

Walkthrough for Students:
1. Application Structure

app.py: The main application file handling routes, logic, and actions.
Templates:
home.html: The front-end interface for interacting with the app.
base.html: The reusable HTML layout.
2. Features & Logic

Adding Students:
Students fill in a form with name, email, and age.
Validations:
All fields must be filled.
Email should not already exist.
Age must be a number.
If valid, the data is stored in a Python list.
Success message is displayed using flash messages.
Viewing Students:
All enrolled students are displayed on the home page.
Deleting Students:
Students can be removed by their email.


3. Running and Using the App

The app runs on localhost.
Students can enroll, see their details, and delete their records dynamically.
4. Explanation of Flash Messages

Flash messages are used for feedback (e.g., "Student added successfully").
Securely signed using the app.secret_key.

