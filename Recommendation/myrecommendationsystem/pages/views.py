from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm,ContactUsForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from .models import Contactus,Moviess,Myrating
import requests
import json
from django.contrib.auth.decorators import login_required
from ast import literal_eval as make_tuple



# Create your views here.
def home(request):
    contexts = Moviess.objects.all()
    query = request.GET.get('q')
    context = {
        'context': contexts
    }
    # if query:
    #     contexts = Moviess.objects.filter(Q(name__contains=query))
    #     return render(request, 'home.html', {'context':contexts})
    # else:
    #     print(context)
    #     return render(request, "home.html", context)
    if query:
        search = Moviess.objects.filter(Q(name__contains=query))
        context = {
            "movies": search
        }
    else:
        movies = Moviess.objects.all()
        context = {
            "movies": movies
        }
    return render(request, 'home.html', context)



def rating(request, moviess_id):
    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_active:
        raise Http404
    print(moviess_id)
    movies = get_object_or_404(Moviess, pk=moviess_id)
    # for rating
    if request.method == "POST":
        rate = request.POST['rating']
        ratingObject = Myrating()
        ratingObject.user = request.user
        ratingObject.Movies = movies
        ratingObject.rating = rate
        ratingObject.save()

        return redirect("home")
    return render(request, 'rating.html', {'movie': movies})




def contact(request):
    my_form = ContactUsForm(request.GET)
    if request.method=="POST":
        my_form = ContactUsForm(request.POST)
        if my_form.is_valid():
            Contactus.objects.create(**my_form.cleaned_data)
            return redirect("contact")


    context = {"form":my_form}
    return render(request,"contactus.html",context)

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully..')
            return redirect('login')
    context = {'form': form}
    return render(request,"register.html",context)

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"username or password is incorrect...")
    context = {}
    return render(request,"login.html",context)


def logoutuser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def recommended(request):
    user_id = request.user.id
    users = request.user
    myratingobjects = Myrating.objects.filter(user=users)
    contexts={
        'message':'Please rate the movie more than four.'
    }
    if len(myratingobjects) != 0:
        url = "http://127.0.0.1:5000/recommend"
        payload = {'user_id': user_id}
        headers = {
            'content-type': "multipart/form-data",
            'cache-control': "no-cache",

        }

        responses = requests.request("POST", url, data=payload)
        #import pdb;pdb.set_trace()
        response = json.loads(responses.text)
        respnses_tuple = make_tuple(response)
        context = list()

        for user_id in respnses_tuple:
            try:
                recommended = Moviess.objects.get(id=user_id)
                context.append(recommended)
            except:
                pass
        # contexts = Moviess.objects.all()
        # query = request.GET.get('q')
        context = {
            'context': context
        }
        return render(request, 'recommendation.html',context)
    else:
        return render(request,'recommendation.html',contexts)