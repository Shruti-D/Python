#Python Program to Find the Sum of First N Natural Numbers.
#Method 1:
num = int(input("Enter the First N Natural Numbers:"))
value = 0
for i in range(1, num+1):
    value = value + i;
print("Sum of N natural numbers:", value)

#Method 2:
num = int(input("Enter Frist N natural numbers:"))
value = int((num*(num+1))/2)
print("Sum of N natural numbers:", value)
