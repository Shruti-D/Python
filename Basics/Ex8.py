#Program to check if the given number is Prime or not in Python.
num = int(input("Enter a Number:"))
count = 0
for i in range(1,num+1):
    if num%i==0:
        count=count+1;
if count==2:
    print(num,"is a Prime Number.")
else:
    print(num,"is not a Prime Number.")
