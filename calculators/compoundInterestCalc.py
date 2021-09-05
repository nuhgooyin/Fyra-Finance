# Compounding Interest Calculator MD
# Formula: final amount = (initial balance) * (1 + interest rate / # compounding periods) ^ (# compounding periods * time period elapsed)
def compoundInterest(principle, interestPercent, period, time):

    interestDecimal = interestPercent / 100
    final = principle * (1 + interestDecimal/period) ** (period * time)

    return final