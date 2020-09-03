
var current_open='';
var next_loading=false;
var total=$("body").innerHeight();
window.onscroll=function()
{
    var current_scroll=window.scrollY;
    var per=(current_scroll/total)*100;

    //    console.log(per+" %");
    if(total-current_scroll<800 && next_loading==false && current_open=="post")
    {
        next_loading=true;
        console.log("loading post");
        load_next();

    }
    else if(total-current_scroll<800 && next_loading==false && current_open=="")
    {
        next_loading=true;
        console.log("loading home");
        load_more();

    }
};

var offset=0;
var id=[]
var titles_=[];
var url_object;
var page_index=1,limit=10;
var url;
$("document").ready()
{
    main();
    window.onpopstate=main;

};

function main(event)
{
    url_object=window.location;
    url=url_object.origin;


    var path=url_object.pathname.split("/");
    switch(path[1])
    {
        case "":
            current_open="";
            //home
            load_more();
            break;
        case "movie" :
            current_open='movie';
            get_details(path[2]);
            break;
        case "watch_list":
            current_open="watch_list";
            watch_list();
            break; 
        case "Recomended":
            current_open="Recomended";
            get_reco();
            break;    
    }

}

function infinite_scroll()
{
    total=$("body").innerHeight();
}

var infinite_post_current_id=0;

function load_more()
{
    offset+=10;

    all_movies(offset)
    /*
    const state = { 'page_id': 1, 'user_id': 5 }
    const url_ = '/page/'+offset;
    history.pushState(state, 'page '+offset, url_);
    */

}



console.log("scroll.js loaded");



function get_reco()
{

}