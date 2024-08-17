import graphene
from graphql_types.response_type import AppType
from middleware.api_key import api_key_required
from services.user_service import UserService


class CreateUserInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)


class UpdateUserInput(graphene.InputObjectType):
    name = graphene.String()
    email = graphene.String()


class CreateUser(graphene.Mutation):

    class Arguments:
        input = CreateUserInput(required=True)

    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    message = graphene.String()
    success = graphene.Boolean()

    @api_key_required
    def mutate(self, info, input):
        user, error = UserService.create_user(input.name, input.email)

        if error:
            return error

        return user


class UpdateUser(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)
        input = UpdateUserInput(required=True)

    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    message = graphene.String()
    success = graphene.Boolean()

    @api_key_required
    def mutate(self, info, id, input):
        user, error = UserService.update_user(id, input.name, input.email)

        if error:
            return error

        return user


class DeleteUser(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()
    success = graphene.Boolean()

    @api_key_required
    def mutate(self, info, id):
        response = UserService.delete_user(id)

        return response


class UserMutation(graphene.ObjectType):
    createUser = CreateUser().Field()
    updateUser = UpdateUser().Field()
    deleteUser = DeleteUser().Field()
