#! Python 3 
# will run out of terminal
# take in an input and put out a number

#compound interest at 4% 
#future value at 3.22

from decimal import Decimal


#takes in numbers and turns them into a list
numbersNeeded = []

a = 0
while a < 1:
    print('Enter your current age:')
    age = int(input())
    print('What is your desired retirement age?')
    retirement_age = int(input())
    print('Enter your current salary')
    salary = int(input())
    print('What is your current super balance?')  #takes in and stores the 3 numbers
    balance = int(input())
    #using the spitfire options from Parker
    print('Which fund would you like to use for growth estimation:\n Conservative - 3.22% \n Moderate - 3.81% \n Balanced - 4.53% \n Growth - 5.21% \n High Growth - 5.85%')
    rate = float(input())

    #numbersNeeded = [age, salary, balance]
    a += 1
print()



# function 1 - takes in wage and calculates after tax amount going into super
def after_tax(salary):
    pre_tax_amount = salary*0.095
    post_tax_amount = salary*0.095*0.15
    return (pre_tax_amount - post_tax_amount)/12
amount_in = after_tax(salary)
print('Amount going into super is:')
print(amount_in)
print()

# function 2 - years till retirement (assuming retirement age of 67)
def years_until_retirement(age):
    years = 67 - age
    return years
years = years_until_retirement(age)
print('Years until retirement:')
print(years)
print()

# function 3 - calculate principal
def compound_interest_principal(balance, years):
    # (1 + r/n)
    body = 1 + (0.04/12)
    # nt
    exponent = 12 * years
    # p(1+r/n)^nt
    return balance * pow(body, exponent)
compound_interest_value = compound_interest_principal(balance, years)
print('Accumulated compound interest is:')
print(compound_interest_value)
print()

#for year in range       java2s website

# function 4 - future value amount
def future_value_amount(amount_in, rate, years):
    decimal_rate = rate/100
    b = (1 + decimal_rate/12)
    e = 12 * years
    divisor = (decimal_rate/12)

    return amount_in * ((pow(b, e) - 1)/divisor)
future_value = future_value_amount(amount_in, rate, years)
print('Future value amount is:')
print(future_value)
print()


#function 5 - super balance
def total_balance(compound_interest_value, future_value):
    total_amount = compound_interest_value + future_value
    return total_amount
total_money = round(total_balance(compound_interest_value, future_value),2)
print("Super balance in today's dollars:")
print(total_money)
print()

# function 6 - accounting for inflation (set rate of 2.5%)
def inflated_amount(total_money, years):
    inflated_balance = total_money * pow(1.025, years)
    return inflated_balance
value = round(inflated_amount(total_money, years),2)
print('Super balance accounting for inflation is:')
print(value)
print()
