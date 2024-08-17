
import graphene

from graphql_types.contract_type import ContractType
from graphql_types.response_type import AppType
from services.contract_service import ContractService


class CreateContractInput(graphene.InputObjectType):
    user_id = graphene.ID(required=True)
    fidelity = graphene.Int(required=True)
    amount = graphene.Float(required=True)
    description = graphene.String()


class UpdateContractInput(graphene.InputObjectType):
    fidelity = graphene.Int()
    amount = graphene.Float()
    description = graphene.String()


class CreateContract(graphene.Mutation):

    class Arguments:
        input = CreateContractInput(required=True)

    id = graphene.ID()
    description = graphene.String()
    user_id = graphene.ID()
    fidelity = graphene.Int()
    amount = graphene.Float()
    created_at = graphene.String()
    message = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, input):
        response, error = ContractService.create_contract(
            input.user_id,  input.fidelity,  input.amount,  input.description)

        if error:
            return error

        return response


class UpdateContract(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)
        input = UpdateContractInput(required=True)
    id = graphene.ID()
    description = graphene.String()
    user_id = graphene.ID()
    fidelity = graphene.Int()
    amount = graphene.Float()
    created_at = graphene.String()
    message = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, id, input):
        response, error = ContractService.update_contract(
            id, input.fidelity, input.amount, input.description)

        if error:
            return error

        return response


class DeleteContract(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, id):
        response = ContractService.delete_contract(id)

        return response


class ContractMutation(graphene.ObjectType):
    createContract = CreateContract().Field()
    deleteContract = DeleteContract().Field()
    updateContract = UpdateContract().Field()
