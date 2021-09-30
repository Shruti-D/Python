def isPrime(n):
    for i in range(2,n//2):
        if n%i==0:
            break
    else:
        print(n)
start = int(input("Enter Start of the Range:"))
end = int(input("Enter End of the Range:"))
for i in range(start,end+1):
    isPrime(i)
    
