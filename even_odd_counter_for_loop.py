limit=int(input("enter limit :"))
even=0
odd=0
for i in range(limit):
    n=int(input("enter number to check even or odd : "))
    if n%2==0:
         print(n," is a even number")
         even +=1
    else:
         print(n,"is a odd number")
         odd +=1
print(limit ,"times complete")
print(even,"times even")
print(odd,"times odd")