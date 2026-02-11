a = []
print("Enter 10 Numbers:")
for i in range(5):
    num=int(input("Num"+str(i+1)+": "))
    a.append(num)
print(a)
sum=0
for i in a:
    sum=sum+i
print("Sum value: ",sum)
