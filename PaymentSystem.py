from enum import Enum
from PaymentHandlers import PaymentHandlers

class PaymentMode(Enum):
    PAYPAL = "PayPal"
    GOOGLEPAY = "GooglePay"
    CREDITCARD = "CreditCard"
    UNKNOWN = "Unknown"

def checkout(mode: PaymentMode, amount: float):
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Invalid amount. Must be a positive number.")

    match mode:
        case PaymentMode.PAYPAL:
            return PaymentHandlers.process_paypal(amount)
        case PaymentMode.GOOGLEPAY:
            return PaymentHandlers.process_googlepay(amount)
        case PaymentMode.CREDITCARD:
            return PaymentHandlers.process_creditcard(amount)
        case _:
            raise ValueError("Invalid payment mode selected.")
