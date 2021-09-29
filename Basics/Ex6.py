#Python Program to Find the Largest Number Among Three Numbers.
n1 = int(input("Enter First Number:"))
n2 = int(input("Enter Second Number:"))
n3 = int(input("Enter Third Number:"))
if n1>n2 and n1>n3:
    print("The Greatest Number:",n1)
elif n2>n1 and n2>n3:
    print("The Greatest Number:",n2)
elif n3>n1 and n3>n2:
    print("The Greatest Number:",n3)
else:
    print("All Numbers are Equal.")
