from django import template


register = template.Library()

@register.filter(name='upper_case')
def upper_case(value: str):
    return value.upper()
