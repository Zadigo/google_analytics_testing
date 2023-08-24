import json
from functools import lru_cache
import secrets

from django.shortcuts import redirect, render
from django.template import Context
from django.urls import reverse
from django.views.decorators.http import require_POST, require_GET
from django.views.generic import TemplateView
from django.views.decorators.debug import sensitive_post_parameters
from google_analytics_testing import forms


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
    template_name = 'articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = create_articles()
        context['articles'] = articles
        context['serialized_articles'] = json.dumps(articles)
        return context


class ArticleView(TemplateView):
    template_name = 'article.html'

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
@sensitive_post_parameters()
def purchase_view(request, **kwargs):
    return redirect(reverse('purchase_sucess'))


@require_GET
def purchase_success_view(request, **kwargs):
    context = Context()
    context.push({
        'transaction_id': secrets.token_hex(15),
        'value': 15,
        'tax': 4.5,
        'currency': 'EUR',
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
    return render(request, 'purchase_success.html', result)
