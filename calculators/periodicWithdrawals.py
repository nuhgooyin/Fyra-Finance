# Calculator with periodic withdrawals 
# Imports
import math
from compoundInterestCalc import compoundInterest

# Function that returns how many withdrawals can be made
# FURTHER IMPROVEMENTS / CHANGES NECESSARY 
# (maybe website has a whole section on its own, with visual elements and more outputs, i.e graphs, charts, etc...)

def periodicWithdrawalCalc(principle, interestDec, numCompoundingPeriods, withdrawalAmount, withDrawalsPerPeriod):
    # Initial variables
    amount = principle
    t = numCompoundingPeriods
    k = withDrawalsPerPeriod
    i = 0
    # How many withdrawals can be made
    numWithdraw = 0
    
    # Each compounding period
    while i == 0 and t > 0:

        # Only run if there is money left, and 
        if amount > 0 and t > 0:

            # Adding interest earnt
            amount += amount * interestDec

            # Count compounding periods
            t -= 1

            # Withdrawals
            for j in range(k):
                amount -= withdrawalAmount
                numWithdraw += 1
        else:
            i = 1
        
        # Need to determine if amount of money will increase or decrease in long run
        # If increase return average increase amount
        # If decrease return how many periods can withdraw for



