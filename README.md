# Stripe Payment Form for Django Projects

This project provides an app for adding a simple payment form to a Django project.
Most [Stripe Checkout](https://stripe.com) documentation assumes you are going to attempt something more ambitious, with Products, Customers, webhooks, etc.
This project, on the other hand, is just a simple form that allows the user to enter an invoice number and payment amount,
and then proceed to make a credit or debit card payment.
It is intended to support developers who want to transition to Stripe from
e.g. [PayPal Payments Standard](https://developer.paypal.com/docs/paypal-payments-standard/integration-guide/formbasics/).

![simple-stripe-payments](https://user-images.githubusercontent.com/2498876/115976160-e6d1a400-a51f-11eb-9a0e-ff5a03ec8c93.png)

While both PayPal and Stripe Checkout have a publishable key that is exposed in client-side JavaScript,
Stripe also requires the use of a secret key that should only be used on the server.

To try out the demo included in this project:
- Set up a Stripe account and obtain the Publishable Key and the Secret Key.
- Create a `local_settings.py` file for your STRIPE_API_KEY (Secret Key) and STRIPE_PUBLIC_KEY (Publishable Key) settings.
- `pip install requirements.txt`
- `python manage.py runserver`

You can also include the app in your own project.

----

[Stripe vs PayPal](https://www.appazur.com/en/2021/03/26/usa-payments-for-canadian/)
