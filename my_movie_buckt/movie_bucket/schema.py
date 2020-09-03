from movie_bucket.models import movie,watch
from graphene import ObjectType, Node, Schema
import graphene
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType, ObjectType
from graphene import InputObjectType
import datetime
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required
from graphql_jwt.decorators import user_passes_test
from graphql_jwt.decorators import superuser_required
import graphql_jwt


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
class movieNode(DjangoObjectType):
    class Meta:
        model = movie

class mybucketNode(DjangoObjectType):
    class Meta:
        model = watch


class Query(ObjectType):
    '''
    movie = Node.Field(movieNode)
    movies = DjangoConnectionField(movieNode)

    movie_bucket = Node.Field(mybucketNode)
    movie_buckets = DjangoConnectionField(mybucketNode)

    '''
    movie = graphene.Field(movieNode, id=graphene.Int())
    
    Watchs = graphene.List(mybucketNode)
    movies= graphene.List(movieNode,offset=graphene.Int())
    iswatched=graphene.List(mybucketNode,id=graphene.Int())
    

    user=graphene.Field(UserType, id=graphene.Int())
 
    users = graphene.List(UserType)
    me = graphene.Field(UserType)
    

    def resolve_iswatched(self,info,id):   
        return watch.objects.filter(user_id_id=info.context.user.id,movie_id_id=id)
    
    @login_required
    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Authentication Failure!')
        return user



    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return get_user_model().objects.get(pk=id)
        return None

    #@classmethod
    @superuser_required
    def resolve_users(self, info, **kwargs):
        return get_user_model().objects.all()


 
    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return movie.objects.get(pk=id)
        return None


    @login_required
    def resolve_Watchs(self, info, **kwargs):
        return watch.objects.filter(user_id_id=info.context.user.id)

    @login_required
    def resolve_movies(self, info, **kwargs):
        offset = kwargs.get('offset')
        return movie.objects.all()[offset:offset+10]


#********************************************************

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)





#######################################################################3







class CreateProduct(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation

        movieId = graphene.Int(required=True)
       
    # The class attributes define the response of the mutation

# Let's define the response of the mutation
    product = graphene.Field(mybucketNode)


    def mutate(self, info,movieId):
        if(watch.objects.filter(user_id_id=info.context.user.id,movie_id_id=movieId).count()>0):
            return False
        now = datetime.datetime.now()
        now=now.strftime("%Y-%m-%d %H:%M:%S.%U")
        print("#",now)

        question = watch.objects.create(
            time=now,
            movie_id_id=movieId,
            user_id_id=info.context.user.id
        )
        question.save()
        # Notice we return an instance of this mutation
        # return an instance of the Mutation 🤷‍♀️
        return CreateProduct(product=question)

#***************** 🔥🔥🔥 Wiring up the mutations 🔥🔥🔥 *******************#

# Mutation for sending the data to the server.
class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    create_bucket_element = CreateProduct.Field()
    create_user = CreateUser.Field()
    '''
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()

    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
    class Mutation(graphene.ObjectType):
    update_question = QuestionMutation.Field()
    '''




'''
class UpdateProduct(graphene.Mutation):
  # The input arguments for this mutation
  class Arguments:
    id = graphene.ID()
    name = graphene.String()
    price = graphene.Float()
    category = graphene.List(graphene.ID)
    in_stock = graphene.Boolean()
    date_created = graphene.types.datetime.DateTime()

  # Let's define the response of the mutation
  product = graphene.Field(ProductType)

  def mutate(self, info, id, name=None, price=None, category=None, in_stock=None, date_created=None):
    product = Product.objects.get(pk=id)
    product.name = name if name is not None else product.name
    product.price = price if price is not None else product.price
    product.in_stock = in_stock if in_stock is not None else product.in_stock
    product.date_created = date_created if date_created is not None else product.date_created

    # Loop through and update categories for our product 😫 
    if category is not None:
      category_set = []
      for category_id in category:
        category_object = Category.objects.get(pk=category_id)
        category_set.append(category_object)
      product.category.set(category_set)

    product.save()
    # Notice we return an instance of this mutation 🤷‍♀️
    return UpdateProduct(product=product)


class DeleteProduct(graphene.Mutation):
  class Arguments:
    # The input arguments for this mutation
    id = graphene.ID()

  # The class attributes define the response of the mutation
  product = graphene.Field(ProductType)

  def mutate(self, info, id):
    product = Product.objects.get(pk=id)
    if product is not None:
      product.delete()
    return DeleteProduct(product=product)
'''


#register quer and mutation class
schema = Schema(query=Query,mutation=Mutation)