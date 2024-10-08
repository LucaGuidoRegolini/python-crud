import os
from sqlalchemy import inspect
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


def register_models(app):
    db_url = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    db.init_app(app)

    inspector = inspect(db.engine)
    existing_tables = inspector.get_table_names()

    if not set([model.__tablename__ for model in [UserModel, ContractModel]]) <= set(existing_tables):
        db.create_all()
