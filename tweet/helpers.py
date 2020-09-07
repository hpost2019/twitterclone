from .models import Tweets
from twitteruser.models import TwitterUser
from notification.models import Notifications
import re


def parse_tweet(tweet):
    pattern = re.compile(r'(@)(\w+)(\s|$)')
    match_found = pattern.search(tweet.text)
    if match_found:
        username = match_found.group(2)
        user = TwitterUser.objects.get(username=username)
        if user:
            Notifications.objects.create(
                notification_tweet=tweet,
                notification_user=user
            )
            return True
    return False


def get_tweets(user_info):
    user_list = [user_info.id]
    for u in user_info.followed.all():
        user_list.append(u.id)
    tweets = Tweets.objects.filter(
        user__id__in=user_list).order_by('-posted_on')
    return tweets


def user_tweets(user_info):
    return Tweets.objects.filter(user__id=user_info.id).count()


def get_user_tweets(user_info):
    return Tweets.objects.filter(user__id=user_info.id).order_by('-posted_on')


def get_tweet(tweet_id):
    return Tweets.objects.filter(id=tweet_id)
