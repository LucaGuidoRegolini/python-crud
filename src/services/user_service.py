from domains.user import User
from repositories.contract_repository import ContractRepository
from responses.graphql_response import GraphqlError, GraphqlMutationResponse
from repositories.user_repository import UserRepository
from models import UserModel


class UserService:

    def get_user(user_id):
        user_model = UserRepository.get_user_by_id(user_id)
        if user_model:
            return User(id=user_model.id, name=user_model.name, email=user_model.email)
        return None

    def create_user(name, email):
        user = User(id=None, name=name, email=email)
        user.validate()

        user_email_exists = UserRepository.get_user_by_email(user.email)
        user_name_exists = UserRepository.get_user_by("name", user.name)

        if user_name_exists or user_email_exists:
            return None, GraphqlError("User already exists")

        user_model = UserModel(name=user.name, email=user.email)
        UserRepository.add_user(user_model)
        return User(id=user_model.id, name=user_model.name, email=user_model.email), None

    def update_user(user_id, name, email):
        user_model = UserRepository.get_user_by_id(user_id)
        if not user_model:
            return None, GraphqlError("User not found")

        user_email_exists = UserRepository.get_user_by_email(email)
        user_name_exists = UserRepository.get_user_by("name", name)

        if user_name_exists or user_email_exists:
            return None, GraphqlError("User name or email already exists")

        user_model.name = name if name else user_model.name
        user_model.email = email if email else user_model.email

        UserRepository.add_user(user_model)
        return User(id=user_model.id, name=user_model.name, email=user_model.email), None

    def delete_user(user_id):
        user_model = UserRepository.get_user_by_id(user_id)
        contracts = ContractRepository.get_contract_by_user_id(user_id)

        if contracts.__len__() > 0:
            return GraphqlError("User has active contracts")

        if user_model:
            UserRepository.delete_user(user_model)
            return GraphqlMutationResponse("User deleted")
        return GraphqlError("User not found")
