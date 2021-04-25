from django.urls import path

from . import views

urlpatterns = [
    path('', views.CheckoutView.as_view(), name='checkout'),
    path('get-session/', views.CheckoutSessionApiView.as_view(), name='checkout-session'),
]
