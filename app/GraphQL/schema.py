import graphene

class User (graphene.ObjectType):
  id= graphene.ID()
  email= graphene.String()
  password= graphene.String()
  is_active= graphene.Boolean()

class Item(graphene.ObjectType):
  id= graphene.ID()
  title = graphene.String()
  description= graphene.String()

class Query(graphene.ObjectType):
  user = graphene.Field(User)
  item = graphene.Field(Item)