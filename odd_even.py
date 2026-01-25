a=int(input("Enter number:" ))
if(a%2==0):
    print("even")
else:
    print("odd")



a=int(input("Value for A: "))
b=int(input("Value for B: "))
operation=input("choose add/sub/mul/div: ")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print("Invalid Operation")



Score=int(input("what is your Score? "))
if(Score<35):
    print("Needs Improvement")
elif(Score>=35 and Score<70):
    print("Good Student")
elif(Score>=70 and Score<=100):
    print("Excellent Student")
else:
    print("Invalid Score")




score=int(input("score persentage: "))
if(score>=70):
    name=input("Enter your Name: ")
    age=input("Enter your Age: ")
    print("You are eligible")
else:
    print("You are not eligible")




salary=int(input("Salary:"))
age=int(input("Age:"))
if(salary>=20000 or age<=25):
    loan=int(input("Loan:"))
    if(loan>50000):
        print("Maximum loan amount is 50000")
    else:
         print("You are eligible for loan")
else:
    print("You are not eligible for loan")





for i in "apple":
    print(i)




for i in range(5):
    print(i)




for i in range(1,5):
    print(i)




for i in range(1,11):
    print(i,"X 2 =",i*2)


a=int(input("A:"))
b=int(input("B:"))
for i in range(a+1,b):
    print(i)
























