def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)                 
    
num=5
ans = fact(num)
print(ans)    

"""
 5*fact(4)
 5*4*fact(3)
 5*4*3*fact(2)
 5*4*3*2*fact(1)

"""




def fact2(n):
    if n == 1 or n ==0:
        return 1;
    else:
        fact_result = 1
        for i in range(2,n+1):
            fact_result *= i
        return fact_result    


a = int(input("Enter a number: "))
print(fact2(a))