from .models import Tweets


def get_tweets(user_info):
    user_list = [user_info.id]
    for u in user_info.followed.all():
        user_list.append(u.id)
    # breakpoint()
    tweets = Tweets.objects.filter(
        user__id__in=user_list).order_by('-posted_on')
    return tweets


def user_tweets(user_info):
    return Tweets.objects.filter(user__id=user_info.id).count()
