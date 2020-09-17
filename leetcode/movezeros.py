# problem URL
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567

nums = [0, 1, 12, 0, 0, 3]
length = len(nums) 
k = 0 
for i in range(length):
    if nums[i] != 0:
        nums[k] = nums[i] 
        k = k + 1 

while k < length:
    nums[k] = 0 
    k = k + 1 

print(nums)          