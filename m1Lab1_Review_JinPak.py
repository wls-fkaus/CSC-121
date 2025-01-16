# Calculate cost for items based on quantity
# Jin Pak
# CSC121 m1Lab1– Review
# 1/14/25

'''
Get number of candles to purchase from the user.
if num_item between 1-19, it will cost 4.75 each
if num_item between 20-49, it will cost 4.50 each
if num_item between 50-99, it will cost 4.25 each
if num_item is greater than or equal to 100, it will cost 4.00 each

calculate total by multiplying num_item and cost per item.

'''

runagain = "yes"

# while loop begin
while runagain == "yes":

    # Get num of candles
    num_candles = int(input("How many candles do you want to buy? "))

    # if else statement to assign cost of candles

    if num_candles > 0 and num_candles < 20:
        cost = 4.75
    elif num_candles > 19 and num_candles < 50:
        cost = 4.50
    elif num_candles > 49 and num_candles < 100:
        cost = 4.25
    elif num_candles >= 100:
        cost = 4.00
    else:
        cost = 0 
        print("Please enter a valid number.")

    # display info to user
    print("\n\n\n")
    print("*" * 30)
    print(f"Number of candles purchased: {num_candles}")
    print(f"The cost per item is: ${(cost):.2f}")
    print(f"The total cost of all the candles purchased is: ${(cost * num_candles):.2f}")
    # while loop ends/ ask if user wants to run again
    runagain = input("Would you like to run the program again?: ")
    
print("Program has ended!!!")