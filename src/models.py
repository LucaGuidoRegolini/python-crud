from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class ContactModel(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    fidelity = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship(
        'UserModel', backref=db.backref('contacts', lazy=True))


def register_models(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    db.init_app(app)
    db.create_all()
