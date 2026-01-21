import os
from random import randint
import time

#Step1 : Take password from user

pas = input("Send the password:")

#step2 : define all possible character

keys =[
    "1","2","3","4","5","6","7","8","9","0"
    "a","b","c","d","e","f","g","h","i","j"
    ,"k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z","!","@","#","$","%","^"
    ,"&","*","A","B","C","D","E","F","G","H","I","J","K"
    ,"L","M","N","O","P","Q","R","S","T","U","V","W","Y","Z"
    ]

# step 3 initialize variable

pwg ="" 
attempts = 0
start_time = time.time()

#keep guessing until password matches
while pwg != pas:
    pwg =""
    attempts +=1

    #steps 5: Generate random password of same length
    for i in range(len(pas)):
        guesspass = keys[randint(0 , 4)]
        pwg = str(guesspass) + str(pwg)
        print(pwg)
        print("attacking...... please wait!")
        os.system("cls")

# step 6 : Calculate total time
end_time = time.time()
total_time = end_time - start_time

# step 7: show final result
print(f"The pass is :{pwg}")
print(f"Total Attempts:{attempts}")
print(f"Time Taken: {total_time:.2f} seconds")