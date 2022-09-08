from django import template
from brewery.models import Measuring, Tank

register = template.Library()


@register.simple_tag()
def get_tanks():
    return Tank.objects.all()
