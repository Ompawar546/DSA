arr = list(map(int, input().split(',')))  

def find_unque_ele(arr):
    freq = {}
    uique_ele = []
    for num in arr :
        if num in freq :
            freq[num]+=1
        else :
            freq[num]=1

    
    for num in freq:
        if freq[num]==1:
            uique_ele.append(num)
    
    return uique_ele                        

print(find_unque_ele(arr))