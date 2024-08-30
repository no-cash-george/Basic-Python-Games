import random


#function that gets user input and checks if it is in the allowed format
def input_check():
    selection = input()
    while not(selection == "Yes" or selection == "No"):
        print("Please enter either Yes or No")
        selection = input()
    return selection 



f = True #flag to determine when the game ends
retry = True #flag to help display the right welcome message
while f:
    if retry:
        print("Welcome to guess the number \n", "Do you want to play?(Yes/No)" )
        
        selection = input_check()
    
    if selection == "Yes":
        number = random.randrange(1,10) #random number generation
        print("I am thinking of a number between 1 and 10 \n", "What number am i thinking? ")
        user_number = int(input())
        i = 1
        #main game loop
        while not(user_number == number) and i <= 5: 
            print("You are wrong!!! \n", "Do you want to retry?(Yes/No)")
            
            selection = input_check()
            
            if selection == "Yes":
                print("What number am i thinking? ")
                user_number = int(input())
                i += 1
            else:
                f = False 
                break
        
        
        if f and i <= 5:
            print("Correct!!!!")
            print("Do you want to play again?(Yes/No)")
            
            selection = input_check()
            
            f = (selection == "Yes") 
        elif i > 5:
            print("Too many wrong answers!!!! Do you want to play again????")

            selection = input_check()
            
            if selection == "No":
                f = False
            
 


        retry = False
                   
    else:
        f = False
