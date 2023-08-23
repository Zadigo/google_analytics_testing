from django.template import Library

register = Library()


@register.inclusion_tag('hotjar.html')
def hotjar(site_id):
    """Implements Hotjar"""
    return {'site_id': site_id}
