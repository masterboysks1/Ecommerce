from django.contrib import admin
from .models import Comment, Item, User, Bidding, Watchlist

# Register your models here.
admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Bidding)
admin.site.register(Watchlist)