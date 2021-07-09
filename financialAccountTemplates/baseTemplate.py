# Financial plans and accounts module
# Includes different account plans characteristics (contribution limit/room, account balance, penalties, etc.)
# Serves as base/ground framework for various investment options

# Imports
import math
from calculators.compoundInterestCalc import compoundInterest
from calculators.marginalTax import marginalTaxCalc
from specificTemplates import TFSA
from specificTemplates import RESP

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

    # What account type
    def accountType(self):
        
        # Default account type is TFSA
        accountType = 0

        # Determine account type
        if accountType == 0:
            tfsa = TFSA()
        elif accountType == 1:
            resp = RESP()

    # Calculate withdrawal
    def withdraw(self):

        # Not withdrawing more than what is in your account
        if self.AmountInAccount - self.withdrawalAmount >= 0:
            
            # Order goes through
            self.AmountInAccount -= self.withdrawalAmount

            # Updates contribution limit
            self.withdrawalAmount += self.contributionLimit
        
        # Withdrawing more than what is in your account
        else:

            # Order is halted error message displayed
            print("Insufficient funds.")

    # Calculate deposit 
    def deposit(self):

        # Add deposit amount to account balance and contribution limit
        self.depositAmount += self.AmountInAccount
        self.depositAmount += self.contributionLimit
