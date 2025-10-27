import unittest
from PaymentSystem import checkout, PaymentMode

class TestPaymentSystem(unittest.TestCase):

    def test_paypal_payment(self):
        result = checkout(PaymentMode.PAYPAL, 100.0)
        self.assertIn("PayPal payment", result)

    def test_googlepay_payment(self):
        result = checkout(PaymentMode.GOOGLEPAY, 150.5)
        self.assertIn("GooglePay payment", result)

    def test_creditcard_payment(self):
        result = checkout(PaymentMode.CREDITCARD, 200.25)
        self.assertIn("Credit Card payment", result)

    def test_invalid_mode(self):
        with self.assertRaises(ValueError):
            checkout(PaymentMode.UNKNOWN, 120.0)

    def test_invalid_amount_negative(self):
        with self.assertRaises(ValueError):
            checkout(PaymentMode.PAYPAL, -50)

    def test_invalid_amount_type(self):
        with self.assertRaises(ValueError):
            checkout(PaymentMode.PAYPAL, "invalid")

if __name__ == "__main__":
    unittest.main()
