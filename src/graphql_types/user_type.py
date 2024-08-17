import graphene
from graphql_types.response_type import AppType


class UserType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()


class UserTypeResponse(AppType, UserType):
    pass
