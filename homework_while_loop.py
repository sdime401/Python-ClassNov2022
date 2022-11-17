#Define my username and password database as a dictionary
password_database={
    "simonballard": "Simon123",
    "yanicknoah": "yanick12345",
    "leonelmessi": "leo1987",
    "samueletoo": "etoo84"
}

# Initializing the username, password and the count
username= ""
passsword= ""
n = 0
# user enter the Loop for iteration and get to input his username and password
while n < 5:
    username = input("Enter your username: ")   
    password = input("Enter your password: ")
    n +=1
    if username in password_database and password_database[username]==password: #this line checks if the username is in the database
        #and password correspond to the username
        print("You have Access!")
        break   #This line exit the code if the previous statement is true
    elif username not in password_database or password_database[username]!=password:  #This line checks if the username is not in the database
        # or the password entered does not have a match in the database
        if n <=4:  #This nested if statement ensures that the code will not prompt the user to try again after the 4th times
            print("Your username or password is wrong! please try again")
        else:
            print("Your account has been locked out for too many failed attempts\n Please contact your administrator") #This line is executed if the code
            #fails more than 4 times
            break  
    else:
        break