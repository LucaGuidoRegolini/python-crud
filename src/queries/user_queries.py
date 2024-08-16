import graphene
from services.user_service import UserService
from graphql_types.user_type import UserType


class UserQuery(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_user(self, info, id):
        response, error = UserService.get_user(id)
        if error:
            return error

        return response
