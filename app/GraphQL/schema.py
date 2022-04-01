import graphene

class User (graphene.ObjectType):
  id= graphene.ID()
  email= graphene.String()
  password= graphene.String()
  is_active= graphene.Boolean()

  def resolve_id(root,info):
    return "1"
  def resolve_email(root,info):
    return "text@gmail.com"
  def resolve_password(root,info):
    return "123"
  def resolve_is_active(root,info):
    return True
class Item(graphene.ObjectType):
  id= graphene.ID()
  title = graphene.String()
  description= graphene.String()

  def resolve_id(root,info):
    return "1"
  def resolve_title(root,info):
    return "Title"
  def resolve_description(root,info):
    return "Nothing Here"

class Query(graphene.ObjectType):
  user = graphene.Field(User)
  item = graphene.Field(Item)

  def resolve_user(root,info):
    return User
  def resolve_item(root,info):
    return Item