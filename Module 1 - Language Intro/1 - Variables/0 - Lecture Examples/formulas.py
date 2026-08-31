principal = 1000  # initial amount to be deposited
rate = 2.7  # interest rate applied to deposit (will be divided by 100)
n = 10  # number of years to compound deposit

# use an over-loaded form of print() to set out each element of the string
print("Initial principal is $", principal)
print("Interest rate is ", rate / 100)
print("Hold for ", n,  " years")


final = principal * ((1 + (rate / 100)) ** n) # calculate the eventual result

# fancy print the output with two decimal places for floating number
print(f"Final value after is ${final:.2f}")

# Here's an example of something extra added but not saved