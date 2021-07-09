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
    def calcExcess(self, accountBalance, contributionRoom, extraAmount):

        # Amount in account is equal or over the contribution limit
        if accountBalance >= contributionRoom:
            
            # Excess amount is difference in accountbalance and contribution limit
            extraAmount = accountBalance - contributionRoom
        
        # Return total excess amount
        return extraAmount

    # How much in penalties one must pay
    def penaltyAccrued(self, roomPenalty, accountBalance, extraAmount):
        baseTemplate = FinancialAccountTemplate()
        amountTakenAway = 0
        
        # Return calculated excess amount
        baseTemplate.calcExcess()

        # Determine amount to take away
        amountTakenAway = extraAmount * roomPenalty

        # Take away the amount
        accountBalance -= amountTakenAway

        # Return amount of penalties taken away
        return amountTakenAway

    # Calculate withdrawal
    def withdraw(self, withdrawAmount, accountBalance, contributionRoom):

        # Not withdrawing more than what is in your account
        if accountBalance- withdrawAmount >= 0:
            
            # Order goes through
            accountBalance -= withdrawAmount

            # Updates contribution limit
            withdrawAmount += contributionRoom
        
        # Withdrawing more than what is in your account
        else:

            # Order is halted error message displayed
            print("Insufficient funds.")

    # Calculate deposit 
    def deposit(self, depositedAmount, accountBalance, contributionRoom):

        # Add deposit amount to account balance and contribution limit
        depositedAmount += accountBalance
        depositedAmount += contributionRoom
