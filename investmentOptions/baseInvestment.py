# Base investment template
# Includes general characteristics of most investment options (interest/roi, required intial investment, taxes, expenses/expense ratio)

# General investment template
class baseInvestment():
    def __init__(self, returnOnInvestment, requiredInitial):

        # Default values
        self.interest = returnOnInvestment
        self.initialInvestment = requiredInitial