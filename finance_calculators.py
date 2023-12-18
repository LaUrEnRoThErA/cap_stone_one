import math

# display appropriate information to user
print("Investment - to calculate the amount amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount the amount you'll have to pay on a home loan.")

# ask user for input
bond_invest = input("Enter either 'investment' or 'bond' from the above menu to proceed: ")

# set input conditions, create variables, gather data
while True:
    lower_bond_invest = bond_invest.lower()

    if lower_bond_invest == "investment":
        investment_amount = float(input("How much money are you depositing: "))
        interest_rate_invest = float(input("Interest rate: "))
        years_investing = int(input("How many years would you like to invest: "))
        comp_simple = input("Would you like 'simple' or 'compound' interest: ")

        # simplify variable names for algorithms, insert algorithm and display answer
        p = investment_amount
        r = interest_rate_invest / 100
        t = years_investing

        if comp_simple == "simple":
            repayment_simple = p *(1 + r * t)
    
            print(f"Total amount once interest is applied is {repayment_simple}. ")

        elif comp_simple == "compound":
            repayment_comp = int(p * math.pow((1+r),t))

            print(f"Total amount once interest is applied is {repayment_comp}. ")
        
        break

    elif lower_bond_invest == "bond":
        house_value = int(input("What is the current value of your house: "))
        interest_rate_bond = int(input("Interest rate: ")) 
        number_months = int(input("How many months do you plan to repay the bond: "))

        # simplify variable names for algorithm, insert algorithm and display answer
        h = house_value
        i = float(interest_rate_bond / 100) / 12
        n = number_months

        print(i)

        amount_per_month = (i * h)/(1 - (1 + i)**(-n))

        print(f"Monthly repayments will be {amount_per_month} ")
       
        break 

    else:
        print("please enter either 'investment' or 'bond'.")










