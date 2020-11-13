from datetime import timedelta

from django import template
from django.utils import timezone

register = template.Library()


@register.filter
def time_diff(value):
    time_now = timezone.now()

    if time_now < value + timedelta(minutes=3):
        return True
