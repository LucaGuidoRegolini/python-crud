import graphene
from graphql_types.response_type import AppType
from services.user_service import UserService
from graphql_types.user_type import UserType


class CreateUser(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, name, email):
        user, error = UserService.create_user(name, email)

        if error:
            return CreateUser(error)

        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        email = graphene.String()

    user = graphene.Field(UserType)

    def mutate(self, info, id, name, email):
        user, error = UserService.update_user(id, name, email)

        if error:
            return UpdateUser(error)

        return UpdateUser(user=user)


class DeleteUser(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)

    response = graphene.Field(AppType)

    def mutate(self, info, id):
        response = UserService.delete_user(id)

        return DeleteUser(response)


class UserMutation(graphene.ObjectType):
    create_user = CreateUser().Field()
    update_user = UpdateUser().Field()
    delete_user = DeleteUser().Field()
