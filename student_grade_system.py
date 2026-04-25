i=0
for i in range(3):
    name = input("enter your name : ")
    age = int(input("enter your age : "))
    course = input("enter your course : ")
    percentage = float(input("enter your 1st year percentage : "))
    if percentage > 100 or percentage < 0:
        Grade ="Invalid Percentage"
    elif percentage >= 80:
        Grade="Distinction"
    elif percentage >= 60:
        Grade="First class"
    elif percentage >= 50:
        Grade="Pass"
    else:
        Grade="Fail"
    
    status = (input("enter yes or no : "))

    if status.lower()=="yes" and      percentage>=50:
          print("good")
          status_text="All Clear"
    else:
         print("try again")
         status_text="Not All Clear"
     
    print("----Student Details----")
    print(f"Name           :{name}")
    print(f"Age               :{age}")
    print(f"Course         :{course.upper()}")
    print(f"Status           :{status_text}")
    print(f"Percentage :{ percentage}")
    print(f"Grade           :{Grade}")


