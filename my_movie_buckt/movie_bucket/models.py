from django.db import models
# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class movie(models.Model):
    id                     =models.BigIntegerField(primary_key=True,help_text='Enter field documentati  on')                   
    popularity             =models.FloatField(default='')                         
    vote_count             =models.BigIntegerField(default='')                     
    video                  =models.BooleanField(default='')                     
    poster_path            =models.TextField(default='')                       
    adult                  =models.BooleanField(default='')                     
    backdrop_path          =models.TextField(default='')                       
    original_language      =models.CharField(max_length=2,default='')                  
    original_title         =models.TextField(default='')                       
    genre_ids              =models.TextField(default='')                       
    title                  =models.TextField(default='')                       
    vote_average           =models.IntegerField(default='')                        
    overview               =models.TextField(default='')                       
    release_date          = models.DateField(default='')                           
    belongs_to_collection  =models.TextField(default='')                       
    budget                 =models.TextField(default='')                       
    genres                 =models.TextField(default='')                       
    homepage               =models.TextField(default='')                       
    imdb_id                =models.TextField(default='')                       
    production_companies   =models.TextField(default='')                       
    production_countries   =models.TextField(default='')                       
    revenue                =models.TextField(default='')                       
    runtime                =models.TextField(default='')                       
    spoken_languages       =models.TextField(default='')                       
    status                 =models.TextField(default='')                       
    tagline                =models.TextField(default='')







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


class my_bucket(models.Model):
    id =models.BigIntegerField(primary_key=True)
    movie_id=models.ManyToManyField(movie)
    time=models.DateTimeField(default='')

    class Meta:
        ordering=tuple(['time'])

    def __str__(self):
        return str(self.id)


