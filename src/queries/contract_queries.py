
import graphene

from graphql_types.contract_type import ContractListResponseType, ContractType, ContractTypeResponse
from middleware.api_key import api_key_required
from services.contract_service import ContractService


@api_key_required
def resolve_get_contracts_by_user(self, info, user_id, page):
    response = ContractService.get_contracts_by_user_id(user_id, page)

    if not response:
        return None

    return response


@api_key_required
def resolve_get_contracts_by_id(self, info, id):
    response = ContractService.get_contract_by_id(id, with_user=True)

    if not response:
        return None

    return response


class ContractQuery(graphene.ObjectType):
    getContractsByUser = graphene.Field(
        ContractListResponseType, user_id=graphene.ID(required=True), page=graphene.Int(required=False, default_value=1), resolver=resolve_get_contracts_by_user)

    getContract = graphene.Field(
        ContractTypeResponse, id=graphene.ID(required=True), resolver=resolve_get_contracts_by_id
    )
