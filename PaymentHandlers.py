class PaymentHandlers:
    @staticmethod
    def process_paypal(amount: float):
        print(f"[PayPal] Processing payment of ${amount:.2f}")
        return f"PayPal payment of ${amount:.2f} processed successfully."

    @staticmethod
    def process_googlepay(amount: float):
        print(f"[GooglePay] Processing payment of ${amount:.2f}")
        return f"GooglePay payment of ${amount:.2f} processed successfully."

    @staticmethod
    def process_creditcard(amount: float):
        print(f"[CreditCard] Processing payment of ${amount:.2f}")
        return f"Credit Card payment of ${amount:.2f} processed successfully."
