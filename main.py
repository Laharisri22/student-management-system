from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="lahari@2007",
    database="Student"
)

cursor = db.cursor()

# Home page
@app.route('/')
def index():
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    return render_template("index.html", student=students)

# Add student
@app.route("/add", methods=["POST"])
def add():
    student_name = request.form['student_name']
    student_section = request.form['student_section']
    student_grade = request.form['student_grade']
    student_branch = request.form['student_branch']

    cursor.execute(
        "INSERT INTO student (student_name, student_section, student_grade, student_branch) VALUES (%s, %s, %s, %s)",
        (student_name, student_section, student_grade, student_branch)
    )
    db.commit()

    return redirect(url_for("index"))

# Delete student
@app.route("/delete/<int:id>")
def delete(id):
    cursor.execute("DELETE FROM student WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
