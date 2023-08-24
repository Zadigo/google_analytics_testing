import json
from functools import lru_cache
import random
import secrets
from django.http import JsonResponse

from django.shortcuts import redirect, render
from django.template import Context
from django.urls import reverse
from django.views.decorators.http import require_POST, require_GET
from django.views.generic import TemplateView
from django.views.decorators.debug import sensitive_post_parameters
from google_analytics_testing import forms


def transform_dict(data):
    return json.dumps(data)


@lru_cache(maxsize=100)
def create_articles():
    articles = []
    for i in range(20):
        article = {'id': None, 'title': None}
        article['id'] = i
        article['title'] = f'Article {i}'
        articles.append(article)
    return articles


class ArticlesView(TemplateView):
    template_name = 'shop/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = create_articles()
        context['articles'] = articles
        context['serialized_articles'] = json.dumps(articles)
        return context


class ArticleView(TemplateView):
    template_name = 'shop/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = create_articles()
        article_id = self.kwargs['pk'] * 1
        article = list(filter(lambda x: x['id'] == article_id, articles))
        print(article)
        context['article'] = article
        context['serialized_article'] = json.dumps(article)
        return context


@require_POST
def newsletter_view(request, **kwargs):
    form = forms.NewsletterForm(request.POST)
    if form.is_valid():
        pass
    return redirect(reverse('home'))


@require_POST
def cart_add_view(request, **kwargs):
    return JsonResponse({'state': True})


# Ecommmerce process > Cart > checkout : shipping -> payment > Success

@require_GET
def cart_view(request, **kwargs):
    context = {
        'value': random.randrange(20, 2600),
        'items': [
            {
                'item_id': random.randrange(0, 20),
                'item_name': 'Stan and Friends Tee',
                'price': 35,
                'quantity': random.randrange(1, 5)
            }
        ]
    }
    return render(request, 'shop/cart.html', {'cart': transform_dict(context)})


@require_GET
def shipping_view(request, **kwargs):
    context = {
        'value': random.randrange(20, 2600),
        'items': [
            {
                'item_id': random.randrange(0, 20),
                'item_name': 'Stan and Friends Tee',
                'price': 35,
                'quantity': random.randrange(1, 5)
            }
        ]
    }
    return render(request, 'shop/shipping.html', {'cart': transform_dict(context)})


@require_GET
def payment_view(request, **kwargs):
    context = {
        'value': random.randrange(20, 2600),
        'items': [
            {
                'item_id': random.randrange(0, 20),
                'item_name': 'Stan and Friends Tee',
                'price': 35,
                'quantity': random.randrange(1, 5)
            }
        ]
    }
    return render(request, 'shop/payment.html', {'ecommerce': transform_dict(context)})


@require_POST
@sensitive_post_parameters()
def purchase_view(request, **kwargs):
    """Processes the payment"""
    purchase_info = {
        'value': random.randrange(20, 2600),
        'items': [
            {
                'item_id': random.randrange(0, 20),
                'item_name': 'Stan and Friends Tee',
                'price': 35,
                'quantity': random.randrange(1, 5)
            }
        ]
    }
    return JsonResponse({'state': True, 'purchase_info': purchase_info})


@require_GET
def purchase_success_view(request, **kwargs):
    context = Context()
    context.push({
        'transaction_id': secrets.token_hex(10),
        'value': random.randrange(20, 2600),
        'tax': 4.9,
        'shipping': 5.99,
        'items': [
            {
                'item_id': 1,
                'item_name': 'Swimsuit',
                'index': 1,
                'item_brand': 'My Brand',
                'price': 15,
                'quantity': 1
            }
        ]
    })
    result = context.flatten()
    result = json.dumps(result)
    result = {'purchase': result}
    return render(request, 'shop/purchase_success.html', result)
