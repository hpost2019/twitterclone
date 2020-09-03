from .models import Notifications


def count_notification(user_info):
    return Notifications.objects.filter(notification_user=user_info).count()
