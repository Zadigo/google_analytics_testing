from django_analytics.events.google import LoginEvent
import json
import random
import secrets
from functools import lru_cache
from typing import Any, Dict
from django import http

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template import Context
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.http import require_GET, require_POST
from django.views.generic import TemplateView

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


class CustomerOrdersView(TemplateView):
    template_name = 'shop/customer_orders.html'


# Ecommmerce process > Cart > checkout : shipping -> payment > Success

class BaseCheckoutView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = {
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
        context['cart'] = transform_dict(data)
        return context


class CartView(BaseCheckoutView):
    template_name = 'shop/cart.html'
    http_method_names = ['get']


class ShippingView(BaseCheckoutView):
    template_name = 'shop/shipping.html'
    http_method_names = ['get']

    @method_decorator(sensitive_post_parameters('address'))
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PaymentView(BaseCheckoutView):
    template_name = 'shop/payment.html'
    http_method_names = ['get']


class PaymentSuccessView(BaseCheckoutView):
    template_name = 'shop/purchase_success.html'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'transaction_id': secrets.token_hex(10),
            'tax': 4.9,
            'shipping': 5.99,
        })
        return context


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


@require_POST
def remove_from_cart_view(request, **kwargs):
    return JsonResponse({'state': True})


@require_POST
def save_address_view(request, **kwargs):
    return JsonResponse({'state': True})


@require_POST
def refund_view(request, **kwargs):
    return JsonResponse({'state': True})


# Accounts

class Login(TemplateView):
    template_name = 'accounts/login.html'

    def post(self, request, **kwargs):
        instance = LoginEvent('G-C5VLPRS4QY', debug=True, user_id=1)
        instance.send()
        print(instance.errors)
        return redirect(reverse('home'))
