from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from google_analytics_testing import views

urlpatterns = [
    re_path(r'^checkout/success$', views.purchase_success_view, name='payment_sucess'),
    re_path(r'^checkout/payment$', views.payment_view, name='payment'),
    re_path(r'^checkout/shipping$', views.shipping_view, name='shipping'),
    re_path(r'^cart/add$', views.cart_add_view, name='add_to_cart'),
    re_path(r'^cart$', views.cart_view, name='cart'),
    re_path(r'^purchase$', views.purchase_view, name='start_payment'),
    re_path(r'^subscribe$', views.newsletter_view, name='subscribe'),
    re_path(r'^articles/(?P<pk>\d+)$', views.ArticleView.as_view(), name='article'),
    re_path(r'^articles$', views.ArticlesView.as_view(), name='articles'),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

