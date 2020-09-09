from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TwitterUser
from tweet.helpers import get_tweets, user_tweets, get_user_tweets, get_tweet
from notification.helpers import count_notification, get_notification, delete_notification
from django.views.generic import TemplateView


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


class ProfileView(TemplateView):
    def get(self, request, user_username):
        user_info = TwitterUser.objects.get(username=user_username)
        followed_count = user_info.followed.all().count()
        tweets = get_user_tweets(user_info)
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


def tweet_view(request, tweet_id):
    # user_info = TwitterUser.objects.get(username=request.user.username)
    # followed_count = user_info.followed.all().count()
    tweets = get_tweet(tweet_id)
    # count_tweet = user_tweets(user_info)
    # count_notify = count_notification(user_info)
    return render(request, "index.html", {
        "title": "Twitter Clone",
        # "user_info": user_info,
        # "followed_count": followed_count,
        "tweets": tweets,
        # "tweet_count": count_tweet,
        # "notif_count": count_notify,
        "template_name": "tweets.html"
    })


@login_required
def notification_view(request, user_username):
    user_info = TwitterUser.objects.get(username=user_username)
    followed_count = user_info.followed.all().count()
    tweets = get_user_tweets(user_info)
    count_tweet = user_tweets(user_info)
    notif = get_notification(user_info)
    delete_notification(user_info)
    count_notify = count_notification(user_info)
    return render(request, "index.html", {
        "title": "Twitter Clone",
        "user_info": user_info,
        "followed_count": followed_count,
        "tweets": tweets,
        "tweet_count": count_tweet,
        "notif_count": count_notify,
        "notifications": notif,
        "template_name": "notifications.html"
    })


@login_required
def follow_view(request, user_username):
    user = TwitterUser.objects.get(username=user_username)
    request.user.followed.add(user)

    return redirect('/' + user.username + '/')


@login_required
def unfollow_view(request, user_username):
    user = TwitterUser.objects.get(username=user_username)
    request.user.followed.remove(user)

    return redirect('/' + user.username + '/')

