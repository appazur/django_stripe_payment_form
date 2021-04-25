function errmsg(txt) {
    document.getElementById("id_errmsg").innerHTML = txt;
}

var stripe = Stripe(JSON.parse(document.getElementById('stripe_public_key').textContent));
var get_session_url = JSON.parse(document.getElementById('get_session_url').textContent);

var amountEl = document.getElementById('id_amount');
if(amountEl) amountEl.focus();
var invoiceEl = document.getElementById('id_invoice');
var checkoutButton = document.getElementById('checkout-button');
var frm = document.getElementById('id_form');
if(frm)
frm.addEventListener('submit', function(e) {
    e.preventDefault();
    errmsg('');
    var amount = amountEl.value;
    var invoice = invoiceEl.value;
    if(amount < 1) {
        errmsg('Please enter the amount you wish to pay.')
    }
    // Require invoice unless field is hidden:
    else if(invoice == "" && window.getComputedStyle(invoiceEl.parentElement).display != 'none') {
        errmsg('Please enter the invoice number.');
    }
    else {
        checkoutButton.disabled = true;
        fetch(get_session_url, {
          method: 'POST',
          body: new FormData(frm),
        })
        .then(function(response) {
          console.log(response);
          var rj = response.json(); // promise
          if (!response.ok) {
            return Promise.reject(rj);
          }
          return rj;
        })
        .then(function(session) {
          if(session && session.id)
          return stripe.redirectToCheckout({ sessionId: session.id });
        })
        .then(function(result) {
          // If `redirectToCheckout` fails due to a browser or network
          // error, you should display the localized error message to your
          // customer using `error.message`.
          if (result && result.error) {
            errmsg(result.error.message);
            checkoutButton.disabled = false;
          }
        })
        .catch(function(error) {
          // It may or not already be a Promise:
          error = Promise.resolve(error);
          error.then(function(jsn) {
              console.log(jsn);
              errmsg(jsn.error.message);
          }).catch(function(err2) {
              // test case: csrf error.
              console.log('Response was not JSON?', err2);
              errmsg("Sorry, an error occurred.");
          });
          checkoutButton.disabled = false;
        });
    }
});
