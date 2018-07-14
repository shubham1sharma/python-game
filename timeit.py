
# print user name
print("welcome to game!")

person = input('Enter your name: ')
print('Hello', person)

# edfine function

def manualgame():
    

    if len(person) < 8:                 # if person name length greater than 8 it quit
        print("would you like to play a game!",person)
        join=input("yes or no(y/n)!")
        if join[0]=="y":
            print("great",person)                         
            print("lets! play\n")
            print("but before play please enter your password\n")         # if password is wrong game not open
            print("your password is unicorn")
            password=""                                   
            while  password != "unicorn":
                password=input("password: ")
            print("welcome in!")
            print("think of your age in your mind:",person)
            join=input("please enter yes(y) for proceed further!\n")                  # game start
            if join[0]=="y":
                print("")
            else:
                print("wrong choice")
            join=input("multiply starting  number of your age with 5 and yes(y) to proceed\n")
            if join[0]=="y":
                print("")
            else:
                print("wrong choice")
            join=input("add this number to 3 and yes(y) to proceed\n")
            if join[0]=="y":
                print("")
            else:
                print("wrong choice")
            join=input("now double this number and call it result and yes(y) to proceed\n")
            if join[0]=="y":
                print("")
            else:
                print("wrong choice")
            join=input("add second number of your age with result let call it x and yes(y) to proceed\n")
            if join[0]=="y":
                print("")
            else:
                print("wrong choice")
            join=input("now deduct 6 from x and yes(y) to proceed\n")
            if join[0]=="y":
                print("this is your age")
            else:
                print("wrong choice")
            

        elif join[0]=='n':
            print("better luck next time!")
        else:
            print("uhhhh.... please enter y or n")
    
    else:
        print("your name length greater than limit")
manualgame()                             # function call

