from django.db import models
from twitteruser.models import TwitterUser
from django.utils import timezone


class Tweets(models.Model):
    text = models.CharField(max_length=140)
    posted_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.text + ' User:' + self.user.username

    @property
    def display_tweet(self):
        return '@'+self.user.username+'-'+self.posted_on
