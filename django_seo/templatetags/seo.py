# TODO: REMOVE

from django.conf import settings
from django.template import Library, Node
from django.template.exceptions import TemplateSyntaxError
from urllib.parse import urlparse

register = Library()


class WebsiteSEONode(Node):
    def __init__(self, extra_context, keys, key=None):
        self.key = key
        self.keys = keys
        self.extra_context = extra_context or {}

    def render(self, context):

        return ''


@register.simple_tag(takes_context=True)
def website_seo(context, key=None):
    """Implement SEO functionnalities
    in the website"""
    items = ['SEO_SOCIALS']

    def get_setting(name):
        return name, getattr(settings, name, {})

    result = list(map(get_setting, items))

    keys = ', '.join(x[0] for x in result)

    extra_context = {}
    for name, value in result:
        _, rhv = name.split('_', 1)
        extra_context.update({rhv.lower(): value})
    context.push(seo=extra_context)

    if key is not None:
        try:
            context.push(**{key: extra_context[key]})
        except KeyError:
            raise TemplateSyntaxError(
                f'Could not find {key} in items. Valid keys are: {keys}')
    return ''


@register.filter(name='canonical')
def canonical(url):
    """In order to prevent urls with a query from
    being explicity indexed by Google, this function
    will partition the url in order to return only
    the host and the path.

    In order words, `http://example.com` and `http://example.com?q=1`
    will resolve to `http://example.com` being
    the single source."""
    url_object = urlparse(url)
    if url_object.query:
        new_url = f'{url_object.scheme}://{url_object.netloc}{url_object.path}'
        return new_url
    return url
