# This is a finance calculator python program.
# The user indicates either bond or investment information. Program caluclates
# monthly payments on bond or final investment amount respectively.

import math

# User inputs either bond or investment.
print("Choose either 'investment' or 'bond' from the menu to proceed. \n")
print("Investment:\t- to calculate the amount of interest you'll earn on a loan.")
print("Bond:\t\t- to calculate the amount you'll have to pay on a home loan.")
payment_option = input("Please enter choice: ")
payment_option = payment_option.upper()  #  inititalise.

# Program calculates bond monthly repayments.
if payment_option == "BOND":
    print("\nPlease enter the following information regarding your bond:")
    present_val = float(input("Enter the present value of your house: \nR"))
    interest_bond = float(input("Enter the annual interest rate (%): \n"))
    interest_bond = (interest_bond / 100) / 12
    time_bond = float(input("The number of months you plan to repay the bond?: \n"))
    repayment_bond_nume = (interest_bond * present_val)  #  Numerator of calculation.
    repayment_bond_denom = (1 - (1 + interest_bond) ** (-time_bond))  
    # repayment_bond_denom is the denominator. 
    repayment_bond = repayment_bond_nume / repayment_bond_denom
    print(f"\nThe monthly repayments will be R{repayment_bond:.2f}.")

# Program calculates value of investment after time period.
elif payment_option == "INVESTMENT":
    print("\nPlease enter the following infomation about your investment:")
    deposit = float(input("Enter the deposit amount: \nR"))
    interest_inv = float(input("Enter the interest rate (%): \n"))
    interest_inv = interest_inv / 100
    time_in = (input("Enter the number of years planned for investment: \n"))
    time_inv = float(time_in)
    interest = input("Will you be using simple or compound interest?: \n")
    interest = interest.upper()

    # If simple interest is used.
    if interest == "SIMPLE":
        simp_amount = deposit * (1 + interest_inv * time_inv)
        interest_diff = simp_amount - deposit
        print(f"\nAfter {time_in} years, your investment will be worth \
            R{simp_amount:.2f}!")
        print(f"(The interest earned is R{interest_diff:.2f}).")
    
    # If compound interest is used.
    elif interest == "COMPOUND":
        comp_amount = deposit * math.pow((1 + interest_inv), time_inv)
        interest_diff = comp_amount - deposit
        print(f"\nAfter {time_in} years, your investment will be worth \
            R{comp_amount:.2f}!")
        print(f"(The interest earned is R{interest_diff:.2f})")
    else:
        print("\nEnter either 'simple' or 'compound' on retry.")
else:
    print("\nPlease enter either 'investment' or 'bond' on retry.")
print("Thank you for using Financial Calculators(pty).")
