from django.shortcuts import render
from movie_bucket.models import movie as movie_,watch
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required(login_url='/login/') #redirect when user is not logged in
def main(request):
    return render(request,'index.html')
    

@login_required(login_url='/login/') #redirect when user is not logged in
def movie(request):
    return render(request,'movie.html')
    
def rec(request):
    user_id=request.user.id
    genres=[]
    langs=[]
    watched=[]
    for i in watch.objects.filter(user_id_id=user_id):
        mov=movie_.objects.filter(id=i.movie_id_id)[0]
        gen=mov.genre_ids
        watched.append(i.movie_id_id)

        if(gen not in genres and gen !=""):
            genres.append(gen)
        if(mov.original_language not in langs):
            langs.append(mov.original_language)


    
    data=[]
    count=0
    for i in  movie_.objects.filter(Q(original_language__in=langs)&Q(genre_ids__in=genres)):
        if(i.id in watched):
            print("skiped",i.title)
            continue
        count+=1
        obj={"id":i.id,
            "lang":i.original_language,
        "poster_path":i.poster_path,
        "title":i.title,
        "time":i.release_date}
        data.append(obj)
        if(count==25):
            break
    return render(request, 'rec.html', {"data":data})

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "registration/login.html",
                    context={"form":form})