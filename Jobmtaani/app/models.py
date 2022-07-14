from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
# user and client
class CustomUser(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    user_location = models.CharField(max_length = 150)
    email=models.EmailField(unique=True)
    client_location = models.CharField(max_length=255)
    client_description = models.TextField()
    def __str__(self):
        return self.first_name





class Placement(models.Model):
    """
    A placement allows investors to bid on company capital raise
    """

    placement_title = models.CharField(max_length=255)
    placement_slug = models.SlugField(unique=True)
    placement_location = models.CharField(max_length=150)
    placement_quote = models.DecimalField(max_digits=10, decimal_places=2)

    placement_description = models.TextField(default=None)
    placement_category = models.CharField(max_length=200, default="welding")

    placement_created = models.DateTimeField(auto_now_add=True)
    placement_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.placement_title


class Bid(models.Model):
    """
    The bid, synonmous with 'order'
    """
    bid_status = models.BooleanField(default=False)

    bid_created = models.DateTimeField(auto_now_add=True)
    bid_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    


    def __str__(self):
        return '{} -{}'.format(self.user, self.bid_status)


class PlacementBid(models.Model):
    """
    The junction table for placement and bid models/tables. Contains every instance of a bid for a placement
    """

    placement = models.ForeignKey(Placement, on_delete=models.CASCADE)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    offer = models.IntegerField()
    shares = models.IntegerField()
    confirmed = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    placementbid_created = models.DateTimeField(auto_now_add=True)
    placementbid_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-placementbid_modified']

    def __str__(self):
        return '{} - {} - {}'.format(self.shares, self.offer, self.user)
