from django import template

register = template.Library()


@register.filter
def ntimes(cnt):
    return xrange(1, cnt+1)
