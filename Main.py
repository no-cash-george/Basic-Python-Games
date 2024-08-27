import random


f = True #flag to determine when the game ends
retry = True #flag to help display the right welcome message
while f:
    if retry:
        print("Welcome to guess the number \n", "Do you want to play?(Yes/No)" )
        selection = input()
        while not(selection == "Yes" or selection == "No"):
            print("Please enter either Yes or No")
            selection = input()
    
    if selection == "Yes":
        #number = random.randrange(1,10) #random number generation
        number = 5
        print("I am thinking of a number between 1 and 10 \n", "What number am i thinking? ")
        user_number = int(input())
        i = 1
        #main game loop
        while not(user_number == number) and i <= 5: 
            print("You are wrong!!! \n", "Do you want to retry?(Yes/No)")
            selection = input()
            while not(selection == "Yes" or selection == "No"):
                print("Please enter either Yes or No")
                selection = input()
            if selection == "Yes":
                print("What number am i thinking? ")
                user_number = int(input())
                i += 1
            else:
                f = False 
                break
        
        
        if f:
            print("Correct!!!!")
            print("Do you want to play again?(Yes/No)")
            selection = input()
            while not(selection == "Yes" or selection == "No"):
                print("Please enter either Yes or No")
                selection = input()  
            f = (selection == "Yes") 
        elif i > 5:
            print("Too many wrong answers!!!! Try Again with a new number")

        retry = False
                   
    else:
        f = False
