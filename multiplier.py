import math
def multiply_even_numbers(list):
    '''
    This function accepts a list of numbers and returns the product of all even numbers in the list.
    
    Parameters:
    list: The user will provide a list of number
  
    Returns:
    int: returns the product of all even numbers
    
    '''
    new_list_1 = [x for x in list if x % 2==0]
    print("Your list of only even numbers", new_list_1)
    product =math.prod(new_list_1)
    if len(list) == 7:
        print(f" The product of all even number is: {product} ")
    else:
        print(" Your function has run but your list is not complete! Check for errors in your input\n Try again")


list_1 =[]
while True:
    
    # This following line will ask the user to enter 7 numbers
    try:
        n = 0
        while n < 7:
            user_input = int(input(" Please enter a number: "))
            list_1.append(user_input)
            n+=1
    except Exception as error:
        print(f" Your code has failed because of the following error: {error} is not an integer")
    
    break
print("Your List entered:", list_1)
print(multiply_even_numbers.__doc__)
multiply_even_numbers(list_1)

