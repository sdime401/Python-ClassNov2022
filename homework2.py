mylist=[]   # This line defines my variable mylist which is an empty list
user_data= input("Do you have an empty list to print? enter Yes or No : ") #I am asking the user whether he wants to print an empty list or not
user_dataed= user_data.upper() # this line convert the user answer to upper case
if user_dataed == "YES":  
    print("[]")                 # If the user answe is Yes, then it prints the empty list
elif user_dataed == "NO":       # if the user answer is no, it will go through a for loop and asking the user to enter 4 digits
    for i in range(4):
        user_input =int(input("Please enter int digit: "))
        mylist.append(user_input)                                   # this line add the user input to the mylist
    print("The Largest and Smallest value are respectively: ",max(mylist), min(mylist))     # this line print the Maximun and Minimun respectively
else:
    print("You should enter either 'Yes' or 'No'.Try again! ") # this line tells the user to either enter 'yes' ot 'no'. I could force the user to do so with a while loop
    


