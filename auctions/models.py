from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import fields
from django.utils import timezone


class User(AbstractUser):
    pass





class Item(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    description = models.CharField(max_length = 64)
    image = models.ImageField(upload_to='images/')
    owner = models.ForeignKey(User, on_delete= models.CASCADE,related_name='posts')
    post_date = models.DateField(default=timezone.now)

    CATAGORIES_CHOICE = [
        ('beauty and accessories', 'beauty & accessories'),
        ('arts and craft', 'arts & craft'),
        ('mobile and accessories', 'mobile & accessories'),
        ('clothing & fashion', 'clothing and fashion'),
        ('vehicles', 'vehicles'),
        ('furniture', 'furniture'),
        ('electronics', 'electronics'),
        ('photography', 'photography'),
        ('household', 'household')
    ]

    catagories = models.CharField(max_length=32, choices=CATAGORIES_CHOICE, default="")
    
    def __str__(self):
        return str(self.name)

class Comment(models.Model):
    post = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments')
    own = models.ForeignKey(User, on_delete= models.CASCADE,related_name='poste') 
    body = models.TextField(default="")
    comment_date = models.DateField(default=timezone.now)


    def __str__(self):
        return 'Comment: {} on {}'.format(self.own ,self.post)

class Bidding(models.Model):
    bidded = models.ForeignKey(Item, on_delete=models.CASCADE,related_name='bidded')
    bidder = models.ForeignKey(User, on_delete= models.CASCADE,related_name='bidder')

    def __str__(self):
        return '{} bid by {}'.format(self.bidded ,self.bidder)

class Watchlist(models.Model):
    watchlist = models.ForeignKey(Item, on_delete=models.CASCADE,related_name='watchlist')
    watchlisted_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='watchlisted_by')
    
    def __str__(self):
        return '{} watchlisted by {}'.format(self.watchlist, self.watchlisted_by)
    