import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class ContractModel(db.Model):
    __tablename__ = 'contract'
    id = db.Column(db.Integer, primary_key=True)
    fidelity = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(120), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship(
        'UserModel', backref=db.backref('contacts', lazy=True))


db_url = os.getenv('DATABASE_URL')


def register_models(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    db.init_app(app)
    db.create_all()
