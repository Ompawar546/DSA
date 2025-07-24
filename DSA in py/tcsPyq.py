def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            return False
    return  True

def sumOfnums(n):
    tsum=0
    for j in range(2,n+1):
        if(isPrime(j)):
            tsum+=j
    return tsum    

n = int(input())
print(sumOfnums(n))



