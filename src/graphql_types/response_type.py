import graphene


class AppType(graphene.ObjectType):
    message = graphene.String()
    success = graphene.Boolean()
