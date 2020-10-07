# time complexity o(n^2)
nums1 = [2,1,1,1]
nums2 = [2,2]
length1 = len(nums1) 
length2 = len(nums2) 
op = [] 
print(len(op))
for i in range(length1):
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            op.append(nums1[i])
            nums2.pop(j)
            break


        
print(op)            
l = [] 
p = [4] 
print(l + p)
# another solution onleetcode
res = []
d = {}
for n1 in nums1:
    if n1 not in d:
        d[n1] = 1
    else:
        d[n1] += 1
for n2 in nums2:
    if n2 in d and d[n2] > 0:
        res.append(n2)
        d[n2] -= 1
# return res
print(res)