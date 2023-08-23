from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from google_analytics_testing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^subscribe$', views.newsletter_view, name='subscribe'),
    re_path(r'^articles/(?P<pk>\d+)$', views.ArticleView.as_view(), name='article'),
    re_path(r'^articles$', views.ArticlesView.as_view(), name='articles'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

