# yourapp/templatetags/custom_tags.py

from django import template
from store.models import Product  # replace with your actual product model

register = template.Library()

@register.simple_tag(takes_context=True)
def append_query_params(context, **kwargs):
    request = context['request']
    updated = request.GET.copy()
    for key, value in kwargs.items():
        updated[key] = value
    return updated.urlencode()
