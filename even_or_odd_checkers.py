def even_or_odd_checkers(number):
    
    if (number % 2) == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
   
num = int(input("Enter a number: "))
even_or_odd_checkers(num)