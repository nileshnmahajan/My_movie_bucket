function get(query,calllback)
{
    var xhr=new XMLHttpRequest();
    xhr.onreadystatechange=function()
    {


        if(this.status==200 && this.readyState==4)
        {
            console.log(this.responseText);
            callback(this.responseText);
        }

        else if(this.status==400 && this.readyState==4)
        {

        }
    };
    xhr.open("post","/graphql/");
    xhr.setRequestHeader("Content-Type","application/json");
    "query\n{\n movies{\n popularit\n tagline\n movieBucketSet }\n}"
    var data=JSON.stringify({query:query,variables:null});
    xhr.send(data);
}

var data;

function all_movies(offset)
{
    $.ajaxSetup({ contentType: "application/json; charset=utf-8", });
    
    //{"query":"{\n  movies(offset: 0) {\n    title\n    id\n  }\n}\n","variables":null}
    $.post("/graphql/",JSON.stringify({query:'query{movies(offset:'+offset+'){\
      originalTitle,\
        id,\
        posterPath,\
        adult,\
        releaseDate,\
        originalLanguage\
      }}'}),function(data,e)
      {
            for(var i=0;i<data.data.movies.length;i++)
            {
              if(data.data.movies[i].posterPath=="")
                  data.data.movies[i].posterPath="/"
               if(data.data.movies[i].adult)   
                console.log(data.data.movies[i]);
                var temp='<a class="movie" href="/movie/'+data.data.movies[i].id+'/")">\
                <div class="option">...</div>\
                <img src="https://image.tmdb.org/t/p/w440_and_h660_face/'+data.data.movies[i].posterPath+'"/>\
                <div class="title">'+data.data.movies[i].originalTitle+'</div>\
                <div class="date">'+data.data.movies[i].releaseDate+'</div>\
                <div class="lang">'+data.data.movies[i].originalLanguage+'</div>\
                </a>';
                $("#body").append(temp);
            }
            next_loading=false;
      });

    /*
      https://image.tmdb.org/t/p/w440_and_h660_face/h4VB6m0RwcicVEZvzftYZyKXs6K.jpg
            https://image.tmdb.org/t/p/w440_and_h660_face/scZlQQYnDVlnpxFTxaIv2g0BWnL.jpg
            https://image.tmdb.org/t/p/w440_and_h660_face/qx3khck1M7Qfrq7Ost8zGzL4EOe.jpg
            https://image.tmdb.org/t/p/w1280/qx3khck1M7Qfrq7Ost8zGzL4EOe.jpg
            */
}


function load_movies(offset)
{
    get('{movies(offset:'+offset+'){\
        title\
        id\
      }}');
}




function details(id)
{



}

function get_details(id)
{
  $.ajaxSetup({ contentType: "application/json; charset=utf-8", });
  $.post("/graphql/",JSON.stringify({query:'query{movie(id:'+id+'){\
    popularity,\
    voteCount,\
    video,\
    posterPath,\
    adult,\
    backdropPath,\
    originalLanguage,\
    originalTitle,\
    genreIds,\
    title,\
    voteAverage,\
    overview,\
    releaseDate,\
    belongsToCollection,\
    budget,\
    genres,\
    homepage,\
    imdbId,\
    productionCompanies,\
    productionCountries,\
    revenue,\
    runtime,\
    spokenLanguages,\
    status,\
    tagline\
  }\
}\
  '}),function(data,e)
  {



    $("#detail").empty();
    var temp='<div id="detail" style="background-image:url(\'https://image.tmdb.org/t/p/w1920_and_h800_multi_faces'+data.data.movie.backdropPath+'\')">\
    <span class="img"><img src="https://image.tmdb.org/t/p/w1280'+data.data.movie.posterPath+'"/></span>\
    <span id="meta">\
      <div class="title">Title :  '+validate(data.data.movie.title)+'</div>\
      <div class="date">Release Date : '+validate(data.data.movie.releaseDate)+'</div>\
      <div class="popularity">popularity : '+validate(data.data.movie.popularity)+'</div>\
      <div class="voteCount">voteCount : '+validate(data.data.movie.voteCount)+'</div>\
      <div class="overview">overview : '+validate(data.data.movie.overview)+'</div>\
      <div class="video">video : '+validate(data.data.movie.video)+'</div>\
      <div class="adult">';
      temp+=data.data.movie.adult==true?'18+':''
      temp+='</div>';
      temp+='<div class="originalLanguage">originalLanguage : '+validate(data.data.movie.originalLanguage)+'</div>\
      <div class="originalTitle">Original Title : '+validate(data.data.movie.originalTitle)+'</div>\
      <div class="voteAverage">voteAverage : '+validate(data.data.movie.voteAverage)+'</div>\
      <div class="budget">budget : '+validate(data.data.movie.budget)+'</div>\
      <div class="imdbId">imdbId : '+validate(data.data.movie.imdbId)+'</div>\
      <div class="runtime">runtime : '+validate(data.data.movie.runTime)+'</div>\
      <div class="spokenLanguages">Spoken Languages : '+validate(data.data.movie.spokenLanguages)+'</div>\
      <div class="tagline">tagline : '+validate(data.data.movie.tagLine)+'</div>\
      <div class="movieBucketSet">movieBucketSet : '+validate(data.data.movie.movieBucketSet)+'</div>\
      <div id="add_to_list"></div>\
      </span>\
          </div>';
    $("#detail").append(temp);
    is_watched(id)
  });
}
function add_to_watch(id)
{
  $("#add_to_list").empty();
  $("#add_to_list").append('you have seen this on : Just seen');
  var q='mutation{createBucketElement(movieId:'+id+'){product{id}}}';
  $.ajaxSetup({ contentType: "application/json; charset=utf-8", });
    
    //{"query":"{\n  movies(offset: 0) {\n    title\n    id\n  }\n}\n","variables":null}
    $.post("/graphql/",JSON.stringify({query:q}),function(data,e){



    });
}
function validate(s)
{
  if(s==null|| s==false)
  return "Not available";
  return s;
}


console.log("main.js 3.0 loaded");

function is_watched(id)
{
  var q='query{  iswatched(id:'+id+'){time}}';

  $.ajaxSetup({ contentType: "application/json; charset=utf-8", });
    
    //{"query":"{\n  movies(offset: 0) {\n    title\n    id\n  }\n}\n","variables":null}
    $.post("/graphql/",JSON.stringify({query:q}),function(data,e){
      if(data.data.iswatched.length==0)
        $("#add_to_list").append('<button onclick="add_to_watch('+id+')">Mark as watched</button>');
      else
        $("#add_to_list").append('you have seen this on : '+data.data.iswatched[0].time);
    });
}

function watch_list()
{
  $("#body").empty();
  var q='query{Watchs{movieId{id,title,posterPath},time}}';

  $.ajaxSetup({ contentType: "application/json; charset=utf-8", });
    
    //{"query":"{\n  movies(offset: 0) {\n    title\n    id\n  }\n}\n","variables":null}
    $.post("/graphql/",JSON.stringify({query:q}),function(data,e)
      {
            for(var i=0;i<data.data.Watchs.length;i++)
            {

                var temp='<a class="movie" href="/movie/'+data.data.Watchs[i].movieId.id+'/")">\
                <div class="option">...</div>\
                <img src="https://image.tmdb.org/t/p/w440_and_h660_face/'+data.data.Watchs[i].movieId.posterPath+'"/>\
                <div class="title">'+data.data.Watchs[i].movieId.title+'</div>\
                <div class="date">'+data.data.Watchs[i].time+'</div>\
                </a>';
                $("#body").append(temp);
            }
            next_loading=false;
      });


}