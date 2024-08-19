import graphene
from flask_graphql import GraphQLView
from queries.contract_mutations import ContractMutation
from queries.contract_queries import ContractQuery
from queries.user_queries import UserQuery
from queries.user_mutations import UserMutation


class Mutations(UserMutation, ContractMutation):
    pass


class Query(UserQuery, ContractQuery):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations, auto_camelcase=False)
