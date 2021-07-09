# Financial plans and accounts module
# Includes different account plans characteristics (contribution limit/room, account balance, penalties, etc.)
# Serves as base/ground framework for various investment options

# Imports
import math
from calculators.compoundInterestCalc import compoundInterest
from calculators.marginalTax import marginalTaxCalc
from baseTemplate import FinancialAccountTemplate

# TFSA Class
class TFSA(FinancialAccountTemplate):
    def __init__(self):
        FinancialAccountTemplate.__init__(self, 0, 6000, 0.01, 0, 0, 0, 0)

# RESP Class
class RESP(FinancialAccountTemplate):
    def __init__(self):
        FinancialAccountTemplate.__init__(self, 0, math.inf, 0, 0, 0, 0, 0)
    
    # RESP total amount calculator (does not alter any object variables, only show number)
    def finalAmountRESP(self, yearlyDep, startingYear):
        # Finding how many cycles available 
        yearsLeft = 17 - startingYear
        # Final amount variable
        totalRESPamount = self.AmountInAccount
        # Gov contribution
        govAmount = 0

        # Add gov contribution into account every year
        for i in range(yearsLeft):
            # Calculate gov contribution, 20% of deposit, up to 500 maximum
            govAmount = yearlyDep * 0.2
            if govAmount > 500:
                govAmount = 500

            # Update total amount
            totalRESPamount = yearlyDep + govAmount
            # Reset govAmount yearly
            govAmount = 0
        
        return totalRESPamount