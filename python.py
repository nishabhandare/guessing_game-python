import random
num=random.randint(1,10)
chance=10
attempt=0
for i in range(chance):
    n=int(input("enter number (1-10): "))
    attempt+=1
    if(n>10 or n<1):
        print("not valid input(1-10)")
        continue
    elif(n==num):
        print("correct guess")
        print("you are winner.")
        print("total attempt : ",attempt)
        break
    elif(n>num):
        print("Greater than number")
    else:
         print("Less than number")
else:
        print("chance finished")
        print ("secret number ",num)
        
print("attempts : ",attempt)
     