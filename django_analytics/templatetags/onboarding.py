from django.template import Library

register = Library()


@register.inclusion_tag('appcues.html')
def appcues(account_id):
    """Implements Appcues"""
    return {'appcues_account_id': account_id}
