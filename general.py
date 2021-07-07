# Financial plans and accounts module
# Includes different account plans characteristics (contribution limit/room, account balance, penalties, etc.)
# Serves as base/ground framework for various investment options

import math

# Financial account default template
class FinancialAccountTemplate():
    def __init__(self, taxRate, contributionRoom, roomPenalty, accountBalance, extraAmount, withdrawAmount, depositedAmount):
        
        # Default values
        self.tax = taxRate
        self.contributionLimit = contributionRoom
        self.contributionLimitPenalty = roomPenalty
        self.AmountInAccount = accountBalance
        self.excessAmount = extraAmount
        self.withdrawalAmount = withdrawAmount
        self.depositAmount = depositedAmount
    
    # Get excess amount in relation to contribution limit
    def excessAmount(self):
        excessAmount = 0
        self.excessAmount = excessAmount

        # Amount in account is equal or over the contribution limit
        if self.AmountInAccount >= self.contributionLimit:
            
            # Excess amount is difference in accountbalance and contribution limit
            excessAmount = self.AmountInAccount - self.contributionLimit
        
        # Return total excess amount
        return excessAmount

    # How much in penalties one must pay
    def penaltyAccrued(self):
        pass
    def accountType(self):
        pass

    # Calculate withdrawal
    def withdraw(self):

        # 
        if self.AmountInAccount - self.withdrawalAmount >= 0:
            self.AmountInAccount -= self.withdrawalAmount

        if 
        self.withdrawalAmount -= self.contributionLimit

    # Calculate deposit 
    def deposit(self):

        # Add deposit amount to account balance and contribution limit
        self.depositAmount += self.AmountInAccount
        self.depositAmount += self.contributionLimit

# TFSA Class
class TFSA(FinancialAccountTemplate):
    def __init__(self):
        FinancialAccountTemplate.__init__(self, 0, 6000, 0.01, 0, 0, 0, 0)

# RESP Class
class RESP(FinancialAccountTemplate):
    def __init__(self):
        FinancialAccountTemplate.__init__(self, 0, math.inf, 0, 0, 0, 0, 0)
    
    # RESP total amount calculator
    def finalAmountRESP(yearlyDep, startingYear):
        yearsLeft = 17 - startingYear

