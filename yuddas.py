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
        time.sleep(.5)
        cyoa2()    
    else:
        time.sleep(.5)
        print("Goodbye then :(")
def cyoa2():
    answer = input("While walking through the park you begin to wander, the terrain turns rougher seeming as if you have came across a little forest. Suddenly you come across two paths left and right, which do you choose? [left/right]\n").lower().strip()
    if answer == "left":
        answer = input("As you decide to choose the left path a quiet area opens up, as you continue to walk through this path, the little forest widens and you are left with the options of continuing the path or turning back, do you [continue/turn back]\n").lower().strip()
        if answer == "turn back":
            print("After choosing the left path you began to get scared and turn back, you are now back at the start and have no choice but to take the right path, unfortunately you are greeted by a pack of wolves and die! Maybe you should’ve continued the path you’ve chosen before. Game Over!")
            time.sleep(.5)
            playagain()
               
        elif answer == "continue":
            print("You slowly but surely continue to go back the left path and not turn back, it seems you have gone too deep and now have to find a way out of the forest")
            time.sleep(.5)
            cyoa3()
        else:
            print("Invalid Input")
            time.sleep(.5)
            cyoa2()
    elif answer == "right":
        print("So you have chosen to follow the path that goes right, unfortunately you run into a pack of wolves and die, you should’ve chosen the other path! Game Over!")
        time.sleep(.5)
        playagain()
    else:
        print("Invalid Input")
        time.sleep(.5)
        cyoa2()            
def cyoa3():
    answer = input("Once again you are stuck, now your choices are harder as there are 3 ways to go left, middle, and right, do you go [left/middle/right]\n").lower().strip()
    if answer == "right":
        print("Maybe the right path is the right way? As you go down the long and enduring right path it seems as if you had walked all the way around the forest, you are now at the other end of the park and no longer in the forest. What would’ve happened if you chose the left path? Game Over!")
        time.sleep(.5)
        playagain()
    elif answer == "left":
        print("You seem to stick with your gut an intuition by once again going down the left path, it seems that you have walked for hours at this rate, shockingly you hear murmurs and people talking, you walk towards the voices seeing a little village.")
        time.sleep(.5)
        cyoa4()
    elif answer == "middle":
        time.sleep(.5)
        cyoa5()       
    else:
        print("Invalid Input")
        time.sleep(.5)
        cyoa3()       
def cyoa4():
    answer = input("In this now huge forest you have the choice of staying with them or turning back,do you [stay/leave]\n").lower().strip()
    if answer == "stay":
        print("It seems that you have stayed with the village! Although not the most comfortable you live with them for the rest of your life. What would’ve happened if you decided to choose the right path? Game Over!")
        time.sleep(.5)
        playagain()
    elif answer == "leave":
        print("The village and villagers didn’t seem to suit you, you decide to turn back and now are left with no other option besides going right, as you go down the long and enduring right path it seems as if you have walked all the way around the forest, you are now at the other end of the park and no longer in the forest. What would’ve happened if you stayed with the village? Or is getting out of the forest what you wanted?")
        time.sleep(.5)
        playagain()
def cyoa5():
    answer = input("So you decide to choose the middle path, while walking down you begin to hear a rush of water, as you get closer you see a waterfall, you notice behind the waterfall there is a little cave, do you [cross/continue]\n").lower().strip()
    if answer == "cross":        
        print("How fun! You decide to cross the waterfall, while climbing over the rocks unfortunately you slip! While gasping for air you’re unable to reach the surface and drown. Uh oh! Maybe you should’ve continued the path… or have not taken the middle path at all.")
        time.sleep(.5)
        playagain()
    elif answer == "continue":
        print("Although the waterfall does intrigue you, getting wet doesn’t seem to be on your plan today so you decide to continue down the path, how unlucky… a bear has spotted you and you are now running for your life! Sadly you are not faster than a bear and he eats you :(  What would’ve have happened if you chose one of the other paths?")
        time.sleep(.5)
        playagain()
cyoa()
