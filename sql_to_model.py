desc='''
 id                     =models.DurationField()                   ,
 popularity             =models.FloatField()                         ,
 vote_count             =models.DurationField()                     ,
 video                  =models.BooleanField()                     ,
 poster_path            =models.TextField()                       ,
 adult                  =models.BooleanField()                     ,
 backdrop_path          =models.TextField()                       ,
 original_language      =models.CharField(max_length=2)                  ,
 original_title         =models.TextField()                       ,
 genre_ids              =models.TextField()                       ,
 title                  =models.TextField()                       ,
 vote_average           =models.AutoField()                        ,
 overview               =models.TextField()                       ,
 release_date          = models.DateField(default=date.today)                           ,
 belongs_to_collection  =models.TextField()                       ,
 budget                 =models.TextField()                       ,
 genres                 =models.TextField()                       ,
 homepage               =models.TextField()                       ,
 imdb_id                =models.TextField()                       ,
 production_companies   =models.TextField()                       ,
 production_countries   =models.TextField()                       ,
 revenue                =models.TextField()                       ,
 runtime                =models.TextField()                       ,
 spoken_languages       =models.TextField()                       ,
 status                 =models.TextField()                       ,
 tagline                =models.TextField(),
''',
,