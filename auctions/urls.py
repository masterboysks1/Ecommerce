from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("catagories", views.catagories, name="catagories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("catagories/<str:category>", views.individual_catagories, name="individual_catagories"),
    path("auctions/listing/<int:item_id>", views.listing, name="listing"),
    path("auctions/user/<str:user>", views.user, name="user"),
    path("auctions/watchlist", views.watchlist, name="watchlist")
]
