from django.template import Library
from django_analytics.utils import load_default

register = Library()


# @register.inclusion_tag('google/ads/tag.html')
# def remarketing(tag=None):
#     """Implements Google Analytics"""
#     tag = load_default(key='google_ads', tag=tag)
#     return {'google_ads_id': tag}


@register.tag('google/ads/conversion_telephone.html')
def conversion_telephone(conversion_id, conversion_label, telephone):
    """Adds a conversion telephone tag to a conversion page"""
    return {
        'conversion_id': conversion_id,
        'conversion_label': conversion_label,
        'telephone': telephone
    }


@register.tag('google/ads/conversion.html')
def conversion(conversion_id, conversion_label):
    """Adds a conversion tag to a conversion page"""
    return {
        'conversion_id': conversion_id,
        'conversion_label': conversion_label
    }
