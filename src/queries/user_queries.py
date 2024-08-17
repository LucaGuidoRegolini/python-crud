import graphene
from middleware.api_key import api_key_required
from services.user_service import UserService
from graphql_types.user_type import UserTypeResponse


@api_key_required
def resolve_user(self, info, id):
    response = UserService.get_user(id)
    return response


class UserQuery(graphene.ObjectType):
    getUser = graphene.Field(UserTypeResponse, id=graphene.ID(
        required=True), resolver=resolve_user)
