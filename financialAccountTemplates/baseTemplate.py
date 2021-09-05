# Base financial plans and accounts template (parent class)
# Includes different account plans characteristics (contribution limit/room, account balance, penalties, etc.)
# Serves as base/ground framework for various investment options

# Imports
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
    def calcExcess(self):

        # Amount in account is equal or over the contribution limit
        if self.AmountInAccount >= self.contributionLimit:
            
            # Excess amount is difference in accountbalance and contribution limit
            extraAmount = self.AmountInAccount - self.contributionLimit
        
        # Return total excess amount
        return extraAmount

    # How much in penalties one must pay
    def penaltyAccrued(self):
        baseTemplate = FinancialAccountTemplate()
        amountTakenAway = 0
        
        # Return calculated excess amount
        baseTemplate.calcExcess()

        # Determine amount to take away
        amountTakenAway = self.excessAmount * self.contributionLimitPenalty

        # Take away the amount
        self.AmountInAccount -= amountTakenAway

        # Return amount of penalties taken away
        return amountTakenAway

    # Calculate withdrawal
    def withdraw(self):

        # Not withdrawing more than what is in your account
        if self.AmountInAccount- self.withdrawalAmount >= 0:
            
            # Order goes through
            self.AmountInAccount -= self.withdrawalAmount
        
        # Withdrawing more than what is in your account
        else:

            # Order is halted error message displayed
            print("Insufficient funds.")

    # Calculate deposit 
    def deposit(self):

        # Add deposit amount to account balance and contribution limit
        self.depositAmount += self.AmountInAccount
        self.depositAmount += self.contributionLimit

    
