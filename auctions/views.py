from django.contrib.auth import authenticate, login, logout
from django.core.files.base import ContentFile
from django.db import IntegrityError
from django.forms.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Item, Comment, Bidding, Watchlist
from .form import Create_listin_form, CommentForm


def index(request):
    return render(request, "auctions/index.html", {
        "items": Item.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def catagories(reqeust):
    return render(reqeust, "auctions/catagories.html", {
        "items": Item.objects.all()
    })

def watchlist(request):
    return render(request, "auctions/watchlist.html", {
        "watchlists": Watchlist.objects.all(), 
        "username": request.user.username
    })

def create_listing(request):
    form = Create_listin_form()
    if request.method == "POST":
        form = Create_listin_form(request.POST, request.FILES, initial={"post_date": timezone.now, "owner": request.user})
    # check if form data is valid
        if form.is_valid():
            
            form.save()
            # name = form.cleaned_data('name')
            # number = form.cleaned_data('number')
            # image = form.cleaned_data('image')
            # description =form.cleaned_data('description')
            # catagories = form.cleaned_data('catagories')
            # post = Item.objects.create(
            #     name = name,
            #     price = number,
            #     image = image,
            #     description = description,
            #     owner = request.user,
            #     catagories = catagories,
            #     post_date = timezone.now
            #      )
            # # save the form data to model
            # post.save()
            return render(request, "auctions/index.html", {
                "items": Item.objects.all()
            })

    return render(request, "auctions/create_listing.html",{
        "items": Item.objects.all(),
        'form': form
    })
            
            

def individual_catagories(request, category):
    return render(request, "auctions/individual_catagories.html", {
        "items": Item.objects.all(),
        "category": category
    })

# for individual each items own page 
# contains comments, bidding owner and suff
def listing(request, item_id):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            content = request.POST.get('body')
            form = CommentForm()
            comment = Comment.objects.create(post = Item.objects.get(id = item_id), own = request.user, body = content, comment_date = timezone.now())
            comment.save()
            
        else:
            form = CommentForm()
            

    return render(request, "auctions/listing.html",{
        "item": Item.objects.get(id = item_id),
        "comments": Comment.objects.all(),
        "bid": Bidding.objects.all(),
        'form': form
    })

def user(request, user):
    user_object = User.objects.all()
    for individual in user_object:
        if user in individual.username:
            username = individual.username
            email = individual.email
            dj = individual.date_joined
    return render(request, "auctions/user.html",{
        "username": username,
        "email": email,
        "date_joined": dj
    })