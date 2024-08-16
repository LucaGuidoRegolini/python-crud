import graphene
from flask_graphql import GraphQLView
from queries.user_queries import UserQuery
from queries.user_mutations import UserMutation

schema = graphene.Schema(query=UserQuery, mutation=UserMutation)


def register_schema(app):
    app.add_url_rule(
        '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
