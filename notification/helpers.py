from .models import Notifications


def count_notification(user_info):
    return Notifications.objects.filter(
        notification_user=user_info, new_item=True).count()


def get_notification(user_info):
    notif = []
    notifications = Notifications.objects.filter(
        notification_user=user_info)
    for n in notifications:
        if n.new_item:
            notif.append(
                n.notification_tweet.user.username + '-' + n.notification_tweet.text)
    return notif


def delete_notification(user_info):
    notifications = Notifications.objects.filter(
        notification_user=user_info, new_item=True)
    for n in notifications:
        n.new_item = False
        n.save()
