limit=int(input("how many no is enter "))
i=1
even=0
odd=0
while i<=limit:
     n=int(input("enter number to check even or odd: "))
     if n%2==0:
          even+=1
          print("your entered number",n," is even ")
     else:
         odd+=1
         print("your entered number",n," is odd ")
     i=i+1
print(limit,"times complete")
print("total even numbers : ",even)
print("total odd numbers : ",odd)