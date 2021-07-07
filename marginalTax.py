# Marginal Tax Calculator MD
# Initializing 
import math

# Formating: [%tax rate, bracket size (upper - lower bound)]
# Ontario income tax bracket
marginal_income_tax_ontario = [[0.050, 45142], [0.0915, 45145], [0.1116, 59713], [0.1216,70000], [0.1316,math.inf]]
# Federal income tax bracket
marginal_income_tax_federal = [[0.15, 49020], [0.2050, 49020], [0.26, 53938], [0.2932, 64533], [0.33, math.inf]]

# Function
def marginalTaxCalc(amount, bracket):
    # defining variables
    tax = 0
    k = len(bracket)
    num = amount
    
    # Looping through each tax bracket
    for i in range(k):
        # If current bracket is lower than amount
        if num > bracket[i][1]:
            # Tax total amount in bracket, and getting remaining amount not yet taxed
            tax += bracket[i][1] * bracket[i][0]
            num -= bracket[i][1]

        # If current bracket contains amount
        else:
            # Tax remaining amount
            tax += num * bracket[i][0]
            break
    
    return tax
        
# Test
# input is inputAmount
# output is taxAmount
inputAmount = 300000
taxAmount = marginalTaxCalc(inputAmount, marginal_income_tax_ontario) + marginalTaxCalc(inputAmount, marginal_income_tax_federal)
print(taxAmount)