from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy


class Model_name(db.Model):
    __tablename__ = 'table_name'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'