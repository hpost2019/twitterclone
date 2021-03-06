from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweets


class Notifications(models.Model):
    notification_tweet = models.ForeignKey(Tweets, on_delete=models.CASCADE)
    notification_user = models.ForeignKey(
        TwitterUser, on_delete=models.CASCADE)
    new_item = models.BooleanField(default=True)

    def __str__(self):
        return self.notification_tweet.text
