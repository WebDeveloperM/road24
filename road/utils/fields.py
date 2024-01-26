from datetime import timedelta

from django.utils import timezone


def expires_default():
    return timezone.now() - timedelta(days=2)


