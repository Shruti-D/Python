#Python Program to Find Sum Of Digits Of a Number
#Method 1:
n = int(input("Enter a Number:"))
total = 0
temp=n
while n>0:
    digit = n%10
    total=total+digit
    n=n//10
print("The Sum of digits in",temp,":",total)

#Method 2:
n = input("Enter a Number:")
total = 0
for i in str(n):
    total += int(i)
print("The Sum of digits in",n,":",total)
