from django.core.cache import cache
from django.template.context import RequestContext

from django_seo.models import LegalBusiness, SEOVersion


def build_dictionnary(name, instance):
    """Build the return dictionnary"""
    data = {}
    concrete_fields = instance._meta.concrete_fields
    fields = {getattr(field, 'name', None) for field in concrete_fields}
    for field in fields:
        if field is None:
            continue
        data[field] = getattr(instance, field)
    return {name: data}
    # data = {}
    # keys = vars(instance).keys()
    # skip_keys = ['_django_version', '_state', '_ik']
    # for key in keys:
    #     if key in skip_keys:
    #         continue
    #     data[key] = getattr(instance, key)
    # return {name: data}


def load_from_cache(name, model):
    """Load the SEO from cache"""
    latest_item = cache.get(name, None)
    if latest_item is None:
        latest_item = model.objects.get_latest_version()
        if latest_item is None:
            return {name: {}}
        else:
            cache.set(name, latest_item, timeout=3600)
    return build_dictionnary(name, latest_item)


def seo(request):
    """Load the SEO data into the templates"""
    return load_from_cache('seo', SEOVersion)


def legal_business(request):
    """Load legal business infos to the templates"""
    return load_from_cache('legal_business', LegalBusiness)
