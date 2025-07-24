nums = [2,7,11,15]
target = 7
ans=[]
x=0
y=x+1

for i in nums:
    if nums[x]+nums[y]==target:
        ans=[x,y]
        print(ans)
        break
    else:
        x+=1
        y+=1    