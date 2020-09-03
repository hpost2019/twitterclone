from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TwitterUser
from tweet.helpers import get_tweets, user_tweets
from notification.helpers import count_notification


@login_required
def index_view(request):
    user_info = TwitterUser.objects.get(id=request.user.id)
    followed_count = user_info.followed.all().count()
    tweets = get_tweets(user_info)
    count_tweet = user_tweets(user_info)
    count_notify = count_notification(user_info)
    return render(request, "index.html", {
        "title": "Twitter Clone",
        "user_info": user_info,
        "followed_count": followed_count,
        "tweets": tweets,
        "tweet_count": count_tweet,
        "notif_count": count_notify,
        "template_name": "tweets.html"
    })
