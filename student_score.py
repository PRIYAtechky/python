Score=int(input("what is your Score? "))
if(Score<35):
    print("Needs Improvement")
elif(Score>=35 and Score<70):
    print("Good Student")
elif(Score>=70 and Score<=100):
    print("Excellent Student")
else:
    print("Invalid Score")
  
