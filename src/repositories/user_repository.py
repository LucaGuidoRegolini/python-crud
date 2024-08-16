from models import db, UserModel


class UserRepository:
    @staticmethod
    def get_user_by_id(user_id):
        return UserModel.query.get(user_id)

    @staticmethod
    def get_user_by_email(email):
        return UserModel.query.filter_by(email=email).first()

    @staticmethod
    def get_user_by(prop_name, prop_value):
        return UserModel.query.filter_by(**{prop_name: prop_value}).first()

    @staticmethod
    def add_user(user_model):
        db.session.add(user_model)
        db.session.commit()

    @staticmethod
    def delete_user(user_model):
        db.session.delete(user_model)
        db.session.commit()
