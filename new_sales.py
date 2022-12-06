def sales(cart):
    '''
    This function add items in your grocery cart and return the total in a receipt test.
    
    Parameters:
    list: The user will provide a dictionary
  
    Returns:
    float: returns the sum of the receipt in a text file
    
    '''
    cart_list=list(cart.values())
    total = sum(cart_list)
    total= str(total)
    with open("receipt.txt", "w") as grocery_cart:
        grocery_cart.write("The total of your grocery is:$ ")  
        grocery_cart.write(total)
    

my_cart ={}
n=0
while n < 6:
    try:
        user1 = input("Please enter the name of an item: ")
        user2 = float(input("Enter the price: "))
        my_cart[user1] = user2
    except ValueError as error:
        print(f"This is your error: {error}. You are now exiting the program. Rerun the code it to make it right ")
        break
    n+=1
#print(thisdict)
sales(my_cart)
