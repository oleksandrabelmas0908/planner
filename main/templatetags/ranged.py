from django import template

register = template.Library()


@register.simple_tag
def ranged(count):
    return range(count)


register.filter("ranged", ranged)
