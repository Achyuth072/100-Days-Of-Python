print('''
                             .-,
                ,---._   _  -' >
               | "\ \\\ //_=33'
               7-_ || \//-' //
               |"= / -'/'' |/
           __-'_   -'-/__  ||
          / ,--'     / ,-'-||
         /  /  ___ //    ,-||_
        /  _--/_  '-    / \|_';
       |  /  // "\\\   /     "
       / /  //        |   , -'
      /  ;,//,        /  /,  \
     |   |_/  |      /  / /  |
     '-\/\_,_,/ _   V  /\,7-"'
        '    /   ''---'  |
             |      \\   |
             |       \\  |
             |       |\\ /
             | \     /|\|
             |  |    || ;
             |  |   /|| ;
             |  | ,/ / /
             |  \ / \/ |
            /    | \_//
            |    | "" /
           ,'   ,'  |,'
           /      \| |
          /     /  \ |
         /     /   / \
        /     /   / ,/
       //  /       /\\
    _-'/        ,-' | )
 ,-'       \_   \   \ |
/__,--      _,-""  /   \
    \____,-'       '---'

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

c1=input("You are at a crossroad. Where do you want to go? Type 'left' or 'right'\n").lower()
if c1=="left":
          c2=input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
          if c2=="wait":
                 c3=input("You arrive at the island unharmed. There is a house with 3 doors. One red one yellow and one blue. Which colour do you choose?\n").lower()
                 if c3=="red":
                    print("You have entered a room full of fire. Game Over.")
                 elif c3=="yellow":
                    print("You have found the treasure. You Win!")
                 elif c3=="blue":
                    print("You have entered a room full of beasts. Game Over.")
                 else:
                    print("Game Over.")       
                          
          else:
                 print("You have been attacked by an angry trout. Game Over.")
else:
      print("You fell into a hole. Game Over.")
          