import time
import random
def playagain():
    answer = input("Do You Want to Play Again?: [yes/no]\n").lower().strip()
    if answer == "yes":
        print("Copy That")
        cyoa()
    elif answer == "no":
        print("Goodbye Then :(")


def cyoa():
    print("Welcome to our Choose Your Own Adventure Game")
    answer = input("Do you want to play?  [yes/no]:\n ").lower().strip()
    if answer == "yes":
        cyoa2()  
   
    else:
        print("Goodbye then :(")
def cyoa2():
    answer = input("You reach a crossroad,do you go [left/right]\n").lower().strip()
    if answer == "left":
        answer = input("You encounter a monster, do you [run/fight]\n").lower().strip()
        if answer == "fight":
            print("Why would you do that, He throws you up and you land on your neck and die. Game Over!")
            playagain()
               
        elif answer == "run":
            print("Smart idea, You got away")
            cyoa3()
        else:
            print("Invalid Input")
            cyoa2()
    elif answer == "right":
        print("you walk aimlessly, and you fall into a pit, Upon impact you crack your neck and die. Game Over!")
        playagain()
    else:
        print("Invalid Input")
        cyoa2()
            
def cyoa3():
    answer = input("You spot a car and a plane, which one do you go for [car/plane]\n").lower().strip()
    if answer == "plane":
        print("You don't know how to fly a plane... Game Over!")
        playagain()
    elif answer == "car":
        answer = input("You get about 3 miles into a nearby town before you run out of gas,do you [leave the car/look for gas]\n").lower().strip()
        if answer == "leave the car": 
            cyoa4()
                    
    else:
        print("Invalid Input")
        cyoa3()
        
def cyoa4():
    answer = input("You wander around in this town and notice a flickering light in the distance,do you [follow the source/wander]\n").lower().strip()
    if answer == "follow the source":
        print("You follow the light to a house at the end of a road")
    
                    
        
cyoa()



