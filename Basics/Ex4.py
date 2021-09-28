#Python Code for finding Sum of N natural Numbers in Given Range.
start = int(input("Enter Start Value of range:"))
end = int(input("Enter End Value of range:"))
value=0
for i in range(start,end+1):
    value = value+i;
print("The sum:",value)
