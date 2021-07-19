# Mortgage calculator NOT DONE YET
# MD
# Fixed interest rates
# Asking price for home, downpayment in decimal, amortization period (years), interest rates decimal value, frequency of payments
def paymentCalcMortgage(price, downpayment, amorPeriod, rate, freq):

    # Amount owed at start
    amount = price - (price * downpayment)

    if freq == "monthly":
        # Montly payment
        n = amorPeriod * 12
        m = (amount * (rate/12) * (1 + rate)**n) / ((1 + rate)**n -1)

    elif freq == "bi-weekly":
        # Every 2 weeks
        n = amorPeriod * 24
        m = (amount * (rate/24) * (1 + rate)**n) / ((1 + rate)**n -1)

    return m



print(paymentCalcMortgage(300000, 0, 30, 0.05, "monthly"))    