import graphene
from graphql_types.response_type import AppType
from graphql_types.user_type import UserType


class ContractType(graphene.ObjectType):
    id = graphene.ID()
    user_id = graphene.ID()
    fidelity = graphene.Int()
    amount = graphene.Float()
    user = graphene.Field(UserType)
    description = graphene.String()
    created_at = graphene.String()


class ContractTypeResponse(ContractType, AppType):
    pass


class ContractTypeWithoutUser(ContractType):
    id = graphene.ID()
    user_id = graphene.ID()
    fidelity = graphene.Int()
    amount = graphene.Float()
    description = graphene.String()
    created_at = graphene.String()


class ContractResponseType(AppType):
    contract = graphene.Field(ContractTypeWithoutUser)


class ContractListResponseType(AppType):
    Contracts = graphene.List(ContractTypeWithoutUser)
    nextToken = graphene.String()
