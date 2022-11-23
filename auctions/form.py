# from .views import watchlist
from django import forms
from .models import Item, Comment


class Create_listin_form(forms.ModelForm):
    # form for lising
    class Meta:
        model = Item
        fields = "__all__"


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']

# class WatchlistForm(forms.ModelForm):
#     class Meta:
#         model = watchlist 
#         fields = "__all__"
