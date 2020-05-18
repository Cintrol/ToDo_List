#from django.template.defaulttags import register
from django import template
from todo_list.settings import PAGE_COUNT
register = template.Library()


@register.filter
def get_count(lists):
    """
    return count empty div block
    """
    return list(range(PAGE_COUNT - len(lists)))