# Mortgage calculator NOT DONE YET
# MD
# Fixed interest rates
# Asking price for home, downpayment in decimal, amortization period (years), interest rates decimal value, frequency of payments
def paymentCalcMortgage(price, downpayment, amorPeriod, rate, freq):

    # Amount owed at start
    amount = price - (price * downpayment)

    # Monthly payment
    if freq == "monthly":

        # How manyh total payments
        n = amorPeriod * 12

        # Amount per payment
        m = (amount * (rate/12) * (1 + rate)**n) / ((1 + rate)**n -1)

    # Bi-weekly payment
    elif freq == "bi-weekly":
        
        # How manyh total payments
        n = amorPeriod * 24

        # Amount per payment
        m = (amount * (rate/24) * (1 + rate)**n) / ((1 + rate)**n -1)

    return m

print(paymentCalcMortgage(300000, 0, 30, 0.05, "monthly"))