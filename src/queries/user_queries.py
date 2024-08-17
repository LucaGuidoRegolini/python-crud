import graphene
from services.user_service import UserService
from graphql_types.user_type import UserTypeResponse


class UserQuery(graphene.ObjectType):
    getUser = graphene.Field(UserTypeResponse, id=graphene.Int(required=True))

    def resolve_user(self, info, id):
        response, error = UserService.get_user(id)
        if error:
            return error

        return response
