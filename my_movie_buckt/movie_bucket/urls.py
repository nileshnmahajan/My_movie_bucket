"""my_movie_buckt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie_bucket import views
from django.views.decorators.csrf import csrf_exempt
from movie_bucket.views import  signup_view
from django.conf.urls import url
from graphene_django.views import GraphQLView
from movie_bucket.schema import schema
urlpatterns = [
    path('', views.main),
    path('signup/', signup_view, name="signup"),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
  
]
