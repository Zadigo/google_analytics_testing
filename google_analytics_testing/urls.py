from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from google_analytics_testing import views

urlpatterns = [
    re_path(r'^customer-orders$', views.CustomerOrdersView.as_view(), name='customer_orders'),
    re_path(r'^checkout/success$', views.PaymentSuccessView.as_view(), name='payment_sucess'),
    re_path(r'^checkout/payment$', views.PaymentView.as_view(), name='payment'),
    re_path(r'^checkout/shipping$', views.ShippingView.as_view(), name='shipping'),
    re_path(r'^cart/remove$', views.remove_from_cart_view, name='cart_remove'),
    re_path(r'^cart/add$', views.cart_add_view, name='add_to_cart'),
    re_path(r'^refund/create$', views.save_address_view, name='refund'),
    re_path(r'^address/add$', views.save_address_view, name='save_address'),
    re_path(r'^cart$', views.CartView.as_view(), name='cart'),
    re_path(r'^purchase$', views.purchase_view, name='start_payment'),
    re_path(r'^subscribe$', views.newsletter_view, name='subscribe'),
    re_path(r'^articles/(?P<pk>\d+)$', views.ArticleView.as_view(), name='article'),
    re_path(r'^articles$', views.ArticlesView.as_view(), name='articles'),
    path('admin/', admin.site.urls),
    path('', views.ArticlesView.as_view(), name='home'),
]

