# Simple Stripe Payments

[Stripe](https://stripe.com) is more powerful and developer-friendly than [PayPal](https://paypal.com), and can [cost less](https://www.appazur.com/en/2021/03/26/usa-payments-for-canadian/).
You may want to switch to Stripe for more payment options or to have more customization possibilities.
However, it can be very intimidating to get started.
While you can easily create a simple payment form in HTML and client-side Javascript using [PayPal Payments Standard](https://developer.paypal.com/docs/paypal-payments-standard/integration-guide/formbasics/),
[Stripe](https://stripe.com) requires you to use a secret server-side key as well as a public key, and therefore a server-side implementation is required.

Most [Stripe](https://stripe.com) documentation assumes you are going to dive into something more ambitious.
This project, on the other hand, is just a simple form that allows the user to enter an invoice number and payment amount,
and then proceed to make a credit or debit card payment. Of course, it can be configured for other kinds of payments as well.

![simple-stripe-payments](https://user-images.githubusercontent.com/2498876/115976160-e6d1a400-a51f-11eb-9a0e-ff5a03ec8c93.png)

This project uses a simple Django (Python) app for the server-side implementation.

You'll need to create a `local_settings.py` file for your STRIPE_API_KEY and STRIPE_PUBLIC_KEY settings. Then run:

`python manage.py runserver`

