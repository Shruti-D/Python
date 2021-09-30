def isPrime(n):
    for i in range(2,n//2):
        if n%i==0:
            break
    else:
        print(n)
start = int(input("Enter Start of the Range:"))
end = int(input("Enter End of the Range:"))
if (start<1 or end<=1):
    print("No Prime Numbers.")
else:
    print("Prime Number from",start,"to",end,":")
    for i in range(start,end+1):
        if(i>1):
            isPrime(i)
    
