import json
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic import TemplateView
import stripe
import logging

logger = logging.getLogger(__name__)


class CheckoutView(TemplateView):
    template_name = 'checkout.html'

    def dispatch(self, *args, **kwargs):
        return super(CheckoutView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        return {
            'get_session_url': self.request.build_absolute_uri(reverse('checkout-session')),
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'amount': self.request.GET.get('amount', 0),
        }


class CheckoutSessionApiView(View):
    def post(self, request, *args, **kwargs):
        try:
            url = request.build_absolute_uri(reverse('checkout'))
            stripe.api_key = settings.STRIPE_API_KEY
            invoice = request.POST.get('invoice') or 'unspecified'
            unit_amount = (Decimal(request.POST.get('amount', 0)) * 100).quantize(Decimal('1.'))
            # REVIEW: set maximum amount to prevent high credit card fees?
            #  For now, acss_debit sets 3000 limit and provides error msg.
            logger.info('CheckoutSessionApiView invoice=%s amount=%s', invoice, unit_amount)
            user_args = {}
            #if request.user.is_authenticated:
            #    user_args['customer_email'] = request.user.email
            session = stripe.checkout.Session.create(
                client_reference_id=invoice,
                line_items=[{
                  'price_data': {
                    'currency': getattr(settings, 'PAYMENT_CURRENCY', 'usd'),
                    'product_data': {
                      'name': getattr(settings, 'PAYMENT_PRODUCT_NAME', 'Invoice Payment'),
                    },
                    'unit_amount': unit_amount,
                  },
                  'quantity': 1,
                }],
                mode='payment',
                payment_method_types=getattr(settings, 'PAYMENT_METHOD_TYPES', ['card']),
                # payment_method_options={
                #     'acss_debit': {
                #       'mandate_options': {
                #         'payment_schedule': 'sporadic',
                #         'transaction_type': 'business',
                #       },
                #     },
                # },
                success_url = url + '?success=1&session_id={CHECKOUT_SESSION_ID}',
                cancel_url = url,
                **user_args
            )

            return HttpResponse(json.dumps({'id': session.id}), content_type="application/json; charset=utf-8")
        except stripe.error.StripeError as e:
            logger.warning(e)
            return HttpResponseBadRequest(json.dumps({'error': {'message': str(e)}}), content_type="application/json; charset=utf-8" )
