import requests

# Configuração da URL do endpoint GraphQL
# Altere para o seu endpoint GraphQL
GRAPHQL_ENDPOINT = 'http://localhost:5000/graphql'

# Função para executar uma query ou mutation


def execute_graphql_query(query, variables=None):
    response = requests.post(
        GRAPHQL_ENDPOINT,
        json={'query': query, 'variables': variables}
    )
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed with status code {
                        response.status_code}: {response.text}")


# Queries e mutations GraphQL
create_user_gql = """
mutation createUser($input: CreateUserInput!) {
  createUser(input: $input) {
    id
    name
    email
  }
}
"""

get_user_gql = """
query getUser($id: ID!) {
  getUser(id: $id) {
    id
    name
    email
  }
}
"""

update_user_gql = """
mutation updateUser($id: ID!, $input: UpdateUserInput!) {
  updateUser(id: $id, input: $input) {
    id
    name
    email
  }
}
"""

delete_user_gql = """
mutation deleteUser($id: ID!) {
  deleteUser(id: $id) {
    success
    message
  }
}
"""

create_contract_gql = """
mutation createContract($input: CreateContractInput!) {
  createContract(input: $input) {
    id
    description
    user_id
    created_at
    fidelity
    amount
  }
}
"""

update_contract_gql = """
mutation updateContract($id: ID!, $input: UpdateContractInput!) {
  updateContract(id: $id, input: $input) {
    id
    description
    user_id
    created_at
    fidelity
    amount
  }
}
"""

get_contract_gql = """
query getContract($id: ID!) {
  getContract(id: $id) {
    description
    user_id
    user {
      id
      name
      email
    }
    created_at
    fidelity
    amount
  }
}
"""

get_contract_withoutnested_gql = """
query getContract($id: ID!) {
  getContract(id: $id) {
    description
    user_id
    created_at
    fidelity
    amount
  }
}
"""

get_contracts_by_user_gql = """
query getContractsByUser($user_id: ID!) {
  getContractsByUser(user_id: $user_id) {
    Contracts {
      id
      description
      user_id
      created_at
      fidelity
      amount
    }
    nextToken
  }
}
"""

delete_contract_gql = """
mutation deleteContract($id: ID!) {
  deleteContract(id: $id) {
    success
    message
  }
}
"""

# Exemplo de execução de queries e mutations
if __name__ == "__main__":
    # Exemplo de variáveis para uma mutation de criação de usuário
    variables = {
        'input': {
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        }
    }
    result = execute_graphql_query(create_user_gql, variables)
    print("Create User Result:", result)

    # Exemplo de variáveis para uma query de obtenção de usuário
    variables = {'id': '1'}
    result = execute_graphql_query(get_user_gql, variables)
    print("Get User Result:", result)

    # Exemplo de variáveis para uma mutation de atualização de usuário
    variables = {
        'id': '1',
        'input': {
            'name': 'Jane Doe',
            'email': 'jane.doe@example.com'
        }
    }
    result = execute_graphql_query(update_user_gql, variables)
    print("Update User Result:", result)

    # Exemplo de variáveis para uma mutation de criação de contrato
    variables = {
        'input': {
            'description': 'Contract 1',
            'user_id': '1',
            'fidelity': 10,
            'amount': 100.0
        }
    }
    result = execute_graphql_query(create_contract_gql, variables)
    print("Create Contract Result:", result)

    # Exemplo de variáveis para uma mutation de atualização de contrato
    variables = {
        'id': '1',
        'input': {
            'description': 'Contract 1 Updated',
            'fidelity': 20,
            'amount': 200.0
        }
    }

    result = execute_graphql_query(update_contract_gql, variables)
    print("Update Contract Result:", result)

    # Exemplo de variáveis para uma query de obtenção de contrato
    variables = {'id': '1'}
    result = execute_graphql_query(get_contract_gql, variables)
    print("Get Contract Result:", result)

    # Exemplo de variáveis para uma query de obtenção de contratos por usuário
    variables = {'user_id': '1'}
    result = execute_graphql_query(get_contracts_by_user_gql, variables)
    print("Get Contracts By User Result:", result)

    # Exemplo de variáveis para uma mutation de remocão de contrato
    variables = {'id': '1'}
    result = execute_graphql_query(delete_contract_gql, variables)
    print("Delete Contract Result:", result)

    # Exemplo de variáveis para uma mutation de remocão de usuário
    variables = {'id': '1'}
    result = execute_graphql_query(delete_user_gql, variables)
    print("Delete User Result:", result)
