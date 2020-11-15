from datetime import timedelta

from django import template
from django.utils import timezone

from shop_app.models import Return

register = template.Library()


@register.filter
def return_status(value):
    try:
        return_object = Return.objects.get(declined_product__id=value)
    except Return.DoesNotExist:
        return "Refund possible"

    return return_object.request_status


@register.filter
def time_diff(value):
    time_now = timezone.now()

    if time_now < value + timedelta(minutes=3):
        return True
