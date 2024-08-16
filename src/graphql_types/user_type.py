import graphene
from graphql_types.response_type import AppType


class UserType(AppType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
