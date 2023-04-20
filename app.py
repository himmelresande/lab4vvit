from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service_db",
    user="postgres",
    password="8090",
    host="localhost",
    port="5432")

cursor = conn.cursor()

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('login')
    password = request.form.get('password')
    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())

    if records:
        return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
    elif username == "" or password == "":
        return render_template('not_blank.html', error='log or pass must be not blank')
    else:
        return render_template('no_user.html', error='wrong login or password')
