from flask import request, redirect, url_for
import stripe

stripe.api_key = 'your_stripe_secret_key'

@app.route('/process_payment', methods=['POST'])
def process_payment():
    premium_category = request.form.get('premium_category')
    amount = 5000 if premium_category == "Platinum" else 3000  # $50 or $30 in cents

    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency='usd',
        payment_method_types=['card'],
    )
    return redirect(url_for('payment_success'))  # Handle redirection after success
