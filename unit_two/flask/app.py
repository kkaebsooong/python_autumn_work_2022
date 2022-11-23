from flask import Flask, render_template, request
from flask_migrate import Migrate
from models import db, InfoModel


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:197328456@localhost:5432/task"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login form"

    if request.method == 'POST':
        surname = request.form['surname']
        new_user = InfoModel(surname=surname)
        db.session.add(new_user)
        db.session.commit()
        return f'Done!'

if __name__ == '__main__':
    app.run(debug=True)

