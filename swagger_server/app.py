import os
import psycopg2
import collections

collections.Callable = collections.abc.Callable

from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="fisherman",
        user=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"],
        port="6666",
    )
    return conn


@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "Employee";')
    employees = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", employees=employees)


@app.route("/create/", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        name = request.form["name"]
        birth = request.form["birth"]
        address = request.form["address"]
        phone = request.form["phone"]
        email = request.form["email"]
        position = int(request.form["position"])
        salary = int(request.form["salary"])
        active = bool(request.form["active"])

        conn = get_db_connection()

        try:
            cur = conn.cursor()
            cur.execute(
                'INSERT INTO "Employee" ("employeeName", "birth", "address", "phone", "email", "positionID", "salary", "active")'
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (name, birth, address, phone, email, position, salary, active),
            )
            conn.commit()
        except:
            conn.rollback()
        finally:
            cur.close()
            conn.close()
            return redirect(url_for("index"))
    return render_template("create.html")
