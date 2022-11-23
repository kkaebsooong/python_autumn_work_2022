import psycopg2
import os
from flask import Flask, render_template, request


app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='task',
                            user='postgres',
                            password='a197328456')
    return conn


@app.route('/students_id')
def get():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"""SELECT *
                      FROM student;""")
    students_id = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', students_id=students_id)
