from django import template

from home.utils import get_tracks

register = template.Library()


@register.filter(name='hidden_track')
def hidden_track(track: str):
    result = track[:8] + len(track[8:]) * '*'
    return result

