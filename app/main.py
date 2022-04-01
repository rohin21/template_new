import graphene
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette.applications import Starlette
from .GraphQL import schema

app = Starlette()
schema = graphene.Schema(query=schema.Query)

app.mount("/", GraphQLApp(schema, on_get=make_graphiql_handler()))  # Graphiql IDE
