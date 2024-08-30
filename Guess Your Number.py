def input_check():
    sel = input
    while not(sel == "Yes" or sel == "No"):
        print("Please answer Yes or No")
        sel = input()
    return sel


print("Hello. Welcome to guess the number. \n Do you want to play?")


selection = input_check()
if selection == "Yes":
    print("Please think of a number from 1 to 100")
    f1 = True
    front = 1
    rear = 100

    while  f1:
        mid = int((front + rear)/2)
        print("Is your number", mid)
        selection = input_check()
        if selection == "Yes":
            print("Haha!! Found it :)")
            f1 = False
                

        else:
            print("Is your number Over or Under ", mid)
            sel = input
            while not(sel == "Over" or sel == "Under"):
                print("Please answer Over or Under")
                sel = input()
                
            if sel == "Over":
                front = mid + 1
            else:
                rear = mid - 1

        if front > rear:
            print(":( You cheated. \n End of game.)")
            f1 = False   