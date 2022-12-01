def addition(num1,num2):
    sum =num1+num2
    print(f"The addition of {num1} and {num2} is {sum}")
def subtraction(num1,num2):
    sub=num1-num2
    print(f"The subtraction of {num1} and {num2} is {sub}")
def multiplication(num1,num2):
    mul=num1 * num2
    print(f"The multiplication of {num1} by {num2} is {mul}")
def division(num1,num2):
    div=num1/num2
    print(f"The division of {num1} by {num2} is {div}")
def modulus(num1,num2):
    mod=num1 % num2
    print(f" {num1} modulus {num2} is {mod}")
def exponentiation(num1,num2):
    exp=num1 ** num2
    print(f" {num1} exponent {num2} is {exp}")
def floor_division(num1,num2):
    fl_div=num1 // num2
    print(f"The floor division of {num1} by {num2} is {fl_div}")
    
number1= float(input("Enter the first number: "))   
operator=input("What Operator do you want to use: Enter '+' for Addition, '-' for Subtraction,'*' for Multiplication, '/'for Division, '%' for Modulus, '**' for Exponentiation, and '//' for Floor division: \n"  )    
number2= float(input("Enter the second number: "))
if operator =="+":
    addition(number1,number2)
elif operator =="-":
    subtraction(number1,number2)
elif operator =="*":
    multiplication(number1,number2)
elif operator =="/":
    division(number1,number2)
elif operator =="%":
    modulus(number1,number2)
elif operator =="**":
    exponentiation(number1,number2)
elif operator =="//":
    floor_division(number1,number2)
else:
    print("You have not entered a valid operator. Please try again!")
    

