nums = [2,7,11,15]
target = 9
d = {} 
op = []
length = len(nums) 
for i in range(length):
    d[nums[i]] = i 

print(d)    
for i in range(length):
    x = target - nums[i] 
    print(f"x = {x}")
    if d.get(x) != None and d[x] != i:
        print(f"added {x}")
        print(f"faster solution {d[x]} , {i}")

        if nums[i] * 2 == target:
            op.append(i)
            op.append(d[x]) 
        else:
             op.append(i)   
      
print(op) 

# another solution better than the first one
def two_sum(nums, target):
    d = {}
    length = len(nums)
    for i in range(length):
        x = target - nums[i] 
        if x in d:
            return print([d[x], i] )
        else:
            d[nums[i]] = i    

two_sum([3,3], 6)             

