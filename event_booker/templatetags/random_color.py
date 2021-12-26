from random import choice
from django import template

register = template.Library()


@register.simple_tag
def random_color_name():
    return choice(['cyan', 'red', 'blue', 'orange', 'darkblue', 'cyan', 'red', 'blue', 'orange', 'darkblue', 'orange2'])
