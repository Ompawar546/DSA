#Hill Valley problem
l=[2,5,4,24,65,45,7,3,86,6,34]
i=0
j=i+1
count=0
for i in range(1,len(l)-1):
    if l[i]>l[i-1] and l[i]>l[i+1] or l[i]<l[i-1] and l[i]<l[i+1]:
        count+=1
print(count)        