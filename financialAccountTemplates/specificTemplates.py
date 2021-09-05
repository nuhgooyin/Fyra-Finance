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

        # Update the contribution room after withdrawal 
        def updateWithdrawal(self):

            # Updates contribution limit
            self.contributionRoom += self.withdrawalAmount

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

        # Update and roll-over contribution 
        self.contributionLimit += currentContrLimit

# RRIF Class
class RRIF(FinancialAccountTemplate):
    def __init__(self):
        FinancialAccountTemplate.__init__(self, 0, 0, 0.01, 0, 0, 0, 0)

        # Withdrawal Table for over 71
        self.withdrawalTable = [
            # Age, % Withdrawal required yearly
            [71, 5.28]
            [72, 5.40]
            [73, 5.53]
            [74, 5.67]
            [75, 5.82]
            [76, 5.98]
            [77, 6.17]
            [78, 6.36]
            [79, 6.58]
            [80, 6.82]
            [81, 7.08]
            [82, 7.38]
            [83, 7.71]
            [84, 8.08]
            [85, 8.51]
            [86, 8.99]
            [87, 9.55]
            [88, 10.21]
            [89, 10.99]
            [90, 11.92]
            [91, 13.06]
            [92, 14.49]
            [93, 16.34]
            [94, 18.79]
            [95, 20]
        ]

    
    # Required withdraw calculator
    def requiredWithdraw(self, age):
        
        # Under 71
        # Use formula
        if age < 71:
            # Determines required withdrawal percent and amount
            reqWpercent = 1/(90-age)
            reqWamount = reqWpercent * self.AmountInAccount
        
        # Over 71
        # Use table
        elif age < 96:
            # Getting correct value from table
            i = age - 71

            # Determine required withdrawal percent and amount
            reqWpercent = self.withdrawalAmount[i][1] / 100
            reqWamount = reqWpercent * self.AmountInAccount

        # Over 95, 20% flat rate
        else:
            # Determine required withdrawal percent and amount
            reqWpercent = 0.2
            reqWamount = reqWpercent * self.AmountInAccount

        return reqWamount
            

       
# Non-registered Class
class NonReg(FinancialAccountTemplate):
    pass

