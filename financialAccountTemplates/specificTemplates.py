# Specific financial plans and accounts module
# Includes different account plans characteristics (contribution limit/room, account balance, penalties, etc.)
# Serves as base/ground framework for various investment options

# Imports
import math
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

# RRSP Class
class RRSP(FinancialAccountTemplate):
    def __init__(self):
        FinancialAccountTemplate.__init__(self, 0, 0, 0.01, 0, 0, 0, 0)

    # Method for contribution limit 
    def contributionLimitCalc(self, previousTax):

        # current contribution limit is 18% of last year's income
        currentContrLimit = 0
        currentContrLimit = previousTax * 0.18

        # Up to a max of $27,830
        if currentContrLimit > 27830:
            currentContrLimit = 27830

        # Roll-over contribution 
        self.contributionLimit += currentContrLimit

# RRIF Class
class RRIF(FinancialAccountTemplate):
    def __init__(self):
        FinancialAccountTemplate.__init__(self, 0, 0, 0.01, 0, 0, 0, 0)

# Non-registered Class