from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "streetlight2026"

DATABASE = "streetlight.db"


# -----------------------------
# Database Connection
# -----------------------------
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# -----------------------------
# Create Table
# -----------------------------
def create_table():
    conn = get_db()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS complaints(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pole_id TEXT NOT NULL,
        ward TEXT NOT NULL,
        street TEXT NOT NULL,
        fault_type TEXT NOT NULL,
        reported_date TEXT NOT NULL,
        status TEXT NOT NULL,
        repaired_date TEXT
    )
    """)
    conn.commit()
    conn.close()


create_table()


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def index():

    conn = get_db()

    search = request.args.get("search", "")
    status = request.args.get("status", "")

    query = "SELECT * FROM complaints WHERE 1=1"
    values = []

    if search:
        query += """
        AND(
            pole_id LIKE ?
            OR ward LIKE ?
            OR street LIKE ?
        )
        """
        keyword = "%" + search + "%"
        values.extend([keyword, keyword, keyword])

    if status:
        query += " AND status=?"
        values.append(status)

    query += " ORDER BY id DESC"

    complaints = conn.execute(query, values).fetchall()

    total = conn.execute(
        "SELECT COUNT(*) FROM complaints"
    ).fetchone()[0]

    pending = conn.execute(
        "SELECT COUNT(*) FROM complaints WHERE status='Pending'"
    ).fetchone()[0]

    progress = conn.execute(
        "SELECT COUNT(*) FROM complaints WHERE status='In Progress'"
    ).fetchone()[0]

    repaired = conn.execute(
        "SELECT COUNT(*) FROM complaints WHERE status='Repaired'"
    ).fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        complaints=complaints,
        total=total,
        pending=pending,
        progress=progress,
        repaired=repaired
    )


# -----------------------------
# Add Complaint
# -----------------------------
@app.route("/add", methods=["POST"])
def add():

    pole = request.form["pole_id"]
    ward = request.form["ward"]
    street = request.form["street"]
    fault = request.form["fault_type"]
    status = request.form["status"]
    date = request.form["reported_date"]

    if pole == "" or ward == "" or street == "":
        flash("Please Fill All Fields")
        return redirect("/")

    conn = get_db()

    conn.execute("""
    INSERT INTO complaints(
        pole_id,
        ward,
        street,
        fault_type,
        reported_date,
        status
    )
    VALUES(?,?,?,?,?,?)
    """,
    (
        pole,
        ward,
        street,
        fault,
        date,
        status
    ))

    conn.commit()
    conn.close()

    flash("Complaint Registered Successfully")

    return redirect("/")


# -----------------------------
# Edit Complaint
# -----------------------------
@app.route("/edit/<int:id>")
def edit(id):

    conn = get_db()

    complaint = conn.execute(
        "SELECT * FROM complaints WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    return render_template(
        "edit.html",
        complaint=complaint
    )


# -----------------------------
# Update Complaint
# -----------------------------
@app.route("/update/<int:id>", methods=["POST"])
def update(id):

    pole = request.form["pole_id"]
    ward = request.form["ward"]
    street = request.form["street"]
    fault = request.form["fault_type"]
    status = request.form["status"]

    repaired = ""

    if status == "Repaired":
        repaired = datetime.now().strftime("%d-%m-%Y")

    conn = get_db()

    conn.execute("""
    UPDATE complaints
    SET
    pole_id=?,
    ward=?,
    street=?,
    fault_type=?,
    status=?,
    repaired_date=?
    WHERE id=?
    """,
    (
        pole,
        ward,
        street,
        fault,
        status,
        repaired,
        id
    ))

    conn.commit()
    conn.close()

    flash("Complaint Updated Successfully")

    return redirect("/")


# -----------------------------
# Delete Complaint
# -----------------------------
@app.route("/delete/<int:id>")
def delete(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM complaints WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    flash("Complaint Deleted Successfully")

    return redirect("/")


# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)