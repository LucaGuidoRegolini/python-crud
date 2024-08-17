
from domains.contract import Contract
from graphql_types.contract_type import ContractListResponseType
from models import ContractModel
from repositories.contract_repository import ContractRepository
from responses.graphql_response import GraphqlError, GraphqlMutationResponse


class ContractService:

    @staticmethod
    def get_contracts_by_user_id(user_id, page=1):
        limit = 10
        offset = (page - 1) * limit
        list = ContractRepository.get_contract_by_user_id(
            user_id, limit, offset)
        nextToken = page + 1 if list.__len__() == limit else None
        return {
            'Contracts': [
                {
                    'id': contract.id,
                    'user_id': contract.user_id,
                    'fidelity': contract.fidelity,
                    'amount': contract.amount,
                    'description': contract.description,
                    'created_at': contract.created_at.isoformat()
                } for contract in list
            ],
            'nextToken': nextToken
        }

    @staticmethod
    def get_contract_by_id(contract_id, with_user=False):

        resp = ContractRepository.get_contract_by_id(contract_id, with_user)

        if not resp:
            return GraphqlError("Contract not found")

        return resp

    @staticmethod
    def create_contract(user_id, fidelity, amount, description=""):
        contract = Contract(user_id, fidelity, amount, description)
        validation = contract.validate()

        if validation:
            return None, GraphqlError(validation)

        contract_model = ContractModel(
            user_id=contract.user_id,
            fidelity=contract.fidelity,
            amount=contract.amount,
            description=contract.description,
            created_at=contract.created_at
        )
        ContractRepository.add(contract_model)

        return contract_model, None

    @staticmethod
    def update_contract(contract_id, fidelity, amount, description=""):
        contract_model = ContractRepository.get_contract_by_id(contract_id)

        if not contract_model:
            return None, GraphqlError("Contract not found")

        contract = Contract(contract_model.user_id,
                            fidelity, amount, description)
        validation = contract.validate()

        if validation:
            return None, GraphqlError(validation)

        contract_model.fidelity = contract.fidelity
        contract_model.amount = contract.amount
        contract_model.description = contract.description
        contract_model.created_at = contract.created_at
        ContractRepository.add(contract_model)

        return contract_model, None

    @staticmethod
    def delete_contract(contract_id):
        contract_model = ContractRepository.get_contract_by_id(contract_id)

        if not contract_model:
            return GraphqlError("Contract not found")

        ContractRepository.delete(contract_model)

        return GraphqlMutationResponse("Contract deleted")
