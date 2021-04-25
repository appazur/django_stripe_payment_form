"""payments_demo URL Configuration
"""
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/checkout/', permanent=False)),
    path('checkout/', include('simple_stripe_payments.urls')),
]
