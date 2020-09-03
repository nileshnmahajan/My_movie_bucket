from django.db import models
# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType, ObjectType
from django.conf import settings


class movie(models.Model):
    id                     =models.BigIntegerField(primary_key=True,help_text='Enter field documentati  on')                   
    popularity             =models.FloatField(default='',null=True)                         
    vote_count             =models.BigIntegerField(default='',null=True)                     
    video                  =models.BooleanField(default='',null=True)                     
    poster_path            =models.TextField(default='',null=True)                       
    adult                  =models.BooleanField(default='',null=True)                     
    backdrop_path          =models.TextField(default='',null=True)                       
    original_language      =models.CharField(max_length=2,default='',null=True)                  
    original_title         =models.TextField(default='',null=True)                       
    genre_ids              =models.TextField(default='',null=True)                       
    title                  =models.TextField(default='',null=True)                       
    vote_average           =models.IntegerField(default='',null=True)                        
    overview               =models.TextField(default='',null=True)                       
    release_date          = models.TextField(default='',null=True)                           
    belongs_to_collection  =models.TextField(default='',null=True)                       
    budget                 =models.TextField(default='',null=True)                       
    genres                 =models.TextField(default='',null=True)                       
    homepage               =models.TextField(default='',null=True)                       
    imdb_id                =models.TextField(default='',null=True)                       
    production_companies   =models.TextField(default='',null=True)                       
    production_countries   =models.TextField(default='',null=True)                       
    revenue                =models.TextField(default='',null=True)                       
    runtime                =models.TextField(default='',null=True)                       
    spoken_languages       =models.TextField(default='',null=True)                       
    status                 =models.TextField(default='',null=True)                       
    tagline                =models.TextField(default='',null=True)
    







    class Meta:
       ordering=['-id']#- denote desending order

    def __str__(self):  
        """String for representing the MyModelName object (in Admin site etc.)."""
        return str(self.id)+" "+self.title
   # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        #return reverse('model-detail-view', args=[str(self.id)])
        pass





class watch(models.Model):

    user_id= models.ForeignKey(get_user_model(), null=True,  on_delete=models.CASCADE)
    movie_id= models.ForeignKey(movie, null=True,  on_delete=models.CASCADE)
    #get_user_model()
    time=models.TextField(default='',null=True)

    class Meta:
        ordering=tuple(['time'])

    def __str__(self):
        return str(self.id)