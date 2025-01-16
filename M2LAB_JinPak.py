# Jin Pak
# 1/16/2025
# M2Lab
# Use functions to simulate shopping


# Create the function to determine if the item exist
def if_item_exist(item):
   '''
   Function takes in one string. If that string exist in a list it will return True, if not, return False.
   '''
   item_list = ["leek", "strawberry", "tuna", "orange", "banana", "bread"]

   if item in item_list:
      return True
   else:
      return False


def get_Cost(item, quantity):
    '''
    Function takes in in an item as a string and a quantity as integer.
    Function calculate the cost using a dictionary and return the total cost.
    '''
    item_prices = {"leek":2.99, "strawberry":3.99, "tuna":6.99, "orange": 1.99, "banana":2.99, "bread":5.99}

    # get cost of item from dictionary
    item_cost = item_prices[item]

    total_cost = quantity * item_cost

    return total_cost

# Define the main function
def main():
    # Call all the other functions
    print("Welcome to Shop!")

    print()

    run_again = "yes"

    final_cost = 0

    while run_again == "yes":
        # get an item from user
        user_item = input("What would you like to purchase?: ")

        print()

        if if_item_exist(user_item) == True:
            amount = int(input(f"How many {user_item}s would you like to purchase?: "))
            final_cost = final_cost + get_Cost(user_item, amount)
        else:
            print("That item does not exist!")

        print()

        run_again = input("Do you want to add more items?: ")

    print(f"${final_cost:.2f}")


# Call the main functions
if __name__=="__main__":
    main()
